# Setting the PATH and CLASSPATH variables

## General considerations

- How do you organise your file structure? You probably want to keep data (such as `Calc.cf`) separeted from programs (such as `bnfc`) that you may want to execute on the data. (Why is it important to keep programs and data separated?)

- This entails the problem that if you want to execute `bnfc -m -haskell Calc.cf` you cannot be simultaneously in the directory that contains `bnfc` and `Calc.cf`.

- The solution is to put the executable `bnfc` "in your path". 

- Entering 

                echo $PATH
        
in your terminal shows the value of the variable `PATH`, that is, all the directories at which the operating system automatically looks for executables (binaries). If you want that an exectuable is automatically found when you type its name in the terminal, you need to make sure that the directory which contains the exectuable is in the path.

## Putting `bnfc` into the path

Either copy `bnfc` into a directory that is already in your path, or change `PATH` to contain `bnfc/source/dist/build/`. I added the line

        export PATH="~/github/bnfc/source/dist/build/bnfc:$PATH"
        
to my `.bash_profile` (because I installed `bnfc` into a directory called `github` in my home directory (`~` denotes the home directory)). <sup>[[2]](#hidden)</sup> 

More on how to change `PATH` can be found [here](https://www.computerhope.com/issues/ch001647.htm) or in many other places. 

Let me know if you have a favourite reference.

<a name="hidden">[2]</a>: Opening aIn a MacOS file dialogue you can see hidden files such as `.bash_profile` by simultaneously holding down the keys "command" and "shift" and "." Alternatively, use the terminal as, for example, in `open -a TextEdit .bash_profile` or `open -a Sublime\ Text\ 2 .bash_profile` or `open -a visual\ studio\ code TestCalc.hs` to open the `.bash_profile` (thanks to Dylan Davis).
