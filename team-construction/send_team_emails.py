"""Email each project team its assignment, cc'ing the team's mentor.

Reads one row per team (the format of team_sheet.csv, plus a mentor UCID
column). By default this is a dry run that only prints the emails; pass
--send to actually send them.

Usage:
  python3 send_team_emails.py [team_sheet.csv]           # dry run
  SMTP_PASSWORD=... python3 send_team_emails.py --send [team_sheet.csv]
"""
import csv
import getpass
import os
import smtplib
import sys
from email.mime.text import MIMEText

SENDER = 'mjk76@njit.edu'
DOMAIN = 'njit.edu'
EXTRA_CC = []                       # e.g. ['ta@njit.edu'] to cc staff on every email
SUBJECT = '[CS 490] Your project team: Team {section}-{team}'

# TODO: paste in the email template. Available fields:
#   {team}          team number, e.g. 7 or H2
#   {section}, {mentor}, {repo}, {title}, {notes}   straight from the CSV
#   {first_names}   e.g. "Alice, Bob, and Carol"
#   {member_list}   one "* Name (ucid@njit.edu)" line per member
template = """
{first_names},

This email is to let you know that our team assignment process has chosen you all as a group for the CS 490 group project. You’ll work together throughout the semester on the project plan, revised project plan, the various demos, and project final submission deliverables.

I strongly recommend that you all meet as soon as possible to get to know one another, if you don’t already. You should start designing your extension to Covey.Town as soon as possible: your initial project proposal is due on {TODO: due date}, AoE; the first demo is due by {TODO: due date}. We recommend that you start by sharing your individual proposals with each other.

Your mentor for this project is {mentor} (cc'd). You must meet with your mentor at least once this week and discuss what project ideas you are considering. I strongly recommend that you take your mentor's advice into account: each mentor understands what a high-quality project looks like and will help me determine your final grade.

You should also schedule a regular meeting time with {mentor}, which you’ll use each week for the rest of the semester for updates on your progress on the project. These meetings are MANDATORY: your grade will be (severely) reduced if you do not schedule and then attend them. (Note that not everyone needs to attend every week - we understand that emergencies happen and other things come up! But, your **team** needs to have the meeting every week.) I or another instructor may attend some of your mentor meetings throughout the semester, as our schedules allow. 

{mentor} will be in touch in a reply to this email with information about how to schedule meetings.

Professor Kellogg
"""


# Each field accepts any of several header spellings (matched case-insensitively).
TEAM = ('Team', 'Team #')
SECTION = ('Section',)
MENTOR = ('Mentor',)
MENTOR_UCID = ('Mentor UCID',)
REPO = ('GitHub repo', 'repo link')
TITLE = ('Feature / project title', 'project title')
NOTES = ('Notes',)


def member_name_cols(i):
    return (f'Member {i}', f'Member {i} name')


def member_ucid_cols(i):
    return (f'UCID {i}', f'Member {i} ucid')


def get(row, columns):
    """Case- and whitespace-insensitive column lookup; '' if absent."""
    wanted = {c.lower() for c in columns}
    for k, v in row.items():
        if k and k.strip().lower() in wanted:
            return (v or '').strip()
    return ''


def read_rows(path):
    """Rows as dicts, skipping any title/blank lines above the header row."""
    with open(path, newline='', encoding='utf-8-sig') as f:
        lines = list(csv.reader(f))
    for i, line in enumerate(lines):
        if line and line[0].strip().lower() in {t.lower() for t in TEAM}:
            header = [h.strip() for h in line]
            return [dict(zip(header, l)) for l in lines[i + 1:] if any(c.strip() for c in l)]
    sys.exit(f'{path}: no header row starting with one of {TEAM}')


def section_label(row):
    """Sheets drop leading zeros ("1" for section 001); put them back."""
    s = get(row, SECTION)
    return s.zfill(3) if s.isdigit() else s


def members(row):
    result = []
    for i in range(1, 6):
        name, ucid = get(row, member_name_cols(i)), get(row, member_ucid_cols(i))
        if ucid:
            result.append((name, ucid.lower()))
    return result


def build_message(row):
    ms = members(row)
    firsts = [name.split()[0] if name else ucid for name, ucid in ms]
    fields = dict(
        team=get(row, TEAM), section=section_label(row),
        mentor=get(row, MENTOR), repo=get(row, REPO),
        title=get(row, TITLE), notes=get(row, NOTES),
        first_names=', '.join(firsts[:-1]) + ', and ' + firsts[-1] if len(firsts) > 1 else firsts[0],
        member_list='\n'.join(f'* {name} ({ucid}@{DOMAIN})' for name, ucid in ms),
    )
    to_addrs = [f'{ucid}@{DOMAIN}' for _, ucid in ms]
    mentor_ucid = get(row, MENTOR_UCID).lower()
    cc_addrs = []
    for a in ([f'{mentor_ucid}@{DOMAIN}'] if mentor_ucid else []) + EXTRA_CC:
        if a.lower() not in cc_addrs and a.lower() not in to_addrs and a.lower() != SENDER:
            cc_addrs.append(a.lower())

    msg = MIMEText(template.format(**fields), 'plain', 'utf-8')
    msg['From'] = SENDER
    msg['To'] = ', '.join(to_addrs)
    if cc_addrs:
        msg['CC'] = ', '.join(cc_addrs)
    msg['Subject'] = SUBJECT.format(**fields)
    # cc'd addresses only receive the mail if they're in the envelope too
    return msg, to_addrs + cc_addrs


def main():
    args = sys.argv[1:]
    send = '--send' in args
    args = [a for a in args if a != '--send']
    path = args[0] if args else 'team_sheet.csv'

    messages = []
    for row in read_rows(path):
        label = f'{section_label(row)}-{get(row, TEAM)}'
        if get(row, NOTES).upper().startswith('EXAMPLE ROW'):
            continue
        named = [get(row, member_name_cols(i)) for i in range(1, 6)
                 if get(row, member_name_cols(i)) and not get(row, member_ucid_cols(i))]
        if named:
            print(f'WARNING: team {label}: no UCID for {", ".join(named)}; '
                  f'{"they" if members(row) else "the whole team"} will not be emailed', file=sys.stderr)
        if not members(row):
            continue
        if not get(row, MENTOR_UCID):
            print(f'WARNING: team {label} has no mentor UCID; mentor will not be cc\'d', file=sys.stderr)
        messages.append(build_message(row))

    if 'TODO' in template:
        print('WARNING: the email template is still a TODO', file=sys.stderr)

    if not send:
        for msg, recipients in messages:
            headers = ''.join(f'{k}: {v}\n' for k, v in msg.items() if k not in
                              ('Content-Type', 'MIME-Version', 'Content-Transfer-Encoding'))
            print(headers + msg.get_payload(decode=True).decode('utf-8'))
            print(f'[envelope recipients: {", ".join(recipients)}]\n' + '=' * 70)
        print(f'Dry run: {len(messages)} emails not sent. Re-run with --send to send them.')
        return

    password = os.environ.get('SMTP_PASSWORD') or getpass.getpass(f'App password for {SENDER}: ')
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(SENDER, password)
        for msg, recipients in messages:
            smtp.sendmail(SENDER, recipients, msg.as_string())
            print(f'sent: {msg["Subject"]} -> {", ".join(recipients)}')


if __name__ == '__main__':
    main()
