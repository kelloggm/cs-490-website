---
layout: page
title: Individual Project Proposal
permalink: /projects/individual-project-proposal.html
parent: Projects
nav_order: 4
---
# Individual Project Proposal **Due Monday 29 September 2025, 11:59pm AoE**{: .label .label-red }
All projects will involve frontend and backend development of a new feature for Covey.Town.
Once teams have been formed, you and your team will decide exactly what kind of new feature you would like to build.
Your feature should be something that can be implemented within the timeframe allotted (5 weeks, plus 2 weeks of planning), and will be implemented in a fork of the main Covey.Town codebase.
You can play with a demo deployment of the app at [app.covey.town](https://app.covey.town), and in the coming weeks, we will provide tutorials and instructions for you to run the entire application in a local development environment, and also to deploy it to the cloud.
Given that you will be up-to-speed on the Covey.Town codebase (and have been introduced to TypeScript, React, NodeJS, and testing frameworks),
and that you will have a team of three or four, we expect that the feature that you propose will be more complex than the feature implemented in the individual
homework.

In this assignment, you'll first suggest a possible project on your own via a one-page project proposal. We'll use your proposals to help us assign teams based on both the direction of the proposals (i.e., we'll try to group people who suggested similar projects) and the quality of the proposals (i.e., we'll try to group people who wrote good proposals together). Hopefully, this gives you an incentive to write a good proposal!

Feel free to look at existing systems like [Gather.Town](https://gather.town), [Sococo](https://www.sococo.com), [Reslash](https://reslash.co), [Screen](https://screen.so/home), and [Gatherly.IO](https://www.gatherly.io) for inspiration on new features to build for Covey.Town. Also see the NYTimes Magazine article [The Race to Fix Fix Virtual Meetings](https://www.nytimes.com/2021/02/17/magazine/video-conference.html). 
Examples of features that students might propose include:
* Create some new form of "Interactable" object, such as a whiteboard or game
* Create an interface for uploading and choosing between different maps and avatars (will require also learning to use the [Phaser3 API](https://photonstorm.github.io/phaser3-docs/index.html))
* Add screenreader support - generate a textual representation of the map and what players can do to interact with it
* Support real persistence: store data in a database (e.g. Postgres + GraphQL), allow users to register and save a profile (e.g. using Auth0) 
* Add direct messaging, image messaging, and other chat features
* Anything else you can imagine that might be useful to a user of Covey.Town

Please note that multiple students (at this stage) or teams (at the preliminary plan stage) might choose to propose the same feature, or a variation of that same feature - this is OK.

When considering project ideas, please keep in mind that you will be allowed to publicly post your project online: while your immediate audience for the project is the course staff, if you are ultimately looking for software engineering jobs or co-ops, this project can be a useful piece of your portfolio. If you build a sufficiently maintainable feature (i.e., if your project is particularly well architected and tested), we will also consider pull requests to merge your feature into the main Covey.Town codebase on GitHub, allowing you to also tell recruiters that you have contributed a feature to an open source project on GitHub!

## Writing a One-Pager

There is a strict one-page limit to the length of your individual proposal. One page is very short! So, it's critical that you use your space well.

We suggest trying to answer the following questions, in this order (e.g., in one paragraph each):
* **Why?** What problem is your project idea trying to solve? Who will benefit if you succeed?
* **What?** What exactly are you proposing? Can you use an analogy to some other service or tool that your audience is likely familiar with to help explain ("I want to add something like X from Y to Covey.Town" is a great way to succinctly explain a new feature!)?
* **How?** What are the technical obstacles? Is there only one way to fix the problem that you're trying to solve in Covey.Town, or are there alternatives (hint: the answer to this question is almost always "yes")? Are there libraries or external tools that you know about that will make it easier to achieve something cool?

There's also a lot of guidance online about how to write a good one-pager, especially in a software engineering context. For example, Amazon famously starts many design meetings with one-pagers. Here are some pieces of advice that we find credible:
* ["How To Write a One-Pager like an Amazonian"](https://francisshanahan.substack.com/p/how-to-write-a-one-pager-like-an) by Fancis Shanahan
* ["Undervalued Software Engineering Skills: Writing Well"](https://blog.pragmaticengineer.com/on-writing-well/) by Gergely Orosz
* 