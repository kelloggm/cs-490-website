"""Match every student on the team sheet to a GitHub username.

Sources, in priority order:
  1. github_overrides.csv  -- hand-collected fixes (columns: ucid, name, github);
                              match on ucid if given, else on name
  2. SURVEYS               -- the surveys; matched on UCID (email local part),
                              falling back to first+last name for rows with no UCID

Each handle found is checked against the GitHub API (via the `gh` CLI) to
make sure the account exists. Writes roster.csv (one row per student) and
prints a report of everything still missing or suspicious.

Usage:
  python3 build_roster.py [--no-verify]
"""
import csv
import json
import os
import re
import subprocess
import sys
from datetime import datetime

from send_team_emails import get, member_name_cols, member_ucid_cols, read_rows, section_label, NOTES, TEAM

TEAM_SHEET = 'team_sheet.csv'
SURVEYS = ['team-formation.csv', 'team-formation-003.csv']
OVERRIDES = 'github_overrides.csv'
OUT = 'roster.csv'

# GitHub usernames: alphanumerics and single hyphens, no leading hyphen, <= 39 chars
HANDLE_RE = re.compile(r'^[A-Za-z0-9](?:[A-Za-z0-9-]{0,38})$')


def clean_handle(raw):
    """Pull a username out of answers like 'https://github.com/x' or 'x (https://github.com/x)'."""
    raw = raw.strip()
    m = re.search(r'github\.com/([A-Za-z0-9-]+)', raw)
    if m:
        return m.group(1)
    token = raw.split()[0] if raw.split() else ''
    token = token.lstrip('@')
    return token if HANDLE_RE.match(token) else ''


def name_key(name):
    """(first, last) lowercased, so 'Christian Alexander Liriano' matches 'Christian Liriano'."""
    parts = re.sub(r'[^a-z\s\'-]', '', name.lower()).split()
    return (parts[0], parts[-1]) if parts else ('', '')


def column(row, prefix):
    """Value of the first column whose header starts with prefix (the surveys word them differently)."""
    for k, v in row.items():
        if k and k.strip().lower().startswith(prefix.lower()):
            return (v or '').strip()
    return ''


def read_survey():
    """ucid -> latest response across all surveys; also name_key -> list of responses."""
    responses = []
    for path in SURVEYS:
        with open(path, newline='', encoding='utf-8-sig') as f:
            for row in csv.DictReader(f):
                responses.append(dict(
                    when=datetime.strptime(column(row, 'Timestamp'), '%m/%d/%Y %H:%M:%S'),
                    ucid=column(row, 'Email Address').lower().split('@')[0],
                    name=column(row, 'Your full name'),
                    section=column(row, 'Which section'),
                    raw=column(row, 'Your GitHub username'),
                ))
    by_ucid, by_name = {}, {}
    for resp in sorted(responses, key=lambda r: r['when']):  # later responses win
        resp['github'] = clean_handle(resp['raw'])
        by_ucid[resp['ucid']] = resp
    for resp in by_ucid.values():
        by_name.setdefault(name_key(resp['name']), []).append(resp)
    return by_ucid, by_name


def read_overrides():
    by_ucid, by_name = {}, {}
    if not os.path.exists(OVERRIDES):
        return by_ucid, by_name
    with open(OVERRIDES, newline='', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            handle = clean_handle(row.get('github', ''))
            if not handle:
                continue
            if row.get('ucid', '').strip():
                by_ucid[row['ucid'].strip().lower()] = handle
            elif row.get('name', '').strip():
                by_name[name_key(row['name'])] = handle
    return by_ucid, by_name


def students():
    """(team label, section, name, ucid) for every student on the team sheet."""
    for row in read_rows(TEAM_SHEET):
        if get(row, NOTES).upper().startswith('EXAMPLE ROW'):
            continue
        section = section_label(row)
        for i in range(1, 6):
            name = get(row, member_name_cols(i))
            if name:
                yield get(row, TEAM), section, name, get(row, member_ucid_cols(i)).lower()


def github_user(handle):
    """Canonical login if the account exists, else None."""
    r = subprocess.run(['gh', 'api', f'users/{handle}', '--jq', '.login + " " + .type'],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None
    login, kind = r.stdout.split()
    return login if kind == 'User' else None


def main():
    verify = '--no-verify' not in sys.argv[1:]
    survey_ucid, survey_name = read_survey()
    over_ucid, over_name = read_overrides()

    rows, problems, used = [], [], {}
    for team, section, name, ucid in students():
        label = f'{section}-{team}'
        github, source, note = '', '', ''
        resp = survey_ucid.get(ucid) if ucid else None
        if not resp and not ucid:
            cands = survey_name.get(name_key(name), [])
            if len(cands) == 1:
                resp = cands[0]
                ucid = resp['ucid']
                note = f'UCID {ucid} inferred from survey by name'
        if ucid in over_ucid or (not ucid and name_key(name) in over_name):
            github, source = over_ucid.get(ucid) or over_name[name_key(name)], 'override'
        elif resp:
            github, source = resp['github'], 'survey'
            if name_key(resp['name']) != name_key(name):
                note = f'survey name "{resp["name"]}" differs'
            if not github:
                note = f'unparseable survey answer {resp["raw"]!r}'

        status = 'ok'
        if not github:
            status = 'missing'
        elif verify:
            login = github_user(github)
            if login is None:
                status = 'not-found'
            else:
                github = login
        if github:
            used.setdefault(github.lower(), []).append(f'{name} ({label})')

        rows.append(dict(team=team, section=section, name=name, ucid=ucid,
                         github=github, source=source, status=status, note=note))
        if status != 'ok' or note:
            problems.append((label, name, ucid or '(no UCID)', status, github, note))

    for handle, who in used.items():
        if len(who) > 1:
            problems.append(('*', ', '.join(who), '', 'duplicate', handle, 'same handle for several students'))

    # Survey respondents who aren't on any team (typos in UCID, or dropped)
    on_sheet = {r['ucid'] for r in rows}
    strays = [r for u, r in survey_ucid.items() if u not in on_sheet]

    with open(OUT, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    n_ok = sum(r['status'] == 'ok' for r in rows)
    print(f'{n_ok}/{len(rows)} students have a {"verified " if verify else ""}GitHub handle. Wrote {OUT}.\n')
    for label, name, ucid, status, github, note in sorted(problems):
        print(f'  {label:8} {name:28} {ucid:10} {status:10} {github:22} {note}')
    for r in strays:
        print(f'  survey response not on team sheet: {r["name"]} ({r["ucid"]}, {r["section"]}) -> {r["github"]}')


if __name__ == '__main__':
    main()
