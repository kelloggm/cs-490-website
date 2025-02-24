---
layout: project
title: "PA3: Code Generator"
permalink: /projects/pa3.html
parent: Programming Assignments
nav_order: 3
due_date: "Monday, 7 April 2025, 11:59PM AoE."
submission_notes: Submit on GradeScope
---

**This page is still under construction: check back for more details later.**

You may complete this assignment in any language listed on the [languages page](../languages/) in buckets 1, 2, or 3. You are required to complete this assignment and PA4 in
the same language (you are expected to modify you PA3 assignment for PA4).

You may work in a team of two people for this assignment. If you worked with a teammate on PA2, you do not need to work with the same teammate for this assignment.
You do not need to keep the same teammate between this assignment and PA4, but if you choose not to work with your
PA3 teammate again on PA4, you _must_ work alone on PA4.
The course staff are not responsible for finding you a willing teammate. You are always permitted to work alone, if you choose.

### Goal

For this assignment you will write a code generator. Among other things, this involves implementing the operational semantics specification of Cool. You will track enough information to generate legitimate run-time errors (e.g., dispatch on void). You do not have to worry about "malformed input" because the semantic analyzer (from PA2) has already ruled out bad programs.
You will also write additional code to unserialize the class map, implementation map, parent map, and annotated AST produced by the semantic analyzer.

### Summary of Checkpoints

