# BNFC and Java

The IPL book is written with Haskell and Java in mind. BNFC also supports other programming languages. For example

    bnfc -m -c       FILE.cf      # to generate C
    bnfc -m -cpp FILE.cf      # to generate C++
    bnfc -m -java FILE.cf      # to generate Java
    bnfc -m -haskell FILE.cf      # to generate Haskell
    
should all work. For Haskell, see the previous lecture. Here we will look at how to get the 
Java part of the [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html) to work.

First, we need to install the latest version of the Java lexer and parser. It is necessary to change the CLASSPATH variable so that
it knows the location of the JLex and Cup. In my case I created directories `/usr/local/bin/java`and `/usr/local/bin/java/Cup`and `/usr/local/bin/java/JLex` and then added to my `.bash_profile`

     export CLASSPATH=$CLASSPATH:.:/usr/local/bin/java/:/usr/local/bin/java/Cup:/usr/local/bin/java/JLex

Install [JLex](http://www.cs.princeton.edu/~appel/modern/java/JLex/) version 1.2.6 (the latest version). To quote from the tutorial "JLex is just one Java file. Put it in some directory, e.g. `/usr/local/java/JLex`. Compile it with `javac Main.java` in that directory". You may also want to look the instructions in the [readme file](http://www.cs.princeton.edu/~appel/modern/java/JLex/current/README). 

You can check the value of `CLASSPATH` by typing `echo $CLASSPATH`. Make sure that the directory in which you compiled `javac Main.java` is in the CLASSPATH.

Install the latest version of [Cup](http://www2.cs.tum.edu/projects/cup/), the Java parser generator.

Now

    bnfc -m -java Calc.cf
    make
 
should result in producing a bunch of `.java` files as described on page 12 of the [slides](http://www.grammaticalframework.org/ipl-book/slides/2-slides-ipl-book.pdf).




   
