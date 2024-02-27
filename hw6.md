---
layout: project
title: "Homework 6: Mutation Testing"
permalink: /projects/hw6.html
parent: Homeworks
nav_order: 7
due_date: "Wednesday, March 13, 2024, 11:59PM AoE"
submission_notes: Submit via Gradescope and Canvas
---

<p>
In this assignment you will write a tool to carry out simple
<a href="https://en.wikipedia.org/wiki/Mutation_testing">mutation
testing</a> on Python programs. Given a program, your tool must generate
mutants of that program such that the mutation
adequacy score (i.e., the percentage of mutants that are killed by each test suite)
correctly rank-orders a number of held-out test suites
for that program in terms of their quality. 
</p>
<p>
You <i>may</i> work with a partner for this assignment. If you do you must
use the same partner for all sub-components of this assignment. 
Use Gradescope and Canvas features to select your partner. 
Only one
partner needs to submit the report on Canvas, but if you both do, nothing
fatal happens.
</p>
<p>
You are still allowed to use online (or "on-this-webpage") resources and
the like as long as you cite them in your writeup.
</p> 

#### Cross-Platform Compatibility and Python

<p>
It is <b>your responsibility</b> to submit Python code that works on 
the grading server. This is true even if (indeed, <i>especially</i> if) the
grading server uses a different version of Python than your development
environment. 
</p>
<p>
This assignment uses Python because the focus is on the mutation algorithm
and not the <A
href="https://en.wikipedia.org/wiki/Compiler#Front_end">compiler
front-end</a>. In theory it would be just as easy to do this assignment
on C++ code using <a href="https://llvm.org/">LLVM</a> (e.g., via
<A href="http://clang.llvm.org/">clang</a>) or the like. 
<A href="https://en.wikiquote.org/wiki/Jan_L._A._van_de_Snepscheut">In
practice</a> that would just add out-of-scope overhead without reinforcing
course concepts. If you are interested in such topics, consider taking an
advanced Programming Languages or Compilers course (or make an appointment to
talk to me about it!).
</p> 

<p>
The grading server uses Python 3.10.12 for this assignment. (Yes,
this is a change from other homeworks.) 
</p> 

### HW6a: Mutation Testing (Python)

<p>
You mutation testing tool will take the form of a Python program
called 
<tt>mutate.py</tt>. Your <tt>mutate.py</tt> accepts two command line
arguments: first, the name of a Python source program to mutate; second,
the number of mutants to produce (see below). 
</p> 
<p>
Your <tt>mutate.py</tt> must create a number of new Python source files 
in the same directory that are mutants of the input program. The mutants
must be named <tt>0.py</tt>, <tt>1.py</tt>, <tt>2.py</tt>, and so on. Each
mutant is a copy of the original program with one or more mutation
operators (see below) applied. Any other output (e.g., logging to standard
output) your <tt>mutate.py</tt> produces is ignored. 
</p> 
<p>
The data structure used to represent Python source files is the
<a href="https://en.wikipedia.org/wiki/Abstract_syntax_tree">abstract
syntax tree (AST)</a>. 
</p> 
<p>
You should use the <a
href="https://docs.python.org/3/library/ast.html"><tt>ast</tt></a> module
(to read Python source files into abstract syntax trees) 
as well as the 
<a href="http://astor.readthedocs.io/en/latest/"><tt>astor</tt></a> module
(to serialize abstract syntax trees out to Python source files). 
</p> 
<p>
Many students report that the so-called
<A href="https://greentreesnakes.readthedocs.io/">"missing Python AST
docs"</a> are quite helpful here. 
</p> 
<p>
Other students and instructors have found 
this quick <a
href="https://www.mattlayman.com/blog/2018/decipher-python-ast/">Python AST
Tutorial</a> to be quite helpful (thanks S. Ajami) for the basic concepts. 
</p> 
<p>
Your program must be <i>deterministic</i> in the sense that if it is run
with the same arguments it should produce the same outputs. (So if you want
to use "random numbers", either set the seed to zero or somesuch at the
start or use the index of the file you are creating as the
random number/seed.) 
</p> 
<p>
The <tt>ast.parse</tt>, <tt>ast.NodeVisitor</tt>,
<tt>ast.NodeTransformer</tt>, and <tt>astor.to_source</tt> portions of the
interface are all likely to be quite relevant for this assignment.
</p> 