You need to make four submissions for this assignment:
* **PA3c1** requires you to write test cases (i.e., Cool programs) that find injected bugs in our reference compiler. This checkpoint ensures that you have a robust test suite for your own compiler before you begin implementing it in earnest. This checkpoint is relatively straightforward (you just need to write small Cool programs), so it due early: on **Friday, March 7**.
* **PA3c2** requires you to produce a simple intermediate representation for (some) Cool programs ("three-address code" (TAC), which we'll discuss in class). While it's up to you how much you want to use TAC for the rest of PA3, we think it's a useful intermediate representation, and we want to force you to make some progress early. And, it's hard to break the compiler up into sensible chunks, so this is the best that we can do. Since producing TAC is pretty straightforward compared to the rest of the compiler implementation, this checkpoint is due relatively quickly after PA3c1: on **Friday, March 14**.
* **PA3c3** requires that your compiler generates assembly instructions for certain simple Cool programs. This is harder than it sounds: once you have this part working, getting to the full compiler is usually easier than getting to this point. For that reason, we give you a few weeks to make it to this point: it is due on **Monday, March 31**.
* **PA3 (full)** requires that your compiler handle all of Cool. It is due on **Monday, April 7**.

### Specification

You must create three artifacts:
1. A program that takes a single command-line argument (e.g., `file.cl-type`). That argument will be an ASCII text Cool class map, implementation map, parent map and annotated AST file (as described in PA2). Your program must emit x86-64 Assembly Language (`file.s`). Your program will consist of a number of source files in a single language.
  * Compiling `file.s` with `gcc -no-pie -static` on a 64-bit x86 Linux system (specifically, Ubuntu 22.04) must produce an executable that, when run, produces the correct output for `file.cl` according to Cool's operational semantics.
   * You will only be given `.cl-type` files from programs that pass the semantic analysis phase of the reference compiler. You are not responsible for correctly handling `(1+"hello")` programs.
2. A plain ASCII text file called `readme.txt` describing your design decisions and choice of test cases. See the grading rubric. A few paragraphs should suffice.
3. Testcases `test1.cl`, `test2.cl`, `test3.cl` and `test4.cl`. The testcases should exercise compiler and run-time error corner cases. See the description of PA3c1, below.

#### Error Reporting

You are guaranteed that the `file.cl-type` input file will be correctly formed and will correspond to a well-typed Cool program. Thus, there will not be any direct static errors in the input. Those were all caught by the semantic analyzer earlier.

However, you must generate `file.s` so that it checks for and reports run-time errors. When your `file.s` program detects an error, it should use Cool's built-ins (e.g., `IO.out_string`)via assembly instructions to cause an error string to be printed to the screen.

To report an error, write the string `ERROR:` _line_number_`: Exception:` _message_ and terminate the program. You may generate your `file.s` so that it writes whatever you want in the message, but it should be fairly indicative. Example erroneous input:
```
class Main inherits IO {
  my_void_io : IO ; -- no initializer => void value
  main() : Object {
    my_void_io.out_string("Hello, world.\n")
  } ;
} ;
```

For such an input, you must generate a well-formed `file.s` assmebly language file. However, when that file is executed on an x86-64 machine, it will produce output such as:
```
ERROR: 4: Exception: dispatch on void
```

To put this another way, rather than actually checking for errors directly, you must _generate assembly code_ that will later check for and report errors. You probably want to
examine how the reference compiler does this to get an idea of what to do.

#### Line Numbers for Error Reporting

The typing rules do not directly specify the line numbers on which errors are to be reported. As of v1.36, the Cool reference compiler uses these guidelines:
* Stack overflow: undefined (not your responsibility)
* Division by zero: location of the division expression
* Substring out of range: location of the internal expression (i.e., 0)
* Dispatch on void: location of dispatch expression
* case-related errors: location of case expression

Note that the reference _interpreter_ uses different line numbers in some cases; you must match the reference _compiler_ (which you invoke by passing the `--x86` argument to `cool`).

#### Commentary

You will have to handle all of the _internal_ functions (e.g., `IO.out_string`) that are defined in the Cool Reference Manual.

You can do basic testing as follows:
```
cool --x86 file.cl-type
gcc -no-pie -static file.s
./a.out &> reference-output
my-code-generator file.cl-type
gcc -no-pie -static file.s
./a.out &> my-output
diff my-output reference-output
```

Whitespace and newlines do not matter in your `file.s` assembly code. However, **whitespace and newlines do matter** for the _output_ of your assembly code. This is because you are specifically being asked to implement IO and string functions.

You should implement all of the [operational semantics rules in the Reference Manual](../crm/modern/Operational%20Semantics.html). You will also have to implement all of the built-in functions on the [five Basic Classes](../crm/modern/Basic%20Classes.html).

### PA3c1: Testing the Reference Compiler

PA3c1 is a **preliminary testing exercise** that introduces a form of [test-driven development](http://en.wikipedia.org/wiki/Test-driven_development)
or [mutation testing](http://en.wikipedia.org/wiki/Mutation_testing) into our software development process and requires you to construct a high-quality test suite.

The goal of PA3c1 is to leave you with a high-quality test suite of Cool programs that you can use to evaluate your own PA3 and PA4 code generators. Writing a code generator requires you to consider many corner cases when reading the formal and informal semantics in the Cool Reference Manual. While you you can check for correct "positive" behavior by executing your code generator's output against the reference compiler on existing "good" Cool programs, it is comparatively harder to check for "negative" behavior (i.e., run-time errors, strange corner cases).

If you fail to construct a rich test suite of semantically-valid programs you will face a frustrating series of "you fail held-out negative test x" reports for PA3c3 and PA3 proper, which can turn into unproductive guessing games. Because students often report that this is frustrating (even though it is, shall we say, infinitely more realistic than making all of the post-deployment tests visible in advance), the PA3c1 preliminary testing exercise provides a structured means to help you get started with the construction of a rich test suite.

The course staff have produced 21 variants of the reference compiler, each with a secret [intentionally-introduced defect](http://en.wikipedia.org/wiki/Fault_injection) related to code generation. A high-quality test suite is one that reveals each introduced defect by showing a difference between the behavior of the true reference compiler and the corresponding buggy version. You desire a high-quality test suite to help you gain confidence in your own PA3 (and, eventually, PA4) submission.

For PA3c1, you must produce semantically-valid Cool programs (test cases). There are 21 separate held-out seeded code generator bugs waiting on the grading server. For each bug, if one of your tests causes the reference and the buggy version to produce difference output, you win: that test has revealed that bug. For full credit your tests must reveal at least 15 of the 21 unknown defects.

The secret defects that we have injected into the reference compiler correspond to common defects made by students in PA3. Thus, if you make a rich test suite for PA3c1 that reveals many defects, you can use it on your own PA3 submission to reveal and fix your own bugs!

For PA3c1 you should turn in (electronically):
* A zip file containing a set of .cl files: Cool code generator testcases.
  * Each testcase you submit must be syntactically semantically valid (i.e., must pass `cool --type`).
  * Each testcase you submit _may_ have a corresponding input file. For example, if you submit `wes.cl` you may also submit `wes.cl-input` (if you do, you must follow this naming convention or it will be ignored).
  * Each testcase you submit must be at most 2048 characters (i.e., `wc -c yourtest.cl` says 2048 or less). You want each of your testcases to be meaningful so that it helps you narrow down a bug later (cf. [Delta Debugging](https://en.wikipedia.org/wiki/Delta_debugging)).
    * You, A Mischevious Student: Ha ha! I will get around this edict by removing comments and compressing whitespace and variable names.
    * Me, A Former Mischevious Student: Remember, the point of PA3c1 is not to make me happy, but to provide you with a high quality test suite. You're only hurting yourself later by making low-quality tests now. When your compiler fails one of your own tests later you'll end up shrinking the test down as part of debugging, so you're not actually saving yourself any time.
  * No testcase should be named `bug`... or `ref`... because the testing server uses those prefices internally. If you submit a test case with such a name it will be ignored. (Limited course resources can either be spent making better lectures, grading your assignments, etc., or ironing out wrinkles such as these from grading scripts. We have chosen to focus on pedagogy.)

Your zip file _may_ also contain:
* `team.txt` -- an optional file listing your other team member (if you are not working in a team, do not include this file)

Hint: because you can find "positive" bugs in your code generator more easily (e.g., by running your code generator on the known-good Cool programs from cool-examples.zip), this exercise is somewhat biased toward "negative" or "tricky" bugs.

