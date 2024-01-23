---
layout: project
title: "Homework 2: Coverage"
permalink: /projects/hw2.html
parent: Homeworks
nav_order: 3
due_date: "Wednesday, February 7, 2024, 11:59PM AoE"
submission_notes: Submit test cases via Gradescope and written report via Canvas
---

Two of the key properties found in industrial software engineering, but not in most academic coursework, are: **the program is large** and **you did not write the program**. If you are hired by Microsoft as a software engineer, they will not ask you to write Office from scratch. Instead, as discussed in class, the vast majority of software engineering is the comprehension and maintenance of large legacy codebases (i.e., old code you did not write).

Thus, there is no particular assumption that you are familiar with the subject program in this assignment. Indeed, that is the point: you will be applying testing concepts to unknown software. In this assignment, we're taking this to the next level (relative to HW1): the subject program is a real, actual program that people use to accomplish actual work.

In this assignment, you will create a high-coverage test suite for a real open-source program: `libpng`, a library
for manipulating image files.
You will then be asked to write a short report reflecting on the activity.

You may work with a partner for this assignment. Only one partner needs to submit for any of the programming assignments on the autograder, but you do need to use Gradescope's interface to select your partner. [(Here is a video showing Gradescope partner selection.)](https://www.youtube.com/watch?v=rue7p_kATLA&t=1m6s). Only one of you needs to submit the written report on Canvas, but similarly you need to create a project group on Canvas in order to submit as a group.

You may use files, benchmarks or resources from the Internet (unlike in many other classes) or instructors, provided you cite them in your written report. (If you use the same resource many times, such as StackOverflow, one citation per resource suffices.)

<details markdown="block">
  <summary>
    Assignment Flavor and Learning Goals
  </summary>
A recurring theme in this course is a focus on everything _except_ writing code. Perhaps surprisingly, other elements, such as reading code, testing code, eliciting requirements, debugging code, and planning projects, are usually more important in industry than simply writing software. Your other electives cover programming — this one covers software engineering.

Many assignments in this class are often more like "open ended puzzles". You won't be writing much code. Instead, you will be reading and using code written by other people. (Yes, that's annoying — that's the point!)

Among other things, we hope this assignment and HW1, together, will give students exposure to: statement (or line) coverage, branch coverage, legacy code bases, white-box testing, black-box testing, writing your own tests from scratch, slightly editing existing tests to improve coverage, thinking about high-coverage inputs from first principles, and using other available resources.

These assignments may be different from what you are used to. HW1 focused on white-box testing and looking at the code. In this homework, there is too much code for you to read it all, so you will have to think of other black-box approaches. 
</details>

<details markdown="block">
<summary>Installing, Compiling and Running Legacy Code</summary>
It is **your responsibility** to download, compile, and run the subject programs in this assignment (and the other assignments in this course). Getting the code to work is **part of the assignment**. You can post on the forum for help and compare notes bemoaning various architectures (e.g., windows vs. mac vs. linux, etc.). Ultimately, however, it is your responsibility to read the documentation for these programs and utilities and use some elbow grease to make them work.

If you are having trouble (e.g., windows is often a bit more complicated than linux for these things), post on the forum. Other students should be able to offer help and advice.

For example, one TA reports that gcc may not easily support static linking on a Mac, but that it took fewer than two minutes to set everything up in Ubuntu.
</details>

### Subject Program: PNG Graphics (C)

