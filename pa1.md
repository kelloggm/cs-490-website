---
layout: project
title: "PA1: Rosetta Stone"
permalink: /projects/pa1.html
parent: Programming Assignments
nav_order: 1
due_date: "Monday, 3 February 2025, 11:59PM AoE."
submission_notes: Submit on GradeScope
---

The [Rosetta Stone](http://en.wikipedia.org/wiki/Rosetta_Stone) aided linguistic understanding by providing the same text in three different languages. In this project you will implement the same simple program in four separate languages. Each of your implementations will have exactly the same interface, will otherwise adhere to the same specification, and should behave exactly the same way.

You must choose one language from each of the following buckets for your four implementations:
* _Bucket 1: Languages You Already Know_: Java, C, C++, or Python3
* _Bucket 2: Languages With An Unusual Type System_: Kotlin, Rust, or Scala
* _Bucket 3: Functional Languages_: OCaml or Haskell
* _Bucket 4: Project Language_: [Classroom Object-Oriented Language (COOL)](../crm/)

Each bucket is intended to challenge you in a different way. _Bucket 1_ gives you a chance to implement the solution in a language you're already comfortable in, so that you can focus on the problem. _Bucket 2_ challenges you to redo that implementation in a language that shares some similarities with languages that you've seen before,
but which also includes some features you might be unfamiliar with. In particular, all _Bucket 2_ languages support programming in a structured imperative style, even if they permit functional programming. _Bucket 3_ challenges you to redo the implementation in a true functional programming language. Finally, _Bucket 4_ will familiarize you with the course project language COOL ("Classroom Object-Oriented Language"). All subsequent assignments in this course (PA2-PA4) involve implementing parts of a COOL compiler, so you'll have an easier time with them if you've used the language a bit. COOL itself is also a bit tricky to program in: it intentionally omits many convenience features of higher-level languages to simplify the compiler implementation process, but that can make it unwieldy for writing "real" programs.

For this assignment, you must work **alone**. Subsequent assignments will allow you (optionally) to work in pairs.

## Specification

Your program must take in a list of dependent tasks and either output a valid order in which to perform them or the single word `cycle`.

Your program will accept a number of lines of textual input (via [standard input](http://en.wikipedia.org/wiki/Standard_streams)). There are no command-line arguments — you must always read from standard input. Do not open a named file. Instead, always read from standard input.

That text input will contain a non-zero but even number of lines. Every two lines represent a _pair_ of tasks. The first line gives the name of a task, the second line gives the name of a task that it depends on. This text input is also called the _task list_.

The task list will contain only standard ASCII characters (no UTF/8 Unicode or special accents). The goal is to test programming and program language concepts, not your internationalization abilities.

Each task name starts at the beginning of the line and extends all the way up to (but not including) the end of that line. So the newline or carriage return characters `\r` or `\n` are not part of the task name. Each task name is at most 60 characters long. (This limit is to make any C implementation easier. Most languages support longer strings natively, and can thus ignore this length limit.)

Example task list:
```
learn C
read the C tutorial
do PA1
learn C
```

The interpretation is that in order to `learn C` one must first `read the C tutorial` and that in order to `do PA1` one must first `learn C`. Desired output for this example:
```
read the C tutorial
learn C
do PA1
```

If the task list containts a _cycle_ of any size, your program should output exactly and only the word `cycle`. Example cyclic input:
```
get a job
have experience
have experience
work on a job
work on a job
get a job
```

Even if the task list contains a few non-cyclic parts, any single cycle forces you to output only the word `cycle`.

Always output to [standard output](http://en.wikipedia.org/wiki/Standard_streams) only. Do not write anything to stderr.

There is no fixed limit on the number of lines in the task list (although it is not zero and it is even).

Two tasks with the same name are really just the same task. Use standard string equality.

Duplicated pairs of tasks are not allowed. For example:
```
learn C
read the C tutorial
do PA1
learn C
learn C
read the C tutorial
```
... that task list is not valid input because the pair `learn C`/`read the C tutorial` appears twice. Program behavior if the task list contains a duplicate pair is undefined. You will not be tested on it.

Your program may **not** cause any other file I/O to be performed, such as creating a temporary file to keep track of some intermediate sorting results or writing to stderr (or even causing the interpreter to write a warning to stderr). You do not need any such temporary files or stderr-printing to solve this problem.

### Choosing Among Unconstrained Tasks

If there are multiple outstanding unconstrained tasks, your program should output them in ascending ASCII alphabetical order. That is, if you ever have two or more tasks, each of which has no remaining dependencies, output the one that comes first ASCII-alphabetically. (This constraint makes your program deterministic; for any given input there is only one correct output.) Example:
```
learn C
understand C pointers
learn C
read the C tutorial
do PA1
learn C
```

Because r comes before u, your output should be:
```
read the C tutorial
understand C pointers
learn C
do PA1
```

To put it another way, consider this task list:
```
B
A
C
D
C
E
```

Which yields a dependency graph like this:
```
A  D E
|  \ /
B   C
```
The proper ordering for this set of tasks is `A B D E C`. Note that `B` comes before `D` and `E`, even though `B` depends on `A`. This is because, once `A` is finished, `B` is free to go and it comes first alphabetically. You may want to consider this requirement when you pick your sorting algorithm. Given this requirement the answer `A D E B C` is incorrect and will receive no credit.

### Resources

Some resources are available to help you:
* [pa1-hint.zip](../assets/pa1-hint.zip) provides concrete implementations of "task list reversal" (a similar, but simpler, problem) in a wide collection of languages, including many of those in our buckets. You might use this resource to compare how to accomplish various tasks in different languages.
* [pa1-testcases.zip](../assets/pa1-testcases.zip) includes a number of test inputs and expected outputs so that you can test your programs before submitting.
* [pa1-testcases-unix.zip](../assets/pa1-testcases-unix.zip) as above, but with unix linefeed formatting in all text files for use in Mac OS X, Ubuntu, or another Linux.

### Commentary

This problem is just [topological sort](http://en.wikipedia.org/wiki/Topological_sort) not-so-cleverly disguised. Feel free to look up how to do toposort on the internet or ask your favorite generative AI tool to explain it to you (but remember that you must turn in your own work; you may not copy someone else's code and claim it as your own).

Take a look at the files in [pa1-hint.zip](../assets/pa1-hint.zip). You could do worse than using them as starting points.

If you're having trouble writing anything reasonable in Cool, don't forget to look at the [other example Cool programs](../assets/cool-examples.zip).

Building and maintaining an explicit graph structure is probably overkill.

### Video Guides

This assignment is a mildly-modified version of [Wes Weimer](https://web.eecs.umich.edu/~weimerw/)'s [similar assignment](https://weimer.github.io/csci2320/pa1.html) (the only differences are in language choices).
Wes has kindly prepared a number of video guides to help students get started in various languages:
* [Python](https://youtu.be/YuNOs0u2YQ0)
* [OCaml](https://youtu.be/LkiIQxC-kQ8)
* [COOL](https://youtu.be/cDl4nTcQn10) (object-oriented style, long)
* [COOL](https://youtu.be/02Drt-cyho8) (imperative style, short)

Reminder: You can watch YouTube videos at 1.5x speed with full audio.

### Checkpoints

This assignment has two checkpoints before the final due date. At the first checkpoint, you must turn in your _Bucket 1_ implementation. At the second checkpoint, you must turn in any one implementation from a bucket other than _Bucket 1_. At the final due date, you need to turn in all four implementations. This structure is designed to encourage you to steadily work on the assignment, rather than trying to do all four implementations in a rush at the end. It also separates the task into three stages, each with a different challenge: (1) before the first checkpoint, the challenge is _Can I write this program at all?_, even in a familiar language; (2) between the first and second checkpoint, the challenge is _Can I write this program in some other language?_; (3) after the second checkpoint, the challenge is _Can I write this program in multiple unfamiliar languages?_. Note that although the checkpoints get progressively more difficult, the time alloted to them is about the same. That's because I expect you to become _very_ comfortable with this program by the time you're working on your fourth implementation.

The schedule for the checkpoints is:
* PA1c1: due Monday, January 27 AoE. Note that this is the the drop date. If you are struggling to finish PA1c1 in time, you should consider dropping the class: the workload is likely too high for you to handle this semester.
* PA1c2: due Thursday, January 30 AoE.
* full PA1: due Monday, February 3 AoE.

Note the ["AoE" timezone](https://en.wikipedia.org/wiki/Anywhere_on_Earth) means "Anywhere on Earth". This means that you can submit that part of the assignment as long as it is the given date _somewhere on the planet_. Currently, the last place where each day ends on Earth is the [Howland and Baker Islands](https://en.wikipedia.org/wiki/Howland_and_Baker_Islands). This transition happens at about 7am eastern time the next day (but this can vary with daylight savings time!). I use AoE for due dates because I won't actually start grading until the next day: if you want to stay up all night doing the assignment, that's your business. It also means that when I say that an assignment is due on a particular date (e.g., "PA1 is due on February 3rd"), you unambiguously know what I mean.

### What To Turn In For PA1c1

For PA1c1, turn in **any one** of the following files:
* `rosetta.py` (Python)
* `rosetta.c` (C)
* `rosetta.cpp` (C++)
* `Rosetta.java` (Java)

We will use the file extension to determine which language you are using. See the [languages page](../languages/) for information about the versions of each language that the grading server supports.

### What To Turn In For PA1c2

Submit any one of the following files:
* `rosetta.kt` (Kotlin)
* `rosetta.rs` (Rust)
* `Rosetta.scala` (Scala)
* `rosetta.hs` (Haskell)
* `rosetta.ml` (OCaml)
* `rosetta.cl` (COOL)

### What To Turn In For PA1

Turn in six files:
* any one of `rosetta.py`, `rosetta.c`, `rosetta.cpp`, **or** `Rosetta.java`
* any one of `rosetta.kt`, `rosetta.rs`, **or** `Rosetta.scala`
* either `rosetta.hs` **or** `rosetta.ml`
* `rosetta.cl`
* `testcase.list`, which should contain a valid **novel** task list (it may or may not contain a cycle — your choice). **Novel** in this context means "different from the test cases distributed with the assignment in some meaningful way that you will identify in your `README.txt`.
* `README.txt`, a **plain ASCII text file** (not a Word file, not an RTF file, not an HTML file) describing your design decisions. Which language did you start with? How did you store the (implicit) graph? Which language was the hardest? Why is your test case novel? One or two English paragraphs should suffice. Spelling, grammar, capitalization and punctuation all count.

### Grading Rubric

PA1 Grading (out of 25 points):
* 20 points — autograding
  * 2 points — autograder tests for PA1c1
  * 2 points - autograder tests for PA1c2
  * 16 points — autograder tests for PA1
  * The scoring is proportional: if there are 8 tests for PA1c1 and your best submission passes 4 of them (50%), you will receive 1/2 points for PA1c1 (50%).
* 4 points — for a clear description in your `README.txt`
  * 4 — thorough discussion of design decisions (including language comparisons) and choice of test cases; a few paragraphs of coherent English sentences should be fine
  * 2 — vague or hard to understand; omits important details
  * 0 — little to no effort, or submitted an RTF/DOC/PDF file instead of plain TXT
* 1 point — for a valid `testcase.list` file


