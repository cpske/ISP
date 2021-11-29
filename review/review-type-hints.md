---
Title: Type Hints Review
---

1. Apply type hints to this function.  Add any required imports for your hints.

```python
import re


def split(expression):
    """Split a string into a list of words.

    The string argument is split at space and punctuation marks (,.?!;:).
    Example:
    >>> split("Water, water everywhere! But not a drop; to drink.")
    ['Water', 'water', 'everywhere', 'But', 'not', 'a', 'drop', 'to', 'drink']
    """
    result = re.split(r"[,.?!:;\s]+", expression)
    try:
        result.remove('')  # empty arg at start or end of list
        result.remove('')
    except ValueError:
        pass
    return result
```

2. Apply type hints to this function.  Add any required imports for your hints.

```python

def average(iter):
    """Return the average of any iterable source of numbers.

    >>> average( [2,5,20] )
    9.0
    >>> average( (0, -0.5, 8.0) )
    2.5
    """
    sum = 0
    count = 0
    for x in iter:
        sum += x
        count += 1
    return sum/max(1,count)
```

3. What happens when you run Python and it encounters a statement that **violates** a type hint, such as this:
   ```python
   def add(a: float, b: float):
       return a + b

   if __name__ == '__main__':
       result = add("hi"," there")   # usage conflicts with type hints
   ```
   - [ ] an error is raised and execution stops
   - [ ] an error is raised but Python continues to execute the code
   - [ ] a warning is printed but Python continues to execute the code
   - [ ] Python ignores type hints and executes the code


4. What are 2 reasons to use type hints?  Be **precise** in your answer.


