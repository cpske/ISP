---
title: Type Hinting –– An Introduction
---

by Mai Norapong

Contents:

- [Motivations for using type hints](#motivations-for-using-type-hints)
- [Ways to type hint](#ways-to-type-hint)
  - [Function annotations (PEP 3107)](#function-annotations-pep-3107)
  - [The typing module (PEP 484)](#the-typing-module-pep-484)
  - [Variable annotations (PEP 526)](#variable-annotations-pep-526)
  - [Summary](#summary)
- [Question / Problem / Task](#question--problem--task)

## Motivations for using type hints

- Improve **readability** for humans and computers
  * Better code completion and refactoring in IDEs
- Acts as live **documentation**
  * Solves the problem of docstrings not being maintained
  * Docstrings don't allow complex types
- Reduce errors
  * Helps a lot in large projects

While Python is known for _dynamic_ or "duck" typing (and some people will
argue against any form of enforced type checking), many (including the retired
BDFL Guido van Rossum) agree that _static type checking_ is still welcome in the form of "gradual type hinting". 

## Ways to type hint

### Function annotations (PEP 3107)

Function annotations were introduced in [**PEP 3107**](https://www.python.org/dev/peps/pep-3107/)
and is available from Python 3.0 onwards.
The PEP allows for this syntax

```python
def foo(a: expression, b: expression = default_value):
    ...
def bar(*args: expression, **kwargs: expression):
    ...
def bazz() -> expression:
    ...
```

This results in a `dict` mapping from parameter names to the Python _expression_; 
the return value is denoted by the key `'return'`. The expression is evaluated
during function definition.

This `dict` can be accessed via a _dunder_ attribute `.__annotations__` which 
doesn't have any effect on the program on its own.

[**PEP 3107**](https://www.python.org/dev/peps/pep-3107/) 
allows for any valid python expression to be there including any `str`, 
`int`, or whatever, but in current practice, we put classes in there.

```python
def catch_all(*args, **kwargs) -> None:
    return

def double_string(s: str, sep: str = '') -> str:
    return f'{s}{sep}{s}'

def my_abs(x: int) -> int:
    if x < 0:
        x = -x
    return x
```

```
>>> catch_all.__annotations__
{'return': None}
>>> double_string.__annotations__
{'string': <class 'str'>, 'return': <class 'str'>}
>>> my_abs.__annotations__
{'x': <class 'int'>, 'return': <class 'int'>}
```

Using these, IDEs and static type checkers like `mypy` can help you check for 
type issues before actual run-time.

In comparison with the bare bones functions below, that you're not really sure
what the function does, the above surely is an improvement without too much effort. 

```python
def catch_all(*args, **kwargs):
    return

def double_string(s, sep):
    return f'{s}{sep}{s}'

def my_abs(x):
    if x < 0:
        x = -x
    return x
```

Many people agree that for small "obvious" functions, you don't really
need a detailed docstring. Type hints add just that moderate amount of detail
without needing too much description via docstrings.

### The typing module (PEP 484)

The [`typing`](https://docs.python.org/3/library/typing.html) module
introduced by [**PEP 484**](https://www.python.org/dev/peps/pep-0484/) 
(added in Python 3.5)
provides "hints" for more complex types.

Let's see it in action.

```python
from typing import Any, Union

Number = Union[int, float, complex]

def catch_all(*args: Any, **kwargs: Any) -> None: ...

def double_string(string: str, sep: str = '') -> str: ...

def my_abs(x: Number) -> Number: ...
```

With `Union`, you can now call `my_abs()` with any numbers and the IDE or `mypy`
won't yell at you.

Types for collections such as List, Set, Dict:

```python
from typing import List

def get_even(list_: List[int]) -> List[int]:
    ...
```

this means that `get_even()` accepts a list of `int` values and returns such
a list, too.
of `int` or a `None` (probably if there aren't any even numbers).

A dictionary where keys are strings, and values can be any type:

```python
from typing import Dict, Any

def parse_request_data(data: Dict[str, Any]) -> None: ...
```

A function that may return an int or may not return anything!

```python
from typing import Optional, List

def index_of(value: str, lst: List[str]) -> Optional[int]:
    ...
```

You can use application classes as type hints, too:

```python
class Question:
    ...
    def get_voted_choices(self) -> models.QuerySet:
        """
        Returns an iterable that iterates over all choices of this
        question that has been voted.
        """
```


Some other useful ones I've used:

- All the standard type extensions: `List`, `Tuple`, `Set`, etc.
- `Iterable` when I only require a function / method's input to be an iterable
  (that is, I can use a for loop with it at least once)
- `Callable` when you're making higher level functions or using a function somewhere
- ...

See the [`typing`](https://docs.python.org/3/library/typing.html) module for more details.

### Variable annotations (PEP 526)

[**PEP 526**](https://www.python.org/dev/peps/pep-0526/) introduces a new syntax
for defining variables available from Python 3.6 onwards.

```bnf
annotated_assignment_stmt ::=  augtarget ":" expression ["=" expression]
```

Don't worry if you don't understand what this means. This is in an Extended 
[Backus-Naur Form](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form), a 
modified version of BNF used by [Python](https://docs.python.org/3.7/reference/introduction.html#notation).

What that means is basically that you can now do this

```python
x: int = 5
```

or just this

```python
x: int
```

It might not look very useful cause many of the time that's pretty obvious and
static type checkers and IDE can figure these things out pretty easily. But in
some cases: 

```python
rating_str: str = soup.find(**{'class': 'wpb_wrapper'}).find(string='Rating').parent.find('span').string
```

The IDE already lost track of what the types are after the first few calls. (And
probably also whoever is reading your code.) By adding type hints to the variable
IDE regains knowledge of what type each variable in the call chain is, so it can
now do code completion for you again, and whoever reads your code can now be a 
little bit happier.


### Type hints for Classes

You can use type hints to convey the meaning "*this class provides a behavior*".
In Java or C-sharp this would be "*implements an interface*".

* A class named `Scoreboard` has an `__iter__` method that can be used to create an iterator, or as the data source in a `for x in data` statement.

```python
from typing import Iterable, Iterator

class Scoreboard(Iterable):
   ...

   def __iter__(self) -> Iterator:
      """This method should return an Iterator.
         Code that wants an iterator will call iter(obj)
         to create one.
      """
      pass
```

* If `Scoreboard` returns an `Iterator` whose values are always `int`, you can improve type checking by specifying this using the notation `Iteratable[type]`:

```python
from typing import Iterable, Iterator, List

class Scoreboard(Iterable[int]):
   def __init__(self):
       self.data: List[int] = []

   def __iter__(self) -> Iterator[int]:
      """This method should return an Iterator.
         Code that wants an iterator will call iter(obj)
         to create one.
      """
      # create an iterator from a range
      return iter(self.data)
```

In Java, we would do this by writing:
```java
class Scoreboard implement Iterator<Integer>
```

* A class has a `__len__` method that returns the "length" or "size" of the object. In Python code, this means you can write `len(obj)`.  The `typing` package defines a `Sized` type for this:

```
from typing import Sized

class CourseList(Sized):
    """List of courses taken by a student"""

    def __init__(self, student_id):
        self.student_id = student_id
        self.courses = []

    def add_course(self, course: Course):
        self.courses.append(course)

    def __len__(self):
        return len(self.courses)
```

### Summary

You can annotate variables, parameters, and the return value of functions. You can annotate classes to indicate behavior they provide (like Java interfaces).
You can also define your own generic classes with the aid of the `typing` 
module, for annotating more complex types.

All of these require Python 3.
Some type hinting is possible in Python 2 (now obsolete) using type comments and stub files (the `.pyi` files you sometimes see).
Type hinting for C libraries is also done using stub files. 

> **Note:** some corporations (like Dropbox) uses Python 3.5 so variable 
> annotations would not be available in those cases (But in the specific case of
> Dropbox, they don't really use the distributed version of Python so I'm not 
> 100% sure if it's available or not—though they do like `mypy`, but just aware 
> of compatibility issues if that's a concern.)


## References

A good place to start is the first reference.

[Python `typing` Package](https://docs.python.org/3/library/typing.html) - the type hints you can use to designate Python types   
[Python Collection Base Classes](https://docs.python.org/3/library/collections.abc.html) in the package `collections.abc`.
* Names of collections and the key methods they provide
* "abc" means Abstract Base Class
[Type Hints - Guido van Rossum](https://www.youtube.com/watch?v=2wDvzy6Hgxg) video by the inventor of Python, who recommends type hints and explains why (PyCon 2015). Highly recommended.   
[Mai's Slides on Python Typing](https://docs.google.com/presentation/d/1zoazXU6r4XZhYgjxGkpdDLirccB9TZg9mN40bW-0D6M/edit) on Google Drive.

[PEP 484](https://www.python.org/dev/peps/pep-0484/) the Typing module    
[PEP 526](https://www.python.org/dev/peps/pep-0526/) annotations for variables    
[PEP 3107](https://www.python.org/dev/peps/pep-3107/)    

