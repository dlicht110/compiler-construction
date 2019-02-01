# Why don't Java and Python have goto statements?

This discussion is motivated by the question of how to implement a specification such as the one from the [previous lecture](https://github.com/alexhkurz/compiler-construction/blob/master/abc.pdf).

In a language with labels and gotos, we can give a nice and direct translation of the picture. For example, in C++, the code translating the state labelled `q2` can be written as

    q2:
    READ_CHAR;
    switch (input) {
        case 'a': goto q2;
        case 'b': goto q3;
        default : goto q1;
    }

where `READ_CHAR' is a macro that assigns the current character to the variable `input`.

Languages such as Java and Python do not have `goto`. We will discuss later why.

Therefore, we need to use a more mathematical approach. Namely, to think of the specification as a function

$$transition : State \times Char \to State$$

For example, the above C++ code corresponds to the mathematical definition

\begin{align}
transition : State \times Char  & \to State\\ \hline
transition(q_2,a) &= q_2\\
transition(q_2,b) &= q_3\\
transition(q_2,x) &= q_1 & \textrm{if $x\notin\{a,b\}}\\
\end{align}

Such a function is easy to implement in Java or Python.

When you finished your assignment, we can compare different solutions and discuss which solution you would prefer.

## "Go To Statement Considered Harmful"

For the remainder of this lecture I want to present some of the history that lead to the prohibition of `goto` in many modern programmming language and discuss some of the advantages and disadvantages of using `goto`.

There is some ``prehistory'' about which you can find out more if you read the articles in the references. But the starting point of the debate is usually taken to be the article

[Edgar Dijkstra: "Go To Statement Considered Harmful" (1968)](https://homepages.cwi.nl/~storm/teaching/reader/Dijkstra68.pdf)

The title of the paper, chosen by the editor Niklaus Wirth, himself one of the important figures in the history of compilers, made history itself, see the Wikepedia entry on [Considered harmful](https://en.wikipedia.org/wiki/Considered_harmful) for a short history and further references.

The most famous quote from the article is probably the opening sentence

        For a number of years I have been familiar with the observation 
        that the quality of programmers is a decreasing function of 
        the density of **go to** statements in the programs they produce.

Today, of course, we need to ask why, at the time, in 1968, programs without `goto`s were the exception.

One reason for the use of `goto`s was that machine and assembley code relies on labels and jumps to implement everything from conditionals over loops to functions/procedures/methods. And while, by 1968, modern high level programming languages such as ALGOL had been developed in academia for a decade or so, the associated method of [structured programming](https://en.wikipedia.org/wiki/Structured_programming) had not yet made it into mainstream programming. [^structuredprogramming]

Another reason, which may be less important nowadays, is that `goto`s allow the programmer more control to write more efficient code.

Furthermore, at the time more than today, programs were visualised and specified by [flowcharts](https://en.wikipedia.org/wiki/Flowchart) and the obvious way to implement a flowchart is to use labels and `goto`s, much in the same way as we used them in the sketched C++ implementation of our specification above.

So what happened? Can flowcharts be implemented without `goto`s? (The theoretical question.) And would that actually improve readability? (The practical question, which is important: Remember that in programming [the reader is always right](https://vimeo.com/14313378#t=10m03s) [^yaronminsky])

The story of the theoretical question starts with  [Bohm and Jacopini: "Flow Diagrams, Turing Machines and Languages with Only Two Formation Rules" (1966)](http://www.cs.unibo.it/~martini/PP/bohm-jac.pdf) who showed that every flowchart can be implemented using if-then-else, sequential composition and while-loops. The paper gives a general method to translate every flowchart into a structured program without `goto`s. As it often happens, the most elegant theoretical results are not directly practical. In this case, the goto-free program obtained from the general method is not necessarily more readable than the one with goto's. 

**Activity:** To illustrate that eliminating goto's does not necessarily improve readability, think about how to replace labels with function definitions and goto's with function calls.

Nevertheless the theoretical result was hugely important as the knowledge that such a translation is possible in principle gave proponents of structured programming the confidence that they are on the right track. And, as history shows, they largely won the battle.

Nevertheless, we should not forget that readability, and sometimes efficiency, are more important than ideological principles. So while structured programming was certainly an important revolution, this does not imply that all uses of goto should be condemned on principle.

**Activity:** What "hidden" uses of goto's routinely show up in your own programming practice? So is legitimate to say that goto's have been eliminated?

## "Structured Programming with go to Statements"

**Activity:** Let us put the discussion to test with an example. How readable is the code below?

        for i = 1 to m  // m is the length of array A
            if A[i] = x then goto found
        i = m+1
        m = i
        A[i] = x
        B[i] = 0
        found: B[i] = B[i] + 1

Discuss whether you find your code without goto more readable than the one above.

 The example above, which emphasises readability, is from [Knuth, "Structured Programming with go to Statements" (1974)](https://pic.plover.com/knuth-GOTO.pdf). I highly recommend to read this very rich, and sometimes funny, article.

Apart from readability, we also hinted at efficiency.

The paper continues with a discussion on how to optimize loops that are executed millions of times. In such a situation even small improvements can be significant and Knuth shows that the flexibility offered by `goto`s can be valuable. Of course, today compilers are highly optimizing and it is a questions whether we should not just trust our compilers instead of trying to optimize ourselves.

[^structuredprogramming]: One of the important ideas of structured programming is that every block has a single entry and a single exit. The opposite extreme of "single-entry-single-exit" is aptly called "spaghetti code". Nevertheless, taken to the extreme "single-entry-single-exit" can decrease readability. What examples in your own programming practice violate the  single-entry-single-exit paradigm? Which `goto`-like statements are provided even in Java and Python?

[^yaronminsky]: There is lots of other good stuff in the video, eg the discussion about [exhaustion checks](https://vimeo.com/14313378#t=31m51s).

