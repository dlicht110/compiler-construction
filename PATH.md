Entering `echo $PATH` in your terminal shows the value of the variable `PATH`, that is, 
all the directories at which the operating system automatically looks for executables (binaries). 
Either copy `bnfc` into a directory in your path, or change `PATH` to contain `bnfc/source/dist/build/`. I added the line

        export PATH="~/github/bnfc/source/dist/build/bnfc:$PATH"
        
to my `.bash_profile` (because I installed `bnfc` into a directory called `github` in my home directory (`~` denotes the home directory)). More on how to change `PATH` can be found [here](https://www.computerhope.com/issues/ch001647.htm) or in many other places. <sup>[[2]](#hidden)</sup> Let me know if you have a favourite reference.

<a name="hidden">[2]</a>: In a MacOS file dialogue you can see hidden files such as `.bash_profile` by simultaneously holding down the keys "command" and "shift" and "." Alternatively, use the terminal as, for example, in `open -a TextEdit .bash_profile` or `open -a Sublime\ Text\ 2 .bash_profile` or `open -a visual\ studio\ code TestCalc.hs` to open the `.bash_profile` (thanks to Dylan Davis).
