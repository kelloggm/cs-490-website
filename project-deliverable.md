---
layout: page
title: Project Final Deliverable
permalink: /projects/project-deliverable.html
parent: Projects
nav_order: 9
---
Changelog:
# Project: Final Deliverable **Due 9 December 2026 11:59pm AoE**{: .label .label-red }

The final project deliverable is the implementation (in GitHub) and the documentation turned in to Canvas. It also includes your final demo.

## Project Implementation and Documentation

Your final team deliverable will be a "release" of your new feature on GitHub (with tests), and will be accompanied by a demo.
*Optionally,* you may also open a pull request to merge your feature into our main repository (submitting a pull request, or the pull request being merged into our
codebase is independent of the grade you receive, but provides a platform for more visibility of your project). 

### Contents

Your final team deliverable will include:
* The implementation of your new feature
* Automated tests for your new feature
* A report that describes how to use your new feature
    
Accompanying the final team deliverable will be an *individual reflection*, which every student must submit on their own. It has the same structure as the [Individual Contribution Report](../projects/contribution-report.html) from November---evidence of the code you wrote, the code you reviewed, and the status of the tasks assigned to you---followed by a substantially longer reflection covering:
* The evolution of your project concept: How does the project that you delivered compare to what you originally planned to deliver? What caused these deviations?
* The software engineering processes that you feel could have been improved in your project: were there any processes that in hindsight, you wish that you followed, or wish that you followed better?
* Your team dynamic: Provide a frank (and ideally, blameless) postmortem of your and your teammates collaborative performance and participation. If you had to do this same project over with the same teammates, what would *you* have done differently (or not) to improve your team's overall performance?


### Submission Instructions

