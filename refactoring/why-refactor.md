---
title: Why Refactor?
---

We have studied several refactorings, including their:

* name
* situation refactoring applies to
* benefit
* how to do it

This reviews focuses on **why** and identifying which refactorings 
can help achieve a specific objective.

```
Extract Method       | less code duplication
                     | reuse code
                     | easier to test
                     | isolate dependencies

Extract Variable     | simplify an expression
                     | reuse an intermediate result
                     | explain the meaning of complex expression

Remove Assignment    | each variable represents only one thing
to Parameters        | enables extraction of parts of the method

Move Method          | increase cohesion
                     | reduce coupling

Move Field           | increase cohesion
                     | reduce coupling

Extract Class        | make a class's methods more focused on one responsibility
                     | enable code reuse (on the extracted parts)

Hide Delegate        | improve code clarity
                     | enable polymorphism
```


## Why 'Move Field'?

'Move Field' means to move an attribute from one class to a different class.

Why? The field is primarily used by a different class.

Give an example from MovieRental.


## What are the benefits of single responsibility classes?

A class that focuses on a specific responsbility is easier to change.
It's also more likely to be reused.

## What refactorings help reduce a class's methods?

1. Move method
2. Extract class
3. Extract superclass
4. Delegate - related to "extract class"
