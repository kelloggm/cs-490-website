---
layout: project
title: "Homework 3: Fuzzing with AFL"
permalink: /projects/hw3.html
parent: Homeworks
nav_order: 4
due_date: "Wednesday, February 14, 2024, 11:59PM AoE"
submission_notes: Submit via Canvas
---

In this assignment you will use tools to automatically create high-coverage test suites for different programs.

You _may_ work with a partner for this assignment.

### Start Early

Professors often exhort students to start assignments early. Many students wait until the night before and then complete the assignments anyway. Students thus learn to ignore "start early" suggestions. This is **not** that sort of suggestion.

<details markdown="block">
  <summary>
    Warning: the tools take hours!
  </summary>  
The tools you must use for this assignment **literally** take
**multiple hours** to run. Some students reported that it took over 14
hours to run! (However, others were able to finish in about five
minutes. Regardless of when you finish, everything is fine.) Even if
you are fast and can finish your work at the last minute, the tools
are not and can not. On a high-powered multi-core rack-mounted
RAID-storage test machine it took 6.3 hours to run the AFL tool.
However, as soon as you get
enough data (see below) you can stop early (just press Ctrl-C).
</details>

However, once running, the tools are completely automated. Thus, you
can start them running overnight, sleep and ignore them, and wake up
to results. This means that even though the assignment may not take
hours of your active personal attention, you must start it days before
the due date to be able to complete it in time.

<details markdown="block">
<summary>Installing, Compiling and Running Legacy Code</summary>
It is **your responsibility** to download, compile, and run the subject programs in this assignment (and the other assignments in this course). Getting the code to work is **part of the assignment**. You can post on the forum for help and compare notes bemoaning various architectures (e.g., windows vs. mac vs. linux, etc.). Ultimately, however, it is your responsibility to read the documentation for these programs and utilities and use some elbow grease to make them work.
</details>

### Subject Program and Tool: PNG Graphics (C) + American Fuzzy Lop

The first subject program is `libpng`'s `pngtest` program, seen earlier in
Homework 2. This reuse has two advantages. First, since you are
already familiar with the program, it should not take long to get
started. Second, you will be able to compare the test cases produced
by the black-box tool to the white-box test cases you made
manually. (You'll have to recompile it with special flags, but it's
the same source code.)

