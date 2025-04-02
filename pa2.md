---
layout: project
title: "PA2: Semantic Analyzer"
permalink: /projects/pa2.html
parent: Programming Assignments
nav_order: 2
due_date: "Monday, 3 March 2025, 11:59PM AoE."
submission_notes: Submit on GradeScope
---

You may complete this assignment in any language listed on the [languages page](../languages/) in buckets 1, 2, or 3.

You may work in a team of two people for this assignment. You may work in a team for any or all subsequent programming assignments. You do not need to keep the same teammate between this assignment and subsequent assignments.
The course staff are not responsible for finding you a willing teammate. You are permitted to work alone, if you choose.

### Goal

For this assignment you will write a _semantic analyzer_. Among other things, this involves traversing the [abstract syntax tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) and the class hierarchy. You will reject all Cool programs that do not comply with the Cool type system.

You will also write additional code to unserialize the AST produced by the provided parser and to serialize the class map, implementation map, parent map, and annotated AST produced by your semantic analysis.

### Summary of Checkpoints

You need to make three submissions for this assignment:
* **PA2c1** requires you to write test cases (i.e., Cool programs) that find injected bugs in our reference semantic analyzer. This checkpoint ensures that you have a robust test suite for your own semantic analyzer. This checkpoint is relatively straightforward (you just need to write small Cool programs), so it due early: on **Friday, February 7**.
* **PA2c2** requires you have a mostly-working semantic analyzer. You must have handled all semantic errors except those related to _typechecking expressions_. And, you only need to output the class map, rather than the full `.cl-type` file format. This checkpoint is the big one for PA2, so it is due one week before the full due date: on **Monday, February 24**.
* **PA2 (full)** requires a complete semantic analyzer. It is due on **Monday, March 3**.

### Specification

