# CS 490 course website (Fall 2026 / "Au26")

Jekyll site for NJIT CS 490-001, deployed to GitHub Pages at
`https://kelloggm.github.io/cs-490-website/`.
The site is being prepared to go live for Au26 while some late-semester details are still
unsettled, so **it must always be presentable to students even when incomplete**. Two
distinct placeholder conventions enforce that split:

- **`TBD` is student-facing.** It means "we know this is unknown and we are fine with
  students seeing it." Use it for unset dates: a bare `TBD` on a `_modules/week-NN.md`
  date line, `| TBD |` in `project-overview.md`'s deliverables table, `Office Hours: TBD`
  in `_staffers/`. **No `TODO` may ever reach the rendered site.**
- **`TODO(au26)` in an HTML comment is internal.** These are the instructor's notes to
  self, invisible to students, and they carry the constraints needed to resolve the item
  (exam period, last day of class, what depends on what). Leave them in place until the
  item is actually resolved; do not convert one to `TBD` and drop its reasoning.

A resource that does not exist yet — a form, a signup sheet — is not a `TBD`; it gets a
link to the coming-soon page (see "Placeholder links" below).

## Deployment

**Pushing to `au26` deploys the site.** `.github/workflows/pages.yml` builds it and
publishes to GitHub Pages; there is no manual copy step, and co-instructors with write
access can update the site themselves. The deploy branch is named in exactly one place ---
the `branches:` list in that workflow --- so a new semester means changing it there.

The workflow deliberately does **not** gate the deploy on the `TODO` check below: a
stray `TODO` is cheap to notice and fix, and a build that refuses to publish over one
would be worse than the problem. Keep checking by hand (see "Verification recipes").

The workflow builds with `--baseurl` supplied by GitHub Pages itself, so `_config.yml`'s
`baseurl: '/cs-490-website'` matters only for local preview. Renaming the repository
changes the live URL but does not break the build.

Two settings live on GitHub, not in this repo, and both bit once during setup:

- Pages' source must be **GitHub Actions**, not the legacy branch build.
- The `github-pages` *environment* has a deployment branch policy. It shipped allowing
  only `main`, which makes `build` pass and `deploy` fail with "Branch is not allowed to
  deploy to github-pages". It now allows `au*` and `sp*`, so a new semester branch needs
  no settings change --- but a branch named outside those patterns would.

`_config.yml`'s `exclude:` must keep `vendor` --- CI installs gems into `vendor/bundle`
inside the workspace, and without the exclude Jekyll tries to build the jekyll gem's own
site template and fails the whole build.

Historically the site was built locally and `cp -r`'d into the personal website
(`../martinjkellogg.com/teaching/cs490-au26/`) by `replace.sh`, which is why the old URLs
are nested under `/teaching/` --- that arrangement predates Pages, from when the personal
site was on an NJIT server. Those old URLs are now **redirect stubs** pointing at the live
site (one per page, plus `index.md` on the personal site); the PDFs and images under that
path were deliberately left in place so old deep links to them still resolve.

`replace.sh` survives for one purpose: **run it once after the semester ends** to overwrite
those stubs with a frozen copy of the final site, so `teaching/cs490-au26/` becomes a
permanent archive like every previous semester --- do this before pointing the workflow at
the next semester's branch, which takes over the live URL.

## Build and check

```bash
bundle exec jekyll build        # writes _site/ (gitignored); ~3s
bundle exec jekyll serve        # local preview
```

A `faraday-retry` warning on every build is harmless. The build almost never fails on bad
content — it will happily render broken links and mismatched numbers, so **verify by
inspection, not by exit code** (see "Verification recipes" below).

## Repo layout

- **Content pages live flat in the repo root** (`about.md`, `ip0.md`, `demos.md`, …). The
  file's location on disk says nothing about its URL; the `permalink:` in its front matter
  does. E.g. `individual-project-plan.md` → `/projects/individual-project-proposal.html`.
- `_modules/week-01.md` … `week-16.md` — the week-by-week **calendar**. `calendar.md` just
  loops over `site.modules`. Each entry is a definition list: a date line, then `: content`.
- `_layouts/` — `project.html` renders a `due_date:` front-matter field as a red "Due …"
  label; `page` (from the theme) does not. Pages with several deadlines (`demos.md`,
  `honors-essays.md`) use `layout: page` and put inline `{: .label .label-red}` labels on
  each one instead.
