---
layout: project
title: "Homework 1: Coverage Warmup"
permalink: /projects/hw1.html
parent: Homeworks
nav_order: 2
due_date: "Wednesday, January 31, 2024, 11:59PM AoE"
submission_notes: Submit via Gradescope (test cases) and Canvas (written report)
---

In this assignment (and in [HW2](hw2.html)), you will create a [high-coverage](https://en.wikipedia.org/wiki/Code_coverage) [test suite](https://en.wikipedia.org/wiki/Test_suite).
The main difference between this homework and HW2 is the complexity of the program you have to test:
in this assignment, the program is relatively simple and you can probably read the whole thing fairly quickly.
In HW2, the program is large enough that you probably can't read the whole thing, even if you spend the whole
week on it. In that way, HW2 is much more realistic.
You will then be asked to write a short report reflecting on the activity.

There is no particular assumption that you are familiar with any of the subject programs in this assignment
or any other assignment in this class.
Indeed, that is the point: you will be applying testing concepts to unknown software.

You may work with a partner for this assignment. Only one partner needs to submit for any of the programming assignments on the autograder, but you do need to use Gradescope's interface to select your partner. [(Here is a video showing Gradescope partner selection.)](https://www.youtube.com/watch?v=rue7p_kATLA&t=1m6s). Only one of you needs to submit the written report on Canvas, but similarly you need to create a project group on Canvas in order to submit as a group.

You may use files, benchmarks or resources from the Internet (unlike in many other classes) or instructors, provided you cite them in your written report. (If you use the same resource many times, such as StackOverflow, one citation per resource suffices.)

<details markdown="block">
  <summary>
    Assignment Flavor and Learning Goals
  </summary>
A recurring theme in this course is a focus on everything _except_ writing code. Perhaps surprisingly, other elements, such as reading code, testing code, eliciting requirements, debugging code, and planning projects, are usually more important in industry than simply writing software. Your other electives cover programming — this one covers software engineering.

Many assignments in this class are often more like "open ended puzzles". You won't be writing much code. Instead, you will be reading and using code written by other people. (Yes, that's annoying — that's the point!)

Among other things, we hope this assignment and HW2, together, will give students exposure to: statement (or line) coverage, branch coverage, legacy code bases, white-box testing, black-box testing, writing your own tests from scratch, slightly editing existing tests to improve coverage, thinking about high-coverage inputs from first principles, and using other available resources.

These assignments may be different from what you are used to. HW1 focuses on white-box testing and looking at the code. In HW2, there is too much code for you to read it all, so you will have to think of other black-box approaches. 
</details>

### Subject Program

The HW1 subject program is a simple python implementation of an abstract data type: the [AVL Tree](https://en.wikipedia.org/wiki/AVL_tree) container data structure.

Test cases for this program take the form of sequences of instructions for manipulating a single global AVL tree:

* `i${number}` — insert number into the tree
* `d${number}` — delete number from the tree
* `p` — print the current tree

For example, if the text file `test1.avl` contains `i1 i2 i3 i4 i5 d4 p`, then `python avl.py test1.avl` produces the output:

```
  2.
 /  \
1   5
/\  /\
   3
   /\
```

We compute coverage for this program using the [coverage](https://coverage.readthedocs.io/en/coverage-5.0.2/) package for Python. Both statement and branch coverage are considered. (For more information about statement and branch coverage, [read here](https://en.wikipedia.org/wiki/Code_coverage#Basic_coverage_criteria) - we've briefly covered these in class, but we'll do into more detail next week.)

The reference `avl.py` implementation is available [here](https://web.eecs.umich.edu/~weimerw/2022-481F/hw1/avl.py). The program is about 300 lines long and is a self-contained single file.

A test suite for this application is a collection of `.avl` files. The reference starter test suite is available [here](https://web.eecs.umich.edu/~weimerw/2022-481F/hw1/avl-tests.zip).

### Python Build, Installation and Coverage Details

Installing coverage may look like this on your Ubuntu setup:

```
$ echo I am typing this in the VirtualBox or Cloud Computing setup from HW0
$ sudo apt-get install python-pip python-dev build-essential
$ sudo pip install --upgrade pip
$ sudo pip install --upgrade virtualenv
$ sudo pip install coverage
```

(If `sudo pip install coverage` fails for you, the [advice here](https://askubuntu.com/questions/1317411/pip-version-returns-syntaxerror-invalid-syntax-after-installation) may help. Some students report that `wget https://bootstrap.pypa.io/pip/2.7/get-pip.py ; sudo python get-pip.py` works for them for the `--upgrade pip` issue.)

Note that `apt-get` is Debian/Ubuntu-specific. If you have another Linux distribution you may need to use something else (`yum` on Red Hat, etc.). If you're using a Mac, you'll need something else entirely. While this homework assignment isn't too hard to do on a Mac, students have reported that HW2 is somewhere between "unbelievably frustrating" and "impossible" to do on a Mac, so you might consider setting up a virtual machine now.

After that, you can use the coverage utility on multiple test cases and view combined coverage results:
```
$ coverage run --append avl.py simple1.avl
1
/\
 2
 /\

$ coverage report
Name     Stmts   Miss  Cover
----------------------------
avl.py     182     99    46%

$ coverage run --append avl.py simple2.avl
  2.
 /  \
1   5
/\  /\
   3
   /\

$ coverage report
Name     Stmts   Miss  Cover
----------------------------
avl.py     182     54    70%

$ coverage erase
```

(If you see `no file to run: 'avl.py'`, go back and make sure you download the `avl.py` file from this webpage above and put it in the directory you are working in.)

Note how the measured coverage of only the first test is low (46%) but the combined coverage result for the two tests is higher. The `--append` option is necessary to avoid overwriting the stored coverage data with each new test run.

Now we consider branch coverage. Simply add `--branch`:
```
$ coverage run --append --branch avl.py simple1.avl

$ coverage run --append --branch avl.py simple2.avl

$ coverage report
Name     Stmts   Miss Branch BrPart  Cover
------------------------------------------
avl.py     182     54     90     19    66%

$ coverage report -m
Name     Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------
avl.py     182     54     90     19    66%   82-85, 88, 101, 109-112, 121,
123-127, 139-141, 145, 189, 201-202, 211, 216, 223-238, 244-248, 253-254,
284, 286-292, 304-306, 81->82, 87->88, 100->101, 107->109, 120->121,
122->123, 138->139, 144->145, 171->exit, 210->211, 212->214, 215->216,
243->244, 250->253, 283->284, 285->286, 301->303, 303->304, 319->312

$ coverage erase
```

The additional columns give branch-specification information (e.g., about partial branches; see the manual), but the final column now gives the branch coverage. The columns _may look different_ on other setups — that's fine. Note also how the `missing` column guides you to line numbers that are not exercised by the current suite.

There is [external written documentation available](https://media.readthedocs.org/pdf/coverage/latest/coverage.pdf) for this utility. Finally, note that this utility can also produce XML and HTML reports, which you may find easier to interpret.

### Recommended Approach

Any test input you create is fine: the goal is to get coverage, not to have good or pretty trees. (Yes, really any random input is fine.)

You will almost certainly need to inspect the source code of the program (i.e., white-box testing) to construct a high-coverage test suite.

We recommend that you start with the test cases we have provided. Because of limits on autograding submissions, and so that you learn how coverage computations work across various systems (a relevant skill for interviews, etc.), you will almost certainly want to install the coverage utilities yourself. As you read the project's source code and expand your test suite, recompute the coverage locally. When you perceive that it has gone up significantly, submit to the grading server for a more official check.

### Submission: test cases

Submit your (individual, not zipped) test cases via Gradescope to the "HW1" assignment. The autograder will
report a score between 0 and 10. You may submit multiple times, but no more than 5 times in any 24-hour period.

The exact grading rubric (e.g., x points for y coverage) is:
statement coverage 50% (one point) to 94% (five points); branch coverage 50% (one point) to 92% (five points).

Note that your local results may differ largely from the autograder results and that is _fine and expected_. For example, you may observe 6.8% line coverage "at home" and 16.8% on the autograder. (Different compilers, header files, optimizations, etc., may result in different branch and line counts.) Your grade is based on the autograder results, regardless of what you see locally.

We always use your best autograder submission result (even if your latest result is worse) for your grade.

Note also that the grading server has resource usage (e.g., CPU time) caps. As a result, if you submit a test suite that is very large or long-running, we may not be able to evaluate your submission. Consider both quantity and quality.

### Submission: written report

You must also write a short two-paragraph report reflecting on your experiences creating a high-coverage test suite for this assigment. (If you are working with a partner, indicate as much in the text or header. Recall from above that you need only submit one copy of the report, but if both you do, nothing bad happens. Select your partner on Canvas.) Consider addressing points such as:
* How did you go about manually creating or otherwise obtaining test cases?
* Did you use or modify any of the tests we provided or tests from the Internet as part of your answer? (Reminder: You are allowed to do that in this class!)
* What was harder than you expected or different than you expected?
* (If you used any external resources, such as image files from the Internet or help from Stack Overflow, list it in an optional third paragraph. There is no particular format -- a list of URLs is fine. If you used the same general source multiple times, just cite it once.)

<details markdown="block">
<summary>I am worried about the my report being too long or too short!</summary>
Many students report stress or uncertainty about the length limit. The safest answer is to go with the restriction as written. The graders are free to dock points if your answer is too long. In practice, there are a bunch of ways to cheese the system (e.g., we don't give a word count). I would expect three short paragraphs to be about the same as two longer paragraphs. The real challenge here is that we are asking you to be concise. In a real software engineering job, your manager will typically not read overly-long reports. So the rule isn't strict, but it's judged by humans. Students are often unhappy when their expectations are unmet. Basically the only failure case here is "you think writing longer is OK" + "the graders decide to be firm about it" so you lose points. So you can write something longer, but you don't have any recourse if the subjective judgment says that yours is too long. If you don't feel comfortable with that gamble (e.g., for students who may not be native English speakers, or may not be confident in their prose), cleave to both the spirit and the letter of the law.
</details>

Rubric:
* 5 points — a two-paragraph report reflecting on your activities creating a high-coverage test suite for this assignment, including comparisons and contrasts between your experiences and expectations (with a third paragraph listing any external sources or files used)
* 4 points — a reasonable report, but lacking a solid description of one or more aspects or significantly exceeding the length limit
* 3 points — a brief report, detailing only half of the required information
* 2 points — a report drawing only the bare minimum of contrasts and comparisons (e.g., between two aspects and no more)
* 1 point — a terse or uninformative report, perhaps describing only one activity or subject
* -1 point — English prose or grammatical errors
* -1 point — Text does not include University email address(es) and/or does not make it clear whether you are working alone or with a partner
* -all points — Submission uses uncited external resources

There is no explicit format (e.g., for headings or citations) required. You may discuss other activities (e.g., validation or automation scripts you wrote, etc.) as well.

The grading staff may select a small number of excerpts from particularly high-quality or instructive reports and share them with the class. If your report is selected you will receive extra credit.

Submit your report to the "HW1" assignment on Canvas.

### Commentary

This assignment is somewhat open-ended. There is no "one true path" to manually creating high-coverage test suites.

You may find yourself thinking something like "I know what to do at a high level, but I don't know specifically what to create here. I could try to read and understand the program to make tests that cause it to do different things, but reading and understanding the program takes a long time, especially since I didn't write this code and I don't really care about it and I'm only doing it because someone is telling me to." Such concerns are, in some sense, the point: they are indicative of industrial software engineering.

Finally, students sometimes wonder if it is possible to get 100% coverage on this assignment. While it should be possible to get 100% coverage for the general AVL tree algorithm, this particular implementation of the algorithm may well have branches that you are unable to reach — especially given this testing setup.

### FAQ and Troubleshooting

In this section we detail previous student issues and resolutions:
1. **Question**: When I type the command `sudo apt-get install python-pip python-dev build-essential` I am prompted for a password — which should I use?
<br>**Answer**: The password should be the one associated with your user account (the one you used to log in to the OS). If you are using a virtual machine, it is the virtual machine login password, not your "real" login password.

2. **Question**: I'm getting "Can't add branch measurements to existing line data".
<br>**Answer**: Run `coverage erase` when switching between statement coverage and branch coverage.

3. **Question**: Can you post guidelines or points of interest for writing high-quality or instructive reports?
<br>**Answer**:  I regret — I cannot. At least, not in the way one is likely to desire when posing such a query. You can
potentially reverse engineer things a bit, but ultimately there's no magic formula. The grading staff may well select a small number excerpts that are worth sharing with the class. You can infer from that that we'll be favoring excerpts that are "family friendly" and that contribute to pedagogical goals: either by bringing something new to light, or by reinforcing or reinterpreting concepts from class. Given my views on liberal arts education, however, this could potentially be anything from a strong link between, say, testing and rhetoric, to some direct point about software maintenance. Usually these sorts of things end up being awarded to students who have clearly spent a bit more time than usual on the assignment. (If you are being very mercenary, it's probably not worth shooting for an ill-defined unsure thing.)



