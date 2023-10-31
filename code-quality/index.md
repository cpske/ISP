---
title: Code Quality
---

Maintaining high quality code is one of the developer's
top responsibilities.

It is easy to neglect code quality when working under a deadline,
fixing bugs, or adding a new feature. Over time the code becomes
harder to understand and maintain, and harder to test.

Eventually, such code is discarded and rewritten.

[What is Code Quality](#what-is-code-quality)    
[10 Best Practices](#10-best-practices)    
[Clean Code](#clean-code)    
[Coding Convention for Project or Organization](#coding-convention-for-project-or-organization)    
[What To Include in your Coding Guide](#what-to-include-in-your-coding-guide)    
[Python Coding Standards](#python-coding-standards)    
[Documentation in Code](#documention-in-code)    
[Style Checkers and Static Analysis](#style-checkers-and-static-analysis-tools)    
[Django's Coding Style Guide](#djangos-coding-style-guide)    
[Java Coding Style](#java-coding-style)    
[Practices of an Agile Developer](#practices-of-an-agile-developer)    

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

## 10 Best Practices

1. Consistently use a **coding standard**. For Python use PEP8.
2. Write [document comments](docstrings) in a standard format: Javadoc or Python docstring. 
3. Use descriptive names for classes, functions, and variables.
4. Write short functions (methods) that do only one thing.
5. Use return values instead of side effects when possible.
6. Avoid unexpected side effects. Use the "*Command Query Separation Principle*".
7. Review all your code.
8. On a team project, review code with others. 
   - Use a Code Review guide & checklist.
9. Use tools to check code. Perform static analysis, linting, and style checking.
   - pylint, flake8, or ruff for style, linting, and some error checking
   - mypy for static analysis
10. Refactor to improve code.

Many projects have a "refactoring day" when the only work done is code review and refactoring.

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


## Coding Convention for Project or Organization

Team projects usually have a "coding standard". It helps others understand your code, and avoids pointless commit conflicts caused when each person's IDE reformats the same block of code.

Google, Microsoft, and the Apache Foundation have organization-wide coding standards.  The [VSCode Project](https://github.com/microsoft/vscode/wiki) has a coding standard.

## What to include in your coding guide 

Some ideas -- you decide what is important to your team.

- how to name files and how to organize them
- code formatting rules
- coding rules
  - naming convention
  - handling exceptions - don't ignore exceptions
  - when to raise an exception
  - logging?
  - assertions?
  - use guard clauses instead of nested "if"?
- do you require type hints?
  - how much detail?
  - do collection type hints use `collections.abc` or `typing`?
- Use [code checking tools](#style-checkers-and-static-analysis-tools)?
- Use an autoformatting tool to make it easy?
  - IDE formatting rules - you can export and share these
  - [Black][black] and [Pylink][pylink] code formatting tools
- [Comments and comment style](#documentation-in-code), especially method and class docstrings.


- Keep it simple and practical

- Document by example is OK, instead of long text (TL;DR)

[black]: https://github.com/psf/black
[pylink]: https://github.com/google/pyink


## Python Coding Standards

PEP8 is the Python "official" coding standard:

- [How to Write Beautiful Code with PEP8](https://realpython.com/python-pep8/) on RealPython. Lot's of helpful examples.
- [pep8.org](http://pep8.org/) is a single page easy-to-read summary of how to use [PEP 8](https://peps.python.org/pep-0008/) the official Python Style Guide.

[Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- Style guide lists "pros" and "cons" of style choices & explains **why** do it.
- Rule #1 is "Run `pylint` over your code using this [.pylintrc][pylintrc]"
- Part 2 is guide for using the Python language 
- Part 3 "Python Style Rules" for coding style
- Part 4 "Parting Words" is: *Be Consistent*
- Google's guide is very prescriptive (do and don't) on how to write code

[pylintrc]: https://google.github.io/styleguide/pylintrc


## Documentation in Code

[PEP257 Docstrings](https://peps.python.org/pep-0257/) is a one page guide to the Python docstring standard.

My [Docstrings](docstrings) write-up describes 3 styles for parameters, returns, and exceptions in docstrings.

We will use [Sphinx style docstrings](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) **except** use **Type Hints** for parameter and return types, *not* docstring comments.  So don't use the `:type var:` tags in docstrings.

```python
def average(values: Collection[float|int]) -> float:
    """Compute the arithmetic average of a collection of values.

    :param values: non-empty collection of numeric values to average
    :returns: the population average of the values
    :raises ValueError: if collection is empty or contains invalid values
    """
```

View docstrings in Python interactive shell:

- `help(something)` shows formatted docstring
- `print(something.__doc__)` shows docstring for `something`

Tools to  generate formatted documentation:

- pydoc
- Sphinx and Napolean (add-on). Create HTML or ReSt format docs. Used to create [ReadTheDocs](https://readthedocs.com) content.

### Comments in Code

- Use comments to explain *why* and details that are not obvious from the code. 
- Don't explain "what" or "how" that is evident from the code itself.


## Style Checkers and Static Analysis Tools

- `flake8` with `flake8-docstrings` extension
- `ruff` a fast alternative to flake8. Claims to check a superset of flake8.
- `pylint` performs both style checking and some static analysis
- `mypy` for static analysis. Uses type hints for improved static analysis.

PyCharm has a builtin code checking tool; you can customize it, or configure PyCharm to use an external tool.

VS Code: choose an external "Lint" tool in settings (CTRL-SHIFT-P and type 'python')

[Python Code Quality][real-python-code-quality] on *RealPython.com* explains best practices & tools.

My [Code Quality Tools](code-quality-tools) page describes how to use some tools.

[real-python-code-quality]: https://realpython.com/python-code-quality/


## Django's Coding Style Guide

Django uses the Python PEP8 and PEP? (another PEP) with a few exceptions, described in the link below.

The link is guidelines for anyone who contributes code to the Django project.
The guide is also useful for developers writing Django apps.

Django uses `flake8` to check coding style.

https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/


## *Practices of an Agile Developer*

Many Tips in [Practices of an Agile Developer](../resources/PAD-quickref.pdf) concern code quality. The authors must think it's important!

Tip 2. *Quick Fixes Become Quicksand*    

Tip 25. *Program Intently and Expressively*    

Tip 26. *Communicate in Code*    

Tip 30. *Write Cohesive Code*    

[PAD Quick Reference](../resources/PAD-quickref.pdf) from *Practices of an Agile Developer*.