- `todo.md` → `/coming-soon.html` is the **placeholder landing page** for resources that
  are not posted yet. It is `nav_exclude`d and `search_exclude`d, so it never appears in the
  sidebar or search and does not affect anyone's `nav_order`.
- `_staffers/`, `assets/` (PDFs of lectures, readings, past exams), `tutorials/`.
- **Office hours are structured data, and the only generated content on the site.** Each
  `_staffers/*.md` carries an `office_hours:` list (`day`, `start`, `end`, `location`, with
  `location: TBD` for unassigned rooms) plus an optional `by_appointment: true`. Two consumers
  read it: `_layouts/staffer.html` renders it back into the prose sentence the staff page has
  always shown (`Office Hours: Mondays, 4:30 PM--5:30 PM (location TBD); ...; or by appointment.`),
  and `office-hours.md` -> `/office-hours/` builds a per-weekday table from `site.staffers`.
  **Never type a time or a room into `office-hours.md`** --- edit the staffer's file and both
  pages update. Times are human-readable (`'4:30 PM'`); the page sorts them with the existing
  `_includes/minutes.liquid`, zero-padded to four digits so the sort is lexicographic. The
  layout still honours the theme's old scalar `office-hours:` field if a file ever sets it.
- `*.md~` files are **stale editor backups from previous semesters**. Ignore them; they are
  gitignored and do not reflect the current site.

## Navigation

Nav is `parent:` + `nav_order:` front matter, rendered by just-the-docs. Current Projects
section order:

| nav_order | page | | nav_order | page |
|---|---|---|---|---|
| 1 | `ip0.md` | | 6 | `demos.md` |
| 2 | `project-overview.md` | | 7 | `contribution-report.md` |
| 3 | `individual-project-plan.md` | | 8 | `project-deliverable.md` |
| 4 | `project-plan.md` | | 9 | `surveys.md` |
| 5 | `revised-project-plan.md` | | 10 | `optional-readings.md` |
| | | | 11 | `honors-essays.md` |

Top-level nav is ordered by relative importance / frequency of access, and every top-level page
carries an explicit `nav_order`: `calendar.md` 1, `about.md` 2, `projects.md` 3, `exam.md` 4,
`tutorials.md` 5, `style.md` 6, `staff.md` 7, `office-hours.md` 8. `style.md` is a top-level page despite its
`/policies/style/` permalink --- there is no Policies section.

Inserting a page mid-sequence means renumbering the ones after it.

## Link conventions

`permalink: pretty` is on. **Relative links resolve against the permalink directory, not the
source file's location.** From any `/projects/*.html` page, the syllabus is `../about/`, a
tutorial is `../tutorials/foo.html`, and a sibling is `../projects/foo.html`. Some pages use
`{{ site.baseurl }}{% link foo.md %}` instead, which is more robust; both styles are in use.

**Placeholder links.** A link to a resource that does not exist yet points at
`{{ site.baseurl }}{% link todo.md %}` and is tagged with a yellow label so the reader can
see it is not live:

```markdown
Your team can sign up for a slot ([signup sheet]({{ site.baseurl }}{% link todo.md %}) **coming soon**{: .label .label-yellow }).
```

Currently eight such links: the team formation survey plus four project surveys in
`surveys.md`, the reading question form and the demo signup sheet in `_modules/week-15.md`,
and the signup sheet in `project-deliverable.md`. Replacing one means deleting the label along with the URL.

**External course links** live in `aux_links:` in `_config.yml`, which renders them as
buttons in the top bar: `Canvas (001)`, `Canvas (003)`, `Canvas (HM1)`, and `Discord`.
There is **no Gradescope this semester** — do not re-add it. The three Canvas courses are
per-section, so in-text links must name the section:

```markdown
Canvas ([section 001](.../68176), [section 003](.../72692), [section HM1](.../68186))
```

`honors-essays.md` is the one exception: Honors students are all in HM1, so it links to
the HM1 course alone. Canvas is linked from clean submission instructions only; where it
is mentioned mid-paragraph (`project-deliverable.md`'s release instructions,
`optional-readings.md`) it is deliberately left unlinked to avoid breaking the prose.

`heading_anchors: true` gives every heading a slugified id, so headings are link targets.
Two consequences:

- **Renaming a heading breaks inbound anchors.** Several rubric headings embed their weight
  (`### 20% Delivered Features` → `#20-delivered-features`), so changing a percentage
  changes the anchor. `demos.md` links to `project-deliverable.html#10-final-demonstration`.
