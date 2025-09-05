---
layout: project
title: "Individual Project 1"
permalink: /projects/ip1.html
parent: Projects
nav_order: 1
due_date: "Monday, 22 September 2025, 11:59PM AoE"
submission_notes: Submit via GradeScope
---

The overall goal of the individual assignment for this semester is to simulate
a "starter task" that you might be asked to take on as a junior engineer who is just starting
on a new software engineering team. The task has been partially planned out for
you by one of our senior engineers, and they estimated that completing it would
take about one working day (i.e., 8 hours time on task). Since you're presumably
taking other classes besides CS 490, we're giving you two weeks for this task.
But you should start early: rushing to finish at the last minute will probably
lead to lower-quality code. The overall goal is to get you used to the Covey.Town
codebase so that you're ready to be effective during the course project throughout
the rest of the semester.

<details><summary>A note on the accuracy of estimates in software engineering.</summary>
As we'll <a href="https://kelloggm.github.io/martinjkellogg.com/teaching/cs490-au25/assets/lecture-process.pdf">discuss later in this class</a>, engineers' estimates of how long
an engineering task will take are notoriously variable. If it takes you significantly
longer (or shorter) to do the task than our senior engineer's estimate, don't worry!
This estimate is here as a rough guide for how long we think this task will take, but
it is common for engineers to mis-estimate by an order of magnitude or more, even
when they know they might do so.
</details>

## Objectives of this assignment
The objectives of this assignment are to:
*  Get you familiar with the basics of TypeScript, VSCode, and the project codebase
*  Learn how to read and write code in TypeScript
*  Translate high-level requirements into code
*  Learn how to write unit tests with Jest

## Assignment scenario

Covey.Town management has noticed a new trend among users of the Covey.Town's
Tic-Tac-Toe game: discussion of [this webcomic](https://www.smbc-comics.com/comic/tic)
which proposes an alternate form of Tic-Tac-Toe. Since the Tic-Tac-Toe game on Covey.Town
has historically not produced good engagement metrics (it's almost like Tic-Tac-Toe is a [solved game](https://en.wikipedia.org/wiki/Solved_game)...), your management would
like to take advantage of this viral interest by implementing the proposed Tic-Tac-Toe
variant in Covey.Town. You've been assigned to implement and test this new feature,
building on the existing Tic-Tac-Toe functionality.

<details><summary>Game specification from the webcomic in plaintext</summary>
<b>Setup</b><br>
Requires 3 people: 2 players and 1 "monitor"<br>
<br>
Each player has three private tic-tac-toe boards, which their opponent cannot see, but the monitor can. They are labeled A, B, and C.<br>
<br>
There are also 3 public tic-tac-toe boards which everyone can see. These are also labeled A, B, and C.<br>
<br>
<b>Gameplay</b><br>
Players take turns writing one symbol in one square on their private board. Squares that are occupied on a private board are also occupied on the corresponding public board.<br>
<br>
Once a player draws a symbol on their private board, the monitor checks to see if their opponent has already occupied that square by writing a symbol on their private board.<br>
<br>
If the square is already occupied, the player who tried to occupy it a second time loses their turn. The symbol in that occupied square is then drawn in the corresponding square of the public board.<br>
<br>
<b>Scoring</b><br>
Whenever a player gets three in a row on a board, up-down, left-right, or diagonal, they get a point. The winning board is not publicly revealed, but players may no longer play on it.<br>
<br>
<b>Winning</b><br>
Whoever has the most points when no more moves are possible wins.
</details>

In the Covey.Town implementation, we want to permit two players to play against each other,
with Covey.Town itself (i.e., your code) serving as the "monitor". We hope that this will allow
folks chattering about this variant on social media to try it out on Covey.Town (and, we hope
they'll stick around afterwards). It's your job to build and test this feature before we release it.

## Getting started with this assignment

The senior engineer who planned this work item has already set up some of the
basic architecture of the feature to help you out. Their code is in the `fall2025-ip1` branch
of the course staff's [Covey.Town repository](https://github.com/kelloggm/covey.town)
that you forked or cloned in [IP0](https://kelloggm.github.io/martinjkellogg.com/teaching/cs490-au25/projects/ip0.html). To get this starter code, you need to fetch this branch. The process
differs depending on whether you _forked_ or _cloned_ the starter repository in IP0.

<details><summary>Forking vs. Cloning</summary>
When you <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo">fork</a> a repository, you create a new <b>remote</b> copy (i.e., on GitHub itself)
of it that's completely under your
control. When you <a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository">clone</a> a repository, you create a <b>local</b> copy (i.e., just on your computer, not on GitHub). <a href="https://github.com/orgs/community/discussions/35849">This little article</a> does a good job explaining the difference, if you want more details.
</details>

### If you **forked** our repository

TODO

### If you **cloned** our repository

TODO