<h4>Mutation Operators</h4>

At minimum, you must implement and support 
the following three mutation activities: 

1. Negate any single <b>comparison</b> operation type (e.g., &gt;= becomes &lt;). 
    * (You should strongly consider handling more than one comparison
    type.  You have free choice for what you do, if anything, for other
    "corner-case" booleans such as <tt>is</tt> or <tt>True</tt>.) 
2. Swap <b>binary operators</b> + and -, as well as * and //. 
    * (You have free choice of which AST node classes are relevant
    here, such as how or whether you deal with FloorDiv vs. regular
    division. Any non-empty choice is full credit. You should strongly 
    consider handling more than binary operators as well.) 
    * (You can swap operators "as you like". The most obvious approach
    is to swap + with -, and so on, but you can try something more creative
    if you want to.) 
3. Delete an assignment or function call <b>statement</b> (i.e., cause it to have no effect). 
    * (You have free choice of which AST node classes are relevant here.
    For example, you might decide that ``assignment'' means Assign,
    AnnAssign and AugAssign. You may also choose to deal with assignments,
    function calls, or both. Any non-empty choice is full credit.)
    * (Other edits that have the "effect" of deleting the assignment
    or function call but are not "officially" deletion are totally fine and
    are full credit.)
    * (Similarly, whether you interpret function call as
    <tt>func()</tt> or <tt>x = func()</tt> or both is up to you.)
    
Notes:
<ul> 
  <li> Note that you should implement these mutations, but they do not all
  have to be equally likely &mdash; or even occur at all. For example, you
  could have code that would correctly swap * to //, but you decide to make
  it run 0% of the time because you think that will be better for mutation
  testing. That's fine and full credit: we can see your source code to tell
  that you completed the assignment, but you get high marks on the
  autograder by not producing dangerous mutants.</li> 
  <li> Students are often anxious about adhering to this part of the
  specification. The quality of your mutation test generator will
  be assessed automatically by the autograder, regardless of which
  operators you use. Separately, whether or not you implemented the right
  operators will be assessed by a human &mdash; a live person who is not
  out to get you. Any reasonable choice you make here is fine, just
  document it. Please be reassured. The pedagogical goal is to get you
  experience with some different AST node types and mutations, not to make
  sure that you found exactly the AnnAssign vs. AugAssign node types and
  memorized the difference between them (in fact, we will not test you on
  any trivia like that, here or on an exam). </li> 
  <li> Note that implementing those three actions may not be enough to get full
  points on the autograder, but you do have to implement those three and
  describe them in your report to get full credit on the report. You may also
  need to implement more operators or heuristics to get full credit on the
  autograder.</li>
  <li> Note also that you do not have to use all three with the
  same frequency (or even use them at all &mdash; you could set their
  probabilities to zero). You <i>do</i>, however, have to implement them as a
  minimal baseline.</li>
</ul> 

<h4>Mutation Testing</h4>
<p>
For this assignment we will make use of the <tt>FuzzyWuzzy</tt> string
matching library as a subject program. A version of the library merged into 
one file is available <A href="../assets/fuzzywuzzy.py">here</a>; it is 686 lines
long. You could also do <tt>git clone
https://github.com/seatgeek/fuzzywuzzy.git</tt>, but the
merged-into-one-file version prevents you from having to write a mutator
that handles multiple files, and is thus highly recommended. 
</p> 
<p>
In addition, two public test suites are provided:
<A href="../assets/publictest-full.py"><tt>publictest-full.py</tt></a> and
<A href="../assets/publictest-half.py"><tt>publictest-half.py</tt></a>. The
latter was produced by removing every other test from the former. They are
thus not independent high-quality test suites, and you are encouraged to
make your own higher-quality test suites (e.g., using the techniques from
previous homeworks).
</p> 
<p>
Recall that one goal of mutation testing is to assess the adequacy of a
test suite. We would thus like the automatic results of our mutation
testing to agree with our intuitive assessment that the <tt>full</tt> test
suite is of higher quality than the <tt>half</tt> test suite. 
</p> 

<details markdown="block">
<summary>Example Mutation Testing Details</summary>

<p>
Here is how
an example run might go: 
<pre>
$ echo I must run this on the HW0 setup and not on my local machine
$ pip3 install pydocstyle  # you may need to install other libraries as well
$ python3 mutate.py fuzzywuzzy.py 10