- Duplicate heading text gets a `-1` suffix. `project-deliverable.md` has both
  `#### Individual Reflection` (submission instructions) and `## Individual Reflection` (the
  assignment), so the assignment's anchor is `#individual-reflection-1`, which
  `project-overview.md` and `_modules/week-15.md` both link to.

## Au26 course structure (as currently committed)

Course grade: **45% exams** (mid-term 1 10%, mid-term 2 15%, final 20%) / **45% project** /
**10% participation & professionalism**. There is no separate "individual assignments"
category — IP0 and the individual reports are graded inside the project.

Project internals, non-Honors / Honors (each column sums to 100):

- Individually graded **9 / 13**: IP0 1, Individual Contribution Report 3, individual
  reflection 5, plus (Honors only) two Honors Reflection Essays at 2 each.
- Team graded **91 / 87**: Honors team weights are the non-Honors values × 87/91, rounded to
  one decimal, with the rounding drift absorbed on "Final implementation" (the only unique
  base value, so no two sibling rows disagree). The student-facing text says only "scaled down
  in the expected way"; the ratio lives in an HTML comment under the table in
  `project-overview.md`. Do not put the ratio back into the prose.

Timeline: IP0 due Sep 8 → proposal Sep 16 → teams announced Sep 21 → **six two-week sprints,
Sep 21–Dec 9** (S0 Sep 21–Oct 2, S1 Oct 5–16, S2 Oct 19–30, S3 Nov 2–13, S4 Nov 16–27,
S5 Nov 30–Dec 9). Preliminary plan Oct 7, revised plan Oct 21 (the Wizard-of-Oz demo deliberately falls
between them, and is graded against the *preliminary* plan's user stories). Demos: deployment Oct 2,
Wizard-of-Oz Oct 16, preliminary 1 (mentor only) Oct 30, preliminary 2 (mentor + instructor)
Nov 20, final in December. Contribution report Nov 13. Team surveys Oct 9 / Nov 6 / Nov 25 /
with the final reflection.

Honors students are placed on all-Honors teams and held to a higher project standard
(more ambition, "no bugs in demos", scales to more concurrent users). That statement is
restated on every page where project expectations appear, each linking back to
`about.md#honors-section` and `project-overview.md#honors-projects`.

There is no IP1 — it was cut for Au26 and its page deleted. Do not reintroduce references
to it; the ambition yardstick in `individual-project-plan.md` now points at existing
Covey.Town features (conversation areas, viewing areas) instead.

## Cross-file invariants

Numbers and dates are deliberately duplicated across pages for the reader's benefit, which
means **almost any change needs to touch several files**:

1. **The weights table lives in two places.** `project-overview.md#summary-of-project-grading`
   is canonical; `project-deliverable.md#summary-of-grading` mirrors it (with
   "(already graded)" annotations) and says so in a sentence. Keep the numbers identical.
2. **Assignment pages restate their own weight** — `ip0.md`, `contribution-report.md`,
   `honors-essays.md`, and the individual-reflection section of `project-deliverable.md`.
   These must agree with the table.
3. **Rubric headings in `project-deliverable.md` embed percentages** in the heading text,
   and the meetings/surveys rubric repeats its percentage in prose.
4. **Every deadline appears twice**: on the assignment page and in the relevant
   `_modules/week-NN.md`. `project-overview.md`'s deliverables table is a third copy.
5. **The six-sprint list is duplicated verbatim** in `project-plan.md` and
   `revised-project-plan.md`.
6. **Office hours are the exception to all of this** --- they are generated, not duplicated.
   Change `_staffers/*.md` and nothing else; `staff.md` and `about.md`'s Coordination section
   link to `/office-hours/` but restate no times.
7. `surveys.md` describes each survey by its anchor event ("the week after the Deployment
   Demo"), so moving a demo invalidates its prose as well as its date.
8. **The per-section Canvas links are repeated in six submission instructions** —
   `ip0.md`, `contribution-report.md`, `project-plan.md`, `individual-project-plan.md`,
   `revised-project-plan.md`, and the individual-reflection section of
   `project-deliverable.md` — plus `honors-essays.md` (HM1 only) and `aux_links:`. The
   Discord URL appears in both `aux_links:` and `about.md`; both point at the server root,
   with no channel id.
9. Lectures and their readings live only in `_modules/`. Lectures can be reordered freely —
   there are few real dependencies — but check that anything the project needs (Process,
   Working in Teams, Requirements, Code Review) still precedes the deliverable that uses it,
   and that mid-term 1 on Oct 12 still covers the intended set. Both mid-terms must fall on a
   Monday: sections 001, 003, and HM1 are coordinated and hold joint exams.
10. **Only the first mid-term and the final have a "Your Choice" question**; the second mid-term
   has none. Stated in `about.md`, `exam.md`, and `optional-readings.md` --- keep all three in sync.
11. **The final demo is a private ten-minute slot with the instructor**, signed up for on a sheet;
   there is no whole-class showcase and it is not pinned to the last day of class. `demos.md`,
   `project-deliverable.md` (both the "Project Demo" logistics and the "10% Final Demonstration"
   rubric), `project-overview.md` and `_modules/week-15.md` all have to agree on that.
12. **Demos are the one exception to the blanket AoE deadline rule** --- they are due at 5:30pm
   local time. `project-overview.md` says so under the deliverables table; `demos.md` carries the
   four actual times.

## Gotchas learned the hard way

- **Anchoring text replacements on a Markdown heading is dangerous.** `"## Individual
  Reflection"` is a substring of `"#### Individual Reflection"`. A `str.index` on the former
  found the latter and silently truncated 175 lines out of `project-deliverable.md`. Anchor
  on `"\n## Heading\n"` with the exact hash count, assert the match count, and assert that
  the region you are about to replace does not contain sections you meant to keep.
- **Prefer `assert s.count(old) == 1` before every replacement.** Several of these files have
  near-duplicate paragraphs (the individual-reflection blurb appears in both
  `project-overview.md` and `project-deliverable.md` with one word different).
- **Jekyll renders Liquid in any `.md` file in the repo root, including this one.** Writing a
  literal `link` or `site.baseurl` Liquid tag as an *example* in a note file gets evaluated for
  real, and a bad path fails the whole build (this happened while writing this file).
  `CLAUDE.md` is therefore listed in `exclude:` in `_config.yml` — both so it does not publish
  to the public site and so its examples cannot break the build. Add any other internal notes
  file to that list too.
- **Do not parse `_site/*.html` with naive regexes.** `compress_html` strips closing tags, so
  `<td>(.*?)</td>` matches nothing. Parse the Markdown source instead.
- **These internal links are already broken and are not your fault**: `favicon.ico`
  (site-wide, theme-level), `assets/lecture-aiase.pdf` (not yet uploaded),
  `stackoverflow.com` in `about.md` (missing scheme), and two tutorial anchors
  (`#arrow-functions`, `#object-dependencies-in-useEffect`). A link check will always report
  them; anything else is new.

## Verification recipes

After editing weights:

```bash
# both columns of both tables must total 100
python3 - <<'EOF'
import re
for p in ('project-overview.md','project-deliverable.md'):
    n=h=0.0
    for line in open(p,encoding='utf-8'):
        m=re.match(r'^\|\s*(.+?)\s*\|\s*(\*\*)?([0-9.]+|---)%?(\*\*)?\s*\|\s*(\*\*)?([0-9.]+|---)%?(\*\*)?\s*\|\s*$',line)
        if not m or '**' in m.group(1): continue
        if m.group(3)!='---': n+=float(m.group(3))
        if m.group(6)!='---': h+=float(m.group(6))
    print(p, round(n,2), round(h,2))
EOF

# the two tables must agree row for row
diff <(grep -oE "\| [0-9.]+% \| [0-9.]+% \|" project-overview.md) \
     <(grep -oE "\| [0-9.]+% \| [0-9.]+% \|" project-deliverable.md)
```

No `TODO` may reach the rendered site. The only legitimate occurrence is the title of a
week 9 reading, "TODOs aren't for doing", which the `[^s]` excludes — note that a
`| grep -v` on the filename cannot work here, because `compress_html` puts each page on a
single line, so every match reports as line 1 with no usable context:

```bash
bundle exec jekyll build
grep -rnoE "TODO([^s]|$)" _site --include="*.html"   # must be empty
```

After editing dates, compare the assignment pages against the calendar:

```bash
grep -n "Due .*2026\|due_date:" *.md
grep -rn "due\*\*" _modules/*.md
```

## Working style that has worked here

The instructor reviews plans before implementation on multi-file changes: present the
schedule/weights/file list, settle open questions, then implement. Consistency analysis is
expected as part of the work — when asked to change one number, check what else states that
number. Flag pedagogical or workload trade-offs (lecture ordering vs. deliverable dates,
deadline clustering) rather than silently resolving them.
