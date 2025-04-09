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
* **PA4c1** requires you to implement a dead-code eliminator for Cool three-address code (i.e., the same format as PA3c2). This dead-code eliminator need not be part of the same codebase as the rest of PA4 -- the specification for it (see below) is standalone. However, your final PA4 submission is required to include a dead-code eliminator, so we strongly suggest that you integrate PA4c1 into your existing codebase. For example, you might have a command-line switch in your main codebase that makes it match the PA4c1 specification, which you enable by default when submitting PA4c1. This checkpoint is due on **Monday, April 28**.
* **PA4 (full)** will be evaluated on the day of the final exam. You will automatically make a submission to PA4 when you submit PA3 (i.e., we will add your PA3 submission to the leaderboard). You can continue to make changes to your optimizer and resubmit it as many times as you'd like between the PA3 and PA4 deadlines.

### PA4c1: Dead Code Elimination

PA4c1 is a stand-alone checkpoint assignment designed to encourage you to write a [dead-code eliminator](http://en.wikipedia.org/wiki/Dead_code_elimination) for [Cool three-address code](../pa3.html#pa3c2-three-address-code-generator).
Since your final PA4 submission is _required_ to include a dead-code eliminator, we encourage you to use this checkpoint as an excuse to implement one. However,
if it would be more convenient for your compiler's design to do dead-code elimination on another IR, you _can_ skip this checkpoint (but we don't
recommend it, and it will cost you a few points). Come talk to the course staff if you're unsure.

