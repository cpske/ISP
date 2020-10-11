---
title: Tips from Practice of an Agile Developer
---

1. Which Tip explains why you should not grab solutions from StackOverflow and put them in your code?

2. In Tip 2, what can a development team do to avoid code full of quick fixes?





## Tip 2. Quick Fixes Become Quicksand

*Aka: don't fall for the quick fix*

Consequences of quick fixes are

* clarity of code goes down. It's hard to see *why* the code should be the way it is.
* code becomes hard to modify

What are two solutions to this?

* practice collective ownership. Read the code that others commit (code reviews).
* unit testing (See Tip 19, *Put Angels on Your Shoulders*)

## Tip 8. Question Until You Understand

Repeatedly asking "why" something occurs or why it's done a certain way
can uncover the underlying true reason.

Asking "why" an implemention does not work as intended can also
uncover the root cause, as opposed the apparent cause of the problem.

## Tip 25. Program Intently and Expressively

Write code in a way that shows your intent, including
use of good names.

Make expressive use of the language.

```
assertIs(question.published_recently(), True)
# or
assertTrue(question.published_recently())
```

guessing-game/game.py


## Tip 26. Communicate in Code

Use comments as documentation for how to use the method.
What can you document?
* what the function does
* preconditions (requirements)
* parameters
* returns
* exceptions raised
* post-conditions (promises)

In code, use ordinary comments to explain why.

## Tip 28. Code in Increments

Code, test, break, review.

Take time to "zoom out".

Look for small ways to improve code. Refactor both code and tests.

## Tip 30. Write Cohesive Code

Applies to classes, components, and packages or releases.

A class containing lots of code for many different functions
will need to change more often, and less likely to be reusable.

"Keep classes focused and components small."
