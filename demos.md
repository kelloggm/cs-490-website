---
layout: page
title: Project Demos
permalink: /projects/project-demos.html
parent: Projects
nav_order: 7
---

# Demos

Each group project team must do at least five demos of various types during the semester.
Some demos will be just your group project mentor, some may be
for the instructor (and your group project mentor), and at least one will be for the whole class.

**Honors teams**: Honors teams are made up entirely of Honors students, and we hold Honors projects to a higher
standard: significantly more ambition than average, significantly more polish, and scaling up to larger numbers
of concurrent users. Demos are where the polish expectation is most visible: our minimum standard for an Honors
team is "no bugs in demos". The rubrics below apply to every team, but when we grade an Honors team's demo we
expect it to be smooth and free of visible defects, not merely functional.
See the [syllabus](../about/#honors-section) and the [project overview](../projects/project-overview.html#honors-projects).

## Deployment Demo

**Due Friday 2 October 2026, 5:30pm EDT**{: .label .label-red }

In this demo, you'll show that you can build and deploy covey.town on a publicly-accessible
server. You'll do this demo with just your group project mentor, during your regular standup
meeting during the week of September 28-October 2. This demo comes early on purpose: deployment
problems are much cheaper to fix at the beginning of the project than at the end of it.

There are two requirements for this demo:
* you provide your group project mentor with a link that they can follow that allows them to join a covey.town
instance controlled by you.
* that instance contains any one visible change from the starter code (e.g., text on the login page that says "hello world"
or something equally simple), to show that this version really has been modified by your team.

There are many ways to deploy covey.town so that it is remotely accessible. The easiest is probably to set up
a free-tier AWS instance (by following [our guidelines](../tutorials/ubuntu.html)) and then set it to allow
incoming traffic on the appropriate ports used by covey.town; see the covey.town documentation for more details.

### Rubric (out of 10 points, 1% of final project grade)

There are only two possible grades for this demo: 0 or 10.

#### Meets minimum requirements:
* Provided link leads to a running covey.town instance.
* Running covey.town instance contains at least one modification that shows that your team controls it.

## Wizard-of-Oz Demo

**Due Friday 16 October 2026, 5:30pm EDT**{: .label .label-red }

The next demo is the ["Wizard-of-Oz"](https://en.wikipedia.org/wiki/Wizard_of_Oz_experiment) demo.
In this demo, you'll show what your project will look like when it is finished. In this demo, you don't
need to actually have any of your code working yet: instead, you'll "fake" working code to show off
your vision for your finished project.

How you fake your finished project is up to you, and will probably vary quite a bit between projects.
Some options include:
* using a professional design tool, such as [Figma](https://www.figma.com/). Figma will give you a
[free license](https://www.figma.com/education/higher-education/) because you are a student.
* using PowerPoint or a similar slideshow tool to build slides that look like your finished feature.
You can use slide animations or transitions to show what your feature will look like in action.
* doing the same using a professional animation tool, such as Adobe Animate or a similar tool
* building a "paper prototype" of the feature, and manually transitioning between its states
* anything else you can imagine.

The key is that you need to convince the course staff that you've thought through how your feature will
behave in enough detail to implement it.

Aim for your demo to take about five minutes, and to showcase all of your feature's user stories
from your revised project proposal. The demo will usually occur during your regular weekly meeting with your
project mentor during the week that the demo is due, which the instructor will try to attend. In the event of a conflict, the instructor will let
you know the week beforehand, but it will be up to you to schedule an alternative slot that all of you,
your project mentor, and the instructor can attend before the deadline.

### Rubric (out of 25 points, 2% of final project grade)

#### Satisfactory:
* Demo materials are professional in appearance
* Demo is about five minutes long
* Demo showcases all user stories from revised project proposal
* Feature(s) demonstrated are plausible to implement

#### Meets minimum requirements:
* Demo is between 3 and 7 minutes long
* Demo showcases at least two user stories from the revised project proposal

## Preliminary Demo 1: With Your Mentor

**Due Friday 30 October 2026, 5:30pm EDT**{: .label .label-red }

This is the first demo in which you show your own working code. By the end of your third sprint,
you should have real, running code for at least one of the user stories from your revised project
plan, even if that user story isn't finished yet. Focus the demo on whatever you have working.

You'll do this demo with just your group project mentor, during your regular standup meeting
during the week of October 26-30. The instructor will not attend: the point of this demo is to
give you a low-stakes checkpoint on real code, and to give your mentor a chance to tell you if
you're behind before it becomes expensive.

For this demo, your code must be deployed in a covey.town instance (but the instance is permitted
to be local to the demo laptop). All demonstrated feature(s) must be implemented: you may not
"fake" them as you could in the Wizard-of-Oz demo. All code used in the demo must be committed to
your project GitHub repository and should have been reviewed by at least one team member other
than its author.

Aim for your demo to take about five minutes.

### Rubric (out of 20 points, 2% of final project grade)

#### Satisfactory:
* Demo shows working code for at least one user story from the revised project plan
* Code is checked into your project GitHub repository and has been through a code review
* Code is demonstrated in a running covey.town instance
* Demo takes about 5 minutes
* At least half of the team has authored a pull request that was merged after a code review

#### Meets minimum requirements:
* Demo shows working code related to your project
* Code is checked into your project GitHub, and no code was pushed directly to `main` without a review
* Code is demonstrated in a running covey.town instance
* Demo takes between 3 and 7 minutes

#### Honors teams:
For a satisfactory demo, we additionally expect that whatever you choose to show is polished: no
visible bugs, no crashes, and no rough edges that you have to explain away. Showing less, but
showing it cleanly, is the better choice for an Honors team.

## Preliminary Demo 2: With the Instructor

**Due Friday 20 November 2026, 5:30pm EST**{: .label .label-red }

By the second preliminary demo, you should have a significant part of the coding for your
feature completed. In this demo, you should show that at least one of the user
stories from your revised project proposal is substantially complete. Focus the
demo around that user story.

For this demo, your code must be deployed in a covey.town instance (but the instance is
permitted to be local to the demo laptop). All demonstrated feature(s) must be implemented:
you may not "fake" them as you could in the Wizard-of-Oz demo. All code used in the demo
must be committed to your project GitHub repository and should have been reviewed by at
least one team member other than its author. Also, by this point we expect that every team member has participated in at least one code review as a code author and at least one review as a reviewer.

Aim for your demo to take about five minutes. The demo will usually occur during your regular weekly meeting with your
project mentor during the week that the demo is due, which the instructor will try to attend. In the event of a conflict, the instructor will let
you know the week beforehand, but it will be up to you to schedule an alternative slot that all of you,
your project mentor, and the instructor can attend before the deadline.

### Rubric (out of 40 points, 4% of final project grade)

#### Satisfactory:
* Demo shows a user story from the revised project proposal
* Demo is fully functional (no crashes, unexplained hangs, etc.)
* Code is checked into your project GitHub repository and has been through a thorough code review (note: a portion of the grade for this demo
is based on the quality of your code reviews up to this point)
* Code is demonstrated in a running covey.town instance
* Demo takes about 5 minutes
* Each team member has authored at least one PR that has been merged after a thorough code review
* Each team member has participated in at least one PR as a reviewer

#### Meets minimum requirements:
* Demo shows working code related to your project
* Code is checked into your project GitHub, and no code was pushed directly to `main` without a review
* Code is demonstrated in a running covey.town instance
* Demo takes between 3 and 7 minutes
* Each team member has contributed to the team's GitHub repo, either as a code author or as a reviewer

#### Honors teams:
For a satisfactory demo, we additionally expect that the user story you demonstrate is polished: no visible bugs,
no crashes, and no rough edges that you have to explain away.

## Final Demo

See the [project deliverables](../projects/project-deliverable.html#10-final-demonstration) page.