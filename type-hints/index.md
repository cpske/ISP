---
title: Type Hints
---

Python is a dynamically typed language.  This makes it easy to write code,
but harder to verify that the code is being used correctly.
Programming tools (and programmers!) have difficulty checking that
methods are being called with the correct type of values,
and that the returned values are used correctly.
Mistakes are often discovered only when the code is executed, 
and sometimes not discovered at all -- but the results are wrong.

### Example

[scorecard.py](scorecard.py) contains 3 syntax or semantic errors.
If you open this file in an IDE does it detect all three errors?
Probably not.  If this code was written a statically typed language
like Java, *any* IDE would immediately detect all the errors.

## Type Hints

Python allows you to write **type hints** in code to indicate data types.
The type hints are optional and ignored by the Python interpretter,
but IDEs and tools like `mypy` use type hints to detect errors.

In the [scorecard](scorecard.py) example, you can add a hint to
the `add_score` method to indicate that the `score` parameter 
must be a `float` (or int) and the method does not return anything:

```python
def add_score(self, score: float) -> None:
```

After you add this type hint, your IDE may detect that the "main" block
is calling `add_score` incorrectly.


## Learn Type Hints

[Mai's Introduction to Type Hints](introduction)

[Python Type Checking Guide](https://realpython.com/python-type-checking/) on RealPython

[typing package doc page](https://docs.python.org/3/library/typing.html)

To understand the type hints for collections and "interface" behavior on classes, you should read the [collections.abc doc page](https://docs.python.org/3/library/collections.abc.html). Each of the types in collections.abc has a corresponding type with the same name in the `typing` package -- use `typing` in your type hints, not `collections.abc`.

For example, if the Scorecard class is a collection of scores with a length and you can iterate over the scores, you can write:

```python
from typing import Iterable, Sized

class Scorecard(Iterable[float], Sized):

    def __len__(self):   # method required by Sized type

    def __iter__(self):  # method required by Iterable type
```

### Type Checking Tools

[mypy](http://mypy-lang.org/) is the most popular type checking tool for Python.  It can be used by itself or integrated into some IDE.
- [Getting Started](https://mypy.readthedocs.io/en/stable/getting_started.html) page contains many simple examples you can learn from.  
- For details on how to use specific type hints, see the index (left hand side) on the [docs](https://mypy.readthedocs.io/en/stable/) page.

[Pycharm](https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html) uses both type inference and type hints to check type usage. It's enabled by default but you can customize it, just like everything in Pycharm.

[Pydev](https://www.pydev.org/) uses type hints to warn of type misuse.

The VS Code [Pyright](https://github.com/microsoft/pyright) extension provides static type checking for VS Code.  Pyright checks usage across all files in a project, which *should* provide better type checking than mypy. So, you shouldn't need mypy. 


### Pylint

[Pylint](https://www.pylint.org/) checks for many kinds of errors in code, including semantic and syntax errors, and coding style violations.  Pylint checks if "interfaces" are truly implemented.  So if you write `class Foo(Sized)` it will check that the class contains a `__len__(self)` method.

Pylint give your code a score of 0 - 10, that adds some incentive and fun to correcting problems in code.

Pylint partially overlaps with mypy, but mypy does more type checking.
