---
title: Refactoring
---

Related topic: [Separate Configuration from Code](separate-configuration)

**Refactoring** refers to modifying the structure of existing code to improve it,
without changing the functionality.

Some things we will cover:

* signs that code needs refactoring -- sometimes called "code smells", a term I *dislike*
* what does "improve code" mean?  Software principles provide objective guides.
* guide lines for when and how to refactor
  - code should be working before refactoring
  - you must have tests before refactoring
  - refactor is small steps and only one at a time 
  - test the result of each refactoring and commit it before doing the next refactoring
* common refactorings, with names
* refactoring Python and Java using an IDE. 
  - Eclipse, IntelliJ (aka PyCharm), and Netbeans provide good refactoring tools 
  - VS Code can perform some refactoring, but not as good as the IDE above

### Presentation Slides

[Intro to Refactoring](Refactoring.pdf)    
[Refactoring Signs and Patterns](Refactoring-Patterns.pdf)      

### Refactoring Signs and Symptoms

How to know when you should refactor code?
Good lists with description and examples, are:

* [Code smells](https://blog.codinghorror.com/code-smells/) at CodingHorror.com
* Chapter 3 of *Refactoring* by Martin Fowler
* [Chapter 24](/ISP/resources/Refactoring - Code Complete.pdf) of *Code Complete 2* by Steve McConnell has a long list
* [From Smells to Refactoring](smells-to-refactoring.pdf) a table mapping symptoms to suggested refactorings, but doesn't explain the refactorings.
  - useful and shows you which refactorings occur most often
  - some symptoms require some advanced coding knowledge

Common signs:

1. Duplicate code - same computation performed in multiple places
2. Long Method - is a method doing more than one thing?
3. Large Class - symptoms are a class with many instance variables, or many methods, esp. methods that don't seem essential to the class's primary responsibility
4. Long parameter list - a method with many parameters
5. Divergent Change - when you try to change one bit of functionality you have to change code in several different methods
6. A method uses members of another class more than the members of it's own class. (*Members* means attributes and methods.)
7. Complex expressions make it hard to understand purpose of code.
8. Switch statements - the code uses a "switch" or "if ... else if ... else if ..." to control variable based on the value of a variable, with one "case" or "if" per alternative. Consider replacing this with polymorphism.
9. "*Three strikes, refactor*" - if you find yourself writing (almost) the same thing 3 times, then refactor it.


### Refactoring Goals

The goal is to create "better" code with the same functionality as the original.  In most cases, the interface remains unchanged.

So, what is good code?

(If I wrote it here, it would be duplication, which is *poor* code. But to get you started ...)

1. High cohesion within a class or module.  

2. Good encapsulation with limited API. (Low coupling.) You can make changes to the implementation of one part without needing to change others.

3. Each piece of information is represented only once in code.

### Refactoring Exercises

1. [Pizzashop refactoring exercise](https://github.com/ISP19/pizzashop)     
2. [Movie Rental refactoring problem](https://github.com/jbrucker/movierental) from Martin Fowler's presentation and article
3. Read about refactoring (below) and create your own refactoring exercise for other students

### More about Refactoring

[JeremyBytes](http://www.jeremybytes.com/Demos.aspx) has material on refactoring as part of "Clean Code".

[Introduction to Refactoring](http://www.math.uaa.alaska.edu/~afkjm/csce401/handouts/refactoring.pdf) PDF has many refactorings with short Java examples -- easy to read.

[Refactoring Techniques](https://refactoring.guru/refactoring/techniques) lots of them

[Refactoring Guru](https://refactoring.guru/refactoring)

[Refactoring in IntelliJ](https://www.jetbrains.com/help/idea/tutorial-introduction-to-refactoring.html#5db90) explains how to do it in IntelliJ, with examples of common refactorings.
 
