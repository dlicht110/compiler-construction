# BNFC Self Check

See the [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html) for reference and more detail.

## Parsing C--

You need to be able to recreate the following in Haskell or Java. According to the tutorial, C or C++ should also work.

In all cases you should start by saving the fibonacci program of the tutorial into a file called

  fibonacci.cmm
  
and saving the "Complete grammar for C--" of the tutorial in a file 

  Cmm.cf

### Haskell

  bnfc -m haskell Cmm.cf
  make
  ./TestCmm fibonacci.cmm

which should answer

    Parse Successful!

and then display the [Abstract Syntax] and the [Linearized tree].

### Java

  bnfc -m java Cmm.cf
  make
  java Cmm/Test <fibonacci.cmm
  
withe same output as for Haskell, see above.

## Answer the following questions

- 