$ cp fuzzywuzzy.py saved.py ; for mutant in [0-9].py ; do rm -rf *.pyc *cache* ; cp $mutant fuzzywuzzy.py ; python3 publictest-full.py 2&gt; test.output ; echo $mutant ; grep FAILED test.output ; done ; cp saved.py fuzzywuzzy.py 
0.py
FAILED (failures=2)
1.py
FAILED (errors=24)
2.py
3.py
FAILED (errors=35)
4.py
FAILED (failures=5)
5.py
6.py
FAILED (failures=22, errors=1)
7.py
FAILED (failures=1)
8.py
9.py
FAILED (errors=40)

$ echo I must run this on the HW0 setup and not on my local machine
$ cp fuzzywuzzy.py saved.py ; for mutant in [0-9].py ; do rm -rf *.pyc *cache* ; cp $mutant fuzzywuzzy.py ; python3 publictest-half.py 2&gt; test.output ; echo $mutant ; grep FAILED test.output ; done ; cp saved.py fuzzywuzzy.py 
0.py
1.py
FAILED (errors=11)
2.py
3.py
FAILED (errors=17)
4.py
FAILED (failures=3)
5.py
6.py
FAILED (failures=11)
7.py
FAILED (failures=1)
8.py
9.py
FAILED (errors=21)
</pre> 
</p> 
<p>
In this example we first create ten mutants. We then run each of those ten
mutants against the <tt>full</tt> test suite, and notice that seven of the  
mutants are "killed" by at least one test (i.e., fail at least one test). 
Finally, we run each of those
mutants against the <tt>half</tt> test suite, and notice that only six 
of the mutants are killed. Thus, in this example, the mutation adequacy
score for the <tt>full</tt> suite is 0.7 and the mutation adequacy score
for the <tt>half</tt> suite is 0.6, so mutation testing has assigned test
suite qualities that order the test suites in a way that matches our
intuition.
</p> 
<p>
(If you see warnings like <tt>zsh: no matches found: *.pyc</tt>, there are
two things to do. First, you are required to to use HW0 for the coding
assignments, not a local machine. Second, double-check what is happening
inside that long command that starts with <tt>cp</tt>. Unless you
understand all of the sub-parts of it, you will not be able to interpret
the warnings. Review HW0 or outside resources for more information on
complex shell commands.) </p> 
<p>
(If you don't ever see <tt>FAILED</tt> when you run this locally, it
typically means that your local installation doesn't have some Python
libraries or modules installed. View the contents of the file
<tt>test.output</tt> for more information.) 
</p> 
<p>
In the example above, note <tt>FAILED (failures=22, errors=1)</tt>. The
distinction between "failures" and "errors" is made by Python's Unit
Testing framework and does not matter for our grading. Basically, 
a "failure" refers to failing the unit test while an "error" refers to any
other exception. You are likely doing a better job if you get all failures
and no errors, but our grading server just looks for <tt>FAILED</tt> (which
includes both). See <A
href="https://docs.python.org/2/library/unittest.html">Python's
Documentation</a> for more information.

</p> 
<p>
Ten mutants is not a large number for randomized testing. We could gain
additional confidence by using a larger sample: 
<pre>
$ cp original_saved_fuzzywuzzy.py fuzzywuzzy.py 
$ python3 mutate.py fuzzywuzzy.py 100

$ echo I must run this on the HW0 setup and not on my local machine
$ cp fuzzywuzzy.py saved.py ; for mutant in [0-9]*.py ; do rm -rf *.pyc *cache* ; cp $mutant fuzzywuzzy.py ; python3 publictest-full.py ; done &gt;&amp; test.output ; grep FAILED test.output | wc -l ; cp saved.py fuzzywuzzy.py 
46

$ cp fuzzywuzzy.py saved.py ; for mutant in [0-9]*.py ; do rm -rf *.pyc *cache* ; cp $mutant fuzzywuzzy.py ; python3 publictest-half.py ; done &gt;&amp; test.output ; grep FAILED test.output | wc -l ; cp saved.py fuzzywuzzy.py 
38
</pre>
</p>
<p>
In the example above, 46 of the mutants are killed by the <tt>full</tt>
suite but only 38 are killed by the <tt>half</tt> suite. 
</p> 
</details>

