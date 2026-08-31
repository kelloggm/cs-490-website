---
layout: page
title: Individual Project Proposal
permalink: /projects/individual-project-proposal.html
parent: Projects
nav_order: 4
---
# Individual Project Proposal **Due Monday 28 September 2026, 11:59pm AoE**{: .label .label-red }
All projects will involve frontend and backend development of a new feature for Covey.Town.
Once teams have been formed, you and your team will decide exactly what kind of new feature you would like to build.
Your feature should be something that can be implemented within the timeframe allotted (~6 weeks, plus ~2 weeks of planning), and will be implemented in a fork of the main Covey.Town codebase.
You can play with a demo deployment of the app at [app.covey.town](https://app.covey.town).
Given that you will be up-to-speed on the Covey.Town codebase (and have been introduced to TypeScript, React, NodeJS, and testing frameworks)
via the individual project,
and that you will have a team of three or four, we expect that the feature that you propose will be significantly more complex than the feature implemented in
[IP1](https://kelloggm.github.io/martinjkellogg.com/teaching/cs490-au26/projects/ip1.html).

If you are in the Honors section, keep in mind that Honors teams are made up entirely of Honors students and that
we hold Honors projects to a higher standard: we expect them to be significantly more ambitious than average,
significantly more polished, and to scale up to larger numbers of concurrent users.
Propose accordingly (see the [syllabus](../about/#honors-section) and the [project overview](../projects/project-overview.html#honors-projects)).

In this assignment, you'll first suggest a possible project on your own via a one-page project proposal. We'll use your proposals to help us assign teams based on both the direction of the proposals (i.e., we'll try to group people who suggested similar projects) and the quality of the proposals (i.e., we'll try to group people who wrote good proposals together). Hopefully, this gives you an incentive to write a good proposal!

Feel free to look at existing systems like [Gather.Town](https://gather.town), [Sococo](https://www.sococo.com), [Reslash](https://reslash.co), [Screen](https://screen.so/home), and [Gatherly.IO](https://www.gatherly.io) for inspiration on new features to build for Covey.Town. Also see the NYTimes Magazine article [The Race to Fix Fix Virtual Meetings](https://www.nytimes.com/2021/02/17/magazine/video-conference.html). 
Examples of features that students might propose include:
* Create some new form of "Interactable" object that models something that might be found in a real conference space, such as a whiteboard or game
  * if you are going to create an interactable version of some sort of game, be careful: it is easy to pick a game that's too simple or too complex
* Create an interface for uploading and choosing between different maps and avatars (will require also learning to use the [Phaser3 API](https://photonstorm.github.io/phaser3-docs/index.html))
* Create an interface for choosing between different visual styles, fonts, avatars, etc.
* Add screenreader support - generate a textual representation of the map and what players can do to interact with it
* Support real persistence: store data in a database (e.g. Postgres + GraphQL), allow users to register and save a profile (e.g. using Auth0) 
* Add direct messaging, image messaging, and other chat features
* Add a working map to the town that allows you to locate (and navigate to?) other players
* Integrate with some external service that will enhance the user experience (e.g., integrating with Spotify to add music to the town)
* Add a virtual assistant to the town that can carry out various actions on behalf of the user via a natural language interface
* Add support for advertising in the town (and potentially integrate with an external ad service like Google)
* Anything else you can imagine that might be useful to a user or operator of Covey.Town

Please note that multiple students (at this stage) or teams (at the preliminary plan stage) might choose to propose the same feature, or a variation of that same feature - this is OK.

When considering project ideas, please keep in mind that you will be allowed to publicly post your project online: while your immediate audience for the project is the course staff, if you are ultimately looking for software engineering jobs or co-ops, this project can be a useful piece of your portfolio. If you build a sufficiently maintainable feature (i.e., if your project is particularly well architected and tested), we will also consider pull requests to merge your feature into the main Covey.Town codebase on GitHub, allowing you to also tell recruiters that you have contributed a feature to an open source project on GitHub.

## Writing a One-Pager

There is a **strict one-page limit** to the length of your individual proposal. One page is very short! So, it's critical that you use your space well.

We suggest trying to answer the following questions, in this order (e.g., in one paragraph each):
* **Why?** What problem is your project idea trying to solve? Who will benefit if you succeed?
* **What?** What exactly are you proposing? Can you use an analogy to some other service or tool that your audience is likely familiar with to help explain ("I want to add something like X from Y to Covey.Town" is a great way to succinctly explain a new feature!)?
* **How?** What are the technical obstacles? Is there only one way to fix the problem that you're trying to solve in Covey.Town, or are there alternatives (hint: the answer to this question is almost always "yes")? Are there libraries or external tools that you know about that will make it easier to achieve something cool?

There's also a lot of guidance online about how to write a good one-pager, especially in a software engineering context. For example, Amazon famously starts many design meetings with one-pagers. Here are some pieces of advice that we find credible:
* ["How To Write a One-Pager like an Amazonian"](https://francisshanahan.substack.com/p/how-to-write-a-one-pager-like-an) by Fancis Shanahan
* ["Microspeak: The one-pager"](https://devblogs.microsoft.com/oldnewthing/20220719-00/?p=106873) by Raymond Chen
* ["Undervalued Software Engineering Skills: Writing Well"](https://blog.pragmaticengineer.com/on-writing-well/) by Gergely Orosz

## Rubric

This assignment will be graded out of 50 points. There are five subscores, for **Ambition**, **Clarity**, **Rationale**, **Technical Challenges and Alternatives**, and **Writing**. These are detailed below.

### Ambition (10 points)

This subscore represents whether your proposal is appropriately-ambitious for a four-person team of undergraduates in half of a semester.
You'll receive less than full credit if your proposal is either too ambitious or not ambitious enough:
* 10 points if your proposal is appropriately-ambitious for a four-person team of undergraduates in half of a semester
* 8 points if your proposal is a bit too ambitious or a bit unambitious. For example, if there is an obvious addition to the project that would make it significantly better and you don't include it, you might get this score.
* 5 points if your proposal is viable but either much too ambitious or not nearly ambitious enough. For example, you might get this score if you propose to re-implement an indie videogame built by a one-person team over the course of years in Covey.Town in 6 weeks, or if you propose something that's only a little more complex than IP1.
* 0 points if your proposal is not viable. For example, you might get this score if you propose to re-implement a commercially-produced videogame that was developed by a team of engineers in six weeks, or if your proposal is no more ambitious than IP1.

Proposals from students in the Honors section are graded against a higher bar: for full marks, an Honors proposal must be
appropriately-ambitious for a four-person Honors team, which means significantly more ambitious than the average proposal.
An Honors proposal should also account for the extra polish and scalability that we expect from Honors projects.

### Clarity (10 points)

This subscore represents whether your proposal is clear to the reader. Any ambiguities in what you are proposing to do will result
in deductions; the amount deducted will depend on the importance and severity of the ambiguity.

### Rationale (10 points)

This subscore represents whether your proposal clearly identifies **why** it will be valuable to users or operators of Covey.Town, and what
the benefit(s) of your proposal will be. In particular, for full credit your proposal should:
* clearly distinguish between goals and non-goals
* identify the target audience of your feature
* make a clear argument for how the proposed feature will benefit the target audience

### Technical Challenges and Alternatives (10 points)

This subscore represents whether your proposal has engaged with the technical difficulties that you're likely to encounter while
building the proposed feature. At a high-level, we're looking for evidence that you've thought the feature through.
Full credit proposals can show that by doing at least one of the following:
* discussing at least one reasonable alternative to the proposed feature that would solve the same problem, and making a credible arguemnt that the proposed feature is the better option
* discussing a difficult technical challenge that you expect to encounter while building the feature and a proposed solution
* discussing libraries that your feature can build on to mitigate expected technical challenges

### Writing (10 points)

This subscore represents the quality of your writing. While the "quality" of writing is subjective in general, for
a one-page project proposal we're looking for the following:
* no typos
* appropriate use of technical jargon
* concision

To help with concision, we recommend thinking about the "length-to-content ratio" (LCR) of your writing. That is, if it's possible
to say the same thing with fewer syllables or words, do so. A longer writeup on the idea of LCR can be found [here](https://docs.google.com/document/d/1iqbMNrIHH2w6i05aEae6y0HnsX53aKrFji5GgGZCyAg/edit?usp=sharing).

## Submission

Your project plan should be submitted as a single PDF in Canvas (TODO: link to this semester's Canvas course) to the assignment "Individual Project Proposal."
The assignment is due by the end of September 28, AoE.
