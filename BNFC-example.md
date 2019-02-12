# BNFC Self Check

See the [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html) for reference and more detail. The self-check is devided into a theory and a practice part.

## Practice: Parsing C-- using BNFC

You need to be able to recreate the following in Haskell or Java. According to the tutorial, C or C++ should also work.

In all cases you should start by saving the fibonacci program of the tutorial into a file called

    fibonacci.cmm
  
and saving the "Complete grammar for C--" of the tutorial in a file 

    Cmm.cf

### Haskell

Run

    bnfc -m haskell Cmm.cf
    make
    ./TestCmm fibonacci.cmm

and check that you get the answer

        Parse Successful!

followed by the [Abstract Syntax] and the [Linearized tree].

### Java

Run

    bnfc -m java Cmm.cf
    make
    java Cmm/Test <fibonacci.cmm
  
and check that you get the same output as for Haskell, see above.

### Exercise

Write your own C-- program and parse it.

## Theory: Answer the following questions

If you are unsure about the answers consult Chapter 2 in [the book](http://www.cse.chalmers.se/edu/year/2012/course/DAT150/lectures/plt-book.pdf) and the [slides](http://www.grammaticalframework.org/ipl-book/slides/2-slides-ipl-book.pdf) and also the [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html).

- Explain the difference between **concrete and abstract syntax**. Why is this distinction important for compiler construction?

- Explain the importance of **precedence levels**. Why does the grammar in `Calc.cf` parse `1+2*3` as `1+(2*3)` and not as `(1+2)*3`?

- Explain the concept of **algebraic data types**. How are algebraic data types programmed in Haskell and Java?

- Explain the BNFC notation for **grammars**. Can you write out in detail how to derive the program Fibonacci from the grammar of C-- ?