<h4>Held-Out Test Suites </h4>
<p>
Writing a mutation analysis that can tell high-quality test suites from
low-quality test suites is the purpose of this assignment. If we give too
many details about the held-out test suites there is a significant danger
that students will "overfit" their answers, making something that satisfies
the autograder rather than something that imparts useful software
engineering knowledge. 
</p> 
<p>
As a result, we intentionally give only vague information about what is in
the held-out test suites: 
</p> 
<ul>
    <li> Test Suites A, B, C, D and E have 92%, 91%, 90%, 88% and 79%
    statement coverage of <tt>fuzzywuzzy</tt>, respectively. Test Suites A,
    B, C, D and E have 80, 57, 47, 32 and 9 tests, respectively. Remember
    that statement coverage is not the "right answer" or "gold standard"
    here, it is a cheap approximation. </li> 

    <li> <b>Swapping Binary Operators</b> can help distinguish Test Suites
    A and B from Test Suites C, D and E. </li> 
  <li> <b>Swapping Comparison Operators</b> can help distinguish between Test
  Suites B, C, D and E. </li> 
  <li> <b>Deleting Assignments and Function Calls</b> can, in theory,
  distinguish between all Test Suites, but is most likely to tease apart
  C, D and E. With care, it can also distinguish A from B.</li>  

  <li> <b><i>Careful</i> Higher-Order Mutation</b> can help distinguish
  between Test Suites B, C and D. </li> 

  <li> <b>Your Creativity</b> may be help distinguish between Test
  Suites A and B. (Figuring this out is part of the assignment.) Test Suite
  A contains over 20 tests not found in B. </li> 

  <li> Remember that increasing the odds of one mutation operator also
  effectively reduces the odds of the others (since you can only produce a
  fixed number of mutants) &mdash; if you are not careful, you may see your
  results oscillate. Similarly, every invalid mutant you create (search for
  <tt>pylint</tt> below) hurts you here &mdash; some students report that
  not creating invalid mutants allowed them to distinguish between Suites A
  and B.</li> 

</ul> 

<p>
The most common student questions for this assignment are along the lines
of "I'm not sure how to improve my score on the autograder. My mutation
analysis cannot tell test suites X and Y apart &mdash; it gives them the
same score. What's in those tests? What should I do?" We explicitly
will not tell you more that what you see on this page.
</p> 

<h4>Using the Library &mdash; Visitor Patterns and Starter Code</h4> 
<p>
A very common source of student confusion relates to how the AST library is
structured. It uses a <a
href="https://en.wikipedia.org/wiki/Visitor_pattern">visitor pattern</a>, a
way of structuring and interfacing code. Such "design
patterns" should have been covered in your undergraduate software engineering class
(for example, I spend
<a href="https://web.njit.edu/~mjk76/teaching/cs490-au23/assets/lecture-20-design-patterns.pdf">one lecture</a>
on them in CS 490). This section is designed to assist
students who aren't already familiar with the visitor pattern.
</p>
<p>
A visitor pattern provides abstraction and modularity by <i>hiding from
you</i> the exact fields and way in which a data structure is traversed or
transformed. (This allows the library writer to change the internal
representation of the data structure later, such as to move from Python 2
to Python 3 or whatever, without all of the client code needing to update.) 
</p> 
<p>
The following "starter code", adapted from <a
href="https://bitbucket.org/takluyver/greentreesnakes/src/master/examples/wrap_integers.py">wrap_integers.py
online</a>, may be useful to students who are not as familiar with visitor
patterns. If you find yourself wondering "How can I tell if this node is a
number or a function call?" or "How can I change this node's value?",
double-check the starter code. 
</p>

<details markdown="block">
<summary>Click to show starter code</summary>

