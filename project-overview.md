---
layout: page
title: Project Overview
permalink: /projects/project-overview.html
parent: Projects
nav_order: 3
---

# Project Overview
The individual and team projects for this class are designed to mirror the experiences of a software engineer joining a new development team:
you will be "onboarded" to our codebase, make several individual contributions, and then form a team to propose, develop and implement a new feature.
The codebase that we are be developing on is a remote collaboration tool called [Covey.Town](https://www.covey.town).
Covey.Town provides a virtual meeting space where different groups of people can have simultaneous video calls, allowing participants to drift between different conversations, just like in real life.
Covey.Town is inspired by existing products like [Gather.Town](https://gather.town), [Sococo](https://www.sococo.com), and [Gatherly.IO](https://www.gatherly.io) --- but it is an open source effort, and the features will be proposed and implemented by you!
All implementation will take place in the TypeScript programming language, using React for the user interface.

### Overview of Project Deliverables

| Date | Deliverable | Description | 
| -----| ----------- | ----------- |
| 9/28/26 | [Individual Project Proposals]({{ site.baseurl }}{% link individual-project-plan.md %}) | Propose a feature for Covey.Town and specify preferences for teammates |
| 10/2/26 | Team Assignment | Teams will be assigned based on individual proposed features. |
| 10/12/26 | [Preliminary Project Plan]({{ site.baseurl }}{% link project-plan.md %}) | As a team, propose and plan a new feature for Covey.Town that can be implemented within 7 weeks |
| 10/26/26 | [Revised Project Plan]({{ site.baseurl }}{% link revised-project-plan.md %}) | Refine the scope of your feature based on staff feedback, define detailed requirements and project acceptance criteria. |
| 10/30/26 | [Deployment Demo]({{ site.baseurl }}{% link demos.md %}) | Show that you can deploy a lightly-modified copy of covey.town to a remotely-accessible machine. |
| 11/6/26 | First [team survey]({{ site.baseurl }}{% link surveys.md %}) | Let us know how you think the project is going. |
| 11/6/26 | [Wizard-of-Oz Demo]({{ site.baseurl }}{% link demos.md %}) | Show what your project will look like, once it is complete, to your project mentor and the instructor. This demo doesn't require you to show any working code: it is purely about design. |
| 11/20/26 | [Preliminary Demo]({{ site.baseurl }}{% link demos.md %}) | Demonstrate one user story to your project mentor and the instructor. In this demo, you need to actually be running your own code (unlike the Wizard-of-Oz demo).  |
| 11/25/26 | Second [team survey]({{ site.baseurl }}{% link surveys.md %}) | Let us know how you think the project is going. |
| 12/9/26 | Project [Implementation and Documentation]({{ site.baseurl }}{% link project-deliverable.md %}) | Deliver your new feature, including design documentation and tests. |
| TODO | Final Demo | You will demo your feature to the instructor by this date. Final demos will happen sometime tbd after the final project submission. |
| TODO | Third [team survey]({{ site.baseurl }}{% link surveys.md %}) | Let us know how you thought the project went. |
| TODO | Project Implementation and Documentation (Resubmission) | If your final demo does not meet your project goals, you may schedule another demo with your project mentor and the instructor no more than one week after the last day of class. Re-submit your code and documentation immediately before the demo. |

All assignments are due on the specified date, AoE (i.e., before the beginning of the next day anywhere on Earth, which is at 7am EST the next day).

### Summary of Project Grading
Your overall project grade (which will account for 45% of your final grade in this course) will be the weighted average of each of the deliverables.

* Planning Documents
  * 7.5% Preliminary Project Plan
  * 10% Revised Project Plan
* Activities During the Project
  * 5% Meetings with Mentor and Team Surveys
  * 10% Ongoing development progress, including code reviews
* Final Deliverables
  * Code 
    * 20% Final implementation of your feature
    * 10% Final test suite of your feature
   * Report
      * 5% Feature Overview
      * 7.5% Technical Overview
      * 7.5% Process Overview
* Demos
  * 1% Deployment demo
  * 2.5% Wizard-of-Oz demo
  * 4% Preliminary demo
  * 10% Final demo
  
In cases where team members do not equally contribute to the project, we may assign different grades to different individuals, up to an extreme of deducting 50% of the team project grade for a student.
We will evaluate each individual's contribution on the basis of a variety of factors, including progress reports at meetings, through inspecting version control history, through each students' self-reflection, and through each students' peer evaluation (during and/or) at the end of the project.
We will make regular efforts to collect and distribute this feedback throughout the project — our ultimate goal is for all students to participate and receive full marks.

### Team Formation
All projects will be completed in a team of 3-4 students (most teams will have 4).
Part of the first deliverable for the project will be a team formation survey: you will be able to indicate
your preferences for teammates. The instructors will assign students to the teams based on a number of factors including your responses to the survey.
Because the team survey will also ask for your GitHub username, which the course staff needs
to have in order to invite you to your project repo (see "Your Team's GitHub Repository", below).

### Individual Project Proposal
You'll write a one-page proposal for a feature. You only need to explain the feature _from a user perspective_ in this document.
We'll create groups so that people whose individual proposals are similar are grouped together.
Your feature should be something that can be implemented within the timeframe allotted (5-7 weeks), and will be implemented in a fork of the main Covey.Town codebase.

### Team Meetings with Mentor
Each team will be assigned a member of the course staff as a mentor, who will also serve as your point of contact for project grading.
During the first week after project teams are announced, you will have a "Kickoff Meeting" with your mentor, where you will meet your mentor and have the opportunity to share any early ideas that you might want feedback on before submitting the preliminary proposal.
Once project begins in full force, you will have regular standup meetings with your mentor (scheduled at your team's and your mentor's convenience, at least once every week) in order to help ensure that you are making progress on the project, and to help address problems that you encounter (be they technical or non-technical problems).

###  Preliminary Project Plan
All projects will involve frontend and backend development of a new feature for Covey.Town.
Once teams have been formed, you and your team will decide what kind of new feature you would like to build.
We suggest starting with one of your individual proposals, but you're welcome to come up with something new together, too, if you'd like.
Talk to your mentor!
Given that you should already be up-to-speed on the Covey.Town codebase (and have been introduced to TypeScript, React, NodeJS, and testing frameworks),
and that you will have a team of three or four, we expect that the feature that you propose will be reasonably complex.
We will let you know if we think your feature is not ambitious enough (or too ambitious) as part of our feedback on your preliminary plan, but we strongly encourage you to discuss
project scope with your project mentor _before_ submitting the preliminary proposal.

The project plan will have two major sections:
* User stories and conditions of satisfaction that describe the feature that you plan to implement.
* Work breakdown: Map your user stories to engineering tasks. Assign each task to a team member (or pair of team members), provide an estimate for how long each task will take, a rationale for that estimate, and schedule those stories into sprints.

### Your Team's GitHub Repository
Your team's development must take place within the GitHub repository created for you by the course staff.
You will get an invitation to this repository when teams are assigned.
This repository will be private by default, and visible only to your team and the course staff.
After the semester ends, you are welcome to make it public - you will have complete administrative control of the repository.

We will pay close attention to the activity in your team's repo: what you do (or don't do) there
will impact your grade. You should maintain good engineering discipline in your repo: make issues for
bugs before you fix them, code review each other's PRs (and don't push straight to `main`!), don't let
CI fail for long periods of time, etc.---all the things we will talk about in class! The course project
is your chance to show the course staff that you're internalizing what we're discussing in class about what good
engineering looks like: don't let the opportunity go to waste.