The HW2 subject program is the [portable network graphics](https://en.wikipedia.org/wiki/Portable_Network_Graphics) file format reference library, [libpng](https://en.wikipedia.org/wiki/Libpng). It is used for image manipulation and conversion.

We will be using the developer-provided `pngtest` driver. It takes as input a single `.png` file.

We compute coverage for this program using the [gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html) test coverage program for gcc. Only **statement** coverage is considered.

The reference implementation (version 1.6.40) is available [here](../assets/libpng-1.6.40.tar.gz). It contains about 85,000 lines of code spread over about 70 files. The SHA-256 checksum is `8f720b363aa08683c9bf2a563236f45313af2c55d542b5481ae17dd8d183bb42`.

A test suite for this application is a collection of `.png` files. The reference implementation comes with over 150 such example files. (You really **can** use any images that came with `libpng`, plus any images from anywhere else, as part of your submitted answer, see below.) Feel free to use an image manipulation or conversion program to create your own files or to use files or benchmarks you find on the Internet or to use the files that come with the program.

The difficulty difference between HW1 and HW2 is large. (For example, students may report that HW1 takes "minutes" while HW2 takes "hours". In addition, many students find that the difficulty lies more in compilation and instrumentation than in high-coverage images.)

### C Build, Installation and Coverage Details

The `gcov` utility usually comes with gcc, so you should not need to do anything specific to install it. (Unless you are trying to use a Mac natively despite our warnings not to do so. In such a world you will likely encounter the issue that gcc static linking may not work on a Mac and that using dynamic linking will give you 0% coverage. You should then install linux in a VM.) However, our subject program depends on the development version of a compression library:
```
$ sudo apt-get install libz-dev 
```

In addition, you will have to compile the project with coverage instrumentation (taking care to use static linking or to otherwise make all of the `libpng` source files, and not just the test harness, visible to coverage):

```
$ echo I am typing this in the VirtualBox or Cloud Computing setup from HW0
$ cd libpng-1.6.40
$ sh ./configure CFLAGS="--coverage -static"
$ make clean ; make 

$ ./pngtest pngtest.png
        Testing libpng version 1.6.40
        ...

$ gcov *.c
        ...
File 'png.c'
Lines executed:37.78% of 1236   # your numbers may differ!
Creating 'png.c.gcov'

File 'pngerror.c'
Lines executed:16.67% of 252    # your numbers may differ!
Creating 'pngerror.c.gcov'

        ...

Lines executed:28.71% of 10606  # your numbers may differ!

$ ./pngtest contrib/gregbook/toucan.png
        ...

$ gcov *.c
        ...

File 'pngwutil.c'
Lines executed:61.90% of 979    # your numbers may differ!
Creating 'pngwutil.c.gcov'

Lines executed:30.72% of 10606  # your numbers may differ 
                                # and everything is still fine!

$ rm *.gcda pngout.png
```

(If you get an error like "bash: cd: libpng-1.6.40: No such file or directory", be sure you downloaded and unpacked the reference implementation from the course website above. If you are certain you downloaded the file and you're still getting an error like that, make sure you also moved the file to your VM or EC2 instance: a common mistake is downloading it to your local machine but not moving it to your work area.)

(If you get an error like "No targets specified and no makefile found" when you run "make clean; make", go back and double-check that the configure step ran correctly. If it said something like "configure: error: zlib not installed", you should resolve all of those issues first.)

Note how gcov gives a separate report for each source file specified on the command line, but also gives a sum total for statement coverage (the final Lines executed reported). Your coverage numbers may be slightly different from the example ones listed above.

(If you are getting output from gcov, but it does not give you the final Lines executed total, you are likely using a different version of gcov. Students who use WSL, for example, have reported that its version of gcov omits the total. Unfortunately, the solution is to go back to HW0 and use one of the required Linux approaches.)

The `png.c.gcov` (etc.) files created by this processed are marked-up source files that include coverage and visitation information. You can view them to determine which lines and branches were covered. Note that [lcov](http://ltp.sourceforge.net/coverage/lcov.php), a graphical front-end to gcov, may [help you interpret](https://qiaomuf.wordpress.com/2011/05/26/use-gcov-and-lcov-to-know-your-test-coverage/) that output for large projects. While it is possible to obtain branch coverage using gcov (e.g., `-b -c`) we will not for this assignment.

Note that `pngtest` creates a new `.png` file named `pngout.png`. (This can confuse some students, because if you collect coverage after running on `*.png` and then do it again, you may get a different answer the second time if you're not careful because of the newly-added file!)

### Recommended Approach

Any test input you create or find is fine: the goal is to get coverage, not to have good or pretty or well-behaved images. (Yes, really any random input is fine. Yes, you can really use a folder of images you found somewhere if you want to and you think that will get good coverage. Yes, really.) Note well, however, the limited resources available on the autograder: if you submit too large of a collection of images, your submission will time out and you will not get any credit for it. We recommend being judicious in your choice of images. You may not upload more than 50 images to the autograder, so choosing "the largest collection of images you can find" is not a good strategy.

### Submission: test cases

Submit your (individual, not zipped) test cases via Gradescope to the "HW2" assignment. You may submit up to
50 images. The autograder will
report a score between 0 and 10. You may submit multiple times, but no more than 5 times in any 24-hour period.

The exact grading rubric (e.g., x points for y coverage) is:
statement coverage 29% (one point) to 36% (ten points).

Note that your local results may differ largely from the autograder results and that is _fine and expected_. For example, you may observe 6.8% line coverage "at home" and 16.8% on the autograder. (Different compilers, header files, optimizations, etc., may result in different branch and line counts.) Your grade is based on the autograder results, regardless of what you see locally.

We always use your best autograder submission result (even if your latest result is worse) for your grade.

Note also that the grading server has resource usage (e.g., CPU time) caps. As a result, if you submit a test suite that is very large or long-running, we may not be able to evaluate your submission. Consider both quantity and quality.

### Submission: written report

You must also write a short two-paragraph report reflecting on your experiences creating a high-coverage test suite for this assigment. (If you are working with a partner, indicate as much in the text or header. Recall from above that you need only submit one copy of the report, but if both you do, nothing bad happens. Select your partner on Canvas.) Consider addressing points such as:
* How did you go about manually creating or otherwise obtaining test cases?
* How did your process for creating a high-coverage test suite differ between this assignment and HW1?
* Did you use or modify any of the tests we provided or tests from the Internet as part of your answer? (Reminder: You are allowed to do that in this class!)
* What was harder than you expected or different than you expected?
* (If you used any external resources, such as image files from the Internet or help from Stack Overflow, list it in an optional third paragraph. There is no particular format -- a list of URLs is fine. If you used the same general source multiple times, just cite it once.)

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

Submit your report to the "HW2" assignment on Canvas.

### Commentary

Like HW1, this assignment is an open-ended puzzle. There is no "one true path" to manually creating high-coverage test suites.

This assignment is intentionally much more difficult than HW1 (for most students). Don't get discouraged by this: the subject program in HW1 is a "toy" program (the implementation of a data structure typically covered in an undergraduate course), while the subject program here is very much a real-world program that people actually use. Real software is much bigger and more complex than the sort of thing you see in (most) undergraduate-level courses!

### FAQ and Troubleshooting

In this section we detail previous student issues and resolutions:

1. **Question**:  I get `The program 'make' can be found in the following packages: * make`. <br>**Answer**: You need to do `sudo apt-get install make` or similar. (If you are uncertain about installing and using `make`, you may need to work
a little extra in this assignment and some of the others to brush up on your Linux programming skills. You may want to watch the video linked in HW0 about Linux fundamentals.)

2. **Question**: Can I really use images I found online to help with this assignment?
<br>**Answer**: Yes, provided that you cite them at the end of your report. This class is about "everything except writing code", in some sense, and in the real world people do everything they can to get high-coverage test suites (including paying people to construct them and using special tools). So you can use image files or benchmarks you find on the Internet if you like — but you'll still have to do the work of paring things down to a small number of high-coverage files. You'll likely get the most out of the assignment if you use a combination of white-box testing, black-box testing and searching for resources — but there are many ways to complete it for full credit.

3. **Question**: I'm getting an error message like:
```
./.libs/libpng16.a(pngrutil.o): In function `png_inflate_claim':
pngrutil.c:(.text+0xd5b): undefined reference to `inflateValidate'
collect2: error: ld returned 1 exit status
Makefile:1005: recipe for target 'pngfix' failed
```
or
```
Note, selecting 'zlib1g-dev' instead of 'libz-dev'
```
**Answer**: You do not have libz-dev installed correctly. One student eventually resolved this by installing an Ubuntu virtual machine.

4. **Question**: I get this error:
```
make: *** No targets specified and no makefile found.  Stop.
```
**Answer**: You need to run `configure` before running `make`. Double-check the build and installation instructions above.

5. **Question:** When I try to run:
```
gcc -o pngtest pngtest.c
```
It chokes with `undefined reference` errors.
<br>**Answer**: Answer: Yes — `pngtest` requires a number of libraries to build. You should follow the installation instructions above (run "configure" then "make", etc.).

6. **Question**: How do other students tackle HW2?
<br>**Answer**: Here's a public answer from one former student describing the process:
    1. Oh my god what is this libpng doing...I'm not very familiar with C...What do I do...
    2. Whatever, I guess I could try several png files first (maybe some big files) and check the coverage. Oops, they only cover around 15%...this is frustrating...
    3. All right, I guess I should read the code and look at the conditionals. It seems libppng handles png files which can have different "parameter values", errors etc.
    4. I tried creating some png files myself setting the parameter values as I want. I searched for some scripts that generate png files. I also tried some software to change an existed png to a new png in the way I want. Great, now my test suite can reach 33%. But after generating some more pngs by manipulating the script, the coverage would not increase further.
    5. Now, should I figure out how to edit the script more to generate more sophisticated pngs? Since C is not my best skill, this will probably cost me a lot of time. How do other people test different png files? Let me scour the web and look for something useful.
    6. Now mixing all the pngs I have together, my test suite can reach much higher than the full marks in the autograder! But I can only submit 50 files...Currently I have more than 100 files...
    7. Let me write a script to automate the selection of the 100+ files. Ah ha, I found a sub set of my test suite that has less than 50 files and can reach higher than 36% coverage.
    8. Finally, I can make a test suite for a real software that I don't know of.