```
# This "Starter Code" shows how to use a visitor
# pattern to replace nodes in an abstract syntax tree. 
# 
# Note well:
# (1) It does not show you how to read input from a file. 
# (2) It does not show you how to write your resulting source
#       code to a file.
# (3) It does not show you how to "count up" how many of 
#       instances of various node types exist.
# (4) It does not show you how to use random numbers. 
# (5) It does not show you how to only apply a transformation
#       "once" or "some of the time" based on a condition.
# (6) It does not show you how to copy the AST so that each
#       mutant starts from scratch. 
# (7) It does show you how to execute modified code, which is
#       not relevant for this assignment.
#
# ... and so on. It's starter code, not finished code. :-) 
# 
# But it does highlight how to "check" if a node has a particular type, 
# and how to "change" a node to be different. 

import ast
import astor

class MyVisitor(ast.NodeTransformer):
    """Notes all Numbers and all Strings. Replaces all numbers with 481 and
    strings with 'SE'."""

    # Note how we never say "if node.type == Number" or anything like that.
    # The Visitor Pattern hides that information from us. Instead, we use
    # these visit_Num() functions and the like, which are called
    # automatically for us by the library. 
    def visit_Num(self, node):
        print("Visitor sees a number: ", ast.dump(node), " aka ", astor.to_source(node))
        # Note how we never say "node.contents = 481" or anything like
        # that. We do not directly assign to nodes. Intead, the Visitor
        # Pattern hides that information from us. We use the return value
        # of this function and the new node we return is put in place by
        # the library. 
        # Note: some students may want: return ast.Num(n=481) 
        return ast.Num(value=481, kind=None)

    def visit_Str(self, node):
        print("Visitor sees a string: ", ast.dump(node), " aka ", astor.to_source(node))
        # Note: some students may want: return ast.Str(s=481)
        return ast.Str(value="SE", kind=None)

# Instead of reading from a file, the starter code always processes in 
# a small Python expression literally written in this string below: 
code = """print(111 + len("hello") + 222 + len("goodbye"))"""

# As a sanity check, we'll make sure we're reading the code
# correctly before we do any processing. 
print("Before any AST transformation")
print("Code is: ", code)
print("Code's output is:") 
exec(code)      # not needed for this homework...
print()

# Now we will apply our transformation. 
print("Applying AST transformation")
tree = ast.parse(code)
tree = MyVisitor().visit(tree)
# Add lineno & col_offset to the nodes we created
ast.fix_missing_locations(tree)
print("Transformed code is: ", astor.to_source(tree))
co = compile(tree, "<ast>", "exec")
print("Transformed code's output is:") 
exec(co)        # not needed for this homework...
```

The output may look something like (but don't panic if yours is a little
different): 

```
$ python3 starter.py
Before any AST transformation
Code is:  print(111 + len("hello") + 222 + len("goodbye"))
Code's output is:
345

Applying AST transformation
Visitor sees a number:  Constant(value=111, kind=None)  aka  (111)

Visitor sees a string:  Constant(value='hello', kind=None)  aka """hello"""

Visitor sees a number:  Constant(value=222, kind=None)  aka  (222)

Visitor sees a string:  Constant(value='goodbye', kind=None)  aka """goodbye"""

Transformed code is:  print(481 + len('SE') + 481 + len('SE'))

Transformed code's output is:
966
```
</details>

<h4>Hints, Advice and Doing Well</h4>

Many students report that they find it easy to get a few points on this
assignment but hard to get a high score. That is, it is hard to write a
<tt>mutate.py</tt> that produces mutants that rank-order the high- and
low-quality test suites. 

If you find that your program is not producing enough high-quality mutants
to assess the adequacy of a test suite, consider the hints and tips
below:

<details markdown="block">
<summary>Hints and Tips</summary>

* Try making a high-quality test suite locally and evaluating against
it. The <tt>privatetest-a.py</tt> file is just  a file that the
instructor created that has a bunch of tests for <tt>fuzzywuzzy</tt> in
it. The other test suites were just that test suite with many test cases
removed. After the previous homeworks, you know a bunch of good ways to make a
high quality test suite. You could do all of this yourself. The advantage
of doing it yourself is that you can try things out "locally" as often as
you want without hitting the submission limit. 
* Take a look at the mutation scores you are receiving from the
autograder. If many of them are very high (e.g., around 80 or more) you 
are likely using mutation operators that are "too powerful" and are
creating mutants that are killed by every test suite. If they are too low
(e.g., around 20) you are likely using mutation operators that are too  weak.
* Make sure you actually have a chance of mutating every relevant
node. For example, if you decide that your <i>n</i>th mutant will 
delete the <i>n</i>th statement in the original and you are asked to
create 10 mutants for a 20-statement program, you will never touch the
second half of the statements. (Doing this correctly may require you to
count the number of relevant items before making any mutations.)
* Consider carefully the number of mutation operators you apply to
create a mutant. If you apply too few the mutant will not be killed by
any tests. If you apply too many, the mutant will be killed by every
test. In both cases such a mutant will not help to distinguish between
high- and low-quality test suites.
* You may want to implement additional mutation operators. See Section
II.b of <a href="../assets/mutation-testing.pdf">Jia and Harman's <i>An
Analysis and Survey of the Development of Mutation Testing</i></a> for
ideas.
* Thought question. Suppose your program is just one main method with
a few if statements. Would you rather mutate the straight-line code at
the beginning of the method, or a statement deeply nested inside some
conditionals? Recall that your goal is to have the mutant killed by
strong test suites but not weak ones. 

