---
title: Refactoring Guide
---

### Software Evolution

Software changes over time.  "Modern" development processes even increase
the amount of change.  Consider:

* *Iterative and incremental development* - software evolves (changes) as you add new features
* *Embrace Feedback and Changing Requirements* - this can cause change at the design level, too.
* *Software reuse* - components may need to change to be suitable for reuse.

Other factors causing change:

* *Software development is a learning process* - we find better designs and better implementations while doing.

## Common Refactorings

* *Replace magic number with a named constant*. This applies to strings and other types as well.
* *Rename a variable with a more informative name*. Short (one letter) names are OK for loop variables, but not much else.  Avoid abbreviations.
* *Introduce explanatory variable* - if you have a long expression used as part of a statement, consider breaking it apart and assigning it to an intermediate variable that explains what it is.
* *Eliminate Duplicate Code* - move it to a separate method, a superclass, or mixin.


## Refactoring Resources and References

* *Refactoring: Improving the Design of Existing Code* by Martin Fowler.  The original and most often recommended refactoring book.
* 
* **Chapter 24: Refactoring** in *Code Complete*
   has checklists for refactoring and describes common refactorings. Easy to read.

* [Code Smells Cheat Sheet](http://www.industriallogic.com/wp-content/uploads/2005/09/smellstorefactorings.pdf) at [Industrial Logic](https://www.industriallogic.com/blog/smells-to-refactorings-cheatsheet/). Summary and Refactoring (2 pages)
    - table of symptoms of poor code and suggested refactorings.
    > The symptoms of poor or hard-to-maintain code are sometimes called *code smells*.
    > I avoid this term because smell is subjective, and I want
    > refactoring guidelines to be objective.