For this checkpoint, your dead-code eliminator should implement a "global" [live-variable analysis](https://en.wikipedia.org/wiki/Live-variable_analysis)
(like the one discussed in class); recall that "global", in the context of optimization, means "considers a single method at once."

#### Specification

You should submit a program that takes a single command-line argument (e.g., `file.cl-tac`). That argument will be an ASCII text Cool Three Address Code file (as described in the PA3c2 specification)
corresponding to a single method. The cl-tac file will always be well-formed (i.e., there will be no errors in the cl-tac file).
Your program must output a revised, valid .cl-tac file to standard output. The output should be the same as the input but with dead code removed.
Your program will consist of a number of source files, all in the same programming language. We suggest (but do not require) that it be a variant of your main
PA3/PA4 codebase; we would implement this specification by setting a flag in our compiler's codebase.

#### Dead Code Elimination

A variable is **live** if it may be needed in the future.
That is, an assignment to variable _v_ at point _p_ is live if there exists a path from _p_ to the function exit along which _v_ is read before it is overwritten.

For example, consider the following TAC:
```
a <- int 1
b <- int 3
c <- + a b 
d <- int 7
retval <- call out_int c 
return retval 
```

On the fourth line, the assignment to _d_ is dead because _d_ is not subsequently used. Dead assignments can be removed. Often eliminating one piece of dead code can reveal additional dead code.
For example, consider this fragment of TAC:
```
a <- int 1
b <- int 3
c <- + a b 
d <- int 7
e <- + d d 
retval <- call out_int c 
return retval 
```

In above example, the assignment to _d_ is **not** dead (yet!) but the assignment to _e_ is dead. Once the assignment to _e_ is eliminated, the assignment to _d_ becomes dead and can then be eliminated. Thus, live variable analysis and dead code elimination must be repeated until nothing further changes.

You should use the [live variable analysis](http://en.wikipedia.org/wiki/Live_variable_analysis) form of [data-flow analysis](http://en.wikipedia.org/wiki/Data-flow_analysis) to determine which assignments are dead code. We discussed this topic in class (in the "Global Optimization" and "Dead Code Elimination" lectures), but you are not required to follow the lecture slides' formalism: you may use any of the (many) equivalent analyses described online, in the textbook, etc - as long as you preserve the program's semantics and remove dead code.

Note that function calls with I/O side effects should never be eliminated.

#### Basic Blocks and Control-Flow Graphs

A [basic block](http://en.wikipedia.org/wiki/Basic_block) is a sequence of instructions with only one control-flow entry and one control-flow exit. That is, once you start executing the instructions in a basic block, you must execute all of them — you cannot jump out early or jump in half-way through.

A _local_ dataflow analysis operates on basic blocks. As part of this checkpoint, you will need to implement a local dead-code eliminator.

As part of this assignment you will also implement a _global_ dataflow analysis that operates on multiple basic blocks (that together form one entire method). A [control-flow graph](http://en.wikipedia.org/wiki/Control_flow_graph) is a graph in which the nodes are basic blocks and the edges represent potential control flow.

You are not required to use these formalisms, exactly, in the your implementation. However, we _strongly_ suggest that you explicitly represent the basic blocks and control-flow graph of the input TAC program.

#### Commentary

A successful implementation of this checkpoint will have the following stages:
1. Deserialize the input .cl-tac file
2. Identify basic blocks and construct the control-flow graph
3. Repeat until nothing changes:
    1. Perform global live variable analysis on the control-flow graph
        * This involves local live variable analysis on individual statements or basic blocks
    2. Eliminate dead code
4. Serialize the result to standard output in .cl-tac format

You can do basic testing as follows:
```
$ cool --tac file.cl --out original
$ cool --tac --opt file.cl --out ref_optimized
$ my-dce original.cl-tac > my_optimized.cl-tac
$ cool ref_optimized.cl-tac > optimized.output
$ cool my_optimized.cl-tac > my.output
$ diff optimized.output my.output
$ cool --profile ref_optimized.cl-tac | grep STEPS
$ cool --profile my_optimized.cl-tac | grep STEPS
```

Passing `--opt` and `--tac` to the reference compiler will cause the reference compiler to perform dead code elimination before emitting the .cl-tac file.

#### Grading

There are fifteen test cases for PA4c1 (they are the same test cases, in the same order, that were used for PA3c3).
We will run each with 10 inputs. You _lose_ one-tenth of a point for each input for which you do not
produce the correct output, to a miniumum of zero. You gain one-tenth of a point for each test input for which
your generated cl-tac, when simulated, executes fewer instructions than a threshold chosen by the course staff.
Your score is rounded down to the nearest integer.

### PA4 (full): the Optimizer

The full PA4 assignment is an explicit competition: your goal is to produce faster assembly programs (while preserving semantics)
than both your classmates' compiler and our reference compiler.
We provide a **pseudo-anonymous leaderboard** for this assignment. Your submissions will automatically appear on the leaderboard.

The leaderboard has three kinds of submissions:
* student submissions. These are labeled with a student-chosen pseudonym.
* reference submissions. These are labeled "reference" and "refernce opt"; they correspond directly to version 1.39 of the reference compiler
without the `--opt` flag and with the `--opt` flag, respectively. You must beat these for full credit on the assignment.
* "Boss" submissions, which are graciously provided by people who have taken this class or a similar one in the past (including your professor).
Beating these is totally optional, but you might enjoy gloating.

#### Pseudonym Rules

Gradescope will ask you to provide a pseudonym for the leaderboard. You may select any string, subject to the following rules:
* the string cannot include your name or the name of any other person enrolled in the class. This rule includes nicknames,
and you must obey its **spirit** rather than its letter. Do not intentionally choose a pseudonym to make fun of a classmate.
* the string cannot violate university policies and/or laws related to hate speech or other offensive material.
* the string cannot be, in the view of the instructor, "unsafe for work".

Submissions that violate these rules will receive scores of zero, and the course staff may take further action against you
(including referring you to the dean of students, failing you, etc.) if you violate them.
We encourage you to choose a humorous, non-identifying name for your team. Be as creative as you like, so long as
it's "safe for work". But please do not make me regret giving you the freedom to pick a name.

You're explicitly permitted to lie to your classmates about which pseudonym refers to your compiler. You are also
permitted to use more than one pseudonym, but please keep the number of pseudonyms relatively small (e.g., no more than
3 or 4 per team, unless there is a good reason).

#### Leaderboard scoring

Our autograder will evaluate each submission along two axes:
* your **correctness score** _C_ is the fraction of a set of (test case, input) pairs for which your compiler's
generated x86 code and the x86 code generated by the reference compiler (without `--opt`) produce the same
output. _C_ is a real value in the range [0, 1].
* your **improvement score** _I_ is the relative improvement of your compiler's generated assembly over the
generated assembly from the reference compiler (again, on a set of Cool program + test input pairs) in
terms of clock cycles, as measured by `perf stat -r 100`. We measure this for each test case + input pair
individually, and then average all pairs for which you got the same output as the reference compiler.
_I_ is a positive real value. It may be either greater or less than 1; a value greater than 1 indicates that the
code you produce is _slower_ than the reference compiler; less than 1 indicates that your code is _faster_.

Your **overall score** _S_ is defined by the following formula (higher is better):

_S = C^2 * 1/I_

Submissions will be ranked on the leaderboard by their overall score, but all three scores will be visible.
Note that the reason that we square your correctness score is that we are explicitly penalizing you for
breaking the .

#### Grading

Grading (out of 100)
* 64 points - for optimizer performance tests
  * -0 - performance better than "reference --opt"
  * -16 - performance better than "reference" but worse than "reference --opt'
  * -32 - performance worse than "reference"
  * -64 - performance worse than "0.9 * reference"
* -48 points - hard-coding some benchmark files rather than writing a generic optimizer
* -24 points - total failure to implement control-flow graphs, liveness and dead code elimination
* -12 points - partial failure to implement control-flow graphs, liveness and dead code elimination
* 16 points - for a clear description in your README
  * 16 - thorough discussion of design decisions (e.g., the handling of the control flow graph, live variable analysis, dead code elimination, how code generation and intermediate representations relate, other optimizations performed) and choice of benchmarks; multiple paragraphs of coherent English sentences are required
  * 8 - vague or hard to understand; omits important details
  * 0 - little to no effort, or submitted an RTF/DOC/PDF file instead of plain TXT
* 8 points - for valid benchmark1.cl and benchmark2.cl
  * 8 - both examples take 50,000 instructions or fewer to execute via the reference compiler with --asm --profile
  * 4 - one benchmark is not valid
  * 0 - no valid benchmarks included
* 8 points - for code cleanliness
  * 8 - code is mostly clean and well-commented
  * 4 - code is sloppy and/or poorly commented in places
  * 0 - little to no effort to organize and document code
* 4 points - for PA4c1
  * 4 - 15 points on PA4c1
  * 3 - 11-14 points on PA4c1
  * 2 - 6-10 points on PA4c1, or you scored 0-5 on PA4c1 but your final optimizer includes DCE and beats reference with `--opt`
  * 1 - 1-5 points on PA4c1, or you scored 0 on PA4c1 but your final optimizer includes DCE and beats reference
  * 0 - 0 points on PA4c1