You may want to avoid generating "useless" or "stillborn" mutants, such
as those that do not parse, always exit with an error, are equivalent to a
previously-generated mutant, etc. See Sections III and IV of the Jia and
Harman survey for ideas. Here are some common student pitfalls. You should
check locally to see if you are making any of these. 

* <b>Not running <tt>pylint</tt>!</b> After creating your mutants,
you can just run <tt>pylint -E [0-9]*.py</tt>. Change your mutation
operations to minimize the number of linting errors reported. (Run pylint
on its own, not inside some other shell script that is piping output
somewhere.) 

* <b>Creating Python programs with bad indentation. </b> Be careful
about deletions. Since Python cares about indentation and the like,
just removing something entirely can mess up the rest of the program. 
Perhaps instead of removing something you may want to replace it with a
statement that has no effect, such as <tt>Expr(Num(1))</tt>? 

* <b>Creating Python programs that reference variables before those
variables are defined.</b> Hack: what if you kept track of the first time
each variable was mentioned and never deleted the first instance and also
never copied a reference before its first mention? 

* <b>Removing or changing something that looks like a function call,
but isn't really, such as the <tt>@functools.wraps(func)</tt> annotation
on line 53</b>. Take into account context and value when changing such
nodes. 

* <b>Mistakenly sharing the tree data structure between mutants and
ending up with more edits than you thought.</b> Try using something like
<tt>ast = copy.deepcopy(original_ast)</tt> to make a deep copy.</li> 

* <b>Flipping a coin at each statement to decide whether or not to
mutate it.</b> This is problematic, because you'll end up with some
mutants with 0 edits and some with 100. Instead, try fixing a budget
in advance (e.g., "this time we will do 2 mutations") and then choosing
random places to apply them. 

* <b>Spending too much time enumerating many possible mutations or
mutation locations first.</b> You will likely hit the timeout on the
autograder &mdash; find a faster way to make a choice at random.

</details>

<h3>HW6b &mdash; Written Report</h3> 
<p>
You must also write a short three-paragraph PDF report reflecting on your
experiences creating a mutation testing tool for this assignment. Your
report must include your University email address(es). 
Consider
addressing topics such as: 
<ul>
  <li> Which mutation operators did you implement? </li> 
  <li> How does your program decide which operators to apply? </li> 
  <li> What was harder than you expected or different than you expected?  </li> 
  <li> How would you compare and contrast mutation analysis with statement
  coverage as a test suite adequacy metric.</li> 
</ul> 
</p> 
Rubric: 
  * 5 points &mdash; a three-paragraph report reflecting on your
  activities creating a mutation testing tool for this assignment,
  including a discussion of mutation operators and your 
  experiences and expectations 
  * 4 points &mdash; a reasonable report, but lacking a solid
  description of one or more aspects or being rote rather than insightful
  or significantly exceeding the length limit
  * 3 points &mdash; a brief report, detailing only half of the required
  information 
  * 2 points &mdash; a report drawing only the bare minimum of contrasts
  comparisons, and explanations 
  * 1 point &mdash; a terse or uninformative report, perhaps describing
  only one activity or operator<
  * -1 point (or more) &mdash; submitted source code does not implement the
  require operators (even loosely)
  * -1 point &mdash; English prose or grammatical errors

<p>
The grading staff may select a small number of excerpts from particularly
high-quality or instructive reports and share them with the class. If your
report is selected you will receive extra credit. 
</p> 

