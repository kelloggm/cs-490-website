---
layout: project
title: "Individual Project 1"
permalink: /projects/ip1.html
parent: Projects
nav_order: 1
due_date: "Monday, 21 September 2026, 11:59PM AoE"
submission_notes: Submit via GradeScope
---

<!-- TODO(au26): this entire assignment is slated to be replaced for Fall 2026 (it did not
     go well in Au25). Until it is rewritten, note that the starter code still points at
     the `fall2025-ip1` branch of github.com/kelloggm/covey.town; a new branch will be
     needed for whatever replaces this. -->

The overall goal of the individual assignment for this semester is to simulate
a "starter task" that you might be asked to take on as a junior engineer who is just starting
on a new software engineering team. The task has been started for
you by one of our senior engineers, and they estimated that completing it would
take about one working day (i.e., 8 hours time on task). Unfortunately, that engineer
will be out sick for the foreseeable future, so it's on your to finish their work.
Since you're presumably taking other classes besides CS 490, we're giving you two weeks for this task.
But you should start early: rushing to finish at the last minute will probably
lead to lower-quality code. The overall goal is to get you used to the Covey.Town
codebase so that you're ready to be effective during the course project throughout
the rest of the semester.

<details><summary>What's a "senior" engineer?</summary>
When someone in industry talks about "senior" engineers, they usually mean "engineers whose judgment is trusted." When you're first hired out of college, you'll (probably) start off as a "junior" engineer, with a senior engineer assigned to mentor you. Usually, junior engineers become senior within a few years. This <a href="https://news.ycombinator.com/item?id=7493290">HackerNews discussion</a> answers this question for you more directly.
</details>

<details><summary>A note on the accuracy of estimates in software engineering.</summary>
As we'll <a href="https://kelloggm.github.io/martinjkellogg.com/teaching/cs490-au26/assets/lecture-process.pdf">discuss later in this class</a>, engineers' estimates of how long
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

