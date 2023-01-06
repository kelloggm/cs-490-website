---
layout: page
title: Project Overview
permalink: /projects/project-overview
parent: Projects
nav_order: 4
---

# Project Overview
The individual and team project for this class are designed to mirror the experiences of a software engineer joining a new development team:
you will be "onboarded" to our codebase, make several individual contributions, and then form a team to propose, develop and implement a new feature.
The codebase that we are be developing on is a remote collaboration tool called [Covey.Town](https://www.covey.town).
Covey.Town provides a virtual meeting space where different groups of people can have simultaneous video calls, allowing participants to drift between different conversations, just like in real life.
Covey.Town is inspired by existing products like [Gather.Town](https://gather.town), [Sococo](https://www.sococo.com), and [Gatherly.IO](https://www.gatherly.io) --- but it is an open source effort, and the features will be proposed and implemented by you!
All implementation will take place in the TypeScript programming language, using React for the user interface.


### Overview of Project Deliverables

| Date | Deliverable | Description | 
| -----| ----------- | ----------- |
| 2/7/23 | Team Formation | Specify preferences for teammates |
| 2/21/23 | [Preliminary Project Plan]({{ site.baseurl }}{% link project-plan.md %}) | Propose a new feature for Covey.Town that can be planned and implemented within 7 weeks |
| 3/7/23 | [Revised Project Plan]({{ site.baseurl }}{% link revised-project-plan.md %}) | Refine the scope of your feature based on staff feedback, define detailed requirements and project acceptance criteria. |
| TBD, one-four days before project showcase | Project Implementation and Documentation | Deliver your new feature, including design documentation and tests |

All assignments are due on the specified date, AoE (i.e., before the beginning of the next day anywhere on Earth, which is at 7am EST the next day).

### Summary of Project Grading
Your overall project grade (which will account for 45% of your final grade in this course) will be the weighted average of each of the deliverables.

* Planning Documents
  * 10% Preliminary Project Plan
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
      * 10% Technical Overview
      * 10% Process Overview
   * 10% Demonstration & Posters
  
In cases where team members do not equally contribute to the project, we may assign different grades to different individuals, up to an extreme of deducting 50% of the team project grade for a student.
We will evaluate each individual's contribution on the basis of a variety of factors, including progress reports at meetings, through inspecting version control history, through each students' self-reflection, and through each students' peer evaluation (during and/or) at the end of the project.
We will make regular efforts to collect and distribute this feedback throughout the project — our ultimate goal is for all students to participate and receive full marks.

### Team Formation
All projects will be completed in a team of 3-4 students.
The very first deliverable for the project will be a team formation survey: you will be able to indicate
your preferences for teammates. The instructors will assign students to the teams based on a number of factors including your responses to the survey.

### Team Meetings with Mentor
Each team will be assigned a member of the course staff as a mentor, who will also serve as your point of contact for project grading.
During the week of February 13-17, you will have a "Kickoff Meeting" with your mentor, where you will meet your mentor and have the opportunity to share any early ideas that you might want feedback on before submitting the project pitch.
Once project begins in full force, you will have regular meetings with your mentor (scheduled at your team's and your mentor's convenience, at least once every two weeks) in order to help ensure that you are making progress on the project, and to help address problems that you encounter (be they technical or non-technical problems).

###  Preliminary Project Plan
All projects will involve frontend and backend development of a new feature for Covey.Town.
Once teams have been formed, you and your team will decide what kind of new feature you would like to build.
Your feature should be something that can be implemented within the timeframe allotted (5-7 weeks), and will be implemented in a fork of the main Covey.Town codebase.
Given that you will be up-to-speed on the Covey.Town codebase (and have been introduced to TypeScript, React, NodeJS, and testing frameworks),
and that you will have a team of three or four, we expect that the feature that you propose will be more complex than the feature implemented in the individual
projects.

The project plan will focus on two sections:
* User stories and conditions of satisfaction that describe the feature that you plan to implement.
* Work breakdown: Map your user stories to engineering tasks. Assign each task to a team member (or pair of team members), provide an estimate for how long each task will take, a rationale for that estimate, and schedule those stories into sprints.

### Creating a GitHub Repository
Your team's development must take place within a private GitHub repository in our GitHub Classroom. To create your repository, each member of your team should follow these instructions:
1. Sign in to [GitHub.com](https://www.github.com/), and then [use our invitation to create a repository with the covey.town codebase](https://classroom.github.com/a/8iDafWvm). Check to see if one of your groupmates has created a group already - if so, select it to join it. Otherwise, you should enter your group number (e.g. "Group 7Y") as the team name. 
2. Refresh the page, and it will show a link to your new repository. Click the link to navigate to your new repository. This is the repository you will use for the project.

This repository will be private, and visible only to your team and the course staff. After the semester ends, you are welcome to make it public - you have complete administrative control of the repository.

### Revised Project Plan
Based on the feedback that you receive from the course staff, you will revise your preliminary project plan, creating a more detailed plan to implement your new feature.

The project plan will include:
* Revised user stories and conditions of satisfaction (based on feedback on the preliminary project plan)
* Revised work breakdown (based on feedback on the preliminary project plan)

Your team will self-organize, as agile teams do, and will use the work breakdown and schedule as the basis for your check-ins with your team's mentor.


### Project Implementation and Documentation
You will be assigned a mentor for your project who will work closely with you for the entire project. You will coordinate with the mentor to setup bi-weekly meetings and regular sprint demos. Peer evaluation will also be used.
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

Finally, you will participate in a "project showcase" during the course's final exam slot. During this showcase, you'll take turns demo'ing your new feature to the rest
of the class, while the rest of your team views the demos of other teams.