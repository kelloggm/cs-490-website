# Provisioning private team repositories for a project course

**For the human reading this:** this directory holds a small toolchain that takes a roster of
project teams and a survey of students' GitHub usernames, and creates one private GitHub
repository per team, seeded from a template repo, with the team's students and their mentor
added to it. It replaces GitHub Classroom. The rest of this file is written for an AI coding
assistant rather than for you: the intended way to use it is to open an agentic assistant
(Claude Code, or similar) in this directory and say something like *"read README.md and help me
provision the team repositories for this semester."* The assistant will ask you for what it
needs and walk you through the steps below, including the parts that need your judgement. You
can of course read on, but you do not have to: nothing here is a manual you must follow yourself.

---

## Instructions for the assistant

You are helping an instructor provision private GitHub repositories for the project teams in
their course. Work through the phases below in order. The instructor is the decision-maker:
surface choices, recommend a default, and do not create repositories or send email until they
have seen a dry run and said to proceed.

### The pieces

| File | Role |
| --- | --- |
| `build_roster.py` | Joins the team sheet to the survey responses, cleans and verifies GitHub usernames, writes `roster.csv`, reports who is still missing. |
| `provision_repos.py` | Creates a GitHub team + private repo per project team from a template, grants access, invites students and mentors. Idempotent; dry run by default. |
| `send_github_reminders.py` | Emails the students who still owe a valid username. |
| `send_team_emails.py` | Emails each team its assignment, cc'ing the mentor. Also the shared CSV-parsing helpers the other scripts import. |
| `make_teams.py` | Forms the teams in the first place from individual project proposals (constraint-based assignment). Separate concern, run earlier in the semester. |
| `make_lookup_page.py` | Generates a course-website page where a student can look up their team by UCID. Stores only salted hashes. |

These are Python 3 scripts with no dependencies beyond the standard library and the `gh` CLI.
Do not port them to Octokit/Node unless asked; a previous iteration deliberately moved away from
that to avoid a Node version dependency.

### Data the instructor must supply

The scripts read CSVs that are **not** in the public repo, because they contain student records.
Ask for them and confirm the column names before running anything:

1. **A team sheet** (`team_sheet.csv`), one row per team: `Team`, `Section`, `Mentor`,
   `Mentor UCID`, then `Member N` / `UCID N` pairs for up to five members, plus `Notes`. A row
   whose `Notes` begins with `EXAMPLE ROW` is a template row and is skipped everywhere. Header
   spellings are matched case-insensitively and several variants are accepted; see the tuples at
   the top of `send_team_emails.py`. Sections are zero-padded, so `1` becomes `001`.
2. **Survey responses** with each student's GitHub username, exported from a form. List every
   export in `SURVEYS` in `build_roster.py`; sections are often surveyed separately, and columns
   are matched by header *prefix* because the wordings differ between forms.
3. **A template repository** on GitHub, marked as a template (`is_template: true`). It may live
   under the instructor's personal account rather than the org.
4. **A GitHub organization** for the semester, plus `gh auth login` as an org owner with the
   `admin:org` and `repo` scopes (`gh auth refresh -h github.com -s admin:org`).

### Phase 1 — build the roster

Run `python3 build_roster.py`. It writes `roster.csv` and prints every student it could not
resolve. Expect to iterate here. What it already handles, so you do not need to re-solve it:

- Usernames pasted as URLs, as `handle (https://github.com/handle)`, or with stray whitespace.
- Duplicate survey submissions: the latest timestamp wins.
- Students who answered a survey but whose UCID is absent from the team sheet: matched by first
  and last name, which tolerates middle names and the "full legal name" variants students use.
- Every username is checked against the GitHub API, so typos and dead accounts surface as
  `not-found` rather than failing later.

Hand-collected corrections go in `github_overrides.csv` (`ucid,name,team,github,note`), which
takes priority over the surveys. When replies to reminder emails arrive as a new form export,
merge them into that file, keyed on UCID, then re-run.