In the Covey.Town implementation, which we're calling "Quantum TicTacToe",
we want to permit two players to play against each other,
with Covey.Town itself (i.e., your code) serving as the "monitor". We hope that this will allow
folks chattering about this variant on social media to try it out on Covey.Town (and, we hope
they'll stick around afterwards). Management thought this was high-priority, and so assigned
a trusted senior engineer to the project. Unfortunately, that engineer got sick before finishing,
so you've been asked to step in and finish their work---all the other senior engineers are busy
with other important tasks.
It's your job to finish building and testing this feature before we release it.

## Getting started with this assignment

The senior engineer who was working on this task has already made a good start: they've
designed most of the feature, implemented and tested most
of the frontend, and stubbed out the backend. Their code is in the `fall2025-ip1` [branch](http://github.com/kelloggm/covey.town/tree/fall2025-ip1)
of the course staff's [Covey.Town repository](https://github.com/kelloggm/covey.town)
that you forked or cloned in [IP0](https://kelloggm.github.io/martinjkellogg.com/teaching/cs490-au26/projects/ip0.html). To get this starter code, you need to fetch this branch. The process
differs depending on whether you _forked_ or _cloned_ the starter repository in IP0.

<details><summary>Can I trust that the senior engineer's code is perfect?</summary>
The short answer is "no": you're still expected to exercise good technical judgment, even when working with code written by someone who is more experienced than you.
If you find (what you think) is a bug in the starter code, you should fix it: don't treat the starter code as if it is perfect or handed-down from on high. That said,
you should probably apply a high standard when trying to decide if the starter code does something correctly: your senior colleague _probably_ knows what they're doing.
</details>

<details><summary>Forking vs. Cloning</summary>
When you <a href="https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo">fork</a> a repository, you create a new <b>remote</b> copy (i.e., on GitHub itself)
of it that's completely under your
control. When you <a href="https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository">clone</a> a repository, you create a <b>local</b> copy (i.e., just on your computer, not on GitHub). <a href="https://github.com/orgs/community/discussions/35849">This little article</a> does a good job explaining the difference, if you want more details.
</details>

### If you **forked** our repository

You'll need to "pull from upstream". Assuming you cloned your own fork, you'll
need to add our fork as a remote (from the folder containing your copy of Covey.Town):
```
git remote add course-staff https://github.com/kelloggm/covey.town.git
```

This command allows you to push to or pull from our repository on GitHub, in addition
to your own. To get the starter code, run:
```
git fetch course-staff
git checkout fall2025-ip1
```

### If you **cloned** our repository

In this case, you just need to fetch our changes and then switch to the appropriate branch:
```
git fetch origin
git checkout fall2025-ip1
```

### Limitations on modifying files

You can modify any files that you'd like, but you are not permitted to modify the existing
tests for Covey.Town: the only test files you can modify are the ones related to Quantum
TicTacToe.
For example, while you are permitted to modify `TicTacToeGame.ts`, you are **not** permitted to modify
its existing test suite: that test suite still must pass unmodified. This restriction represents a
backwards-compatibility constraint that is common in the real world: you're allowed to modify code
_as long as its externally-visible behavior doesn't change_. Note that the list of files in
`package.json` needs to include everything that you modified; see the submission instructions.

## Implementation Tasks

There are three high-level tasks you need to do:
* **Task 1:** implement the backend of the game (in `QuantumTicTacToe.ts`) and test it (in`QuantumTicTacToe.test.ts`). This has barely been started, so this should be the bulk of your work.
* **Task 2:** wire up the backend so that it can handle incoming events (`QuantumTicTacToeGameArea.ts`). The senior engineer who handed this off to you has written a complete test suite and
started it already: you just have to finish it.
* **Task 3:** finish wiring up the frontend and the backend by implementing the `_updateFrom` method in `QuantumTicTacToeAreaController.ts` in the frontend. Your colleague has already written tests for this, as well.

We suggest that you complete the tasks in the order presented here, but it's up to you.

### **Task 1**: QuantumTicTacToeGame (58 points)

The `QuantumTicTacToeGame` class extends the base `Game` class. The senior engineer has already
defined the relevant types for the game's state and for moves, which you can find in
the file `shared/types/CoveyTownSocket.d.ts`. They're also reproduced below:
<details><summary>QuantumTicTacToe types</summary>
{% highlight typescript %}
/**
 * Type for a move in Quantum TicTacToe
 */
export interface QuantumTicTacToeMove extends TicTacToeMove {
  board: 'A' | 'B' | 'C';
}

/**
 * Type for the state of a Quantum TicTacToe game.
 * The state of the game is represented similarly to the regular TicTacToe
 * game, but using the our Quantum move structure. We also store
 * the xScore and oScore so that it's not necessary to rerun old
 * games to determine their score.
 */
export interface QuantumTicTacToeGameState extends WinnableGameState {
  moves: ReadonlyArray<QuantumTicTacToeMove>;
  x?: PlayerID;
  o?: PlayerID;
  xScore: number;
  oScore: number;
  publiclyVisible: {
    A: boolean[][];
    B: boolean[][];
    C: boolean[][];
  };
}
{% endhighlight %}
</details>

Note how `QuantumTicTacToeMove` extends the existing `TicTacToeMove` type. The senior engineer
working on this project wanted to reuse as much of the existing TicTacToe logic as possible,
and that should be one of your goals as well as you finish their work.

#### Constructor (1 point)

The class needs a constructor that initializes all of its fields.

Grading:
* constructor implementation passes our tests: 1 point

#### Joining and Leaving the Game (8 points)

First, you should implement the basic joining and leaving functionality via the `_join()` and `_leave()` methods.
You'll need to manage the "subgames" (A, B, and C) as well as any state that the Quantum game itself
needs to manage. The senior engineer wrote a few basic tests for these functions, but you'll want
to write some of your own, as well. We recommend that you look at the implementation of the similarly-named
methods in `TicTacToeGame.ts` and `Game.ts` to get an idea of how these are supposed to work.

Grading:
* _join implementation passes our tests: 4 points
* _leave implementation passes our tests: 4 points

#### Applying a Move: Core Game Semantics (22 points)

The `applyMove` method is the core of the game: it needs to take a move and correctly update
the corresponding subgame. The senior engineer who was working on this project suggested three
helper methods: `_validateMove`, `_checkForWins`, and `_checkForGameEnding`, which are stubbed
out already. You'll need to implement these and the rest of `applyMove` itself.

The senior engineer who was working on the project had also started writing the testing infrastructure
for this method before they got sick: they wrote a `makeMove` method and two simple tests that use it
(in `QuantumTicTacToeGame.test.ts`). You'll want to expand these tests significantly.

#### Testing (27 points)

There are basic tests for `_join()`, `_leave()`, and `applyMove` present, but they aren't nearly
complete enough. You should write test cases as you implement the features above. On the autograder,
we will inject a set of 180 bugs into the reference implementation of `QuantumTicTacToeGame.ts`. For
full credit, you test suite must detect at least 167 of these 180 injected bugs. The following table
gives the scoring function for this part:

| Mutants detected | Points |
|---|---|
| >= 167 | 27 |
| 166 | 24 |
| >= 164 | 21 |
| >= 161 | 18 |
| >= 156 | 15 |
| >= 148 | 12 |
| >= 135 | 9 |
| >= 124 | 6 |
| >= 90 | 3 |
| < 90 | 0 |
|---|---|

### **Task 2**: wiring up `QuantumTicTacToeGameArea` (12 points)

The `QuantumTicTacToeGameArea` receives `InteractbleCommand`s from players who enter the area on their client. The main responsibility of this class is to interpet those commands, dispatching them as appropriate to the `QuantumTicTacToeGame` instance that it manages. In this task, you will implement the `handleCommand` method of `QuantumTicTacToeGameArea`.

There are three types of commands that the `QuantumTicTacToeGameArea` will receive, which map directly to the three methods of `QuantumTicTacToeGame` that you've already implemented.

The senior engineer whose work you're building on wrote a complete test suite for `handleCommand`, so you don't need to write any additional tests for this class.

Grading:
* your `handleCommand` implementation passes the tests: 12 points

### **Task 3:** finishing the frontend in `QuantumTicTacToeAreaController` (20 points)

The `_updateFrom` method in `QuantumTicTacToeAreaController` is responsible for synchronizing the local state of the `QuantumTicTacToeAreaController` with a new game state model received from the backend. It orchestrates the updates to the game board's visual representation and emits events to notify the UI of any changes.

It needs to:
* call the `_updateFrom` method from its superclass
* reconstruct the visible state of the three tic-tac-toe boards (A, B, and C) in the UI based on the `newModel` it receives from the backend
* emit events when the board has changed ("boardChanged" event) or when the turn has changed ("turnChanged"), because these have UI effects

In essence, this method acts as the bridge between the raw game state from the server and the user-facing representation of the game, ensuring that players only see what they are supposed to see according to the rules of Quantum Tic-Tac-Toe.

Grading:
* your `_updateFrom` method passes the tests: 20 points

## Grading
This submission will be scored out of 100 points, 90 of which will be automatically awarded by the grading script, with the remaining 10 manually awarded by the course staff.

Your code will automatically be evaluated for linter errors and warnings. Submissions that have *any* linter errors will automatically receive a grade of 0. **Do not wait to run the linter until the last minute**. To check for linter errors, run the command `npm run lint` from the terminal. The handout contains the same eslint configuration that is used by our grading script.

Your code will be automatically evaluated for functional correctness by a test suite that expands on the core tests that are distributed with the starter code.
Your tests will be automatically evaluated for functional correctness by a process that will inject bugs into our reference solution: to receive full marks your tests must detect a minimum number of injected bugs. 
Each submission will be graded against the same set of injected bugs (repeated submissions will not receive new/different injected bugs).
You will __not__ receive detailed feedback on which injected bugs you do or do not find.

The autograding script will impose a strict rate limit of 5 submissions per 24 hours.
Submissions that fail to grade will not count against the quota.
This limit exists to encourage you to start early on this assignment: students generally report that assignments like this take between 3-20 hours.
If you start early, you will be able to take full advantage of the resources that we provide to help you succeed: office hours, discussion on Discord --- and the ability to have a greater total number of submission attempts.

Your code will be manually evaluated for conformance to our course [style guide]({{ site.baseurl }}{% link style.md %}). This manual evaluation will account for 10% of your total grade on this assignment. We will manually evaluate your code for style on the following rubric:

To receive all 10 points:
* All new names (e.g. for local variables, methods, and properties) follow the naming conventions defined in our style guide
* There are no unused local variables
* All public properties and methods (other than getters, setters, and constructors) are documented with JSDoc-style comments that describes what the property/method does, as defined in our style guide
* The code and tests that you write generally follows the design principles discussed in lecture 2. In particular, your design does not have duplicated code that could have been refactored into a shared method.

We will review your code and note each violation of this rubric. We will deduct two points for each violation, up to a maximum of deducting all 10 style points.

### Submission

Submit your assignment to Gradescope (TODO: link to this semester's Gradescope course).
Please contact the instructors immediately if you have difficulty accessing the course on Gradescope.
The course entry code for Gradescope is pinned in the "#ip1-help" channel on Discord.

To submit your assignment: run the command `npm run zip` in the top-level directory of Covey.Town. This will produce a file called `covey-town.zip`. Submit that zip file on Gradescope.
Only the list of files in the `"files"` entry in the `package.json` will be included in this zip file. If you modified a file that isn't already listed there, you need to add it
to that list before you submit (we've listed an overly-conservative set of files that you are _might_ want to modify - no need to worry if you didn't make any changes to one of the files on the list).

Gradescope will provide you with feedback on your submission, but note that it will *not* include any marks that will be assigned after we manually grade your submission for code style (these marks will remain hidden until it is graded). It may take up to 40 minutes for the grading script to complete.

Gradescope is configured to only provide feedback on at most 5 submissions per-24-hours per-student (submissions that fail to run or receive a grade of 0 are not counted in that limit). We strongly encourage you to lint and test your submission on your local development machine, and *not* rely on Gradescope for providing grading feedback - relying on Gradescope is a very slow feedback loop.
To check for linter errors, run the command `npm run lint` from the terminal. The starter code contains the same eslint configuration that is used by our grading script.