As a corollary of the above, it is critical that the authors of commits in your GitHub repository reflect
who actually wrote what code. If you are pair programming, make sure to use
[Git's co-author feature](https://docs.github.com/en/pull-requests/how-tos/commit-changes/creating-a-commit-with-multiple-authors)
to attribute commits to more than one author. We will expect to see consistent streams of commits from all
team members throughout the semester.

### Revised Project Plan
Based on the feedback that you receive from the course staff, you will revise your preliminary project plan, creating a more detailed plan to implement your new feature.
Note that the revised plan due date overlaps with the first sprint, so you will be expected to start working on your project right away once your preliminary plan is approved.
Some teams will have only a few things to fix in their revised plan, but others may need to make significant changes based on our feedback. That's an incentive to get it right
the first time: we will expect the same level of polish from all teams by the end of the semester regardless.

The project plan will include:
* Revised user stories and conditions of satisfaction (based on feedback on the preliminary project plan)
* Revised work breakdown (based on feedback on the preliminary project plan)

Your team will self-organize, as agile teams do, and will use the work breakdown and schedule as the basis for your check-ins with your team's mentor.

### Project Implementation and Documentation
You will be assigned a mentor for your project who will work closely with you for the entire project.
You will coordinate with the mentor to setup weekly meetings and regular sprint demos. Peer evaluation will also be used.
Your final team deliverable will be a "release" of your new feature on GitHub (with tests), and will be accompanied by a demo.
*Optionally,* you may also open a pull request to merge your feature into our main repository (submitting a pull request, or the pull request being merged into our
codebase is independent of the grade you receive, but provides a platform for more visiblity of your project). 

Your final team deliverable will include:
* The implementation of your new feature
* Automated tests for your new feature
* A report
    
Accompanying the final team deliverable will be an *individual reflection*, which every student must submit on their own, which will include your reflections on:
* The evolution of your project concept: How does the project that you delivered compare to what you originally planned to deliver? What caused these deviations?
* The software engineering processes that you feel could have been improved in your project: were there any procesess that in hindsight, you wish that you followed, or wish that you followed better?
* Your team dynamic: Provide a frank (and ideally, blameless) postmortem of your and your teammates collaborative performance and participation. If you had to do this same project over with the same teammates, what would *you* have done differently (or not) to improve your team's overall performance?