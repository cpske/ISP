---
title: Logging
---

Logging is an essential part of a professional application.
Logging is required by law for some kinds of applications,
such as those involving financial transactions and medical records.

The presentation provide an overview and some examples of security
breaches that were detected using logs.

Presentation [Introduction to Logging](Logging.pdf)

## Practice

Please do this [Logging Practice](logging-practice)
with starter code in [demo_log.py](demo_log.py).

## Logging in Django

Django extends the Python logging module.
You can configure logging in your Django `settings.py` file.

You can also configure logging for a specific "app" in the `app.py` file, 
which is described in the second article below.  
But it's usually better to configure logging in `settings.py`.
Logging configuration done in `app.py` or any other file may
go unnoticed when you try to modify logging at a later time.

* [Django Logging, The Right Way](https://lincolnloop.com/blog/django-logging-right-way/) clear explanation with examples
* [Disabling Error Emails in Django](https://lincolnloop.com/blog/disabling-error-emails-django/) explains how to remove default loggers in Django
* [Logging](https://docs.djangoproject.com/en/3.1/topics/logging/) in the official Django docs

### Execise: Log all Function Calls

Logging function calls can help you understand a part of a code.

Here's a function that uses recursion to find integer factors
of a number.

It uses `print` statements to show calls and returns.
Makes the function hard to read, right?  
And we will eventually want to remove those print statements
from the function (more work and potential for errors).

```python
def factor(n):
    """Return the prime factors of n including 1.  

    n must be a positive integer.
    """
    print(f"factor({n})")
    if n < 1:
        raise ValueError("argument must be positive integer")
    if n == 1:
        print("return [1]") 
        return [1]
    for f in range(2, n):
        if n % f == 0:
            factors = [f] + factor(n//f)
            print("return", factors)
            return factors
    factors = [n]
    print("return", factors)
    return factors

if __name__ == '__main__':
    for n in [36, 37, 110, 240000]:
        print(f"factor(n) = ")
        print(factor(n))
```

Try calling it to see how it works.

Exercise 1: Replace the "print" statements with log statements using level DEBUG.


## Creating a "Decorator" for Logging

What if you want to log each time a function is invoked and each time the function returns? That can be useful when debugging a function, such as the factorial function.

In Python, you can dynamically define new functions in code.
A function can return a function, too (called "*higher level functions*").

You can use this to write a "decorator" that wraps calls to another function.
The wrapper is called a *Decorator* since it is used to "decorate" (add some extra behavior) to an existing function.

Here's a decorator that prints each time a function is called and prints the return value:

```python
def print_decorator(fun):
    """
    Print calls to a function.

    Argument:
        fun - a function to decorate
    Returns:
        a new function that adds printing to the original function
    """
    def new_fun(*args, **kwargs):
        print(f"calling {fun.__name__}({args}, {kwargs})")
        result = fun(*args, **kwargs)
        print("return", result)
        return result

    return new_fun
```

There are 2 ways to use this decorator.

1. Decorate an existing function:
   ```python
   import math
   mysqrt = print_decorator(math.sqrt)
   r = mysqrt(27)
   ```

2. Decorate a function's definition:
   ```python
   @print_decorator
   def average(a, b):
      """average of a and b"""
      return (a + b)/2


   avg = average(10, 25)
   ```

In both cases, when the function is called it will print both the call and returned value.

Exercise 2: Define a `log_decorator` and use it to decorate the `factor` function instead of the log (or print) statements inside the function. 
Does it make the code cleaner and easier to read?

## Logging Services

You can use a **logging service** to receive, monitor, analyze, and store logs.

Commercial web sites can generate hundreds of megabytes (or more!) of log info every day.  Those logs need to be filtered, scanned for suspicious activity or error messages, and summarized.  Logging services do this. 

Logging Services also aggregate logs from many machines or many apps. A busy web service may have several hosts running the same application to provide faster responses. A logging service will combine logs from many hosts.

Some logging services are:

* [Loggly](https://loggly.com) log analysis and monitoring. Log monitoring service used by Pizza Hut :-).
* [Sentry](https://sentry.io) has a free "developer" tier and toolkits to make it easy to send you app logs to Sentry.
