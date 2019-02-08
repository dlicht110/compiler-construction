# BNFC installation

The [BNFC homepage](http://bnfc.digitalgrammars.com/) is the first place to go, but installation instructions are out of date, so we need to work a bit to find our way. I will add information here as we go along and learn more about the best way to get this done.

## Working under Windows

Download the [binaries](https://github.com/BNFC/bnfc/releases).

## Working under Linux/MacOS

Installing BNFC under Linux/MacOS requires installing Haskell and compiling the source code. 

Download and install Haskell.


Create a directory in which you want to clone the BNFC github directory and `cd` there.

    git clone https://github.com/BNFC/bnfc
    cd bnfc
    make
    cd examples
    bnfc -m -haskell Calc.cf
    make
    echo "23 + 4 * 70" | ./TestCalc 
    cp ../document/tutorial/calc/haskell/Interpreter.hs .
  
modify TestCalc.hs as discribed in the [slides](http://www.grammaticalframework.org/ipl-book/slides/2-slides-ipl-book.pdf) on page 33 and save the file as Calculator.hs
  
    ghc --make Calculator.hs
    echo "1 + 2 * 3" | ./Calculator
    
you have successfully compiled and run your first program