The associated test input generation tool is [American fuzzy lop](https://en.wikipedia.org/wiki/American_fuzzy_lop_(fuzzer)) (hereafter "AFL"), version 2.52b. A mirror copy of the AFL tarball is [here](../assets/afl-2.5.2b.tgz), but you should visit the [project webpage](http://lcamtuf.coredump.cx/afl/) for documentation. As the (punny? bunny?) name suggests, it is a [fuzz testing tool](https://en.wikipedia.org/wiki/Fuzzing).

You will use AFL to create a test suite of `.png` images to exercise the `pngtest` program, starting from all of the `.png` images provided with the original tarball.
Note that you can terminate AFL as soon as you reach 510 `paths_total` (also called total paths in the GUI)— AFL does not stop on its own (instead, press Ctrl-C to stop it).

### AFL installation and use details

AFL claims that one of its key advantages is ease of use. We will consider four separate high-level steps in this dynamic analysis.

#### Step 1: Compile AFL

Follow along with AFL's [quick start guide](http://lcamtuf.coredump.cx/afl/QuickStartGuide.txt). Extract the AFL tarball (to its own directory) and run "make".

Note that this results in files such as `afl-gcc` and `afl-fuzz`, which we will use in subsequent steps.

#### Step 2: 'Instrument' libpng

Do _not_ re-use your HW2 copy of libpng. (It is possible, but leads to much confusion.) Instead, download a fresh copy of the reference implementation (version 1.6.40) [here](../assets/libpng-1.6.40.tar.gz) and place it in a new folder for Homework 3 (e.g., HW3).

Change to that `libpng-1.6.40` directory and re-configure `libpng` with a special configure line like this:
```
$ CC=/REPLACE/THIS/TEXT/WITH/YOUR/PARTICULAR/PATH/TO/afl-gcc_(don't_just_copy_this_in_unchanged) ./configure --disable-shared CFLAGS="-static" 
$ make 
```

The "CC" bit will look something like (but maybe different for you) `CC=/home/ubuntu/cs684/hw3/afl-2.52b/afl-gcc` — note that there is no trailing slash. If you see `configure: error: C compiler cannot create executables`, double-check your spelling here. Also, folder names with spaces (like "CS 684/HW 3") will not work: rename the folder to remove the spaces.

Multiple students have reported that WSL does not work with AFL and that they needed to move to an Ubuntu virtual machine instead (as per HW0). See the FAQ below.

Note that you are not using "coverage" or `gcov` for this part of the homework assignment. We only want AFL instrumentation for now.

#### Step 3 — Choosing seed images

AFL uses initial inputs you provide and mutates them to find new inputs that cover additional parts of the program. (For more information, see its documentation.) The initial inputs you provide are called seed inputs. Since we are testing libpng, the seed inputs are "images".

Because AFL repeatedly processes these seed files, if you include very large or very many seed files, AFL will take too long to run.

Make a new subdirectory to hold your seed files. This subdirectory may be called `testcase_dir` in the documentation, but you can name it whatever you want. Most students put their 50 manual test cases from HW2 there, but if your HW2 images are large, consider only including the smaller ones. (You'll want to know the total coverage of the seed images you start with for the HW3 written report, but since you've left your HW2 installation alone, you can compute that using the same method you used in HW2. Delete the old coverage information in your HW2 folder, run pngtest on all of your seed images, and run `gcov` to list the total coverage.)

#### Step 4 — AFL generates inputs for libpng

Now it is time to run AFL on libpng.
```
$ sudo su
# echo core > /proc/sys/kernel/core_pattern
# exit
$ /REPLACE/THIS/TEXT/WITH/YOUR/path/to/afl-fuzz -i testcase_dir -o findings_dir -- /path/to/pngtest_(not_.c_nor_.png_but_the_executable_you_built) @@
```

(In this command, the `/path/to/pngtest_(not_.c_nor_.png_but_the_executable_you_built)` part is the absolute path to the `pngtest` executable that is created after running `make` in the `libpng` directory for HW3 in Step 2 above. For example, it might potentially look something like `/home/ubuntu/HW3/libpng-1.6.40/pngtest` but might be slightly different for you.)

Do double-check the end of the previous line for `@@`. It is _required_, it is **not a typo**, and if you did not type it in (to tell AFL where its randomly-created arguments to `pngtest` go) you are likely to "get stuck" when enumerating paths and tests (see FAQ below).

Note that `findings_dir` is a new folder you make up: `afl-fuzz` will put its results there (in a `queue` subfolder). The results will be "images" (both good and bad) produced by AFL to get high coverage. The results will all have ugly names, but they will be the output of AFL.

Note that _you must stop afl-fuzz yourself_ (just press Ctrl-C), otherwise it will run forever — it does not stop on its own. Read the Report instructions below for information on the stopping condition and knowing "when you are done".

Note also that you can _resume_ afl-fuzz if it is interrupted or stopped in the middle (you don't "lose your work"). When you try to re-run it, it will give you a helpful message like:
```
To resume the old session, put '-' as the input directory in the command
line ('-i -') and try again.
```

Just follow its directions. **Warning:** when you resume AFL it will _overwrite_ your `findings/plot_data` file (which you need for the final report), so be sure to save a copy of that somewhere before resuming.

Note that `afl-fuzz` may abort the first few times you run it and ask you to change some system settings (e.g., `echo core | sudo tee /proc/sys/kernel/core_pattern`, `echo core >/proc/sys/kernel/core_pattern` etc.). For example, on Ubuntu systems it often asks twice. Just become root and execute the commands. Note that `sudo` may not work for some of the commands (e.g., `sudo echo core >/proc/sys/kernel/core_pattern` will fail because bash will do the `>` redirection before running `sudo` so you will not yet have permissions, etc.) — so just become root (e.g., run `sudo sh`) and then execute the commands in a root shell. If you are getting `core_pattern: Permission denied` errors, make sure you become root first before executing the commands:
```
sudo su
echo core > /proc/sys/kernel/core_pattern
exit
```

The produced test cases are in the `findings_dir/queue/` directory. They may not have the `.png` extension (instead, they might have names like `000154,sr...pos/36,+cov`), but you can rename them if you like. Note that AFL can and will produce "invalid" PNG files to test error handling code; such "invalid" PNG files will appear to produce errors or otherwise not be viewable. This is normal and expected.

At some point, many students are tempted to ask a question like "Is it normal that my XYZ Machine got to ABC paths in PQR minutes?" We acknowledge that students are often anxious about this assignment. For many students, this may be a first experience using an off-the-shelf tool with an unknown running time.
As a software engineer, you will need to be comfortable with _scheduling_ and _risk_ (especially with respect to schedules).
Part of this homework is designed to give you a feeling for what it is like to employ a software engineering process in the face of _uncertainty_. We want to give you experience with this in a safe (classroom) setting, rather than having your first experience with this be on the job. Regretfully, there is no way for us to answer questions about whether or not it is normal that your particular machine took some particular time. I know students really wish we could reduce their anxiety or uncertainty about this process. In practice, the running time of AFL depends on many factors, including the side and number of the seed images, the speed of your CPU and disk, the load on the machine, and so on. There is no secret formula for how long it is supposed to take that we are hiding from you but will reveal if you ask such a question directly. Instead, living with this uncertainty — feeling uncomfortable about it, and having to complete the assignment anyway — is a key point of the assignment.

<details markdown="block">
<summary>Help! I can't open AFL's output!</summary>
You will almost certainly find that AFL's output queue folder does not contain files with the `.png` extension. In addition, you will almost certainly find that most of the files produced by AFL are "invalid" PNG files that cause program executions to cover error cases (e.g., `libpng read error`).

This is **normal**.

Double-check all of the instructions here, and the explanations in the course lectures for how these tools work: there's no need to panic. In addition, you might try alternate image viewers (rather than just the default one). For example, multiple students have reported that uploading apparently-invalid images to GitHub (no, really) works well for viewing them.
</details>

While AFL is running, you can read the [technical whitepaper](http://lcamtuf.coredump.cx/afl/technical_details.txt) to learn about how it works and compare the techniques it uses to the basic theory discussed in class.

TODO



