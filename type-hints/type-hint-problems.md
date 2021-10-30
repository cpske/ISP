---
title: Type Hinting Problems
---

Questions by Mai Norapong, from his [Type Hints Introdoction](introduction).


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

`______int______`   0. `(3,)` or `(4,)`  ❌ # fails type check, no points  
`_____object____`   0. `(3,)` or `(4,)`  ❌ # passes type check, but too broad, no points  
`_____tuple_____`   0. `(3,)` or `(4,)`  ⭕ # passes type check, but could be better, partial credits  
`___Tuple[int]___` 0. `(3,)` or `(4,)`  ⭕ # passes type check, full points  

`________________`   1. `'\u005e\u005e'` or `'just a string'`  
`________________`   2. `[<__main__.A object at 0x000001A6C4F18610>, <__main__.A object at 0x000001A6C4F18C40>]`  
`________________`   3. `[1, 2, 3, 4, 5]` or `[2.75, 5.5, 8.25]` or `[1, 2.]`  
`________________`   4. `{'one': 1, 'two': 2, 'three': 3}` but not `{'one': '1', 'two': '2'}`  
`________________`   5. `<QuerySet []>` or `range()`  
`________________`   6. `[(0, 5), (5, 0), (5, 5)]`    
`________________`   7. `lambda x: None`  
`________________`   8. `lambda: 'some string'`

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

