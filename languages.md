---
layout: page
title: Supported Languages
description: Information about supported programming languages.
---

This page discusses the languages supported in this class. It has two goals:
* explain the course policies on language choice for the programming assignments, and
* give technical details on the versions of each language that the course supports.

## Language Choice for Programming Assignments

PA1 groups the languages into four buckets:
* _Bucket 1: Languages You Already Know_: Java, C, C++, or Python3
* _Bucket 2: Languages With An Unusual Type System_: Kotlin, Rust, or Scala
* _Bucket 3: Functional Languages_: OCaml or Haskell
* _Bucket 4: Project Language_: [Classroom Object-Oriented Language (COOL)](../crm/modern/)

For PA2-4, you may work in any of the above languages except COOL[^1]. For each of those assignments,
the input language is COOL (or, more accurately, a pre-parsed version of COOL). The output for PA3 and
PA4 is x86-64 assembly. Details of the supported assembly language are provided below on this page.

Completing PA2-4 in a language from Bucket 1 has no penalties or benefits.

Completing PA2-4 in a language from Bucket 2 entitles you to one extra [test case view](../about/#office-hours-and-viewing-test-cases) per assignment.

Completing PA2-4 in a language from Bucket 3 entitles you to two extra test case views per assignment and one point of extra credit per assignment (only on the
final submission, not on the checkpoints).

You may switch languages between PA2 and PA3, but I don't recommend doing so. You must not switch between PA3 and PA4, because
PA4 builds on PA3---I expect you to modify you PA3 implementation to complete PA4. See the assignment pages for more details.

## Source and Target Languages

### Cool

**Cool** is a _Classroom Object-Oriented Language_ — it is essentially a small subset of Java. It's small enough to be manageable for semester projects but large enough to help you to learn all of the concepts and to write non-trivial programs. This course uses Cool version 1.36.

Here is a "Hello, World" program in Cool:
```
(* hello-world.cl *)
class Main inherits IO {
  main() : Object {
    out_string("Hello, world.\n")
  } ;
} ;
```

#### Cool Reference Manual

The Cool programming language is formally specified and defined in _The Cool Reference Manual_, a document that you will grow to love (or hate) over the course of this semester. Multiple versions are available:
* [CRM Modern](../crm/modern/) — a revised manual with improved readability, but requiring browser JavaScript
* [CRM Modern (One Page, HTML)](../crm/onepage/crm-onepage.html) - a revised manual with improved readability, but requiring browser JavaScript (one single webpage)
* [CRM Classic](https://web.eecs.umich.edu/~weimerw/2016-ldi/cool-manual/cool-manual.html) — the "old-school" manual, requiring only basic HTML and images

#### Cool Reference Compiler

Different versions of the reference compiler are available for different platforms. Information on running the compiler is available in the reference manual.
* [Linux/x86 (64 bit)](../assets/cool/linux-x86_64/cool) (v. 1.36) (1.36 binaries with alternate library requirements: [B](../assets/cool/linux-x86_64/cool-136b) [C](../assets/cool/linux-x86_64/cool-136c) [D](../assets/cool/linux-x86_64/cool-136d))
* [Linux/x86 (32 bit)](../assets/cool/linux-x86/cool) (v. 1.36)
* [Mac OS X Apple M-Series Chips (ARM-64)](../assets/cool/darwin-arm/cool) (v. 1.36) 
* [Mac OS X/x86 (Intel Chips)](../assets/cool/darwin/cool) (v. 1.36)
* [Win32/x86](../assets/cool/win32-x86/cool.exe) (v. 1.36)

Don't forget to run `chmod a+x ./cool` on Unix platforms to make these executable.

We also provide a library of sample Cool programs [here](../assets/cool-examples.zip).

#### Additional Cool Resources

There are a number of other Cool resources available online; this is not an exhaustive list. If you find others that are useful, contact the course staff
and they can be added here. Note that these resources are provided "as-is": the course staff can't promise to help you with them if you're having trouble. But,
feel free to ask your classmates on the course forum!
* There is [Cool syntax highlighting support for Vim](https://www.vim.org/scripts/script.php?script_id=1216).
* If you like XEmacs, the [Berkeley Harmonia project](https://harmonia.cs.berkeley.edu/harmonia/projects/harmonia-mode/doc/index.html) has a Cool mode. It offers quite a bit more than syntax highlighting, but not all of the semantic features are guaranteed to be compatible with our dialect of Cool.
* The Sublime text editor supports [Cool syntax highlighting](https://github.com/princjef/sublime-cool-highlighter).
* An easy-to-script [implementation of Delta Debugging](https://web.eecs.umich.edu/~weimerw/2016-ldi/reading/delta-2006.08.03.tar.gz) is available, written by Daniel S. Wilkerson and Scott McPeak.

### x86-64

There are many dialect and syntax options of "x86 assembly language". This course _only allows_ the 64-bit version supported by **gcc** on **Linux**.
If your regular development machine doesn't support this flavor of x86, you'll need to use a virtual machine ([instructions here](../tutorials/ubuntu.html)).
Note that we use the default [AT&T syntax](https://en.wikipedia.org/wiki/X86_assembly_language#Syntax).

To find out if your development machine supports our flavor of x86-64 assembly language, try this:
```
./cool --x86 hello-world.cl
gcc -no-pie -static hello-world.s
./a.out
```

If there were no assembler or linker errors and you saw "Hello, world.", your system can handle our x86-64 assembly.

Although we're invoking `gcc`, that's just shorthand: it's calling `as` and `collect2` and whatnot to assemble the `.s` file into an object file and link that object file into an executable. You can see the individual steps with `gcc -v`.

---
**A Note on Position Independent Executables**

On modern Linux systems (including Ubuntu since version 17.10),
`gcc` assumes that all assembly code should be [position independent](https://en.wikipedia.org/wiki/Position-independent_code) by default.
The reference compiler does not produce position-independent code, though (and you are not required to produce position-independent code, either). The
`-no-pie` and `-static` flags to `gcc` tell the assembler and linker to produce a non-position-independent executable when assembling and linking.
For all assembly code in this course, you should always use these flags when assembling and linking.

---

Useful links for assembly programming that were helpful in the construction of the reference compiler:
* Randal E. Bryant and David R. O'Hallaron's [x86-64 Machine Level Proramming](https://web.eecs.umich.edu/~weimerw/2015-4610/reading/bryant-ohallaron-x86-64.pdf)
* Wikibook's [X86 Assembly/GAS Syntax](http://en.wikibooks.org/wiki/X86_Assembly/GAS_Syntax)
* Stack Overflow on [Assembly Debugging with GDB](http://stackoverflow.com/questions/2420813/using-gdb-to-single-step-assembly-code-outside-specified-executable-causes-error)
* GDB's [Manual on Inspecting Registers](http://web.mit.edu/gnu/doc/html/gdb_10.html#SEC63)

## Language Choices

---

#### Bucket One: Languages You Already Know

### Python

[Python](https://en.wikipedia.org/wiki/Python_(programming_language)) is a high-level, general-purpose programming language.
Python is dynamically typechecked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its [comprehensive standard library](https://docs.python.org/3.10/library/index.html).

NJIT students should be familiar with Python from CS 100, CS 301, and other required courses. Therefore, it is a "Bucket 1" language.

This course uses Python version 3.10.12. The command we use to run a Python submission is either `python3 rosetta.py` (for PA1) or `python3 main.py` (for PA2-4).

### C

[C](https://en.wikipedia.org/wiki/C_(programming_language)) is a general-purpose systems programming language, popularized along with Unix in the 1970s and 1980s.
Its design emphasizes cleanly reflecting the capabilities of CPUs of that era. C is an imperative procedural language, supporting structured programming, lexical variable scope, and recursion, with a static type system. It was designed to be compiled to provide low-level access to memory and language constructs that map efficiently to machine instructions, all with minimal runtime support. Despite its low-level capabilities, the language was designed to encourage cross-platform programming. A standards-compliant C program written with portability in mind can be compiled for a wide variety of computer platforms and operating systems with few changes to its source code.

NJIT students should be familiar with C from their systems programming courses, including CS 288. Moreover, all computer scientists should have at least a passing
familiarity with C, since it is the historical ["lingua franca"](https://en.wikipedia.org/wiki/Lingua_franca) for systems programming. Therefore, it is a "Bucket 1" language.

This course uses the [GNU Compiler Collection](https://gcc.gnu.org/) ("gcc") C compiler, version 11.4.0. (More specifically, `(Ubuntu 11.4.0-1ubuntu1~22.04)`.)
We use the following commands to compile and run your C submissions: `gcc rosetta.c ; ./a.out` (for PA1) and `gcc *.c *.h ; ./a.out` (for PA2-4).

### C++

[C++](https://en.wikipedia.org/wiki/C%2B%2B) is a high-level, general-purpose programming language that extends C. C++ has object-oriented, generic, and functional features, in addition to facilities for low-level memory manipulation. C++ was designed with systems programming and embedded, resource-constrained software and large systems in mind, with performance, efficiency, and flexibility of use as its design highlights. C++ has also been found useful in many other contexts, with key strengths being software infrastructure and resource-constrained applications, including desktop applications, video games, servers (e.g., e-commerce, web search, or databases), and performance-critical applications (e.g., telephone switches or space probes).

NJIT students should be familiar with C++ because it is used in CS 280. Therefore, C++ is a "Bucket 1" language.

This course uses the [GNU Compiler Collection](https://gcc.gnu.org/)'s `g++` compiler, version 11.4.0. (More specifically, `(Ubuntu 11.4.0-1ubuntu1~22.04)`.)
We use the following commands to compile and run your C submissions: `g++ rosetta.cpp ; ./a.out` (for PA1) and `g++ *.cpp *.h ; ./a.out` (for PA2-4).

### Java

[Java](https://en.wikipedia.org/wiki/Java_(programming_language)) is a high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is a general-purpose programming language intended to let programmers write once, run anywhere --- meaning that compiled Java code can run on all platforms that support Java without the need to recompile. Java applications are typically compiled to bytecode that can run on any Java virtual machine (JVM) regardless of the underlying computer architecture. The Java runtime provides dynamic capabilities (such as reflection and runtime code modification) that are typically not available in traditional compiled languages.

NJIT students should be familiar with Java from CS 113. Therefore, it is a "Bucket 1" language.

This course uses `javac` version 11.0.24, via the [OpenJDK](https://openjdk.org/) project. We use the following commands to compile and run your Java submission:
`javac Rosetta.java & java Rosetta` (for PA1) and `javac *.java & java Main` (for PA2-4).

---

#### Bucket Two: Languages With An Unusual Type System

### Kotlin

[Kotlin](https://kotlinlang.org/) ([wiki](https://en.wikipedia.org/wiki/Kotlin_(programming_language))) is a cross-platform, statically typed, general-purpose high-level programming language with type inference. Kotlin is designed to interoperate fully with Java, and the JVM version of Kotlin's standard library depends on the Java Class Library, but type inference allows its syntax to be more concise.
Unlike Java, Kotlin makes a distinction between nullable and non-nullable data types. It also shares several design principles with Scala. Kotlin is a fully-supported language for Android app development.

No required classes at NJIT use Kotlin, so it is Bucket 2.

This course uses `kotlinc` (available [here](https://kotlinlang.org/docs/command-line.html)) version `kotlinc-jvm 2.0.20 (JRE 11.0.24+8-post-Ubuntu-1ubuntu322.04)`.
We use the following commands to compile and run your Kotlin code: `kotlinc Rosetta.kt ; kotlin RosettaKt` (for PA1) and `kotlinc *.kt ; kotlin MainKt` (for PA2-4).

### Rust

[Rust](https://www.rust-lang.org/) ([wiki](https://en.wikipedia.org/wiki/Rust_(programming_language))) is a general-purpose programming language emphasizing performance, type safety, and concurrency. It enforces memory safety, meaning that all references point to valid memory. It does so without a traditional garbage collector; instead, memory safety errors and data races are prevented by the "borrow checker", which tracks the object lifetime of references at compile time.
It is popular for systems programming, and there have been calls to replace C and C++ with Rust in critical applications.

No required classes at NJIT use Rust, so it is Bucket 2.

This course uses `rustc` version `rustc 1.75.0 (82e1608df 2023-12-21)` (built from a source tarball).
To compile and run your Rust code, we use the following commands: `rustc rosetta.rs ; ./rosetta` (for PA1) and `rustc -o a.out *.rs ; ./a.out` (for PA2-4).

### Scala

[Scala](https://www.scala-lang.org/) ([wiki](https://en.wikipedia.org/wiki/Scala_(programming_language))) is a strong statically typed high-level general-purpose programming language that supports both object-oriented programming and functional programming. Designed to be concise, many of Scala's design decisions are intended to address criticisms of Java. Scala source code can be compiled to Java bytecode and run on a Java virtual machine (JVM). When running on the JVM, Scala provides language interoperability with Java so that libraries written in either language may be referenced directly in Scala or Java code. Unlike Java, Scala has many features of functional programming languages, including currying, immutability, lazy evaluation, and pattern matching. It also has an advanced type system supporting algebraic data types, covariance and contravariance, higher-order types (but not higher-rank types), anonymous types, operator overloading, optional parameters, named parameters, raw strings, and an experimental exception-only version of algebraic effects that can be seen as a more powerful version of Java's checked exceptions.

No required classes at NJIT use Scala, so it is in Bucket 2.

This course uses Scala version 2.11.12. To compile and run your Scala code, we use the following commands: `scalac Rosetta.scala ; scala Rosetta` (for PA1) and `scalac *.scala ; scala Main` (for PA2-4).

---

#### Bucket Three: Functional Languages

### Haskell

[Haskell](https://www.haskell.org/) ([wiki](https://en.wikipedia.org/wiki/Haskell)) is a general-purpose, statically-typed, purely functional programming language with type inference and lazy evaluation. Haskell has pioneered several programming language features such as type classes, which enable type-safe operator overloading, and monadic input/output (IO). It is a purely functional programming language, which means that functions generally have no side effects. Haskell has a strong, static type system based on Hindley–Milner type inference.

Haskell is a purely functional language, and therefore is in Bucket 3. If you're not sure how to get started with Haskell, I recommend [Learn You A Haskell For Great Good!](https://learnyouahaskell.com/)

This course uses [The Glorious Glasgow Haskell Compilation System](https://www.haskell.org/ghc/), version 8.8.4.
To compile and run your Haskell code, we use the following commands: `ghc -o rosetta rosetta.hs ; ./rosetta` (for PA1) and `ghc -o a.out *.hs ; ./a.out` (PA2-4).

### OCaml

[OCaml](https://ocaml.org/) ([wiki](https://en.wikipedia.org/wiki/OCaml)) is a general-purpose, high-level, multi-paradigm programming language. Languages derived from the original "Meta Language" (the "ml" in "Ocaml") are best known for their static type systems and type-inferring compilers. OCaml unifies functional, imperative, and object-oriented programming under an ML-like type system. OCaml's type-inferring compiler greatly reduces the need for the manual type annotations that are required in most statically typed languages. For example, the data types of variables and the signatures of functions usually need not be declared explicitly, as they do in languages like Java and C#, because they can be inferred from the operators and other functions that are applied to the variables and other values in the code. Effective use of OCaml's type system can require some sophistication on the part of a programmer, but this discipline is rewarded with reliable, high-performance software.

While OCaml is not a purely functional language, its [standard library](https://ocaml.org/manual/4.13/api/index.html) is very limited, making it difficult to program in non-functional styles without additional libraries[^2]. It is therefore in Bucket 3.

This courses uses `ocamlc` version 4.13.1.
To compile and run your OCaml code, we use the following commands: `ocamlopt -o rosetta unix.cmxa str.cmxa rosetta.ml ; ./rosetta` (for PA1) and `ocamlopt -o a.out unix.cmxa str.cmxa *.ml ; ./a.out`.[^3]

[^1]: You don't want to use COOL as your implementation language, anyway. It intentionally omits many convenience features of higher-level languages to simplify the compiler implementation process, but that can make it unwieldy for writing "real" programs.

[^2]: While you're not allowed to use it for this class, the [Base](https://opensource.janestreet.com/base/) library from Jane Street is the preferred "standard library that's not in the standard library" for most production uses of OCaml that I've encountered.

[^3]: Note that `ocamlc` and `ocamlopt` are _argument-order-sensitive_: files are compiled in the order that they are supplied. It is your responsibility to name your files in such a way that all dependencies are respected by `ocamlopt`. No, we will not run `ocamldep` for you.)