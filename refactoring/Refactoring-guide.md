---
title: Common Refactorings
---

- *Replace magic number with a named constant*. This applies to strings and other types as well.

- *Rename a variable with a more informative name*. Short (one letter) names are OK for loop variables, but not much else.  Avoid abbreviations.

- *Introduce explanatory variable* - if you have a long expression used as part of a statement, consider breaking it apart and assigning it to an intermediate variable that explains what it is.

- *Eliminate Duplicate Code* - move it to a separate method, a superclass, or a mixin. Sometimes duplicate code is caused by some work being done by the wrong object.  For example, many views in "KU Polls" containing code to find a user's vote instead of a method in the Vote class to do that.

- *Eliminate Unnecessary "else"*.  When the "then" part of an "if" statements causes a return from a function or method, you do not need the following "else".  The same applies to "try - except" blocks in Python.
  ```python
  # in a Person class
  def __eq__(self, other) -> bool:
      if not isinstance(other, self.__class__):
          return False
      else:    <-- NOT NEEDED. REMOVE IT.
          return self.name == other.name and self.id == other.id
   ```

- *Move Method* - if a method is using data or other methods from another class (not a superclass) more than its own class, it probably should be moved to the other class. This is the *Information Expert* principle.

- *Extract Method* - if a method is long or appears to be doing more than one thing, try to extract a coherent block of code to another method. This may also improve your ability to test the code.
