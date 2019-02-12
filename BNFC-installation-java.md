# BNFC and Java

The IPL book is written with Haskell and Java in mind. BNFC also supports other programming languages. For example

    bnfc -m -c       FILE.cf      # to generate C
    bnfc -m -cpp FILE.cf      # to generate C++
    bnfc -m -java FILE.cf      # to generate Java
    bnfc -m -haskell FILE.cf      # to generate Haskell
    
should all work. For Haskell, see the previous lecture. Here we will look at how to get the 
Java part of the [BNFC tutorial](http://bnfc.digitalgrammars.com/tutorial/bnfc-tutorial.html) to work.

First, we need to install the latest version of the Java lexer and parser. It is necessary to change the CLASSPATH variable so that
it knows the location of the JLex and Cup. In my case I added to my `.bash_profile`

    export CLASSPATH=$CLASSPATH:.:/usr/local/bin/java/:/usr/local/bin/java/Cup:/usr/local/bin/java/JLex

Install [JLex](http://www.cs.princeton.edu/~appel/modern/java/JLex/) by following the instructions in the readme file.

Install [Cup](http://www2.cs.tum.edu/projects/cup/), the Java parser generator.





   
