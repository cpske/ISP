### 1. Fill in the blanks with type annotations that would make objects on the right pass `mypy` type check

________str\_\_\_\_\_\_\_         1. `'\u005e\u005e'` or `'just a string'`  
______List\[A]\_\_\_\_\_\_       2. `[<__main__.A object at 0x000001A6C4F18610>, <__main__.A object at 0x000001A6C4F18C40>]`    
_List\[Union\[int, float]\_ 3. `[1, 2, 3, 4, 5]` or `[2.75, 5.5, 8.25]` or `[1, 2.]`  
____Dict\[str, int]\_\_\_\_    4. `{'one': 1, 'two': 2, 'three': 3}` but not `{'one': '1', 'two': '2'}`  
______Iterable\_\_\_\_\_        5. `<QuerySet []>` or `range()`  
__List\[Tuple\[int, int]]\_ 6. `[(0, 5), (5, 0), (5, 5)]`    
__Callable\[..., None]\_    7. `lambda x: None`  
___Callable\[[], str]\_\_\_   8. `lambda: 'some string'`


### 3. Add appropriate type hints to these code snippets
```python
from typing import *

# No.1
KT = TypeVar('KT')
VT = TypeVar('VT')

def swap_keys_and_values(dict_: Dict[KT, VT]) -> Dict[VT, KT]:
    """Returns a dict with swapped keys and values."""
    if not isinstance(dict_, dict):
        raise TypeError("'self' must be a dict")
    if len(set(dict_.values())) != len(dict_):
        raise ValueError("values aren't unique, can't swap keys and values")
    return {v: k for k, v in dict_.items()}

# No.2
T = TypeVar('T')

def remove_duplicate(iterable: Iterable[T]) -> List[T]:
    """Returns a list with no duplicates."""
    return list(set(iterable))

# No.3
def normalized(s: str, mode: str = 'NFKC') -> str:
    """Returns a NFKC normalized str."""
    import unicodedata
    return unicodedata.normalize(mode, s)

# No.4
def count_chars(s: str, normalize: bool = False) -> Dict[str, int]:
    """Returns a dict mapping from characters in ``s`` to their frequency."""
    d: Dict[str, int] = dict()
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
    lst = []
    pair = []
    for elem in iterable:
        pair.append(elem)
        if len(pair) == 2:
            temp = tuple(pair)
            temp = cast(Tuple[T, T], temp)
            lst.append(temp)
            pair.clear()
    assert len(pair) != 2, "somehow pair wasn't cleared"
    if len(pair) != 0:
        raise ValueError("iterable has a left-over element '{}'"
                         .format(pair[0]))
    return lst
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
