---
title: Refactoring
---

**Refactoring** refers to modifying the structure of existing code to improve it,
without changing the external functionality.

Things we will cover:

* Signs that code needs refactoring -- sometimes called "code smells", a term I *dislike*
* What does "improve code" mean?  Software principles provide objective guides.
* Guide lines for when and how to refactor:
  1. code should be working before refactoring
  2. you must have tests before refactoring
  3. refactor is small steps and only one at a time 
  4. don't add new functionality while you refactor
  5. test the result of each refactoring and commit it before doing the next refactoring
* Common refactorings, with names
* Refactoring Python or Java using an IDE
  - Eclipse, IntelliJ (aka PyCharm), and Netbeans provide good refactoring tools 
  - VS Code can perform some refactoring, but not as good as Eclipse & IntelliJ/PyCharm

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
* [Code Smells on Refactoring Guru](https://refactoring.guru/refactoring/smells) some descriptions seem vague to me

Common signs that code needs improvement:

1. Duplicate code - same computation performed in multiple places
2. Long Method - is a method doing more than one thing?
3. Large Class - symptoms are a class with many instance variables, or many methods, esp. methods that don't seem essential to the class's primary responsibility
4. Long parameter list - a method with many parameters
5. Divergent Change - when you try to change one bit of functionality you have to change code in several different methods
6. Feature Envy - A method uses members of another class more than the members of it's own class. (*Members* means attributes and methods.)
7. Complex expressions make it hard to understand purpose of code.
8. Switch statements - the code uses a "switch" or "if ... else if ... else if ..." to control what the code does based on the value of a variable. Consider replacing this with polymorphism.
9. Temporary Field - an attribute (field) is used to store some value as a way of sharing it between methods, or as an optional feature
10. "*Three strikes, refactor*" - if you find yourself writing (almost) the same thing 3 times, then refactor it.


### Refactoring Goals

The goal is to create "better" code with the same functionality as the original.  In most cases, the interface remains unchanged.

So, then...

### What is good code?

[How do you define "good code"](https://developerzen.com/how-do-you-define-good-code-c8a383c207a4) article. 

Readable - In *Code Complete*, **code readability** is emphasized throughout the book.  Reabability improves each of these aspects of a program:

- Ease of comprehension
- Reviewability
- Error rate
- Maintainability - can modify or extend
- Development time - a result of the above
- External quality - a result of the above

Characteristics of good code are (from Paul DiLascia of MSDN):

- Easy to Read
- Clarity - how easy can you understand the design, purpose, and function of the code?
  - Code may be "easy to read" but still be hard to understand how it functions or its design
  - As example, functions without side effects whose results depend only on the parameters are easier to understand
- Simplicity - code is concise, but not to the point of making it hard to read
- Modularity 
- Layering - internally the program structure appears to have layers. Lower layers provide services but don't know about higher layers, so dependencies are one-way. 
  - Not all applications can be designed using layers.
- Efficiency - your program is fast and economical in resource use. It doesn't hog files or connections, starts quickly, and doesn't try to do more than is required.

Another motivation for refactoring is:

> The fundamental challenge of programming is managing complexity.    
> Simplicity, readability, modularity, layering, design, efficiency, and elegance
> are all time-honored ways to achieve clarity, which is the antidote to complexity.

### Refactoring Exercises

1. [Pizzashop refactoring exercise](https://github.com/ISP19/pizzashop) 

2. [Movie Rental refactoring problem](https://github.com/jbrucker/movierental) from Martin Fowler's presentation and article

3. Read about refactoring (below) and create your own refactoring exercise for other students

### Refactoring and Design Patterns

The "goals" behind refactoring are often the same as the goals that motivate Design Patterns.

Many refactorings restructure code so that the code uses some design pattern.  

> In the Movie Rental problem, does the refactoring of the movie Price Code look like the *Strategy Pattern*?

Hence, it is helpful to know some Design Patterns. Especially the *context*, *forces*, and *applicability* of each pattern.


### Learn Refactoring

[How Do You Define "Good Code"?](https://developerzen.com/how-do-you-define-good-code-c8a383c207a4) article summarizes some guidance from *Code Complete* (famous book) and MSDN. 

[JeremyBytes](http://www.jeremybytes.com/Demos.aspx) has material on refactoring as part of "Clean Code".

[Introduction to Refactoring](http://www.math.uaa.alaska.edu/~afkjm/csce401/handouts/refactoring.pdf) PDF has many refactorings with short Java examples -- easy to read.

[Refactoring Guru](https://refactoring.guru/refactoring). In particular:
  - [Refactoring Techniques](https://refactoring.guru/refactoring/techniques) 
  - [Code Smells](https://refactoring.guru/refactoring/smells)

[Refactoring in IntelliJ](https://www.jetbrains.com/help/idea/tutorial-introduction-to-refactoring.html#5db90) explains how to do it in IntelliJ, with examples of common refactorings.
 

## Related Topics

* [Separate Configuration from Code](separate-configuration)
* [Design Patterns](https://skeoop.github.io/patterns/) some refactorings use a design pattern to restructure the code
