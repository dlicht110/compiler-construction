# compiler-construction
Notes and Materials for a course on Compiler Construction Spring 2019 at Chapman University

(under construction, read at your own risk :-) )

Organisation:

- We will follow the book [Implementing Programming Languages](http://www.grammaticalframework.org/ipl-book/) by [Aarne Ranta](http://www.cse.chalmers.se/~aarne/). Currently, the plan is to work through Chapters 2 - 6, which are available [online](http://www.cse.chalmers.se/edu/year/2012/course/DAT150/lectures/plt-book.pdf).  There is also a [list or errata](https://github.com/andreasabel/plt-errata). 

- Join the [Google group for the course](https://groups.google.com/forum/#!forum/chapman-compiler-construction-2019) by following the link and selecting "Apply for membership". Use the group for questions and discussions relating to the course. 

- Assignments are solved in groups of up to three students. I do not recommend working on your own as the assignments involve substantial work. 

- Create a private github repository in which you will maintain the solutions to the assignments. Do not share your code and the work on your assignments with students not in your group. As all groups do the same assignments, sharing code between groups consitutes plagriarim.

- **Plagiarism:** While discussing the assignments in the Google group and sharing ideas is perfectly fine, passing on code to students of another group is plagiarism. If you use code from other sources you need to highlight these sources when you submit your work and also in comments in the code itself. 

- There are many excellent reference to automata and language theory, the best known of which is "Introduction to Automata Theory, Languages, and Computation" by Hopcroft and Ullman (older second hand editions are fine, I studied from that book in 1990 and even that edition contains much more than we need). I list here some online tutorials and lecture notes which may be helpful.
  - [Introduction to Automata Theory, Languages, and Computation by Hopcroft, Motwani, Ullman]( https://mcdtu.files.wordpress.com/2017/03/introduction-to-automata-theory.pdf) Parts of Chapter 2 - 5  
  - [Introduction To The Theory Of Computation by Michael Sipser]( http://fuuu.be/polytech/INFOF408/Introduction-To-The-Theory-Of-Computation-Michael-Sipser.pdf)  Chapter 1 and part of Chapter 2  
  - [Lecture Notes on Regular Languages and Finite Automata by Marcelo Fiore](https://www.cl.cam.ac.uk/teaching/1011/RLFA/LectureNotes.pdf)  
  - [Introduction to Theory of Computation by Anil Maheshwari and Michiel Smid](https://cglab.ca/~michiel/TheoryOfComputation/TheoryOfComputation.pdf)
  - [Introduction to Languages and The Theory of Computation by John Martin](http://techmela.ucoz.com/_ld/0/22_Introduction_to.pdf)
  - [MIT Open Courseware](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-045j-automata-computability-and-complexity-spring-2011/lecture-notes/)
  - [Brian Harvey's notes](https://people.eecs.berkeley.edu/~bh/pdf/v3ch01.pdf)
 
  
Assessment:

- 54% of the course: 5 Assignments, first is worth 10%, the others 11%. (As this is the first time I run this course, there is a small chance that the plan will have to be changed, eg in case we go through the material slower than expected ... it is certainly a good idea to get a good start on the first assignments.) To pass an assignment programs need to run and test. I also may ask you to explain your solutions to me during office hours. Each assignment is graded either as pass (full marks) or fail (no marks). The criterion for passing is whether the program performs correctly according to the given specification.
  - Assignment 0 (not assessed): [Let me know](mailto:akurz@chapman.edu) the group you are in. Deadline Wed Jan 30 (11:59 pm PST).
  - Assignment 1: Warm up. Tba on Wed. Deadline Wed Feb 6 (11:59 pm PST). 
  - Assignment 2: [Grammar and Parser for C++](http://www.grammaticalframework.org/ipl-book/assignments/assignment1/assignment1.html). Deadline tba
  - Assignment 3: [Type Checker for CPP](http://www.grammaticalframework.org/ipl-book/assignments/assignment2/assignment2.html).  Deadline  tba  
  - Assignment 4: [Interpreter for CPP](http://www.grammaticalframework.org/ipl-book/assignments/assignment3/assignment3.html).  Deadline  tba  
  - Assignment 5: [Code Generator for CPP](http://www.grammaticalframework.org/ipl-book/assignments/assignment4/assignment4.html).  Deadline  tba  

- 46% of the course on theoretical aspects such as automata, grammars, type inference, etc: 
  - 4 quizzes/tests worth 4% each. Each test will roughly cover a quarter of the material relevant for the final exam.
  - Final exam worth 30%. The final exam will cover the same material as the tests.

Further reading:

- For general reading and background consider "Structure and Interpretation 
of Computer Programs" by Abelson and Sussman, which is available as [pdf](https://web.mit.edu/alexmv/6.037/sicp.pdf) or on the [web](http://mitpress.mit.edu/sites/default/files/sicp/full-text/book/book-Z-H-1.html#titlepage).

- Some texts on Compiler Construction available online are by
  - [Torben Mogensen](http://hjemmesider.diku.dk/~torbenm/Basics/) 2000/2010
  - [Niklaus Wirth](http://www.ethoberon.ethz.ch/WirthPubl/CBEAll.pdf), 1996/2005
  - [Waite and Goos](https://www.cs.cmu.edu/~aplatzer/course/Compilers/waitegoos.pdf), 1984/1996
  - ...

One of the main skills you will learn in this course is parsing. It is not only one of the essential (and difficult) parts in compiler construction but also appears in many other contexts such as (this is just a list of links I found interesting at the time of writing, I am not trying to be complete or rank by importance or authority):
- [natural language processing](https://nlp.stanford.edu/software/lex-parser.shtml)
- [translating between languages](https://www.grammaticalframework.org/)
- [cognitive science and psycholinguistics](https://dl.acm.org/ft_gateway.cfm?id=1697283&ftid=740323&dwn=1&CFID=46563369&CFTOKEN=6c231f65c04a5d4b-BEC94DA1-0566-3330-88B6AA7DA1DCC514), see also [Jakub Szymanik](http://www.jakubszymanik.com/)
- [geology](https://pubs.usgs.gov/ds/2006/146/htmldocs/process.htm)
- [knitting](http://alliejon.es/blog/2014/03/24/adding-syntax-highlighting-to-knitting-patterns/)
- [music](https://link.springer.com/chapter/10.1007%2F3-540-45722-4_3)
- ...

In particular the latter links point to parsing and automata theory being a general tool for pattern matching and pattern recognition.
