---
title: Code Quality
---

Writing and maintaining high quality code is perhaps a developer's
most important responsibility.

It is easy to neglect code quality when working under a deadline,
fixing bugs, or adding a new feature. Over time the code becomes
harder to understand and maintain, and harder to test.

Best Practices for Code Quality include:

1. Consistently use a **coding standard** (coding style)
2. Write document comments (Javadoc or Python docstring) using a standard
3. Use descriptive names
4. Strive for short functions (methods) that do just one thing
5. Use return values instead of side effects where possible.
6. Avoid unexpected side effects.  This includes the "command query separation principle".
7. Review all your code.
8. On a team project, ask others to review your code.
9. Use tools to check your code.
10. Refactor occasionally.  Many projects have a "refactoring day" when the only work done is review and refactoring.

### Clean Code

[Clean Code](http://www.jeremybytes.com/Downloads/CleanCode.pdf) PDF by JeremyBytes. His web page on [clean code](ww.jeremybytes.com/Demos.aspx#CC) has other useful material.

* Important lessons from *Clean Code* and *Code Complete*.

* How to use Checkstyle. How to configure and safe a code style Eclipse or IntelliJ.

* Look at coding guidelines from some real projects. Apache is good source.

### Documenting Your Code

* Python Docstrings, Javadoc, or Scaladoc to create documentation for everyone to use.  
* Syntax of Python Docstrings.
    - 3 variations: Python official docstrings, Google style, Numpy style
* Tools for formatting them:
    - pydoc
    - python interactive: help(something)
    - Sphinx and the Napolean addon
* Code comments to explain *why* and details not obvious from code

## Style Guide and Coding Convention

To make code *easy to read* it should have a consistent format.
Team projects usually have a "coding standard" -- some companies
have a single company coding standard.

For Python:

1. [pep8.org](http://pep8.org/) is a single page easy-to-read summary of how to use [PEP 8](https://www.python.org/dev/peps/pep-0008/) the official Python Style Guide.
2. Python Guide for Docstrings [PEP 257](https://www.python.org/dev/peps/pep-0257/)
3. [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
    - Part 2 is guidelines for using the Python language 
    - Rule #1 is "run `pylint` over your code"!
    - Part 3 "Python Style Rules" are rules for coding style
    - Part 4 "Parting Words" is *Be Consistent*
    - Google's guide is very prescriptive (do and don't) on how to write code.

For Java:

1. Programming 2 (Java) coding standard.
2. Oracle's Java coding standard.

## Tips from "*Practices of an Agile Developer*"

Many of the tips relate to code quality -- they must think it's important!

Exercise: create a list of Tips related to code quality and give 
an example of each one.
