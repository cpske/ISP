---
title: Type Hinting –– an Introduction
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

- Improved **readability** for humans and computers
  * Improve code completion and refactoring in IDEs
- Acts as live **documentation**
  * Solves the problem of docstrings not being maintained
  * Docstrings don't allow complex types
- Reduce errors
  * Helps a lot in large projects

While Python is known for its _dynamic_ or "duck" typing (and some people will
argue against any form of enforced type checking), many (including the retired
BDFL Guido van Rossum) agree that _static type checking_ is still welcome (in the form of 
"gradual type hinting"). 

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

With these, IDEs and static type checkers like `mypy` can help you check for 
any type issues, before actual run-time.

In comparison with these bare bones functions below that you're not really sure
what it does, the above surely is an improvement without too much effort. 

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

(Many people agree that for small "obvious" functions, you don't really
need a detailed docstring. Type hints add just that moderate amount of detail
without needing too much description via docstrings)

### The typing module (PEP 484)

[**PEP 484**](https://www.python.org/dev/peps/pep-0484/) introduced the 
[`typing`](https://docs.python.org/3/library/typing.html) module, in Python 3.5
which allows for more complex types.

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

Some more examples:

```python
from typing import Optional, List

def get_even(list_: List[int]) -> Optional[List[int]]: ...
```

You and the IDE both know that `get_even()` can return both a `list`a
of `int` or a `None` (probably if there aren't any even numbers).

```python
from typing import Dict, Any

def parse_request_data(data: Dict[str, Any]) -> None: ...
```

This function only accepts data in the form of a `dict` with a `str` as the key.

```python
class Question:
    ...
    def get_voted_choices(self) -> models.QuerySet:
        """
        Returns an iterable that iterates over all choices of this
        question that has been voted.
        """
```

Any kind of `class` can be used.

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

* If `Scoreboard` returns an `Iterator` whose values are (say) `int`, you can improve type checking by specifying this using the notation `Iteratable[type]`:

```python
from typing import Iterable, Iterator

class Scoreboard(Iterable[int]):
   def __init__(self):
       self.data = range(0,10)

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


---
## Problems

To do these problems you need `mypy`. Install it using:
```bash
$ pip install mypy
```
then run it on your Python code:
```bash
$ mypy path/to/yourfile.py
```

### 1. Fill in the blanks with type annotations that would make objects on the right pass `mypy` type check
That is, `mypy` should not complain about anything.
```
x: <your answer> = <an object on the right>
```
no points for being too broad (if it's too broad, it doesn't help you with anything)

**Example:**

______int\_\_\_\_\_\_   0. `(3,)` or `(4,)`  ❌ # fails type check, no points  
_____object\_\_\_\_   0. `(3,)` or `(4,)`  ❌ # passes type check, but too broad, no points  
_____tuple\_\_\_\_\_   0. `(3,)` or `(4,)`  ⭕ # passes type check, but could be better, partial credits  
___Tuple\[int]\_\_\_ 0. `(3,)` or `(4,)`  ⭕ # passes type check, full points  

__________________   1. `'\u005e\u005e'` or `'just a string'`  
__________________   2. `[<__main__.A object at 0x000001A6C4F18610>, <__main__.A object at 0x000001A6C4F18C40>]`  
__________________   3. `[1, 2, 3, 4, 5]` or `[2.75, 5.5, 8.25]` or `[1, 2.]`  
__________________   4. `{'one': 1, 'two': 2, 'three': 3}` but not `{'one': '1', 'two': '2'}`  
__________________   5. `<QuerySet []>` or `range()`  
__________________   6. `[(0, 5), (5, 0), (5, 5)]`    
__________________   7. `lambda x: None`  
__________________   8. `lambda: 'some string'`

### 2. For each type annotation, give an example object that would pass `mypy` type check

**Example:**

&nbsp; 0. `Dict[str, Dict[str, Any]]`
```pythonstub
{'data': {'question_id': 34, 'choice_id': 132, 'error_msg': None}}
```

&nbsp; 1. `Iterable[Union[int, float]]`  

&nbsp; 2. `Sequence[Dict[str, float]]`

&nbsp; 3.  `Any`

&nbsp; 4.  `None`

&nbsp; 5.  `Dict[str, Optional[str]]`

&nbsp; 6.  `Literal['r', 'rt', 'w', 'wt']`

&nbsp; 7.  `N = TypeVar('Number', int, float); Tuple[N, N]`

&nbsp; 8.  `Mapping[float, int]`


### 3. Add appropriate type hints to these code snippets

There should be type hints for all function/method's parameters and return value.
Try to be forgiving for parameter types and specific for return type.

**Example:**
```python
from typing import Callable, Iterable, Iterator

# No.0
def my_map(a: Callable, b: Iterable) -> Iterator:
    return map(a, b)
```

**Problems:**
```python
from typing import *

# No.1
def swap_keys_and_values(dict_):
    """Returns a dict with swapped keys and values."""
    if not isinstance(dict_, dict):
        raise TypeError("'self' must be a dict")
    if len(set(dict_.values())) != len(dict_):
        raise ValueError("values aren't unique, can't swap keys and values")
    return {v: k for k, v in dict_.items()}

# No.2
def remove_duplicate(iterable):
    """Returns a list with no duplicates."""
    return list(set(iterable))

# No.3
def normalized(s):
    """Returns a NFKC normalized str."""
    import unicodedata
    return unicodedata.normalize('NFKC', s)

# No.4
def count_chars(s, normalize=False):
    """Returns a dict mapping from characters in ``s`` to their frequency."""
    d = dict()
    for c in s:
        if normalized:
            c = normalized(c)
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
```

### 4. Fill in the blanks in the code so that the `mypy` type check passes

**Example:**

```python
from typing import Any, Iterable, List, Tuple, TypeVar

# No.0
T = TypeVar('T')

def group_up(iterable: Iterable[T], n: int) -> List[Tuple[Any, ...]]:
    """Group up each consecutive element of the iterable given.

    Args:
        iterable (Iterable): The iterable to make pairs with
        n (int): The length of each group to make

    Returns:
        A new list of grouped up elements.

    Raises:
        ValueError: When ``iterable`` is not of length c x n, where c
            is an integer. (i.e. when there are left-over elements)
    """
    ##### code begins #####
    lst = []
    group = []
    for elem in iterable:
        group.append(elem)
        if len(group) == n:
            lst.append(tuple(group))
            group.clear()
    assert len(group) != n, "somehow group wasn't cleared"
    if len(group) != 0:
        raise ValueError("iterable has left-over elements '{}'"
                         .format(group))
    return lst
    #####  code ends  #####
```

```python
from typing import *

# No. 1
T = TypeVar('T')

def pair_up(iterable: Iterable[T]) -> List[Tuple[T, T]]:
    """Pairs up each consecutive element of the iterable given.

    Args:
        iterable (Iterable): The iterable to make pairs with

    Returns:
        A new list of paired up elements.

    Raises:
        ValueError: When ``iterable`` is not of length 2n, where n
            is an integer. (i.e. when there is a left-over element)
    """
    ##### code begins #####
    #####  code ends  #####

# No.2
def bar():
    ##### code begins #####
    #####  code ends  #####

# No.3
def bazz():
    ##### code begins #####
    #####  code ends  #####

# No.4
def buzz():
    ##### code begins #####
    #####  code ends  #####
```

