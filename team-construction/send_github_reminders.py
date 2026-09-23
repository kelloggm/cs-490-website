"""Email each student who still needs to give us a (valid) GitHub username.

Reads roster.csv from build_roster.py and emails every student whose status
isn't "ok", one email per student. Any other CSV with ucid and name columns
works too (e.g. github_overrides.csv); if it has no status column, everyone
in it is emailed. By default this is a dry run that only prints the emails;
pass --send to actually send them.

Usage:
  python3 send_github_reminders.py [roster.csv]           # dry run
  SMTP_PASSWORD=... python3 send_github_reminders.py --send [roster.csv]
"""
import csv
import getpass
import os
import smtplib
import sys
from email.mime.text import MIMEText

from send_team_emails import DOMAIN, SENDER

EXTRA_CC = []                       # e.g. ['ta@njit.edu'] to cc staff on every email
SUBJECT = '[CS 490] You have not yet provided a valid GitHub username to the CS 490 staff'

# TODO: paste in the email template. Available fields:
#   {first_name}, {name}, {ucid}
#   {team}, {section}    e.g. 7 and 001, or H2 and HM1
#   {status}             "missing" (no usable answer) or "not-found" (no such GitHub account)
#   {given_handle}       what they gave us, if anything ('' when status is missing)
template = """
{first_name},

Our records indicate that your username was "{status}", meaning:
* "missing": you did not complete the team formation survey,
which was due by the end of the day on Friday, September 18, or
* "not-found": you did complete the survey, but the GitHub username
that you provided is invalid (e.g., because it does not exist).
Perhaps you made a typo.

Either way, we require your username to invite you to your team's
private GitHub repository, which we will create on your behalf. Fill
out {TODO: form link} by the end of the day on
{TODO: deadline - usually two days}. If you fail to do so, we will add a reading
quiz with a score of zero to your gradebook in the course.

Dr Kellogg
"""


def read_students(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        rows = list(csv.DictReader(f))
    if rows and 'status' in rows[0]:
        rows = [r for r in rows if r['status'] != 'ok']
    return rows


def build_message(row):
    ucid = row['ucid'].strip().lower()
    name = row.get('name', '').strip()
    team = row.get('team', '').strip()
    section = row.get('section', '').strip()
    if '-' in team and not section:  # github_overrides.csv has team as "001-7"
        section, team = team.split('-', 1)
    status = row.get('status', 'missing').strip()
    fields = dict(
        first_name=name.split()[0] if name else ucid, name=name, ucid=ucid,
        team=team, section=section, status=status,
        given_handle=row.get('github', '').strip() if status != 'missing' else '',
    )
    to_addrs = [f'{ucid}@{DOMAIN}']
    cc_addrs = [a.lower() for a in EXTRA_CC if a.lower() not in to_addrs and a.lower() != SENDER]

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
    path = args[0] if args else 'roster.csv'

    messages = []
    for row in read_students(path):
        if not row.get('ucid', '').strip():
            print(f'WARNING: no UCID for {row.get("name", "?")}; they will not be emailed', file=sys.stderr)
            continue
        messages.append(build_message(row))

    if 'TODO' in template or 'TODO' in SUBJECT:
        if send:
            sys.exit('The email subject or template is still a TODO; not sending.')
        print('WARNING: the email subject or template is still a TODO', file=sys.stderr)

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
