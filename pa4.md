---
layout: project
title: "PA4: Optimizer"
permalink: /projects/pa4.html
parent: Programming Assignments
nav_order: 4
due_date: "Day of Your Final Exam, 2025, 11:59PM AoE."
submission_notes: Submit on GradeScope
---

**This page is still under construction: check back for more details later.**

You are advised to complete this assignment in the same language you used for PA3. Your starter code for this assignment is typically your final PA3 submission.
You are permitted to, but strongly discouraged from, starting over without using your PA3 submission. If you plan to do so, you should discuss the situation
with the instructor and/or TAs first.

You may work in a team of two people for this assignment if and only if you worked in a team for PA3 and both teammates are still willing to work together.
If either teammate does not want to work together anymore, both of you _must_ work alone (but you may each start from a copy of the shared PA3 starter code).
The course staff are not responsible for finding you a willing teammate. You are always permitted to work alone, if you choose.

### Goal

For this assignment you will write an _optimizing_ code generator. This typically involves transforming the abstract syntax tree into a control-flow graph of three-address code and applying a number of dataflow analyses and optimizations. In addition, students typically apply pattern-matching optimizations at the AST level and peephole optimizations at the assembly level.

In all cases, the optimized assembly code you emit must produce **exactly the same** result as the reference compiler. The first rule of optimization is "don't break the program".

You do not have to worry about "malformed source code" because the semantic analyzer (from PA2) has already ruled out bad programs.

This assignment is an explicit competition. You will receive more credit if your optimizer is "better" than that of other students in terms of the number of machine cycles
that your generated assembly code takes to execute various test programs.

### Summary of Checkpoints

There is one checkpoint for the Optimizer:
* **PA4c1** requires you to implement a dead-code eliminator for Cool three-address code (i.e., the same format as PA3c2). This dead-code eliminator need not be part of the same codebase as the rest of PA4 -- the specification for (see below) is standalone. However, your final PA4 submission is required to include a dead-code eliminator, so we strongly suggest that you integrate PA4c1 into your existing codebase. For example, you might have a command-line switch in your main codebase that makes it match the PA4c1 specification, which you enable by default when submitting PA4c1. This checkpoint is due on **Monday, April 21**.
* **PA4 (full)** will be evaluated on the day of the final exam. You will automatically make a submission to PA4 when you submit PA3 (i.e., we will add your PA3 submission to the leaderboard). You can continue to make changes to your optimizer and resubmit it as many times as you'd like between the PA3 and PA4 deadlines.
