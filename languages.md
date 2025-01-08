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
* _Bucket 4: Project Language_: [Classroom Object-Oriented Language (COOL)](../crm/)

For PA2-4, you may work in any of the above languages except COOL[^1]. For each of those assignments,
the input language is COOL (or, more accurately, a pre-parsed version of COOL). The output for PA3 and
PA4 is x86-64 assembly, in TODO style. Details of the supported assembly language are also provided on this page.

Completing PA2-4 in a language from Bucket 1 has no penalties or benefits.

Completing PA2-4 in a language from Bucket 2 entitles you to one extra [test case view](../about/#office-hours-and-viewing-test-cases) per assignment.

Completing PA2-4 in a language from Bucket 3 entitles you to one extra test case view per assignment and one point of extra credit per assignment (only on the
final submission, not on the checkpoints).

You can switch languages between PA2 and PA3, but I don't recommend doing so unless you really struggled with PA2. You should not switch between PA3 and PA4, because
PA4 builds on PA3---I expect you to modify you PA3 implementation to complete PA4. See the assignment pages for more details.

## Source and Target Languages

### COOL

TODO: more details. See the [Reference manual](../crm/).

### x86-64

TODO: more details.

## Language Choices

### Python

### C

### C++

### Java

### Kotlin

### Rust

### Scala

### Haskell

### OCaml

[^1]: you don't want to use COOL as your implementation language, anyway. It intentionally omits many convenience features of higher-level languages to simplify the compiler implementation process, but that can make it unwieldy for writing "real" programs.