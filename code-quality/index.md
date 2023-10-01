---
title: Code Quality
---

Maintaining high quality code is one of the developer's
top responsibilities.

It is easy to neglect code quality when working under a deadline,
fixing bugs, or adding a new feature. Over time the code becomes
harder to understand and maintain, and harder to test.

Eventually, such code is discarded and rewritten -- a waste of money.

## What is Code Quality?

*Code Quality* is subjective, but accepted **characteristics** of good quality code are:

- code does what it should
- code can be tested (testable)
- easy to understand
- uses a consistent style
- is well-documented
- can be maintained (the above factors influence this)

References:

- [What is Code Quality?][perforce-code-quality] on Perforce.com
- [Code Quality Metrics][dzone-code-quality-metrics] on DZone.com

[perforce-code-quality]: https://www.perforce.com/blog/sca/what-code-quality-and-how-improve-code-quality
[dzone-code-quality-metrics]: https://dzone.com/articles/code-quality-metrics

## How to Improve Code Quality

The above articles recommend these best practices:

1. Use a Coding Standard
2. Analyze Your Code - both manually and using [tools](code-quality-tools)
3. Follow Code Review Best Practices
4. Refactor Code

**10 Specific Practices**

1. Consistently use a **coding standard**. For Python use PEP8.
2. Write [document comments](docstrings) (Javadoc or Python docstring) in a standard format
3. Use descriptive names for classes, functions, and variables
4. Write short functions (methods) that do only one thing
5. Use return values instead of side effects when possible
6. Avoid unexpected side effects. Use the "*Command Query Separation Principle*".
7. Review all your code.
8. On a team project, ask others to review your code.
9. Use tools to check your code. Perform static analysis, linting, and style checking.
10. Refactor to improve code.

Many projects have a "refactoring day" when the only work done is code review and refactoring.

*Zen of Python* on Code Quality. Run Python and type:

```python
   >>> import this
```

## Clean Code

*Clean Code* refers to code that follows good design principles and is well-written. 

Clean Code is easier to read, test, maintain, and evolve.    
What *defines* Clean Code can be vague and subjective, 
just as "good", "well", and "easy" are subjective.

[Clean Code](http://www.jeremybytes.com/Downloads/CleanCode.pdf) PDF by JeremyBytes. His web page on [clean code](ww.jeremybytes.com/Demos.aspx#CC) has other useful material.

To discuss:

* Important lessons from *Clean Code* and *Code Complete*.

* How to use Checkstyle for Java or Pylint and Flake8 for Python.

* Look at coding guidelines from some real projects. [Apache](https://apache.org) is a good source.


## Coding Style and Coding Convention

Team projects usually have a "coding standard" -- some companies
have a single coding standard.
Google, Microsoft, and the Apache Foundation have coding standards.

Over time, **common coding guidelines** have emerged.
There is *some* variation in the details of a coding style guide,
but they all agree on most of the details.


## Coding Standard for Python

These docs show the Python "official" coding standard, called PEP8:

- [How to Write Beautiful Code with PEP8](https://realpython.com/python-pep8/) on RealPython. Lot's of helpful examples.
- [pep8.org](http://pep8.org/) is a single page easy-to-read summary of how to use [PEP 8](https://www.python.org/dev/peps/pep-0008/) the official Python Style Guide.
- Python Guide for Docstrings [PEP 257](https://www.python.org/dev/peps/pep-0257/)

- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
  - Style Guide lists "pros" and "cons" of style choices & explains **why** to help you decide what's important.

  - Rule #1 is "run `pylint` over your code"! (using Google's .pylintrc)
  - Part 2 is guidelines for using the Python language 
  - Part 3 "Python Style Rules" are rules for coding style
  - Part 4 "Parting Words" is *Be Consistent*
  - Google's guide is very prescriptive (do and don't) on how to write code


### Documenting Your Code

[PEP257 Docstrings](https://peps.python.org/pep-0257/) is a one page guide to the Python docstring standard.

Documenting parameters, returns, and exceptions is important!
There are (at least) 3 styles for this,
which are described in my [Docstrings](docstrings) write-up.

We will use [Sphinx style docstrings](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) **except** use Type Hints for parameter and return types, *not* docstring comments.  So don't use the `:type var:` tags in docstrings.

Tools for generating nice documentation from docstrings:
- pydoc
- python interactive: `help(something)` shows formatted docstring
- `print(something.__doc__)` shows docstring for `something`
- Sphinx and Napolean (add-on). Used to create ReadTheDocs style web docs.

### Comments in Code

- Use comments to explain *why* and details that are not obvious from code. 
- Don't explain "what" or "how" that is evident from the code itself.


### Code Quality and Code Checking Tools

[Python Code Quality][real-python-code-quality] best practices & tools, on RealPython.com.

My [Code Quality Tools](code-quality-tools) page describes some tools for Python.

Recommended Tools: 

- `flake8` with `flake8-docstrings` extension
- `ruff` a fast alternative to flake8. Claims to check a superset of flake8.
- `mypy` for static checking using type hints.
- PyCharm has a builtin code checking tool, and be configured to use an extneral tool
- VS Code: choose an external "Lint" tool in settings

[real-python-code-quality]: https://realpython.com/python-code-quality/

### Django's Coding Style Guide

Django uses the Python PEP8 and PEP? (another PEP) with a few exceptions, described in the link below.

The link is guidelines for anyone who contributes code to the Django project.
The guide is also useful for developers writing Django apps.

Django uses `flake8` to check coding style.

https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/


### Coding Style For Java

1. Programming 2 (Java) coding standard.
2. Oracle's Java coding standard.

## *Practices of an Agile Developer*

Many Tips in the book *Practices of an Agile Developer* concern code quality. The authors think it's important!

Tip 2. *Quick Fixes Become Quicksand*    

Tip 25. *Program Intently and Expressively*    

Tip 26. *Communicate in Code*    

Tip 30. *Write Cohesive Code*    


[Quick Reference](../resources/PAD-quickref.pdf) from *Practices of an Agile Developer*.