#### Code and documentation
 After you have pushed all of your code (and documentation) to your team's GitHub repository, create [a release](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/managing-releases-in-a-repository) on GitHub, and apply the tag version `final-submission`. After your release is created, you'll find that there is now a `.zip` that can be downloaded from GitHub that contains a snapshot of your entire repository. Download this zip file, unpack it, and follow the instructions that you provided in your README to double-check that the course staff will be able to run your project locally (this step is handy to make sure that you didn't forget to include some key files in git). If needed, you can delete the release, make some changes, and re-release up until the deadline. **Submit this zip file to Canvas** under the assignment "Project: Code Submission". Submit your report separately to Canvas, under the assignment "Project: Report".

#### Project Demo

<!-- TODO(au26): set the demo window in the paragraph below. Our last regular class meeting
     is Wed Dec 9, the university's last day of classes is Sun Dec 13, and the reading days
     are Dec 14 and Dec 15. The Au25 wording was "the last day of class and the two reading
     days immediately thereafter". -->

You will make a live (in-person) demo to the instructor in the last week of classes. Your demo must last for no longer than ten minutes.
Your team can sign up for a slot (TODO: link to this semester's signup sheet);
slots are available TODO.
Make sure that at least one member of your team has a laptop that can access your deployed covey.town instance with them when you arrive for your
demo. Because demos are short and often scheduled back-to-back, if your whole team is not present and ready to start your demo at the time that you've
signed up for, you will lose your slot and you will have to sign up for a later one.
 
#### Individual Reflection
Create a PDF of your reflection, and submit it to Canvas ([section 001](https://njit.instructure.com/courses/68176), [section HM1](https://njit.instructure.com/courses/68186); section 003's Canvas link is TBD), under the assignment "Project: Individual Reflection". 

## Grading
Each project will be graded by the team's assigned mentor and one other member of the course staff (including at least one instructor). We do not expect all teams to deliver all of the features that were initially proposed - in the (relatively short!) implementation period, there are sure to be some teams that encounter unexpected technical hurdles. As described in greater detail in the rubrics below, teams that have regular communication with their mentor regarding their project status may be permitted variances to their project scope. For most of the submission components below, we provide two benchmark rubrics: one for a submission that is satisfactory (full marks), and one that would be meeting our minimum expectations (a pass). In practice, when grading projects we will usually assign numeric grades and provide partial credit, using these rubrics as guidelines for those two extremes. 

In cases where team members do not equally contribute to the project, we may assign different grades to different individuals, up to an extreme of deducting 50% of the marks from a student. We will evaluate each individual's contribution on the basis of a variety of factors, including progress reports at meetings with your mentor, through inspecting version control history, through each student's self-reflection, and through each team's (or student's) peer evaluations during and/or at the end of the project. We will make regular efforts to collect and distribute this feedback throughout the project. Our ultimate goal is for all students to participate and receive full marks.

### Honors Projects

Honors teams are made up entirely of students from the Honors section, and we hold Honors projects to a higher
standard than other projects. When we apply the rubrics below to an Honors team, we expect that the delivered
project:
* is significantly more ambitious than the average project in the class,
* is significantly more polished---in particular, we expect to encounter _no bugs_ while testing an honors project,
* scales up to larger numbers of concurrent users than a typical project would (and that your report and your
tests give us some evidence that it does), and
* the engineering process used by the team (and therefore the Technical and Process Overview documents) show a high level of sophistication, taking advantage of some of
the more advanced techniques that we discussed in lecture, as appropriate to the project.

An Honors project that would be "satisfactory" from a non-Honors team may not receive full marks.
See the [syllabus](../about/#honors-section) and the [project overview](../projects/project-overview.html#honors-projects).

### Summary of grading

The canonical version of this table is on the [project overview](../projects/project-overview.html#summary-of-project-grading) page.

| Component | Non-Honors | Honors |
| --------- | ---------- | ------ |
| **Individually graded** | **9%** | **13%** |
| Individual Project 0 (already graded) | 1% | 1% |
| Individual Contribution Report (already graded) | 3% | 3% |
| Individual reflection | 5% | 5% |
| Honors Reflection Essays (2 essays, worth 2% each) | --- | 4% |
| **Team graded** | **91%** | **87%** |
| Preliminary Project Plan (already graded) | 5% | 4.8% |
| Revised Project Plan (already graded) | 8% | 7.6% |
| Meetings with mentor and team surveys | 5% | 4.8% |
| Ongoing development progress, including code reviews | 10% | 9.6% |
| Deployment demo (already graded) | 1% | 1% |
| Wizard-of-Oz demo (already graded) | 2% | 1.9% |
| Preliminary demo 1, with your mentor (already graded) | 2% | 1.9% |
| Preliminary demo 2, with the instructor (already graded) | 4% | 3.8% |
| Final demo | 10% | 9.6% |
| Final implementation of your feature | 20% | 19% |
| Final test suite of your feature | 10% | 9.6% |
| Report: Feature Overview | 4% | 3.8% |
| Report: Technical Overview | 5% | 4.8% |
| Report: Process Overview | 5% | 4.8% |

Each column adds up to 100%; this sum is worth 45% of the course grade.

Here are the detailed rubrics for the final deliverables:
### 20% Delivered Features 
We will grade each delivered project holistically using the following two rubrics:

#### Satisfactory:
* Implemented feature satisfies the conditions of satisfaction as proposed by the team and as agreed to by the course staff. If technical difficulties resulted in features being dropped, the project may still earn full marks on "delivered features," but these difficulties must have been documented with the course staff as you encountered them during development.
* Implemented feature can be deployed locally following the instructions provided with the code submission in its README without any debugging by the course staff.
* Implemented feature contains no ESLint warnings or errors; does not include any eslint-disable or ts-ignore flags
* New code follows our course [style guide]({{ site.baseurl }}{% link style.md %}): names follow its conventions, and public properties and methods (other than getters, setters, and constructors) are documented with JSDoc-style comments

#### Meets minimum requirements:
* Implemented feature largely satisfies acceptance criteria as proposed by the team, but may not meet the course staff’s interpretation of those criteria.
* Implemented feature can be deployed locally following the instructions provided with the code submission in its README, with minor debugging by the course staff (e.g., one or two minor missing steps).
* The implementation may have some obvious flaws, but largely works without crashing.
* Implemented feature does not include any eslint-disable or ts-ignore flag

### 10% Testing
The project must include evidence of testing. Ideally, all new features will be accompanied by fully automated tests, but in some circumstances (particularly when engaging with Phaser, the game library, or Tiled, the map editor), this may not be feasible. If automated tests are not possible, include a discussion of your manual testing strategy, including a script that a future developer could use to manually test the feature.

#### Satisfactory:
* Any new or modified backend features include tests that validate that the feature works as intended. These tests cover the changed code, and also contain well-written assertions that thoroughly check the expected behaviors.
* Tests contains no ESLint warnings or errors; does not include any eslint-disable or ts-ignore flags

#### Meets minimum requirements:
* Any new or modified backend features include at least one test, which may or may not be an effective test.
* Tests may contain ESlint warnings (but no errors); does not include any eslint-disable or ts-ignore flags

### Activities During the Project

#### 5% Weekly Meetings with Mentor and Team Surveys
Throughout the semester, each team will be meeting with their mentor and with the instructor to discuss their project progress. Attendance at these meetings and demonstrations of progress will, cumulatively, account for 5% of the project grade. You will also be asked to complete Team Surveys and/or Peer evaluations to help track the progress.
Note that being present for meetings (both literally and intellectually)
with your mentor also factors into your individual Participation and Professionalism grade, so though this is a small part of the
*project* grade, its weight in your final grade is larger.

#### 10% Ongoing development progress, including code reviews
Each team is expected to use their GitHub repository, regularly committing changes while developing their project. You will also be expected to use pull-requests and code reviews.

##### Satisfactory:
* There is a clear development history visible from the git repository: features were delivered incrementally, and not in a single (or several) commits at the end of the project
* There is evidence of code review - for example, pull requests that have comments on them
* There is a correspondence between commit messages and the technical tasks that they are associated with; there are few (if any) commits with meaningless commits messages like `.` or `Add files via upload`.
* Each team member has made at least 4 commits over the lifespan of the project

##### Meets minimum requirements:
* There is a clear development history visible from the git repository: features were delivered incrementally, and not in a single (or several) commits at the end of the project
* Each team member has made at least 2 commits over the lifespan of the project

### Final Report 
The final report should consist of three sections:

#### 4% Report -- Feature Overview

##### Satisfactory:
* The Feature section contains sufficient documentation for a user to interact with your updated version of Covey.Town.
* The documentation covers all steps that the user would need to take to exercise all of your user stories.
* Screenshots are included that capture the key interactions between a user and your new feature.
* Course staff were able to follow these instructions to successfully interact with your project implementation.
* The section is at most 4 pages (roughly 2,000 words maximum), NOT including figures. Fewer pages are absolutely acceptable, consider this a rough limit

##### Meets minimum requirements:
* The Feature contains documentation for a user to interact with your updated version of Covey.Town, but perhaps does not fully describe how.
* The documentation includes at least one or two screenshots, but screenshots do not capture interactions with all of the user stories.
* The course staff were able to figure out how to use it through trial and error.
* The section is at most 4 pages, NOT including figures. Fewer pages are absolutely acceptable, consider this a rough limit

#### 5% Report - Technical Overview
##### Satisfactory:
* Technical Overview contains a description of any substantive changes to the existing Covey.Town codebase, and of the architecture of your new code.
* It uses UML diagrams, CRC cards, state diagrams or any of the other techniques that help describe the structure.
* It provides a well-reasoned rationale for why this is the "right" design.
* Important technical and design trade-offs are justified by referencing discussions in lecture or assigned readings from the rest of the course.
* The document is at most 2 pages (fewer pages are absolutely acceptable, consider this a rough limit) 
##### Meets minimum requirements:
* Technical Overview includes a description of all major changes to the code compared to our existing Covey.Town codebase.
* The document is at most 2 pages (fewer pages are absolutely acceptable, consider this a rough limit) 

#### 5% Process Overview
##### Satisfactory:
* Process overview contains a detailed description of the manner in which agile project management processes were used during the project (i.e., sprints, sprint reviews, retrospectives and blameless reviews).
* It provides a summary of what was planned to happen in each sprint vs what actually happened, with a discussion of what was revised as a result.
* Process decisions are justified by referencing discussions in lecture or assigned readings from the rest of the course.
* The document is at most 2 pages (fewer pages are absolutely acceptable, consider this a rough limit) 

#### Meets minimum requirements:
* It provides a summary of what was planned to happen in each sprint vs what actually happened, with a discussion of what was revised as a result. 
* The document is at most 2 pages (fewer pages are absolutely acceptable, consider this a rough limit) 

### 10% Final Demonstration
Each team will be required to demonstrate their feature to their classmates and to the instructor(s) and TA(s) on the last day of class.

Select projects may be hosted in a project showcase. Here are the projects from Spring 2022 [project showcase](https://neu-se.github.io/CS4530-Spring-2022/assignments/project-showcase).

#### Satisfactory:
* Demo is functional on the final day of class and is consistent with the project as described in the rest of your final submission

#### Meets minimum requirements:
* Demo is functional on the final day of class and is mostly consistent with the project as described in the rest of your final submission

#### Honors teams:
For full marks, we additionally expect no bugs in the demo: it should run cleanly, without crashes, visible defects, or
rough edges that you have to explain away.

### Resubmission After the Final Demo

Sometimes, project teams can't quite finish everything they've promised by the time of the final demonstration on the last day of class.
It's better to deliver a feature late than never deliver it, so if you find yourself in this situation, you're permitted to continue working
on your project and resubmit your project materials and do another demo for the instructor and your project mentor.

If your team is in this situation, you must:
* On the same day as the final demo (i.e., the last day of class), send an email to the instructor, your project mentor TA, and your teammates declaring that
you intend to resubmit. Each of your teammates must respond by this deadline indicating that they agree that a resubmission is appropriate.
* In writing (email is fine), declare exactly which feature(s) or user stor(ies) you will complete by the resubmission deadline. This email must be received
by the instructor and TAs no later than one week after the deadline for your initial email declaring your intention to resubmit (i.e., it must be received no more than one week later, AoE, than the last day of class).
* You must schedule a meeting with your project mentor and the instructor before the class' final exam (note: day of the final exam is **not** acceptable) to re-demonstrate your
feature. The deadline for scheduling this demo is the same as the deadline for providing the scope of work email (see previous bullet point): no more than one week after the last day of class. Note that the instructor generally does not check email on the weekend.

The consequences of choosing to resubmit are:
* you will not receive your final grades on your project materials until **after** your resubmission demo.
* you must resubmit all project deliverables before your rescheduled demo.
* you will be held to a higher standard on all project materials, since your team will have extra time to polish them.
* your final grades on all materials will be evenly split between the grade you would have received on your original submission and
the grade you receive on your resubmission. Additionally, a 5% late penalty is automatically applied to your resubmission. A further
5% penalty is applied if, in the view of the instructor, your resubmission does not substantially improve on your original submission.
Do not resubmit unless your work was substantially incomplete at the regular deadline: these policies mean that resubmitting is only a good
idea if your project would otherwise be graded poorly.

## Individual Reflection

Accompanying the final team deliverable will be an individual reflection, which every student must submit on their own.
It is worth 5% of your project grade, as one of the project's individually-graded components.
Satisfactory completion of all parts of this reflection is *also* required to receive an "A" grade in the course, and may be used to calibrate project scores across multiple team members.
The individual reflection also provides an opportunity for students to provide confidential feedback on the performance of their teammates.

This assignment has the same shape as the [Individual Contribution Report](../projects/contribution-report.html)
that you submitted in November: three short sections of *evidence* about what you personally did, followed by a
reflection. The difference is scope and depth. Sections 1-3 now cover the whole project rather than the first
seven weeks, and section 4 is much longer---it is the main part of this assignment.

You may reuse material from your November report in sections 1-3, updated for everything that happened since.

### 1. Code you wrote

List the pull requests that you authored in your team's repository over the whole project. For each one, give:
* the PR number and a link to it,
* a one-sentence description of what it does, and
* whether it was merged.

If you pair programmed, say so, and make sure the commits in question use
[Git's co-author feature](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors)
so that the history reflects who actually wrote the code.

#### Satisfactory:
* Every pull request you authored is listed, with a link, a one-sentence description, and its merge status.
* Pair-programmed work is identified as such.

### 2. Code you reviewed

List the pull requests that you reviewed (that were authored by someone else), with links. For each, give a
one-sentence description of what you asked for or what you caught. If you approved a pull request without
comments, say so---it is a legitimate outcome, but we want to know.

#### Satisfactory:
* Every pull request you reviewed is listed, with a link and a one-sentence description of what you asked for or caught.

### 3. Your tasks from the work breakdown

List the tasks from your team's revised project plan that were assigned to you, and give the final status of each:
done, dropped, or reassigned. For anything that was not completed as planned, explain why in a sentence or two.

#### Satisfactory:
* Every task assigned to you in the revised project plan appears, with its final status.
* Every task that was not completed as planned is accompanied by an explanation.

### 4. Reflection

This is the substantial part of the assignment: a narrative covering the three topics below. Expect it to run
somewhere in the range of 1000-1500 words in total; there is no hard limit, but padding will not help you.

Good reflections are specific, and are grounded in the evidence you gave in sections 1-3: "we dropped the
notification user story in Sprint 4 because the WebSocket work in PR #41 took three times as long as I estimated"
is worth much more than "we ran out of time."

#### Project Concept

Reflect on the evolution of your project concept: How does the project that you delivered compare to what you originally planned to deliver? What caused these deviations?

##### Satisfactory:
* Is at least 2 paragraphs long;
* Includes at least 1 paragraph describing all variances from original project concept;
* Includes at least 1 paragraph of personal reflection on the cause of any variances from the project concept.

#### Project Process

Reflect on the evolution of your development process: How did the process by which you designed and implemented evolve from your original project plan? Were there any processes that in hindsight, you wish that you followed, or wish that you followed better?

##### Satisfactory:
* Is at least 2 paragraphs long;
* Includes at least 1 paragraph describing all variances from the software development processes envisioned in your original project plan;
* Includes at least 1 paragraph describing software processes (described in class or not) that you wish you had followed, or wish you had followed better, supported by evidence from your personal experience working on the project.

#### Project Team

Reflect on your team dynamic: Provide a frank (and ideally, blameless) postmortem of your and your teammates collaborative performance and participation. If you had to do this same project over with the same teammates, what would you have done differently (or not) to improve your team’s overall performance? Do you think that each of your teammates are deserving of the same grade as you?

##### Satisfactory:
* Is at least 2 paragraphs long;
* Includes at least 1 paragraph reflecting on your own performance as a team member on this project, including what you would have done differently, given what you know now;
* Includes at least 1 paragraph reflecting on your overall team dynamic, including strengths and weaknesses. Reflect on how you might have organized your team differently given what you know now.
