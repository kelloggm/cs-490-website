---
layout: project
title: "Homework 5: Invariants and Partial Oracles"
permalink: /projects/hw5.html
parent: Homeworks
nav_order: 6
due_date: "Wednesday, February 28, 2024, 11:59PM AoE"
submission_notes: Submit via Canvas
---

### High-level goal

The high-level goal of this two-part assignment is to learn about program invariants and partial test oracles (property-based testing and metamorphic testing).
Both of these were discussed [in lecture](../assets/lecture-06.pdf) this week.

Each part of the assignment requires you to do a task and then answer questions about
your findings, similar to HW3 and HW4. There is no autograder for this assignment.

You _may_ work with a partner for this assignment.

### Part 1: Invariants

#### Instructions

1. Familiarize yourself with the [Daikon Invariant Detector](https://plse.cs.washington.edu/daikon/download/doc/daikon/index.html).

2. Then, run Daikon on a [data structure](https://en.wikipedia.org/wiki/Data_structure) example of your choice. You may choose to run Daikon for any supported programming language (see installation instructions). You may select any data structure, but we recommend choosing a standard data structure such as a tree, graph, heap, stack, queue, trie, or hash table. If the data structure comes with a test suite, you may use that test suite. You are
also permitted to write (or generate, e.g. using one of the tools that we've discussed in this course) your own test suite.

    We strongly suggest selecting a data structure implementation that you are already familiar with. In particular, students are typically
most successful at this assignment when they select a data structure that _they implemented_ (usually, in a previous class, such as CS 610).
You **may not** select a program that has already been a subject program in this course (in particular, you may not select
`avl.py` from HW1) or that appears as an example in the Daikon user manual (linked above). Note that the data structure implementation you
select does not need to be publicly available, but you will need to make it available to the course staff (so, for example, if you
have some code from a prior course, you might include it with your submission on Canvas; I've configured Canvas to accept as many files as
you want to provide for this assignment).

#### Questions

Answer these questions as part of your writeup [rubric notes in these brackets].

1. Provide a link to the chosen data structure or include the implementation of the data structure in your submission on Canvas
(in your answer to this question, mention each extra file that you submit and its purpose).
Also provide a link to the test suite you used (or include the test suite in your submission), and explain where you got the test suite.
For this data structure and the corresponding Daikon output,
give one example for a true invariant and one example for a discovered invariant that only holds for the given test suite.
[1 point for true invariant, 1 point for invariant that only holds for the given test suite. Unbounded negative points for failing to provide
all required information.]

2. Briefly explain which (if any) types of invariants discovered by Daikon are generally useful for testing and/or debugging (alternatively, briefly explain which types are not useful). There are no wrong answers: the provided answer is evaluated based on its justification not the expressed believe.
[4 points for well-reasoned argument.]

3. For a software system that you are familiar with, briefly explain that system and state at least two types of invariants of interest (useful for testing and/or debugging). Briefly explain whether and how these invariants can be dynamically discovered.
[1 point for each invariant and explanation.]


### Part 2: Testing with Partial Oracles

This part has two variants (A and B). You only need to complete one of them. However, if you complete both, you'll receive two bonus points
on the assignment.

#### Instruction: Variant A

1. Clone an open-source repository of your choice for a non-trivial software system that is amenable to metamorphic testing. The software system may be written in any programming language, but it must provide a build system for compilation and testing. You may **not** select a program that was used as part of a previous assignment in this course as a _subject_ program (so you could select AFL, but you could not select libpng).

2. For the chosen software system, design **two** metamorphic relations (MRs):
* The two MRs must hold for arbitrary, well-formed inputs.
* For **at least one MR**, the output relation must **not** be the identity function.

3. Implement your two MRs as test-case generators, which take an initial test case as input and produce a follow-up
test case as output.

4. Based on the designed MRs, automatically generate a few test cases and execute them. (For the initial test cases, you may rely on random input generation, any existing test cases, or manually created test cases.)

#### Instructions: Variant B

1. Choose a non-trivial online software system for classification (e.g., text, images, code, etc.).

2. For the chosen software system, design **three** metamorphic relations (MRs):
* The three MRs must hold for arbitrary, well-formed inputs.
* For **at least two** MRs, the output relation must **not** be the identity function.

3. Based on the designed MRs, generate a few test cases, execute the online system, and observe its output. (You may automate the test-case generation.)

#### Questions

Answer these questions as part of your writeup [rubric notes in these brackets].

4. Describe the chosen software system and justify for each of the designed MRs why it must hold for arbitrary, well- formed inputs.
[1 point for the description of the system, 2 points for the descriptions of the MRs.]

5. Briefly summarize your observations about testing with MRs and state at least two characteristics of effective MRs. You may reason about the specific MRs you designed or MRs in general. [2 points for insightful observation, 1 point each for characteristics of effective MRs.]

### Submission: Written Report

Write up your answers to the 5 questions above (Part 1 Questions 1-3, Part 2 Questions 1-2).
Submit a plaintext (.txt) or PDF file to Canvas. Also submit any code or test cases that you used
that are not publicly-available and linked from your report.

Although we do not have explicit formatting guidelines that we require you to follow, is is easier for the graders to interpret text that is presented clearly. We encourage you to format your results in a manner that you think would simplify reading later. (One way to double-check would be to write your report draft and then step back for a few minutes and then re-read the text or have your partner re-read the text.) You may organize your report as paragraphs, bullet points, explicit answers to each question, or whatever other organization you think will be easiest for us to interpret.

As usual in this class, you may use files, benchmarks or resources from the Internet (unlike in many other classes), provided you cite them in your written report. (If you use the same resource many times, such as StackOverflow, one citation per resource suffices.)

### Frequently-asked Questions

1. **Question**: I'm not sure what "non-trivial software system" means in Part 2.

    **Answer**: For Variant A, the software should be publicly-available (e.g., on Github) and actively-maintained (i.e., commits are regularly made to add features or fix bugs). It should also exist to accomplish some task - it must not be a toy or a course project (e.g., a "twitter clone" that is not actually deployed anywhere is not allowed). We recommend that you select a program in the same category as the subject programs from previous homeworks, (e.g., JSoup or libpng would be good choices, if they had not been used in previous homeworks).

    For Variant B, the software should be actively supported, and you should be able to point to a URL. We typically expect you to choose well-known online classification systems if you choose Variant B.

2. **Question**: Is it possible to start Part 2 before finishing Part 1?

    **Answer**: There are no dependencies between Part 1 and Part 2, and you can complete them in either order.