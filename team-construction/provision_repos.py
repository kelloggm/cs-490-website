"""Create one private repo + GitHub team per project team, from a template repo.

Reads roster.csv (from build_roster.py) for student handles and team_sheet.csv
for mentors. For each team it makes sure that:
  1. the org team exists (privacy: closed)
  2. the repo exists, generated from TEMPLATE, private
  3. the team has push access to the repo
  4. every student with a verified handle is on the team (non-org-members get
     an org invitation by email; they have no access until they accept)
  5. the mentor is a maintainer of the team, if MENTOR_GITHUB has them

Every step checks existing state first, so it's safe to re-run, e.g. after
collecting more handles. By default this is a dry run; pass --apply to make
changes. The token needs the admin:org and repo scopes:
  gh auth refresh -h github.com -s admin:org

Usage:
  python3 provision_repos.py [--apply] [--only 001-7,HM1-H2]
"""
import csv
import json
import subprocess
import sys
import time
from collections import defaultdict

from send_team_emails import MENTOR_UCID, NOTES, TEAM, get, read_rows, section_label

ORG = 'njit-cs490-au26'
TEMPLATE = 'kelloggm/covey.town'   # must be marked as a template repo on GitHub
ROSTER = 'roster.csv'
TEAM_SHEET = 'team_sheet.csv'

# Mentor UCID -> GitHub handle. Mentors not listed here are skipped with a warning.
MENTOR_GITHUB = {
    'mjk76': 'kelloggm',         # Martin
    # TODO: add TAs/other instructors
}


def repo_name(section, team):
    """Also used as the team name. Team numbers repeat across sections, so include the section."""
    return f'au26-{section}-team-{team.zfill(2)}'.lower()


def api(method, path, body=None):
    """Call the GitHub REST API through gh. Returns (http status, parsed JSON or None)."""
    cmd = ['gh', 'api', '--method', method, '--include', path]
    if body is not None:
        cmd += ['--input', '-']
    r = subprocess.run(cmd, input=json.dumps(body) if body is not None else None,
                       capture_output=True, text=True)
    # headers, blank line, then the body; text mode has already normalized CRLF to LF
    head, _, payload = r.stdout.partition('\n\n')
    try:
        status = int(head.split()[1])
    except (IndexError, ValueError):
        sys.exit(f'gh api {method} {path} failed: {r.stderr.strip()}')
    try:
        data = json.loads(payload) if payload.strip() else None
    except json.JSONDecodeError:
        data = None
    return status, data


def check(status, data, what):
    if status >= 300:
        msg = (data or {}).get('message', '')
        raise RuntimeError(f'{what}: HTTP {status} {msg}')


def load_teams():
    """label -> dict(section, team, students=[(name, github)], missing=[names], mentor_ucid)"""
    teams = {}
    for row in read_rows(TEAM_SHEET):
        if get(row, NOTES).upper().startswith('EXAMPLE ROW'):
            continue
        section, team = section_label(row), get(row, TEAM)
        teams[f'{section}-{team}'] = dict(section=section, team=team, students=[], missing=[],
                                          mentor_ucid=get(row, MENTOR_UCID).lower())
    with open(ROSTER, newline='') as f:
        for r in csv.DictReader(f):
            t = teams[f'{r["section"]}-{r["team"]}']
            if r['status'] == 'ok':
                t['students'].append((r['name'], r['github']))
            else:
                t['missing'].append(r['name'])
    return teams


def provision(label, t, apply):
    name = repo_name(t['section'], t['team'])
    say = (lambda s: print(f'  {s}')) if apply else (lambda s: print(f'  [dry run] would {s}'))
    print(f'\n--- {label} -> {ORG}/{name}')

    # 1. team
    status, team = api('GET', f'orgs/{ORG}/teams/{name}')
    if status == 404:
        team = None  # a 404 body is an error message, not a team
        say(f'create team {name}')
        if apply:
            status, team = api('POST', f'orgs/{ORG}/teams', {'name': name, 'privacy': 'closed'})
            check(status, team, 'create team')
    else:
        check(status, team, 'look up team')
    slug = team['slug'] if team else name

    # 2. repo
    status, repo = api('GET', f'repos/{ORG}/{name}')
    if status == 404:
        repo = None
        say(f'create private repo {ORG}/{name} from {TEMPLATE}')
        if apply:
            status, repo = api('POST', f'repos/{TEMPLATE}/generate',
                               {'owner': ORG, 'name': name, 'private': True})
            check(status, repo, 'create repo')
            for _ in range(15):  # generation is asynchronous; wait until the repo is usable
                if api('GET', f'repos/{ORG}/{name}')[0] == 200:
                    break
                time.sleep(2)
    else:
        check(status, repo, 'look up repo')
        if not repo['private']:
            print(f'  WARNING: {ORG}/{name} already exists and is PUBLIC')

    # 3. team access to repo
    status, _ = api('GET', f'orgs/{ORG}/teams/{slug}/repos/{ORG}/{name}')
    if status != 204:
        say(f'grant team {slug} push access to {name}')
        if apply:
            check(*api('PUT', f'orgs/{ORG}/teams/{slug}/repos/{ORG}/{name}', {'permission': 'push'}),
                  'grant repo access')

    # 4 + 5. members and mentor
    wanted = [(gh, 'member', n) for n, gh in t['students']]
    mentor_gh = MENTOR_GITHUB.get(t['mentor_ucid'])
    if mentor_gh:
        wanted.append((mentor_gh, 'maintainer', f'mentor {t["mentor_ucid"]}'))
    else:
        print(f'  WARNING: no GitHub handle for mentor {t["mentor_ucid"] or "(none)"}; not added')
    for gh, role, who in wanted:
        status, m = api('GET', f'orgs/{ORG}/teams/{slug}/memberships/{gh}')
        if status == 200 and m['role'] == role:
            continue
        say(f'add {gh} ({who}) as team {role}')
        if apply:
            status, m = api('PUT', f'orgs/{ORG}/teams/{slug}/memberships/{gh}', {'role': role})
            check(status, m, f'add {gh}')
            if m['state'] == 'pending':
                print(f'    {gh} invited to {ORG}; access starts once they accept')
    for n in t['missing']:
        print(f'  SKIPPED: {n} has no verified GitHub handle; re-run once it is collected')


def main():
    args = sys.argv[1:]
    apply = '--apply' in args
    only = None
    if '--only' in args:
        only = set(args[args.index('--only') + 1].upper().split(','))
    if 'TODO' in ORG or 'TODO' in TEMPLATE:
        sys.exit('Set ORG and TEMPLATE at the top of provision_repos.py first.')

    status, org = api('GET', f'orgs/{ORG}')
    check(status, org, f'look up org {ORG}')
    # With any other base permission, every student in the org could see every team's repo
    base = org.get('default_repository_permission')
    if base != 'none':
        msg = f'{ORG} gives all members "{base}" access to every repo; set base permissions to "No permission"'
        if apply:
            sys.exit(f'{msg} before running with --apply.')
        print(f'WARNING: {msg}.')
    check(*api('GET', f'repos/{TEMPLATE}'), f'look up template {TEMPLATE}')

    teams = load_teams()
    failed = []
    for label, t in teams.items():
        if only and label.upper() not in only:
            continue
        try:
            provision(label, t, apply)
        except RuntimeError as e:
            print(f'  ERROR: {e}')
            failed.append(label)

    print(f'\n{"Done" if apply else "Dry run done; re-run with --apply to make these changes"}.'
          + (f' Failed: {", ".join(failed)}' if failed else ''))


if __name__ == '__main__':
    main()
