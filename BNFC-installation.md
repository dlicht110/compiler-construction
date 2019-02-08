# BNFC installation

Go to the [BNFC homepage](http://bnfc.digitalgrammars.com/).

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
