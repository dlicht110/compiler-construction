# BNFC Self Check

See the [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html) for reference and more detail. The self-check is devided into a theory and a practice part.

## Practice: 

### Parsing C-- using BNFC

You need to be able to recreate the following in Haskell or Java. According to the tutorial, C or C++ should also work.

In all cases you should start by saving the fibonacci program of the tutorial into a file called

    fibonacci.cmm
  
and saving the "Complete grammar for C--" of the tutorial in a file 

    Cmm.cf

#### Haskell

Run

    bnfc -m -haskell Cmm.cf
    make
    ./TestCmm fibonacci.cmm

and check that you get the answer

        Parse Successful!

followed by the [Abstract Syntax] and the [Linearized tree].

#### Java

Run

    bnfc -m -java Cmm.cf
    make
    java Cmm/Test <fibonacci.cmm
  
and check that you get the same output as for Haskell, see above.

### Exercise 1

Write your own C-- program and parse it.

### Exercise 2
You will not know the programming language Promela. In this exercise you will see how to use a BNF in order to understand whether a program in a programming language you don't know is a legal program (this will help you to learn how to write your own grammar later). In other words, the task is to take the [Promela grammar](http://spinroot.com/spin/Man/grammar.html) and parse the following program by hand. Return an error message if the program cannot be parsed. (The program is a variation of the [Peterson algorithm](https://en.wikipedia.org/wiki/Peterson%27s_algorithm).)

```
bool	turn, flag[2];
byte	cnt;

active [2] proctype P1()
{	pid me, other;

    me = _pid;
    other = 1 - _pid;

    again: flag[me]=1;
    turn=other;
    ! (flag[other] && turn = other) ->

    /* begin critical section */
    cnt++;
    printf("cnt=%d \n", cnt); 
    assert cnt == 1; 
    cnt--;        
    flag[me]=0;
    /* end critical section */
 
    goto again
}

#define flag0 (flag[0] == 0)
#define flag1 (flag[0] == 1)
```


## Theory: Answer the following questions (Exercise 3)

If you are unsure about the answers consult Chapter 2 in [the book](http://www.cse.chalmers.se/edu/year/2012/course/DAT150/lectures/plt-book.pdf) and the [slides](http://www.grammaticalframework.org/ipl-book/slides/2-slides-ipl-book.pdf) and also the [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html).

- Explain the difference between **concrete and abstract syntax**. Why is this distinction important for compiler construction?

- Explain the importance of **precedence levels**. Why does the grammar in `Calc.cf` parse `1+2*3` as `1+(2*3)` and not as `(1+2)*3`?

- Explain the concept of **algebraic data types**. How are algebraic data types programmed in Haskell and Java?

- Explain the BNFC notation for **grammars**. Can you write out in detail how to derive the program Fibonacci from the grammar of C-- ?
