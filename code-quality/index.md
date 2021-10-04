---
title: Code Quality
---

Writing and maintaining high quality code is one of the developer's
most important responsibilities.

It is easy to neglect code quality when working under a deadline,
fixing bugs, or adding a new feature. Over time the code becomes
harder to understand and maintain, and harder to test.

## Best Practices for Code Quality

1. Consistently use a **coding standard** (coding style)
2. Write [document comments](docstrings) (Javadoc or Python docstring) using a standard format
3. Use descriptive names for classes, functions, and variables
4. Strive for short functions (methods) that do just one thing
5. Use return values instead of side effects where possible
6. Avoid unexpected side effects. This includes the "command query separation principle".
7. Review all your code.
8. On a team project, ask others to review your code.
9. Use tools to check your code.
10. Refactor to improve code.  

Many projects have a "refactoring day" when the only work done is code review and refactoring.

*Zen of Python* on Code Quality. At the Python interactive prompt, type:

```python
>>> import this
```

## Clean Code

*Clean Code* refers to code that follows good design principles and is well-written. 
Clean Code is easier to read, test, maintain, and evolve.    
Just what *defines* Clean Code is a bit vague and subjective, 
just as "good", "well", and "easy" are subjective.

[Clean Code](http://www.jeremybytes.com/Downloads/CleanCode.pdf) PDF by JeremyBytes. His web page on [clean code](ww.jeremybytes.com/Demos.aspx#CC) has other useful material.

To discuss:

* Important lessons from *Clean Code* and *Code Complete*.

* How to use Checkstyle for Java or Pylint and Flake8 for Python.

* Look at coding guidelines from some real projects. [Apache](https://apache.org) is a good source.


## Coding Style and Coding Convention

Code is *easier to read* if you consistently apply 
some guidelines, and *easier for others to read* if everyone
on the team uses the same coding style.

Team projects usually have a "coding standard" -- some companies
have a single company coding standard. 
Google, Apache Foundation, and Microsoft have coding standards.

Over time, common coding standards and guides have emerged.
There is *some* variation in the details of a coding style guide,
but they all agree on most of the details.


## Coding Standard

These docs show the Python "official" coding standard, called PEP8:

* [pep8.org](http://pep8.org/) is a single page easy-to-read summary of how to use [PEP 8](https://www.python.org/dev/peps/pep-0008/) the official Python Style Guide.
* Python Guide for Docstrings [PEP 257](https://www.python.org/dev/peps/pep-0257/)

This article is very helpful with good examples:

* [How to Write Beautiful Code with PEP8](https://realpython.com/python-pep8/) on RealPython.

Google has a detailed style guide, that includes "pros" and "cons" of style choices. It explains **why** and can help you decide what's important.

* [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
  - Rule #1 is "run `pylint` over your code"! (using Google's .pylintrc)
  - Part 2 is guidelines for using the Python language 
  - Part 3 "Python Style Rules" are rules for coding style
  - Part 4 "Parting Words" is *Be Consistent*
  - Google's guide is very prescriptive (do and don't) on how to write code


### Documenting Your Code

See [Docstrings](docstrings) for how to write documentation comments in Python.

* Python Docstrings, Javadoc, or Scaladoc are documentation for a project. They can be shown as web pages or shown dynamically in an IDE.
* Syntax of Python Docstrings.
  - 3 variations: Python official docstrings, Google style, Numpy style

In Python, there is not a universal agreement for how to document parameters, return values, and exceptions for a method or function. There are 3 styles:
* Tools for creating documentation from docstrings:
  - pydoc
  - python interactive: `help(something)` shows formatted docstring
  - `print(something.__doc__)`
  - Sphinx and the Napolean addon. Used to create ReadTheDocs style web docs.
* Code comments should explain *why* and details not obvious from code. 
* Don't explain "how" that is evident from the code itself.


### Code Quality and Code Checking Tools for Python

[Python Code Quality][real-python-code-quality] best practices & tools, on RealPython.com.


### Django's Coding Style Guide

Django uses the Python PEP8 and PEP? (another PEP) with a few exceptions, described in the link below.

The link is guidelines for anyone who contributes code to the Django project.
The guide is also useful for developers writing Django apps.

Django uses `flake8` to check coding style.

https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/


### Coding Style For Java

1. Programming 2 (Java) coding standard.
2. Oracle's Java coding standard.


## Code Quality and Style Checking Tools

[Code Quality Tools](code-quality-tools) describes tools for Python.

## Tips from "*Practices of an Agile Developer*"

Many Tips in the book relate to code quality -- the authors must think it's important!

## Exercise

Create a list of the Tips from PAD related to code quality and give 
an example of each one.

[Quick References](../resources/PAD-quickref.pdf) from *Practices of an Agile Developer*
