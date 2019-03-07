# compiler-construction
Notes and Materials for a course on Compiler Construction Spring 2019 at Chapman University.

Quick links to BNFC installation instructions and other documentation, to be used in addition to the official [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html) and the  book [Implementing Programming Languages](http://www.grammaticalframework.org/ipl-book/):

- [BNFC: basic installation instructions](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-installation.md)
- [BNFC: adding the Java lexer and parser](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-installation-java.md)
- [BNFC: self check](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-example.md)
- BNFC/Happy parser:
  - The BNFC/Happy [`.info`-files](https://hackmd.io/s/ryllVQdIN) and an example of shift-reduce parsing
  - How to eliminate [shift/reduce and reduce/reduce](https://hackmd.io/s/S11sLzo84) conflicts
  - Understanding [LALR(1) parsing](https://hackmd.io/s/S11sLzo84) with a worked example.

Lecture by Lecture:

- [Lecture 1.1](lecture-1.1.md): Organisation, Assessment, Short introduction to parsing.

- Lab 1.2: Discussion of Assignment 1.
  - [Assignment 1](https://hackmd.io/s/HyaDeaXzN#) 
  - due Wed, Feb 6, see [Lecture 1.1](lecture-1.1.md) for details

- [Lecture 1.3](https://hackmd.io/s/S110eS-VE#): How to implement a state machine and why do Java and Python not have gotos? **Homework:** Read the articles referenced in [the lecture](https://hackmd.io/s/S110eS-VE).

- [Lecture 2.1](http://www.grammaticalframework.org/ipl-book/slides/1-slides-ipl-book.pdf): A brief introduction to compiler construction from Chapter 1 of [the book](http://www.grammaticalframework.org/ipl-book/). **Homework:** Read [Chapter 1](http://www.cse.chalmers.se/edu/year/2012/course/DAT150/lectures/plt-book.pdf).

- [Lecture 2.2](lecture-2.2.md): Determinstic Finite Automata. **Homework:** Exercise 2.2.4 (possibly 2.2.5 and 2.2.6) and Exercise 2.2.10 (possibly 2.2.11) from [Introduction to Automata Theory]( https://mcdtu.files.wordpress.com/2017/03/introduction-to-automata-theory.pdf). These exercises are relevant for tests and final.

- Lecture 2.3: **How to build a compiler/interpreter in 50min**. We looked at the [slides](http://www.grammaticalframework.org/ipl-book/slides/2-slides-ipl-book.pdf) up to page 35, see also Chapter 2 of [the book](http://www.cse.chalmers.se/edu/year/2012/course/DAT150/lectures/plt-book.pdf). For installation  introductions see the [BNFC homepage](http://bnfc.digitalgrammars.com) or my [BNFC installation instructions](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-installation.md). **Homework:** First install Haskell (not necessary if you use the windows binaries), then install BNFC. *Deadline: Monday, Feb 11, before class* (If there are problems with installation we will try to sort it out on Monday in class.)

- Lab 3.1: The aim of the lab is for everybody to be able to replicate my [BNFC installation instructions](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-installation.md). *From today on I will assume that everybody has bnfc installed and is able to run the calculator. Let me know if this is not the case.*

- Lecture 3.2: The aim of this lecture is to understand more about parsing. I link the grammars of [C](https://cs.wmich.edu/~gupta/teaching/cs4850/sumII06/The%20syntax%20of%20C%20in%20Backus-Naur%20form.htm) and [Java](https://docs.oracle.com/javase/specs/jls/se11/html/jls-19.html). In the lecture we explained how the grammar of C-- of the [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html) works. Then we started on Exercise 2 in  [BNFC self check](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-example.md). Trying to find the bug in the program of Exercise 2 is **Homework** (to do before the class on Friday, Feb 15, when we will look at this together).

- Lecture 3.3: The aim of the coming labs/lectures is to finish the material of Chapter 2 in [the book](http://www.cse.chalmers.se/edu/year/2012/course/DAT150/lectures/plt-book.pdf) and the [slides](http://www.grammaticalframework.org/ipl-book/slides/2-slides-ipl-book.pdf) and of the [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html). **Homework:**  [Install the Java lexer and parser](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-installation-java.md) and finish Exercise 2 of the [BNFC self check](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-example.md).

- Lab/Lecture 4.1: [Working towards Assignment 2](http://www.grammaticalframework.org/ipl-book/assignments/assignment1/assignment1.html).
[Install the Java lexer and parser](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-installation-java.md).

- Lab 4.2: The aim is to sort out any remaining problems with installing BNFC. For those who missed this in class there is a **Homework:** Exercise 0 of the [BNFC self check](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-example.md).

- Lecture 4.3: How to build a parse tree, illustrated by [Exercise 2](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-example.md). **Homework:** Exercise 3 of the [BNFC self check](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-example.md).

- Assignment 2: [Grammar and Parser for C++](http://www.grammaticalframework.org/ipl-book/assignments/assignment1/assignment1.html). Deadline for the first test file Thursday, Feb 28, (11:59 pm PST), for the rest of the assignment Sunday, March 10, (11:59 pm PST).  

  - Read Section 2.10 of [Implementing Programming Languages](http://www.cse.chalmers.se/edu/year/2012/course/DAT150/lectures/plt-book.pdf). See also `bnfc/examples/cpp/cpp.cf`.
  - The [LBNF reference](https://bnfc.readthedocs.io/en/latest/lbnf.html#lbnf-in-a-nutshell) can be a good resource, for example the section on [terminators and separators](https://bnfc.readthedocs.io/en/latest/lbnf.html#terminator).

- Lecture 5.1: Nondeterminstic Finite Automata](https://hackmd.io/s/ByjJ8eWUE). **Homework:** Exercise 2.3.1 and 2.3.2 from [Introduction to Automata Theory]( https://mcdtu.files.wordpress.com/2017/03/introduction-to-automata-theory.pdf). These exercises are relevant for tests and final.
  
- [Lecture 5.2](https://hackmd.io/s/SJv6u2GL4#): Composing Automata

- [Lecture 5.3](https://hackmd.io/s/rkA6Af484#): Regular Expressions. 

- [Lecture 6.1](https://hackmd.io/s/ryllVQdIN#): How does shift-reduce parsing work?  **Homework:** Do the exercise from the lecture notes. These exercises are relevant for tests and final.

- [Lecture/Lab 6.2/6.3](https://hackmd.io/s/rJoVGDh84#): How to eliminate shift/reduce and reduce/reduce conflicts. **Homework:** Do the exercise from the lecture notes. These exercises are relevant for Assignment 2.

- [Lecture 7.1](https://hackmd.io/s/S11sLzo84#): How does the LALR(1) parser generated by BNFC and Happy work?  **Homework:** Do the exercise from the lecture notes. This exercise is relevant for tests and final.


coming up soon:


- [Lecture](https://hackmd.io/s/r1ioqQEIE#): Regular Languages, Minimization, Pumping Lemma. 

- Lecture: Shift/reduce and reduce/reduce conflicts in BNFC generated parsers.

- Assignment 3:

  - 
 
  - 

