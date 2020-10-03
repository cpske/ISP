---
title: Code Quality
---

Writing and maintaining high quality code is one of the developer's
most important responsibilities.

It is easy to neglect code quality when working under a deadline,
fixing bugs, or adding a new feature. Over time the code becomes
harder to understand and maintain, and harder to test.

Best Practices for Code Quality include:

1. Consistently use a **coding standard** (coding style)
2. Write document comments (Javadoc or Python docstring) using a standard
3. Use descriptive names
4. Strive for short functions (methods) that do just one thing
5. Use return values instead of side effects where possible
6. Avoid unexpected side effects. This includes the "command query separation principle".
7. Review all your code.
8. On a team project, ask others to review your code.
9. Use tools to check your code.
10. Refactor occasionally.  Many projects have a "refactoring day" when the only work done is review and refactoring.

*Zen of Python* on Code Quality. Try this:

```python
>>> import this
```

### Clean Code

*Clean Code* refers to code that follows good design principles and is well-written. 
Clean Code is easier to read, test, maintain, and evolve.    
Just what *defines* Clean Code is a bit vague and subjective, 
just as "good", "well", and "easy" are subjective.

[Clean Code](http://www.jeremybytes.com/Downloads/CleanCode.pdf) PDF by JeremyBytes. His web page on [clean code](ww.jeremybytes.com/Demos.aspx#CC) has other useful material.

To discuss:

* Important lessons from *Clean Code* and *Code Complete*.

* How to use Checkstyle for Java or Pylint and Flake8 for Python.

* Look at coding guidelines from some real projects. Apache is good source.

## Coding Style and Coding Convention

Code should have a consistent format to make it *easy to read*,
especially easy for others to read.    
Team projects usually have a "coding standard" -- some companies
have a single company coding standard.

The Python standard coding style is defined in two Python docs: 

* [pep8.org](http://pep8.org/) is a single page easy-to-read summary of how to use [PEP 8](https://www.python.org/dev/peps/pep-0008/) the official Python Style Guide.
* Python Guide for Docstrings [PEP 257](https://www.python.org/dev/peps/pep-0257/)

Useful article: [How to Write Beautiful Code with PEP8](https://realpython.com/python-pep8/) on RealPython.

Google has their own detailed style guide, that includes "pros" and "cons" of style choices:

[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
 - Rule #1 is "run `pylint` over your code"! (using Google's .pylintrc)
 - Part 2 is guidelines for using the Python language 
 - Part 3 "Python Style Rules" are rules for coding style
 - Part 4 "Parting Words" is *Be Consistent*
 - Google's guide is very prescriptive (do and don't) on how to write code.

### Documenting Your Code

See [Comments](comments) for how to write comments in Python.

* Python Docstrings, Javadoc, or Scaladoc create documentation for a project. They can be shown as web pages or shown dynamically in an IDE.
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

Many Tips in the book relate to code quality -- they must think it's important!

Exercise: create a list of Tips related to code quality and give 
an example of each one.