Report the remaining gaps to the instructor grouped by team, and flag likely drops separately;
they usually know which students have vanished.

### Phase 2 — chase the missing usernames

`send_github_reminders.py` emails everyone in a CSV whose `status` is not `ok`. Default input is
`roster.csv`; pass a filtered file to email a subset. **Always pass an explicit file if a
previous batch has already been emailed** — re-running the default will mail everyone again.

The message body and subject are the instructor's to write; leave them as `TODO` and ask. The
script refuses to send while either is still `TODO`. Sending needs `SMTP_PASSWORD` (a Gmail app
password) and `--send`; without `--send` it prints the messages for review. Show the instructor
the dry run first, every time.

### Phase 3 — check the organization settings

Before provisioning, verify with `gh api orgs/<org>`:

- **`default_repository_permission` must be `none`.** GitHub defaults it to `read`, which would
  let every student in the org read every other team's private repository. `provision_repos.py`
  refuses to run with `--apply` until this is fixed. This is the single most important check in
  the whole process.
- `members_can_create_repositories` is best set to `false`.
- Check the plan. Organization invitations are rate-limited per 24 hours, and a free org's limit
  is low enough that a course of ~130 students will hit it; a Team plan (GitHub Education grants
  one) raises it to 500/day. If the limit is hit, affected teams report an error and a re-run the
  next day finishes the job.

### Phase 4 — provision

Set `ORG`, `TEMPLATE`, and `MENTOR_GITHUB` (mentor UCID → GitHub username) at the top of
`provision_repos.py`, and confirm the naming scheme in `repo_name()`. The default is
`au26-001-team-07`, `au26-hm1-team-h3`: it includes the section because team numbers repeat
across sections, and the same string is used for both the repo and the GitHub team. Verify
mentor usernames against the API before trusting them; display names are a good sanity check.

Then:

1. `python3 provision_repos.py` — full dry run, no changes. Show the instructor the counts.
2. `python3 provision_repos.py --only <one-team> --apply` — a live test on a single team, ideally
   one the instructor mentors themselves.
3. Verify that test independently of the script's own output, then run
   `python3 provision_repos.py --apply` for the rest.

Every step checks current state first, so re-running is safe and is the normal way to add
students whose usernames arrived late. Re-running does not re-invite anyone.

### Phase 5 — verify

Do not report success from the script's log alone; audit against the roster by querying GitHub:
each repo private and generated from the template, exactly one team holding `push` on it, and
each team's membership equal to its roster plus its mentor. A team's full membership is its
accepted members *plus* its pending team invitations, since invitees do not appear as members
until they accept.

Two things that look like bugs but are not:

- **Org owners are listed as implicit maintainers of every team.** An audit will report the
  instructor as "extra" on teams they were never added to. Harmless.
- **Students show as pending for days.** An invitation grants nothing until accepted; the repo
  simply does not appear for them until then. Expect to re-check acceptance rates and nag.

### Things that have bitten this code before

- `subprocess` with `text=True` normalizes CRLF to LF, so an HTTP response parsed out of
  `gh api --include` splits on `\n\n`, not `\r\n\r\n`. Getting this wrong silently yields empty
  response bodies that only break on the *second* run, when resources already exist.
- A `404` from the GitHub API still has a JSON body (an error message), so test the status code,
  not the truthiness of the parsed body, when deciding whether something exists.
- Repository generation from a template is asynchronous; poll until the repo is readable before
  assigning permissions.

### Working style for this task

The instructor is an experienced software engineer and reads the code. Prefer small standard
library scripts over new dependencies, match the existing style, and keep dry-run-by-default and
idempotency in anything you add. Student data is sensitive: keep it in this working directory,
never commit it, and never send it anywhere other than GitHub and the students themselves. When
generating a file that will be copied into a public repo, check it for names, UCIDs and email
addresses first.
