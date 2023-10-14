---
title: Refactoring
---

**Refactoring** refers to modifying the structure of existing code to improve it,
without changing the external functionality.

### Things we will cover

* Signs that code needs refactoring -- sometimes called "code smells", a term I *dislike*
* What does "good code" mean?  Software principles provide objective guides.
* When and how to refactor:
  1. code should be working before refactoring
  2. you must have tests before refactoring
  3. refactor is small steps and only one at a time 
  4. don't add new functionality while you refactor
  5. test the result of each refactoring and commit it before doing the next refactoring
* [Common refactorings](Refactoring-guide), with names
* Refactoring in Python or Java using an IDE
  - IDEs provide refactoring tools that make refactoring faster and eliminate errors
  - VS Code performs some refactoring, but not as good as Eclipse, IntelliJ, or PyCharm


### Presentation Slides

[Intro to Refactoring](Refactoring-Intro.pdf)    
[Refactoring Signs and Patterns](Refactoring-Signs-Patterns.pdf)      


### Refactoring Signs and Symptoms

How to know when you should refactor code?

**Common signs** that code needs improvement:

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

> A common name for these symptoms is "Code Smells".    
> I **really dislike** this term because "smell" is subjective -- we need objective criteria to identify things to refactor, not impressions.

Good lists of signs with description and examples, are:

* [Code Smells](https://refactoring.guru/refactoring/smells) on Refactoring Guru
* [Code smells](https://blog.codinghorror.com/code-smells/) article at CodingHorror.com
* Chapter 3 of *Refactoring* by Martin Fowler (a whole book on Refactoring!)
  - Chapter 3 refers to other parts of the book for how to do the refactoring
* [From Smells to Refactorings](smells-to-refactorings.pdf) table maps symptoms to suggested refactorings. Very popular "cheat sheet".
  - shows you which refactorings occur most often
* [Chapter 24](/ISP/resources/Refactoring-Code-Complete.pdf) of *Code Complete 2* by Steve McConnell has a long list of refactorings


### Refactoring Goals

The goal is to create "better" code with the same functionality as the original.  In most cases, the interface remains unchanged.

Another motivation for refactoring:

> The fundamental challenge of programming is managing complexity.    
> Simplicity, readability, modularity, layering, design, efficiency, and elegance are all time-honored ways to achieve clarity, which is the antidote to complexity.


### What is good code?

[How do you define "good code"](https://developerzen.com/how-do-you-define-good-code-c8a383c207a4) article. 

In *Code Complete*, Steve McConnel states the good code is maintainable. He memphasizes  **readable code** throughout the book.  

> *on readability...*    
> Communication with other people is the motivation behind the quest for ... self-documenting code.
>
> You write readable code because it helps other people read your code. Readability has a positive effect on all these aspects:
> - Comprehensibility (easy of comprehension)
> - Reviewability
> - Error rate
> - Debugging
> - Maintainability - can modify or extend over time
> - Development time - a result of the above
> - External quality - a result of the above

Characteristics of good code from Paul DiLascia of MSDN:

- **Simplicity** - code is concise, but not to the point of making it hard to read
- **Easy to Read**
- **Clarity** - how easy can you understand the design, purpose, and function of the code?
  - Code may be "easy to read" but still be hard to understand its function or design
  - For example, functions without side effects whose results depend only on the parameters are easier to understand
- **Modularity**
- **Layering** - program's internal structure appears to have layers that separate levels of abstraction or concerns. Lower layers provide services but don't know about higher layers, so dependencies are one-way. 
- **Efficiency** - a program is fast and economical in resource use. It doesn't hog files or connections, starts quickly, and doesn't try to do more than is required.

### Common Refactorings

[Refactoring Techniques](https://refactoring.guru/refactoring/techniques) lists refactorings grouped by technique, such as "*Composing Methods*" or "*Simplifying Conditional Expressions*"

[Common Refactorings](Refactoring-guide) an *incomplete* list of most common refactorings.

### Learn Refactoring

[Refactoring Guru](https://refactoring.guru/refactoring). In particular:
  - [Refactoring Techniques](https://refactoring.guru/refactoring/techniques) names of refactorings and how to do them
  - [Code Smells](https://refactoring.guru/refactoring/smells)

[Introduction to Refactoring](http://www.math.uaa.alaska.edu/~afkjm/csce401/handouts/refactoring.pdf) PDF has many short & easy to read examples. Code uses Java.

[Refactoring in IntelliJ](https://www.jetbrains.com/help/idea/tutorial-introduction-to-refactoring.html#5db90) explains how to do it in IntelliJ, with examples of common refactorings.


### Refactoring Exercises

1. [Pizzashop refactoring exercise](https://github.com/ISP19/pizzashop) 

2. [Movie Rental refactoring problem](https://github.com/jbrucker/movierental) from Martin Fowler's presentation and article


### Refactoring and Design Patterns

The "goals" behind refactoring are often the same as the goals that motivate Design Patterns.

Many refactorings restructure code so that the code uses some design pattern.  

> In the Movie Rental problem, does the refactoring of the movie Price Code look like the *Strategy Pattern*?

Hence, it is helpful to know some Design Patterns. Especially the *context*, *forces*, and *applicability* of each pattern.
 

## Related Topics

* [Separate Configuration from Code](separate-configuration)

* [Design Patterns](https://skeoop.github.io/patterns/) some refactorings use a design pattern to restructure the code
