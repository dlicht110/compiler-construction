# BNFC and Java

The IPL book is written with Haskell and Java in mind. BNFC also supports other programming languages. For example

    bnfc -m -c  Calc.cf      # to generate C
    bnfc -m -cpp Calc.cf      # to generate C++
    bnfc -m -java Calc.cf      # to generate Java
    bnfc -m -haskell Calc.cf      # to generate Haskell
    
should all work. I will assume that you successfully [my BNFC installation instructions](https://github.com/alexhkurz/compiler-construction/blob/master/BNFC-installation.md). Here we will look at how to get the 
Java part of the [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html) to work.

First, we need to install the latest version of the Java lexer and parser. It is necessary to change the CLASSPATH variable so that
it knows the location of the JLex and Cup. In my case I created directories `/usr/local/java`and `/usr/local/java/Cup`and `/usr/local/java/JLex` and then [added to my `.bash_profile`](https://github.com/alexhkurz/compiler-construction/blob/master/PATH.md)

     export CLASSPATH=$CLASSPATH:.:/usr/local/java/:/usr/local/java/Cup:/usr/local/java/JLex

Install [JLex](http://www.cs.princeton.edu/~appel/modern/java/JLex/) version 1.2.6 (the latest version). To quote from the tutorial "JLex is just one Java file. Put it in some directory, e.g. `/usr/local/java/JLex`. Compile it with `javac Main.java` in that directory". You may also want to look the instructions in the [readme file](http://www.cs.princeton.edu/~appel/modern/java/JLex/current/README). 

You can check the value of `CLASSPATH` by typing `echo $CLASSPATH`. Make sure that the directory in which you compiled `javac Main.java` is in the CLASSPATH.

Install the latest version of [Cup](http://www2.cs.tum.edu/projects/cup/), the Java parser generator. In my case, I put `java-cup-11b.jar` into `/usr/local/java/Cup` and then unzipped it using 

    sudo unzip java-cup-11b.jar
    
(you may not need sudo).

Now, going back to the directory `examples` in the directory `bnfc` downloaded from github

    bnfc -m -java Calc.cf
    make
 
should result in producing a bunch of `.java` files as described on page 12 of the [slides](http://www.grammaticalframework.org/ipl-book/slides/2-slides-ipl-book.pdf).

To test whether the parser works enter (still working in the directory `bnfc/examples')

    echo "23 + 4 * 70" | java Calc/Test 
        
which should give you 

            Parse Succesful!
            [Abstract Syntax]
            (EAdd (EInt 23) (EMul (EInt 4) (EInt 70))) 
            [Linearized Tree]
            23 + 4 * 70





   
