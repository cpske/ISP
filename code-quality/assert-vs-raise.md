---
title: Assertions, Exceptions, and Special Condtions
---

When something unexpected happens in the code for a function or method,
there are 4 ways we can indicate that there is a problem:

1. raise an exception, with a message
2. use assert to raise AssertionError with a message
3. return a special value (something that normally could not be returned)
4. print a message on the console

Consider a function to return the index of a value in a list.

```python
def index(lst, value):
    """Return the index of the first element in lst that equals value"""
    return lst.index(value)

>>> lst = ['a', 'b', 'c', 'b']
>>> index(lst, 'b')
1
>>> index(lst,'z')
ValueError: 'z' is not in list
```

1. Raise Exception    
   In this example, the built-in `list.index()` method raises ValueError if the argument is not in the list.  So we don't need to add any code.

2. Use **assert** with a test that the value is in the list.
   ```python
   def index(lst, value):
       assert value in lst, f"{value} is not in list"
       return lst.index(value)

   >>> index(['a', 'b', 'c'], 'd')
   AssertionError: 'd' is not in list
   ```

3. Return a special value. Let's return -1, which would normally never be the index.
   ```python
   def index(lst, value):
       if value not in lst:
           return -1
       return lst.index(value)

   >>> index(['a', 'b', 'c'], 'd')
   -1
   ```

4. Print a message on the console. In this case, we still need to return *something* so the program will execute.  If we just write `return` Python will return `None`:
   ```python
   def index(lst, value):
       if value not in lst:
           print(f"{value} is not in list")
           return
       return lst.index(value)

   >>> index(['a', 'b', 'c'], 'd')
   # nothing is printed
   ```

Which solution is best?

The answer depends on the purpose of the function and the condition you are checking for.

* Use **assert** to check conditions that should never occur in correct code, including violations of preconditions or invariants (things that should always be true)
  - assert is used to catch programming errors and for debugging
  - if `assert` fails, the program will halt with an AssertionError. This is better than silently ignoring the error until the program fails, since it helps identify the source of the problem.
  - the programmer not expected to catch AssertionError
  - In production use, asserts can be disabled using the python `-O` option.
  - `assert` statements provide internal documentation of what is expected to be true -- preconditions and other conditions that should be true if the code is correct

* Use **exceptions** for error conditions that could occur in correct code, and for public functions/methods (such as in a library) where the function might be invoked with incorrect values.
  - the programmer may catch the exception and handle it

* For unusual or unexpected conditions that can reasonably occur in correct code and are not errors, you can return a special value or raise Exception. The choice depends on preference and how the code is intended to be used.
  - the programmer is expected to check for the special return value

* Printing a message on the console is **never** a good solution. 
  - For an interactive application, let the caller print a message via the normal UI.

* Logging can be used along with exceptions to log error conditions.


In the `index()` function, searching for a value that is not in a list may be a reasonable thing to do (depends on the application).
So, "raise an excepton" or "return a special value" are both acceptable solutions.
- Python's `list.index(value)` raises ValueError
- Java's `list.indexOf(value)` returns -1 if value is not in the list


## Don't Raise the root `Exception` Type

You should raise a specific exception type, such as ValueError or TypeError. 
If you are writing a library function and none of the predefined
exception types apply to the situation, then define your own 
exception subclass.

You should not raise the base `Exception` or `BaseException` types, 
which are base classes for other exceptions.

Why not?
* It's not descriptive or specific
* If the programmer uses `try ... except Exception` it will catch any exception, including things that it's not intended to catch.
* `try ... except BaseException` will also catch KeyboardInterrupt (Ctrl-C)!

```python3
# BaseException catches Keyboard Interrupts like Ctrl-c
try:
    name = input("What's your name?")
except BaseException:
    name = "anonymous"
print("Hello,", name)

# Run it and press CTRL-C instead of typing a response
What's your name?  <CTRL-C>
Hello, anonymous
```


## Exercise

This function computes the avarage of a list of numbers:

```python
def average(values) -> float:
    """Return the average of a list of values. Must supply at least one value"""
    return sum(values) / len(values)
```

1. If the `values` parameter is empty, what happens?

2. Modify the code to raise ValueError if the list is empty.

3. Add an `assert` to test for empty list. Display a message if the assert fails.

4. Creata a `zaverage` function the returns 0.0 if the list is empty. You can do this without "if ... else".

5. Which solution do you think is best for average?  Why?


## Exercise

Read the first line from a file and return it:

```python
def head(filename) -> str:
    """Return the first line from a file."""
    file = open(filename, 'r')
    first_line = file.readline()
    file.close()
    return first_line
```

1. What should `head` do if the requested filename does not exist or the application cannot open the file?

2. What should `head` do if the file is empty?

3. Is there anything that we might use `assert` to check for?
   - no need to check that filename is a string. `open` will catch that.

4. Rewrite `head` to use your solution. If applicable to your code, also rewrite to use a "with" block to automatically close the file when execution leaves the block.

## Syntax of Assert

```python
assert condition, expression
```

"Assert" a *condition* that should be True.
If the *condition* is False, then an AssertionError is raised with the result of `expression` as the exception message text.  `expression` can be a string or anything the produces a string.

```python
assert math.sqrt(25)==5, "sqrt is broken"
```

## References

- [Assertions and Exceptions](https://stefan.sofa-rockers.org/2018/04/16/assertions-and-exceptions/)
- [Python what is raise and assert](https://medium.com/@jadhavmanoj/python-what-is-raise-and-assert-statement-c3908697bc62)