You must create three artifacts:
1. A program that takes a single command-line argument (e.g., `file.cl-ast`). That argument will be an ASCII text Cool abstract syntax tree file (as described below in the section "The .cl-ast File Format"). Your program must either indicate that there is an error in the input (e.g., a type error) or emit `file.cl-type`, a serialized Cool abstract syntax tree, class map, implementation map, and parent map. If your program is called `checker`, invoking `checker file.cl-ast` should yield the same output as `cool --type file.cl`. Your program will consist of a number of files in the language of your choice. The main entry point for your program must be in a file called `main.$EXT`, where `$EXT` is replaced by the customary file extension used by your programming language of choice (e.g., `main.ml` for OCaml, or `main.c` for C). If you are using a language that typically capitalizes file names (like Java), you should follow that convention as you normally would (so, a Java implementation's entrypoint should be in `Main.java`). Your program cannot rely on non-standard external dependencies, and must build using your language's standard compiler command. See the [language page](../languages/)'s entry for your language for more details.
2. A plain ASCII text file called `readme.txt` describing your design decisions and choice of test cases. See the grading rubric. A few paragraphs should suffice.
3. Testcases `good.cl`, `bad1.cl`, `bad2.cl` and `bad3.cl`. The first should pass the semantic analysis stage. The remaining three should yield semantic analysis errors.

### The .cl-ast File Format

The input to your program will be in the `.cl-ast` format described in this section. The `cool` reference compiler produces `.cl-ast` files from `.cl` files; you should use it to do so when testing. You may assume that your program only receives well-formed `.cl-ast` files. If you want to see examples of the format, use the `--parse` flag of reference compiler to generate `.cl-ast` files.

If you are having trouble reading in `.cl-ast` files, you are almost certainly doing something wrong: the format is designed to be easy to parse (it may require a bit of work to cover all cases, but the code you write should be pretty formulaic). Check with the TAs if you're finding it difficult for any reason---the usual case is a misunderstanding of the specification, which is easy to clear up by explaining the trouble to the TA.

The general format of a `.cl-ast` file follows the Cool Reference Manual Syntax chart. Basically, we do a [pre-order traversal](http://en.wikipedia.org/wiki/Tree_traversal) of the abstract syntax tree, writing down every node as we come to it.

We now describe exactly what the parser outputs for each kind of node. You can view this as specifying a set of mutually-recursive tree-walking functions. The notation "superclass:_identifier_" means "output the superclass using the rule (below) for outputting an _identifier_". The notation "\n" means "output a newline".
* **To Output An AST**. A Cool AST is a list of classes. Output the list of classes.
* **To Output A List (of classes, or features, or whatever).** Output the number of elements, then a newline, then output each list element in turn.
* **To Output A Class.** Output the class name as an identifier. Then output either:
  * `no_inherits` \n
  * `inherits` \n superclass:_identifier_
  <br>Then output the list of features.
* **To Output An Identifier.** Output the source-file line number, then a newline, then the identifier string, then a newline.
* **To Output A Feature.** Output the name of the feature and then a newline and then any subparts, as given below:
  * `attribute_no_init` \n name:_identifier_ type:_identifier_
  * `attribute_init` \n name:_identifier_ type:_identifier_ init:_exp_
  * `method` \n name:_identifier_ _formals-list_ \n type:_identifier_ body:_exp_
* **To Output A Formal.** Output the name as an identifier on line and then the type as an identifier on a line.
* **To Output An Expression.** Output the line number of the expression and then a newline. Output the name of the expression and then a newline and then any subparts, as given below:
  * `assign` \n var:_identifier_ rhs:_exp_
  * `dynamic_dispatch` \n e:_exp_ method:_identifier_ args:_exp-list_
  * `static_dispatch` \n e:_exp_ type:_identifier_ method:_identifier_ args:_exp-list_
  * `self_dispatch` \n method:_identifier_ args:_exp-list_
  * `if` \n predicate:_exp_ then:_exp_ else:_exp_
  * `while` \n predicate:_exp_ body:_exp_
  * `block` \n body:_exp_-list
  * `new` \n class:_identifier_
  * `isvoid` \n e:_exp_
  * `plus` \n x:_exp_ y:_exp_
  * `minus` \n x:_exp_ y:_exp_
  * `times` \n x:_exp_ y:_exp_
  * `divide` \n x:_exp_ y:_exp_
  * `lt` \n x:_exp_ y:_exp_
  * `le` \n x:_exp_ y:_exp_
  * `eq` \n x:_exp_ y:_exp_
  * `not` \n x:_exp_
  * `negate` \n x:_exp_
  * `integer` \n `the_integer_constant` \n
  * `string` \n `the_string_constant` \n
  * `_identifier_` \n variable:_identifier_ <p style="color:red;">(note that this is not the same as the integer and string cases above)</p>
  * `true` \n
  * `false` \n
* **To Output A let Expression.** (Output the line number, as usual.) Output `let` \n. Then output the binding list. To output a binding, do either:
  * `let_binding_no_init` \n variable:_identifier_ type:_identifier_
  * `let_binding_init` \n variable:_identifier_ type:_identifier_ value:_exp_
  <br>Finally, output the expression that is the body of the let.
* **To Output A case Expression.** (Output the line number, as usual.) Output `case` \n. Then output the case expression. Then output the case-elements list. To output a case-element, output the variable as an _identifier_, then the type as an _identifier_, then the case-element-body as an _exp_.

Example input `.cl` file:
```
(* Line 01 *)
(* Line 02 *)
(* Line 03 *)  class List {
(* Line 04 *)     -- Define operations on lists.
(* Line 05 *)
(* Line 06 *)     cons(i : Int) : List {
(* Line 07 *)        (new Cons).init(i, self)
(* Line 08 *)     };
(* Line 09 *)
(* Line 10 *)  };
```

Corresponding `.cl-ast` file, _with comments_ (will not be present in the output of the reference compiler):
```
fier
6                      --   line number of return type identifier
List                   --   return type identifier
7                      --    line number of body expression
dynamic_dispatch       --    kind of body expression
7                      --     line number of dispatch receiver expression
new                    --     kind of dispatch receiver expression
7                      --      line number of new-class identifier
Cons                   --      new-class identifier
7                      --     line number of dispatch method identifier
init                   --     dispatch method identifier
2                      --     number of arguments in dispatch
7                      --      line number of first argument expression
identifier             --      kind of first argument expression
7                      --       line number of the identifier
i                      --       what is the identifier?
7                      --      line number of second argument expression
identifier             --      kind of second argument expression
7                      --       line number of the identifier
self                   --       what is the identifier?
```

### Error Reporting

To report an error, write the string:
```
ERROR: $line_number: Type-Check: $message
```
to standard output and terminate the program. You may write whatever you want in the message, but it should be fairly indicative. Example erroneous input:
```
class Main inherits IO {
 main() : Object {
   out_string("Hello, world.\n" + 16777216) -- adding string + int !?
 } ;
} ;
```
Example error report output:
```
ERROR: 3: Type-Check: arithmetic on String Int instead of Ints
```

#### Line Number Error Reporting

The typing rules do not directly specify the line numbers on which errors are to be reported. The Cool reference compiler uses these guidelines (possibly surprising ones are _italicized_), which you should also follow:
* Errors related to parameter-less method `main` in class `Main`: always line 0
* Inheritance cycle: always line 0
* Other inheritance type problem: inherited type identifier location
* self or `SELF_TYPE` used in wrong place: self (resp. `SELF_TYPE`) identifier (resp. type) location
* Redefining a feature: (second) feature location
* Redefining a formal or class: (second) identifier location
* Other attribute problems: attribute location
* Redefining a method and changing types: (second) type location
* Other problems with redefining a method: method location
* Method body type does not conform: method _name identifier_ location
* Attribute initializer does not conform: attribute _name identifier_ location
* Errors with types of arguments to relational/arithmetic operations: location of relational/arithmetic operation expression
* Errors with types of `while` / `if` subexpression(s): location of (enclosing) `while` or `if` expression (_not_ the location of the conditional expression)
* Errors with case expression (e.g., lub): location of `case` expression
* Errors with conformance in `let`: location of `let` expression (_not_ location of initializer)
* Errors in blocks: location of (beginning of) block expression
* Errors in actual arguments: location of method invocation expression (_not_ the location of any particular actual argument)
* Assignment does not conform: assignment expression location (_not_ right-hand-side location)
* Unknown identifier: location of identifier
* Unknown method: location of method name identifier
* Unknown type: location of type

Remember that you do not have to match the English prose of the reference compiler's error messages at all. You just have to get the line number right.

Semantic checks are _unordered_ — if a program contains two or more errors, you may indicate whichever you like. (All of our test cases for grading will contain at most one error so this will not be an issue.)

### The .cl-type File Format

If there are no errors in `file.cl-ast` your program should create `file.cl-type` and serialize the class map, implementation map, parent map, and annotated AST to it.

The class and implementation maps are described in the Cool Reference Manual.

A `.cl-type` file consists of four sections:
1. The class map.
2. The implementation map.
3. The parent map.
4. The annotated AST.

Simply output the four sections in order, one after the other.

We will now describe exactly what to output for the class and implementation maps. The general idea and notation (one string per line, recursive descent) are the same as in the `.cl-ast` file format, described above.

**The Class Map**
* Output `class_map`\n.
* Output the number of classes and then \n.
* Output each class in turn (in ascending alphabetical order):
  * Output the name of the class and then \n.
  * Output the number of attributes and then \n.
  * Output each attribute in turn (in order of appearance, with inherited attributes from a superclass coming first):
    * Output `no_initializer` \n and then the attribute name \n and then the type name \n.
    * _or_ Output `initializer` \n and then the attribute name \n and then the type name \n and then the initializer expression.

**The Implementation Map**
* Output `implementation_map`\n.
* Output the number of classes and then \n.
* Output each class in turn (in ascending alphabetical order):
  * Output the name of the class and then \n.
  * Output the number of methods for that class and then \n.
  * Output each method in turn (in order of appearance, with inherited or overridden methods from a superclass coming first; internal methods are defined to appear in ascending alphabetical order):
    * Output the method name and then \n.
    * Output the number of formals and then \n.
    * Output each formal's name only:
      * Output the name and then \n
    * If this method is inherited from a parent class and not overriden, output the name of the ultimate parent class that defined the method body expression and then \n. Otherwise, output the name of the current class and then \n.
    * Output the method body expression.

**The Parent Map**
* Output `parent_map`\n
* Output the number of parent-child inheritance relations and then \n. This number is equal to the number of classes minus one (since `Object` has no parent).
* Output each child class in turn (in ascending alphabetical order):
  * Output the name of the child class and then \n.
  * Output the name of the child class's parent and then \n.

**The Annotated AST**
* With two exceptions, the annotated AST format is identical to the normal AST format described above for the `.cl-ast` file.
* The first change involves expressions. To output an **Expression**:
  1. Output the line number of the expression and then a newline (as in the `.cl-ast` format).
  2. **Output the name of type associated with the expression and then a newline.** For example, the expression 3+x is associated with the type Int. This is not required for any of the checkpoints for PA2, only in the final version of PA2.
  3. Output the name of the expression and then a newline and then any subparts (as in the `.cl-ast` format).
* The second change is a new kind of expression, _internal_, used to represent the bodies of predefined methods. Internal expressions are those that are handled by the run-time system — you might think of them as part of the standard library. You output **Internal Expressions** (including the type annotation, as above) as follows:
  * 0 \n _type_ \n `internal` \n Class.method \n
  <br>The valid kinds of internal expressions (i.e., the values for Class.method) are:
    * IO.in_int IO.in_string IO.out_int IO.out_string Object.abort Object.copy Object.type_name String.concat String.length String.substr
  <br>They are formally defined in the Cool Reference Manual.

_Note that you must output information about all classes and methods defined in the program as well as all base classes (and their methods). Do not just print out "classes actually used" or "methods actually called" or something like that. Output all classes and methods — no optimizations or shortcuts!_

### Detailed .cl-type Example

Now that we've formally defined the output specification, we can present a worked example. Here's the example input we will consider:
```
class Main inherits IO {
  my_attribute : Int <- 5 ;
  main() : Object {
    out_string("Hello, world.\n")
  } ;
} ;
```

Resulting `.cl-type` class map output _with comments_ (each row represents one line of the `.cl-type` output; you only need to emit the left-most column):

| .cl-type class map | comment |
| --- | --- |
| class_map |  |
| 6 | number of classes |
| Bool | note: includes predefined classes |
| 0 | |
| IO | |
| 0 | |
| Int | |
| 0 | |
| Main | |
| 1 | Our Main has one attribute... |
| initializer | |
| my_attribute | ...named "my_attribute"... |
| Int | ...with type Int |
| 2 | initializer expression line number |
| Int | initializer expression type (see above: this is an expression _annotated_ with a type) -- do **not** emit these _expression_ types for PA2c2! |
| integer | initializer expression kind |
| 5 | which integer constant is it? |
| Object | |
| 0 | |
| String | |
| 0 | |

Resulting `.cl-type` implementation map _with comments_:

| .cl-type implementation map | comment |
| --- | --- |
| implementation_map | |
| 6 | six classes |
| Bool | first is Bool |
| 3 | - Bool has 3 methods |
| abort | - first method in Bool is abort() |
| 0 | -- abort() has zero formal parameters |
| Object | -- name of parent class from which Bool inherits abort() |
| 0 | -- abort's body expression starts on line 0 |
| Object | -- abort's body expression has type Object |
| internal | -- abort's body is an internal kind of expression (i.e., a system call; see above) |
| Object.abort | -- extra detail on abort's body expression |
| copy | - second of Bool's three methods is copy() |
| 0 | -- copy has 0 formal arguments |
| Object | -- name of parent class from which Bool inherits copy() |
| 0 | -- copy's body expression starts on line 0 |
| SELF_TYPE | -- copy's body expression has type SELF_TYPE |
| internal | -- copy's body is an internal kind of expression (i.e., a system call; see above) |
| Object.copy | -- extra detail on copy's body expression |
| ... many lines skipped ... | |
| Main | another class is Main |
| 8 | Main has 8 methods |
| ... many lines skipped ...	| |
| main | - one of Main's methods is main() |
| 0 | -- main has 0 formal arguments |
| Main | -- the name of the class where Main.main() is defined |
| 4 | -- the body expression of Main.main starts on line 4 |
| SELF_TYPE | -- the body expression of Main.main has type SELF_TYPE |
| self_dispatch | -- the body of Main.main() is a self_dispatch kind of expression |
| ... many lines skipped ...	| |

Finally, the resulting `.cl-type` parent map output _with comments_:

| .cl-type parent map | comment |
| parent_map | |
| 5 | there are five clases with parents (Object is the sixth class) |
| Bool | Bool's parent... |
| Object | ...is Object |
| IO | IO's parent...|
| Object | ...is also Object |
| Int | |
| Object | |
| Main | Main's parent... |
| IO | ...is IO, rather than Object, because of the "inherits IO" on line 1 |
| String | |
| Object | |

Writing the rote code to output a `.cl-type` text file given an AST may take a bit of time but it should not be difficult; our reference implementation does it in 35 lines and cleaves closely to the structure given above. Reading in the AST is similarly straightforward; our reference implementation does it in 171 lines.

### Commentary

You can do basic testing as follows:
```
$ cool --parse file.cl
$ cool --out reference --type file.cl
$ my-checker file.cl-ast
$ diff -b -B -E -w file.cl-type reference.cl-type
```

You should implement all of the typing rules in the Cool Reference Manual. There are also a number of other rules and corner cases you have to check (e.g., no class can inherit from Int, you cannot redefine a class, you cannot have an attribute named self, etc.). They are sprinkled throughout the manual. Check everything you possibly can.

### PA2c1 — Creating PA2 Tests

PA2c1 is a preliminary testing exercise that introduces a form of [test-driven development](http://en.wikipedia.org/wiki/Test-driven_development) or [mutation testing](http://en.wikipedia.org/wiki/Mutation_testing) into our software development process and requires you to construct a high-quality test suite.

The goal of PA2c1 is to leave you with a high-quality test suite of Cool programs that you can use to evaluate your own PA2 type checker. Writing a type checker requires you to consider many corner cases when reading the formal and informal typing rules in the Cool Reference Manual. While you you can check for correct "positive" behavior by comparing your typechecker's output to the reference compiler's output on existing "good" Cool programs, it is comparatively harder to check for "negative" behavior (i.e., correctly reporting ill-typed Cool programs).

If you fail to construct a rich test suite of syntactically-valid but semantically-invalid programs you will face a frustrating series of "you fail held-out negative test x" reports for PA2 proper, which can turn into unproductive guessing games. Because students often report that this is frustrating (even though it is, shall we say, infinitely more realistic than making all of the post-deployment tests visible in advance), the PA2c1 preliminary testing exercise provides a structured means to help you get started with the construction of a rich test suite.

The course staff have produced 20 variants of the reference compiler, each with a secret [intentionally-introduced defect](http://en.wikipedia.org/wiki/Fault_injection) related to type-checking. A high-quality test suite is one that reveals each introduced defect by showing a difference between the behavior of the true reference compiler and the corresponding buggy version. You desire a high-quality test suite to help you gain confidence in your own PA2 submission.

For PA2c1, you must produce syntactically valid Cool programs (test cases). There are 20 separate held-out seeded type-checker bugs waiting on the grading server. For each bug, if one of your tests causes the reference and the buggy version to produce difference output (that is, either a different `.cl-type` file or a different error report), you win: that test has revealed that bug. For full credit your tests must reveal at least 15 of the 20 unknown defects.

The secret defects that we have injected into the reference compiler correspond to common defects made by students in PA2. Thus, if you make a rich test suite for PA2c1 that reveals many defects, you can use it on your own PA2 submission to reveal and fix your own bugs!

### Video Guides

This assignment is a mildly-modified version of [Wes Weimer](https://web.eecs.umich.edu/~weimerw/)'s [similar assignment](https://weimer.github.io/csci2320/pa4.html).
Wes has kindly prepared a number of video guides to help students get started on...:
* [PA2c1](https://youtu.be/2CMhLddBt1M) (which his course calls "PA4t")
* [PA2c2](https://youtu.be/Wa9zMygcv_M) (which his course calls "PA4c")
* [PA2 (full)](https://youtu.be/Oxpgrkmsxhg) (which his course calls "PA4")

(Aside: the reason that the type checker in Wes' class is "PA4" but in this class it's "PA2" is that Wes can't make the assumption that students have built a lexer and parser before (as NJIT students hopefully did in CS 280). So, Wes' course includes a "PA2: Lexer" and "PA3: Parser" before this assignment. That leaves Wes' course with less time at the end of the course, so they build a Cool _interpreter_ rather than a compiler---meaning that their course misses out on code generation and optimization, which in my opinion are the most interesting parts.)

### What to Turn In For PA2c1

For PA2c1 you should turn in (electronically):
* A set of up to 99 .cl files: Cool typechecker testcases.
  * Each testcase you submit must be syntactically valid (i.e., must pass `cool --parse`).
  * Each testcase you submit may be semantically valid or semantically invalid, your choice (i.e., it can pass or fail `cool --type`).
  * If you submit more than 99 tests, some will be ignored.

Hint: because you can find "positive" bugs in your typechecker more easily (e.g., by running your typechecker on the correct Cool programs from `cool-examples.zip`), the PA2c1 exercise is strongly biased toward "negative" bugs (i.e., the secret buggy typecheckers usually fail to report certain semantic errors).

### PA2c2 — Typechecking Everything But Expressions

PA2c2 is a checkpoint for your full semantic analyzer implementation (unlike PA2c1, which only requires you to write test cases). The typechecker is a large project (and a large part of your grade), so it behooves you to start it early. PA2c2 exists so that students are motivated to have _something_ working earlier, because we know that students are deadline-driven :)

For PA2c2 you should turn in an early version of PA2 that does the following:
* Reads in the `.cl-ast` file given as a command-line argument.
  * You do not need to use a parser generator to read in the `.cl-ast` file — its format was specifically chosen to make it easy to read with just some mutually-recursive procedures. It should take you (much) less than 150 lines to read in the `.cl-ast` file.
* Does every bit of typechecking and semantic analysis possible _without typechecking expressions_.
  * Thus you should not annotate types in initializer expressions in the class map.
* Prints out error messages as normal.
* Outputs _only the class map_ to `.cl-type` if there are no errors.
  * You can use the `--class-map` command-line argument to get the reference compiler to spit out the class map after typechecking (for comparison).

Thus you should build the class hierarchy and check everything related to that. For example:
* Check to see if a class inherits from `Int` (etc.).
* Check to see if a class inherits from an undeclared class.
* Check for cycles in the class hierarchy.
* Check for duplicate method or attribute definitions in the same class.
* Check for a child class that redefines a parent method but changes the parameters.
* Check for a missing method `main` in class `Main`.
* Check for `self` and `SELF_TYPE` mistakes in classes and methods.
* This list is **not exhaustive** -- read the Cool Reference Manual carefully and find everything you might check for without typechecking expressions.
* Basically, you'll look at classes, methods and attibutes (but not method bodies).

---
**Question**: What's the exact list of errors I have to check for in PA2c2?

**Answer 1**: No such list is provided! Part of the assignment is thinking up all possible checks that do not involve expressions.
<br>**Answer 2**: Use the test cases you made for PA2c1.

---

### What to Turn In For PA2c2

You must turn in these files:
* `source_files` — your implementation, including exactly one of the following files:
  * `main.c`
  * `main.py`
  * `main.cpp`
  * `Main.java`
  * `main.kt`
  * `main.rs`
  * `Main.scala`
  * `main.ml`
  * `main.hs`

### What to Turn In For PA2

You must turn in these files:
* `source_files` — your implementation, including exactly one of the following files:
  * `main.c`
  * `main.py`
  * `main.cpp`
  * `Main.java`
  * `main.kt`
  * `main.rs`
  * `Main.scala`
  * `main.ml`
  * `main.hs`
* `readme.txt` - your README file
* `good.cl` - a novel positive test case
* `bad1.cl` - a novel negative test case
* `bad2.cl` - a novel negative test case
* `bad3.cl` - a novel negative test case

### Grading Rubric

PA2 Grading (out of 100 points):
* 66 points — for autograder tests
  * The scoring is directly proportional to the number of autograder tests you pass.
* 5 points — for a correct PA2c1 submission
* 5 points — for a correct PA2c2 submission
* 8 points — for a clear description in your README
  * 8 — thorough discussion of design decisions (e.g., handling of the class hierarchy, case and new and dispatch) and choice of test cases; a few paragraphs of coherent English sentences should be fine
  * 4 — vague or hard to understand; omits important details
  * 0 — little to no effort, or submitted an RTF/DOC/PDF file instead of plain TXT
* 8 points — for valid and novel `good.cl`, `bad1.cl`, `bad2.cl` and `bad3.cl` files
  * 8 — wide range of test cases added, stressing most Cool features and three error conditions, novel files (note: it is acceptable for these test cases to be a selection of the best ones from your PA2c1 submission: that's what we expect)
  * 4 — added some tests, but the scope not sufficiently broad
  * 0 — little to no effort, or course files resubmitted as tests
* 8 point — for code cleanliness
  * 8 — code is mostly clean and well-commented
  * 4 — code is sloppy and/or poorly commented in places
  * 0 — little to no effort to organize and document code
