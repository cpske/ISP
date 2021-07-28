---
title: Documentation in Comments
---

Java, Python, Scala, and other languages have standards for documenting
code in comments.  Java and Scala have tools to create nicely formatted
API documentation can from these comments, called "Javadoc" or "Scaladoc".

Almost all reusable code for Java and Scala provide a complete 
API reference in this way.  Here are some examples:

* Java API 
* JUnit API

Python has a standand format for writing documentation in comments
called "docstrings".  You should use it.

Java has a standard called "Javadoc" which is *much better* than Python
and can generate beautiful, cross-referenced HTML pages.  
The entire Java API docs are created using Javadoc.


## Python Docstring Comments

Documentation comments in Python are called **docstring** comments.

Here's an example for a function using Pyton's official PEP257 style:
```python
def max(a, b):
    """Return the maximum of two values a and b.

    Parameters:
    a (int): first number for max comparison
    b (int): second number for max comparison

    Returns:
    int: the max of a and b
    """
    if a > b: 
       return a
    return b
```

1. The docstring for a function must be the **first thing** inside the function
and use a multi-line comment (""").  Same rule for class docstrings.
2. The first line of the docstring is a **complete sentence** describing what it does, ending with a period.
3. Followed by a blank line.
4. (Optional) Additional text describing what the function or class does.  You can omit this if the function is simple (like min or max).
5. Document *parameters*, their names, what the mean, any conditions on their values, e.g. "must be positive", "may not be empty").
   - ISP Style: Don't document the data type!  Use **type hints** instead. E.g. write `a` instead of `a (int)`.
6. Document what the function returns (*return value*), and any *Exceptions* raised.

The standard for documenting parameters, returns, and exceptions is not universal.    
There are 3 styles:

* Pydoc style, used in Python API (PEP257)
* Google style
* Numpy style, which uses reStructured Text (reST) mark-up

Here's an example using Google's convention:
```python
def max(a, b):
    """Return the maximum of two values a and b.

    Args:
        a (int), b (int): two numbers to find the maximum of

    Returns:
        int: the max of a and b

    Raises:
        TypeError: if a or b is not a number
    """
    if not isinstance(a, Number): raise TypeError()
    if not isinstance(b, Number): raise TypeError()
    if a > b: 
        return a
    return b
```

## Use Type Hints instead of Data Types in Comments

The Google and PEP257 standards document the *data type* of parameters in the comment.
It is more useful to write the types as **Type Hints** and omit the type from docstring comments.  Avoid redundancy and inconsistency!

The `max` function works with either int or float, so instead of 'int' we can use Number
for the type hints:

```python
from numbers import Number

def max(a: Number, b: Number) -> Number:
    """Return the maximum of two values a and b.

    Args:
        a, b: two numbers to find the maximum of

    Returns:
        the maximum of a and b
    """
    if a > b: 
       return a
    return b
```
Notice the docstring does **not** include data type of Args and Returns (*avoid redundancy*).


## Module and Class Comments

PEP257 recommends

* File begins with a module comment
* Classes have a comment describing the class and it's members.
* OK to omit "protected" members from comments

```python
"""A bank account that performs deposits and withdrawals."""
from re import split

from money import Money


class BankAccount:
    """The first line is a sentence describing bank account.

    Then a longer description of a bank account and its methods.
    """

    def __init__(self, name, min_balance=0):
    """Create a new bank account with an owner and initial balance of zero.

    Parameters:
    name (str): name of the account
    min_balance (float):  minimum required balance, default is 0.
    """
```

### My Recommendation for Class Docstrings

1. Document what the class does, not *how* it does it. Describe any special dependencies or preconditions on using the class.
2. Give an example of how to create objects of the class.
3. Document attributes of the class.
4. **Don't** write a summary of all the methods in th class. That's redundant!  Each method should have it's own docstring.


## Viewing Python docstrings

You can view the docstring comment in the Python interpreter.
This works for functions, classes, modules, and packages (if they have a docstring): 
```python
>>> help(print)
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    ...
>>> import re    # 're' is the incredibly useful regular expression module
>>> help(re)
```

Here's an example class docstring from the popular `requests` library,
an add-on package for performing HTTP requests.

```python
>>> import requests
>>> help(requests.Request)

class Request(RequestHooksMixin)
    A user-created :class:`Request <Request>` object.
    
    Used to prepare a :class:`PreparedRequest <PreparedRequest>`, which is sent to the server.
    
    :param method: HTTP method to use.
    :param url: URL to send.
    :param headers: dictionary of headers to send.
    :param files: dictionary of {filename: fileobject} files to multipart upload.
  Usage::
    >>> import requests
    >>> req = requests.Request('GET', 'https://httpbin.org/get')
```

This docstring uses colons (:) for parameters and keywords used in formatting.
This is the numpy style docstring.
Please don't use this format in ISP -- it's harder to read.


## Use pydoc to view docstrings

Use `pydoc` from the command line to view documentation for packages, classes, modules, and functions:

```shell
cmd> pydoc os
   (shows docs for os module)
cmd> pydoc math.sqrt
   (shows doc for sqrt function)
```

## When to Write Docstrings

You should write docstring comments for:

* **Classes**
  - describes purpose of the class
  - parameters of the constructor
  - public methods
  - example of using the class

* **Functions and methods**
  - describe purpose of the function or method
  - parameters, and restrictions on their values
  - the return value, if any
  - exceptions that may be raised

* **Modules**
  - describe purpose of the module
  - module docstrings go at top of the file, before imports

* **Packages** (for this course, package docstrings are not required)
  - put package docstrings in the package's `___init__.py` file.
  - purpose of the package
  - list the modules and subpackages (this can become out-of-date! Python should do this automatically)


## Python Doctest Comments

Doctest comments are runnable code examples included in docstrings.
They provide examples of how to invoke a method, class, or function,
and also provide a quick test.  Here's an example

```python
from typing import List

def average(values: List[float]) -> float:
    """Return the average of a list of numbers.

    Parameters:
        values: a list or tuple of numbers to average

    >>> average([2, 3, 4])
    3.0
    >>> average([2, 3, 4, 0])
    2.25
    >>> average([2])
    2.0
    """
    return sum(values)/len(values) if len(values) > 0 else 0.0
```
Each line starting with `>>>` is a Python statement that produces
some result.  The next line(s) are the expected result.
The `doctest` module will execute the doctest statements and
compare the actual and expected results.  

By default, doctest  prints *nothing* if the test is correct
and an error if it fails.  Use the "verbose" option (or -v flag)
to always print the result.

There are two ways to run doctest. Using the command line:
```shell
cmd>  python -m doctest -v average.py

3 tests in 1 item.
3 passed and 0 failed.
```

Or by providing a "main" block that runs doctest:
```python
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
```
The `-v` flag and `verbose=True` arguments are optional, of course.

Doctest are most commonly used in function and method docstrings,
but you can also use them in a class docstring to illustrate how
to use the class.

The expected output that you write for a doctest must **exactly**
match the actual output. For the `average` function, if we wrote:

```python
def average(values):
   """
   >>> average([2, 3, 4])
   3
```
The test will fail! Because the actual output is `3.0` not `3`.

If the expected output is a string, then use **single quotes** not double quotes
because that's the way the Python interpreter displays strings.


## Using Type Hints (Annotations)

To call a function of object constructor, a programmer needs to know
what **type** of value(s) to pass as parameters. 
Python doesn't require you to define the data type of parameters
and returned values, but you can optionally do so.

Python 3.6 and above let you can include *type annotations* in your code. Python ignores them when running your code.  
Annotations help document your code, and also are used by some tools to find bugs
such as passing incorrect value types to a function.

Example: function to compute length of an (x,y) vector. Its also
the hypothenuse of a right triangle, hence the function name.

```python
def hypot(x: float, y: float) -> float: 
    """Return the Euclidean norm of a vector with given x and y lengths."""
    return math.sqrt(x*x + y*y)
```

The syntax for type hints is:

* parameters:  'param: data_type` as in `x: float`.
* return value:  `fun() -> type` as in `rand() -> int`

## Resources

To learn more about Python docstrings:

* [Documenting Python Code](https://realpython.com/documenting-python-code/) on realpython.com has examples of function and class docstrings, and advise on how to write.  They have some videos, too.
* Detailed [Google Docstrings example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) at readthedocs.io.
* Detailed [NumPy Docstrings example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy)
* [NumPyDoc](https://numpydoc.readthedocs.io/en/latest/format.html) official documentation of NumPy/SciPy docstrings.