<h3>Submission</h3>
<p>
Submit a single <tt>mutate.py</tt> file to the autograder on Gradescope. Submit a single
PDF report via Canvas. In your PDF report, you must include your name and
NJIT UCID (as well as your partner's name and UCID, if applicable).
</p>
<p>
For the autograder submission, we have manually prepared a number of private
(i.e., held-out) test suites of known quality. For example, Private Test
Suite A is known to be better than Private Test Suite B. You receive points
if your mutant adequacy score shows that A is is better than B (i.e., if A
kills more of your mutants than B). We check "A &gt; B" and "A &gt;= B"
separately; the former is worth more points. 
</p> 
<p>
While there are visible tests with <i>private</i> content (in that you
don't get to see what they contain), there are no <i>hidden</i> tests (here
or on any other homework in this course), so the score you see on the
Autograder is your final score. 
</p> 

Note that the autograder will reject your submission (and give you a score of
zero) if your <tt>mutate.py</tt> does any of the following:
* crashes while producing mutants
* does not produce the requested number of mutants or does not name the mutants as specified above
* produces a "mutant" that is identical to the input program (that is, containing no mutations)

You will be graded based on your _highest_ autograder score from all submissions that you
make. Note however that there is a soft limit of <b>5 autograder submissions per 24 hour period</b>: we don't
want you to "play the lottery" by e.g., trying different random seeds. This limit is not enforced
automatically, but we can see how many submissions that you've made on Gradescope; we'll investigate
any cases with unusually high numbers of submissions (in practice, this means as long as you are not
abusing the autograder, you don't need to keep track of this limit: if you accidentally make six submissions
in 23 hours and 59 minutes, nothing bad will happen.). If you did egregiously violate this limit, your grade may be
reduced as we see fit. If you egregiously violate this limit _accidentally_ (i.e., you find this text just after spending
an hour making submission after submission), contact the course staff immediately: while we may assess a penalty, we'll
look much more kindly on it if you admit your mistake.

<h3>FAQ and Troubleshooting</h3>
<p>
In this section we detail previous student issues and resolutions: 
<ol>

<li><p><b>Question:</b> When I try to create mutants, even locally, the
<tt>to_source</tt> function complains.</p>
<p><b>Answer:</b> If you create a Python AST that is missing critical
information (like an important tree child, or location information) or
otherwise create something totally invalid, the library won't even let you
print it out. For example, if you had "x = y + z" and you remove the "z"
node entirely without doing anything else, the library might not even print
out the result at all because it is not valid Python. Even something as
simple as saying <tt>ast.GtE</tt> instead of <tt>ast.GtE()</tt> can cause
this. 
</p> 
</li> 

<li><p><b>Question:</b> It feels like the autograder is non-deterministic. I
feel like I am submitting the same <tt>mutate.py</tt> twice and getting
different results. 
<p>
<p><b>Discussion:</b> There are many possible issues here that all result
in the same observed symptom. </p> 

<p><b>Answer 1:</b> Your <tt>mutate.py</tt>  may be non-deterministic.
(This is rare, since student are careful about it.) </p> 

<p><b>Answer 2:</b> Your <tt>mutate.py</tt>  may be creating <i>mutants</i>
that are, themselves, non-deterministic. This is much trickier, and happens
surprisingly often. </p> 

<p><b>Answer 3:</b> Your test automation may be using stale information or
cached values. Even with the <tt>rm -rf *.pyc *cache*</tt>, you may be
testing on mutants created by a previous run of <tt>mutate.py</tt> if you
are not careful. </p> 

<p><b>Answer 4:</b> There may be differences between the autograder setup
and your local setup. For example, the autograder uses <tt>export
PYTHONHASHSEED=0</tt> to try to determinize the order in which hashmaps are
iterated. 

<p><b>Discussion:</b> Ultimately, it may not be worth your time to track
this down. Remember that we use your best submission, not your last one.
Start early. 
</p> 

<li> <p><b>Question:</b> I am getting erors like
<tt>TypeError: 'type' object is not subscriptable</tt>. Help!
</p>
<p><b>Answer:</b> Double-check the spelling on the AST pieces you are
creating or manipulating. For example,
use <tt>ast.GtE()</tt> not the incorrect <tt>ast.GtE</tt> (note the
parentheses, which are required).
</p> 
</li> 


<li> <p><b>Question:</b> When I run locally, I get
<pre>
ImportError: No module named 'astor'
</pre></p>
<p><b>Answer:</b> Make sure you install (again!) with <tt>pip3</tt> and
<tt>python3</tt> rather than <tt>pip</tt> and <tt>python</tt>. </p> </li> 

<li> <p><b>Question:</b> I am trying to delete things, but I get this
error: 
<pre>
assert node is None, node
AssertionError: <class '_ast.Pass'>
</pre> 
</p>
<p><b>Answer:</b> You have <tt>ast.Pass</tt> but want <Tt>ast.Pass()</tt>
instead (note the parentheses). However, you may actually not want to
"delete" things like this at all (look around for other hints). </p></li> 

<li> <p><b>Question:</b> Is fuzzywuzzy.py being modified? When I run all of
my mutants to test them it really looks like fuzzywuzzy is being changed.
</p>
<p><b>Answer:</b> Good observation. Your <tt>mutate.py</tt> does not change
it directly, but the example shell script commands we have above do (look
for <tt>cp</tt> which means "copy"). Just copy a saved version back over
the original.</p></li> 

<li> <p><b>Question:</b> When I run my <tt>mutate.py</tt>, I get this error
when trying to print out my mutants:
<pre>
"AttributeError: 'Assign' object has no attribute 'value' "
</pre>
</p>
<p> <b>Answer:</b> This error occurs when the AST library tries to
pretty-print your abstract syntax tree data structure back out to (ASCII)
Python source. The AST library expects each node object to have certain
fields (properties) filled out. Sometimes a node operation that can look
totally reasonable to you (e.g., making a new node, setting it as the child
of some other node) can result in a node object not having all of the
fields set. If you are changing the types of nodes directly, I would
recommend that you instead use their friendly constructors &mdash; that may well
end up fixing this problem for you. (This is explicitly a bit of a
challenge; dig around first and get used to the AST library before asking
for help here.) 
</p> 

<li> <p><b>Question:</b> How can I get the parts of an AST node? Suppose I
want to figure out the identified on the left-hand side of an assignment:
<pre>
Assign(targets=[Name(id='x', ctx=Store())], value=Num(n=9))
</pre></p>
<p><b>Answer:</b> Check out
<a href="https://greentreesnakes.readthedocs.io/en/latest/nodes.html">the
node documentation</a>. In this particular example, some students report 
success with <tt>node.targets[0].id</tt> to extract the id from
an instance of the the Assign class.
</p>
<p>
Similarly, suppose you want to change the right-hand side of the assignment
to "None", but leave the left-hand side alone. Have your node transformer
do something like: 
<pre>
return ast.copy_location(ast.Assign(targets=node.targets, value=ast.NameConstant(value=None)), node)
</pre>

<li> <p><b>Question:</b> I've just started deleting statements, but now I
get: 
<pre>
AttributeError: module 'string' has no attribute 'strip'
</pre> 
</p>
<p><b>Answer:</b> If you look closely, you'll see that
<tt>fuzzywuzzy.py</tt>
has <tt>if PY3: string = str</tt> on lines 14-15. If you make big changes
there you end up changing which module the code will use, which can have
far-reaching effects. Be careful! </p> 

<li> <p><b>Question:</b> I'm getting errors like
<pre>
AttributeError: module 'ast' has no attribute 'Constant' 
</pre> 
or
<pre>
AttributeError: 'Classdef' object has no attribute 'starargs'
 </pre> 
</p>
<p><b>Answer:</b> The autograder uses Python 3.10.12 with astor version 0.8.1. You'll want
to make sure you're using the same versions. 
</p> 
<li> <p><b>Question:</b> Some online documentation makes a big deal about
<tt>generic_visit</tt>, but I don't really understand it. Can you
elaborate?
</p>
<p><b>Answer:</b> To some degree, using it or not is your choice. Suppose
you want to change every assignment from "x = y" to "x = y + 1".
</p> 
<p> 
In a language like C, you can write "a = b = 3". (Don't ever do this.) The
interpretation of this statement is that you first assign b=3, and then
that result (3 in this case) is also assigned into a.
</p> 
<p>
If you do <i>not</i> do the "generic visit" thing and instead replace the
top-level assignment only,  you'll end up with something like this:
</p> 
<pre>
a = (b = 3) + 1
</pre> 
<p>
[ After this program, b=3 and a=4. ]
</p>
<p>
If you do the "<i>generic visit</i>" thing and recursively transform the child
nodes as well,  you'll end up with something like this:
</p> 
<pre> 
a = (b = 3 + 1) + 1
</pre> 
<p>
[ After this program, b=4 and a=5. ]
</p> 
<p> 
Which one do you want? It's your choice. If you have a theory about which
one is a better mutation operator, do that. 
If you don't care, it's safe to default to the full recursive handling of
all sub-nodes.
</p> 
</li> 
