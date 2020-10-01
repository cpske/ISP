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

Python also has this capability, but the standard is less precise than Java.

## Python docstring Comments

Documentation comments in Python are called **docstring** comments.
Here's an example for a function:
```python
def max(a, b):
    """Return the maximum of two values a and b.

    Parameters:
        a, b - two numbers to find the maximum of
    Returns:
        the max of a and b
    """
    if a > b: return a
    return b
```

1. The docstring for a function must be the first thing inside the function
and use a multi-line comment (""").
2. The first line of the comment should be a concise description of what it does.
3. If the function is very simple, a one-line descriptoin is enough. Otherwise, leave a **blank line** and then write a more complete description.
4. Document *parameters*, *return value* (if any), and any *Exceptions* raised.  The standard for how to format these is not very precise.  There are 3 styles (described below):
    * Pydoc style, used in Python API
    * Google style
    * Numpy style, which uses restructured text mark-up

## Viewing Python docstrings

The interactive Python interpreter will display the docstring comments
of a function, class, or method when you use the `help` command:
```python
>>> help(print)
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    ...
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

This docstring formats parameters and special keywords using colons (:).
For example, `:param method:` means that constructor has a parameter for the HTTP method to use ('GET', 'POST') and a parameter named `url` for the URL to connect to.

## Use pydoc to view docstrings

Use `pydoc` from the command line to view documentation for packages, classes, modules, and functions:

```shell
cmd> pydoc os
   (shows docs for os module)
cmd> pydoc math.sqrt
   (shows doc for sqrt function)
```

## Writing Docstrings

You should write docstring comments for:

* classes
  - describes purpose of the class
  - parameters of the constructor
  - public methods
  - example of using the class
* functions and methods
  - describes purpose of the function or method
  - parameters, and restrictions on their values
  - meaning and type of the return value, if any
  - exceptions that may be raised
* modules
  - describe purpose of the module
  - module docstrings go at top of the file, before imports
* packages
  - purpose of the package
  - list the modules and subpackages (though this can become out-of-date. Python should do this automatically)
  - put package docstrings in the package's `___init__.py` file.

## Python Doctest Comments

Doctest comments are runnable code examples included in docstrings.
They provide examples of how to invoke a method, class, or function,
and also provide a quick test.  Here's an example

```python
def average( values ):
    """Return the average of a list of numbers.
    Parameters:
        values is a list or tuple of numbers

    >>> average([2,3,4])
    3.0
    >>> average([2,3,4,0])
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
def average( values ):
   """
   >>> average([2,3,4])
   3
```
The test would fail! Because the actual output is `3.0` not `3`.
If the expected output is a string, then use single quotes (not double quotes)
because that's the way the Python interpretter displays string results.


## Python Type Annotations

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

* [Documenting Python Code](https://realpython.com/documenting-python-code/) on realpython.com has examples of function and class docstrings, and advise on how to write.
* Detailed [Google Docstrings example](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) at readthedocs.io.
* Detailed [NumPy Docstrings example)[https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html#example-numpy]
* [NumPyDoc](https://numpydoc.readthedocs.io/en/latest/format.html) official documentation of NumPy/SciPy docstrings.
