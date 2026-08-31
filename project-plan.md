---
layout: page
title: Project Plan
permalink: /projects/project-plan.html
parent: Projects
nav_order: 5
---
# Preliminary Project Plan **Due Monday 28 September 2026, 11:59pm AoE**{: .label .label-red }
This is the first team assignment of the group project. In this assignment, your team
will:
* settle on a feature that everyone in the group is happy to propose. This feature can be one of the ones that one of you proposed in the individual project proposals, but it doesn't have to be.
* write a _project plan_ that lays out in greater detail both the design of your feature and how you plan to break up the work that's necessary to build it.
Specifically, the project plan will include:
* Introductory problem statement
* User stories and acceptance criteria: high level description of how users will interact with your new feature. 
* Work breakdown: Define engineering tasks that will be necessary to implement your new feature. Map each task to a sprint. 

Your mentor will review your project plan and provide you with feedback on the scope and details provided in this plan.
Your team will self-organize, as agile teams do, and will enhance and adapt its plan during the project lifecycle.
As such, the primary goal of this document is to *begin* the planning process, and *not* to produce a detailed plan that must be followed precisely.
The course staff will provide feedback on your project to help ensure that the scope of your project is appropriate.

**Honors teams**: every member of your team is an Honors student, and we hold Honors projects to a higher standard.
We expect an Honors project to be significantly more ambitious than average, to be significantly more polished,
and to scale up to larger numbers of concurrent users. Plan for all three from the start:
in particular, your user stories, conditions of satisfaction, and work breakdown should reflect the extra ambition,
and your work breakdown should include the testing and scalability work that the other two expectations imply.
See the [syllabus](../about/#honors-section) and the [project overview](../projects/project-overview.html#honors-projects).

We list page *maximums* for each section as general guidance of what we are willing to grade. Please do not feel compelled to use all of the pages provided, and remember that a diagram or table can be as expressive (or more) as a comparable amount of text.

## Problem Statement, User Stories and Acceptance Criteria (max 4 pages)
Your project plan should begin with a 1-3 paragraph introductory problem statement: what problem in Covey.Town does your (proposed) feature solve? Provide a paragraph (or two) that describes why you are interested in building this feature. 

Given the problem statement, develop three user stories that show how a user would interact with the feature. User stories are requirements specified in the format 
"As a < type of user >, I want < some goal > so that < some reason >."
My conditions of satisfaction are < list of common cases and special cases that must work >.

You should include three different user stories to describe how users will interact with your feature.
Your three user stories should cover the key behavior that your feature will provide.
Do not provide more than three user stories. Your problem statement and description of user stories and conditions of satisfaction should be between 2-4 pages.

We've provided a [tutorial](../tutorials/user-stories.html) on writing user stories to help with this part.

## Work Breakdown (max 10 pages)
Given the project concept that you have chosen and the functionality that you expect to implement to satisfy your user stories, define a breakdown of the work that will be necessary to complete the project.

A work breakdown includes all of the tasks necessary to accomplish the project, and will be an artifact that we will refer back to throughout the project to evaluate whether you are making satisfactory progress.
Consider all of the kinds of tasks that your team will need to perform, including knowledge acquisition, design, implementation, testing and documentation tasks.
It is hard to say (generically) how many work items are necessary---not all work items are equally difficult or require the same amount of engineering effort.

Each task on the work breakdown should be assigned to exactly one team member, who should provide a "T-Shirt" estimate for how long it will take (along with a justification for that estimate).
Consider the dependencies between tasks: perhaps an API needs to be designed and specified before implementation can begin; perhaps your development environment needs to be configured before anything else can proceed.
Assign tasks to sprints considering these dependencies.

Given the preliminary nature of your project, we do not expect that you will know all of the details about precisely how to implement your feature such that you could break it down into tasks that you feel could be implemented in a day or two.
However: Large tasks (those which you can not provide a responsible estimate for) must be accompanied by smaller "research" tasks that can be performed early on in the project, providing clear deadlines by which the task must either be refined into smaller tasks (based on new knowledge gathered), or reworked/abandoned.
Your team's first sprint begins the week teams are announced, so Sprint 0 is already in progress by the time this plan is due: describe what you have done in it so far, and schedule any remaining research tasks into Sprint 1.

For example: Consider if you were proposing a "Viewing Area" project (this was an individual project in previous semesters). It might be difficult to consider how to break down a task like "Implement the frontend components for sychnronized video playback" into something that you could commit to doing within a day or two. Given that this is a task that can be delayed until the end of the project (no other tasks depend on it), it would be wise to consider having some tasks early on in the project, such as: "Find react components that embed YouTube videos," and "Implement simple video player that does not synchronize playback." Completing these smaller tasks early would let you both demonstrate that some forward progress is being made, and also allow you to create a much more responsible estimate for how that last, otherwise insurmountably large task would take.

Be realistic, and leave time for contingencies and for your other courses.
If you are uncertain that some tasks will be feasible, then be sure to include evaluation tasks earlier-on in the project that will allow for "go/no-go" decisions to move forward on a task or drop it.

We understand that it is quite difficult to estimate the technical complexity of a new project (as you are doing in the case of this course).
We will provide you with feedback on this preliminary project plan, which you will use to produce a revised project plan (due two weeks after the main project plan).
Throughout the project period, teams will meet regularly with their mentor, who will help track progress on a week-to-week basis and help to determine when adjustments to the project scope are needed.

Each work item should contain the following information:
* Task to be performed
* User story (or stories) that this task relates to
* Team member responsible for completing the task
* T-shirt size estimate of how long will be needed to complete the task, using the following buckets:
    * Small: Can likely be completed by one team member in one sitting of less than 3-4 hours
    * Medium: Likely to require involvement of multiple team members, over the course of 1-2 days
    * Large: Currently unable to provide a responsible estimate. 
* A brief (1-2 sentence max) justification of how you reached the size estimate of the task 
* Milestone for delivering the task, chosen from one of the following two-week sprints:
  * Sprint 0: Sep 21 - Oct 2 (already underway when the preliminary plan is due)
  * Sprint 1: Oct 5 - Oct 16
  * Sprint 2: Oct 19 - Oct 30
  * Sprint 3: Nov 2 - Nov 13
  * Sprint 4: Nov 16 - Nov 27
  * Sprint 5: Nov 30 - Dec 9 (note: this sprint is shorter than the others---only about 8 working days. We don't recommend scheduling many tasks in this sprint, because of the likelihood that some tasks from prior sprints might not be done yet.)

Your work breakdown should take the format of a simple textual list.
 
## Submission 
Your project plan should be submitted as a single PDF in Canvas (TODO: link to this semester's Canvas course) to the assignment "Preliminary Project Plan."
Each team submits a single document to Canvas: when uploading the submission, your teams should already be present in Canvas. Be sure to tag your team mates.
The assignment is due by the end of September 28, AoE.

## Grading
The project plan will account for 5% of your project grade, and will be graded out of 75 points. The grading of the project plan is further broken down as follows:

### Introductory problem statement (5 points): 
* Receive full marks if there is a narrative consisting of 4-10 sentences that describes a specific problem that your project aims to solve.
* Receive partial credit if the narrative is present, but does not describe a problem that the project aims to solve
* Minor deductions for factual errors ("don't say false things") or egregious overclaims ("our project will usher in a new era of world peace")

### User stories (12 points):
Each of the three user stories will account for 4 points of your grade on this assignment and graded as follows:
* Receive full marks if:
  * The user story fits the problem statement
  * The user story satisfies the INVEST criteria for good user stories (construed quite broadly)
  * The user story includes conditions of satisfaction that cover the "normal" expected behavior of the feature, and any relevant error cases

### Work breakdown (58 points):
Your work breakdown will be evaluated holistically on the following rubric:

#### Coverage of tasks needed (20 points):
Receive full marks if the work breakdown includes all (reasonably expected) tasks to implement your feature, considering these kinds of tasks: 
  * Background research 
  * Design of interfaces and data types
  * Deployment of third-party services
  * Implementation
  * Testing
  * Documentation

It is not possible to state generically for all projects whether *all* of the above types of tasks are necessary.
However, we believe that this list is exhaustive (we do not expect other kinds of tasks).

#### Assignment of tasks (9 points):
Receive full marks if
* Each element of the work breakdown is assigned to specific team members, and we can clearly identify which specific team member is primarily responsible for each "small" or "medium" task. You have a bit of flexibility about how you want to assign tasks (e.g., it's permitted for you to have "primary" and "secondary" team members for each tasks, just one team member per task, etc.) as long as it is clear to the course staff which team member has the primary responsibility for each task.
* The distribution of tasks of each size are roughly similar between the whole team (no single person is assigned significantly more or fewer tasks of one size)
* Each team member has at least one task assigned to them during each sprint)

#### Sizing of tasks (20 points):
Receive full marks if each element on the work breakdown:
* Has a size estimate (small, medium, or large) that is provided by the team member assigned the task.
* Has a responsible justification for that estimation
* Every "large" task:
  * Is accompanied by a reasonable explanation of why the team is unable to provide a responsible estimate
  * Is accompanied by at least one small or medium task, scheduled well-before the "large" task is due to be completed. We would expect that most of these research tasks are scheduled to sprint 1, or perhaps sprint 2.

#### Scheduling of tasks (9 points):
Receive full marks if each element on the work breakdown:
* Is assigned to a sprint
* There are no obvious constraint violations (tasks that logically must happen before others should be scheduled before them)
* There are no "Large" tasks scheduled in sprint 0 or sprint 1

