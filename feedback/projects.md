---
title: Feedback on Projects
---

## Real or Fake?

*Good comments*: inform the reader. Describe what something does and why.

*Bad comments*: state what is obvious from the code. 

*Really Bad*:   state nothing at all.

Example: VeggieHub
```python
class Category(models.Model):
    """Category model"""
    not pass


class State(models.Model):
    """State model"""
    not pass


class Restaurant(models.Model):
    """Restaurant model"""


class Review(models.Model):
    """Review model"""
    

class BookMark(models.Model):
    """BookMark model"""
    not worth it
```

| Project            | Model Docstring             |
|--------------------|-----------------------------|
| EPL                | OK but minimal, no models in "predict" app. |
| KU Active          | Useless or none.                   |
| KU Hub             | Some models have, some have none.  |
| Marvel Universe    | Not so marvelous -- NO Docstring!     |
| PlanMe             | Useless. "Model definition of User". |
| SIP                | No Docstring!                   |
| TurTask            | Good! Has :param: descriptions, too. |
| VeggieHub          | Useless. "Category Model", etc. |
| Wistify            | No Docstring!                   |
| WordWise           | Good! Has :param: descriptions, too. |


Good:

- PlanMe refactored models into a package with separate files.
- KU-Active refactored models into a package with separate files.
- KU-Hub refactored models into a package with separate files.
- WordWise refactored models into a package with separate files.


## Violation of Package Naming (should be lowercase, no "-")

- MarvelUniverse
- SIP

## Separate & Secure Configuration -- Use What You Learned

In KU Polls you learned how to separate configuration data from code.    
This is a good practice for *any* software.

Are teams applying this to their projects?  Mostly, **YES**

Not Applying: Wistify

```python
# settings.py
SECRET_KEY = 'django-insecure-cr1v8x%7t=h7)c%%p(lls3_z$wap(2^25=5*edkr%i049!u@y2'

DEBUG = True

ALLOWED_HOSTS = []
```



### Secure Development

The software industry unanimously recommends:

> Security must be part of the development process, **not added at the end**.


Insecure Defaults:

```python
ALLOWED_HOSTS = ['*']                  # EPL, Wistify
DEBUG = config('DEBUG', default=True)  # MarvelUni, KU-Hub, Wistify
```

You should add `ALLOWED_HOSTS` to the external config so you can use
different values for development and production. Restrict ALLOWED\_HOSTS 
in a development environment. You should be careful that `DEBUG`
is False on a deployed server, since `DEBUG=True` can be used to discover 
environment variables (your secrets). 

The safe default for DEBUG is `False`.



## 2. Better and More Tests Needed

Projects I reviewed have very little unit testing.

Unit tests generally contain **more lines of code** than your model and controller 
classes combined, since unit tests have to test several cases.

1. Write good unit tests for all methods that involve any non-trivial logic.
   * Test important behavior, not just methods.
   * Not necessary to test trivial methods or simple constructors. Carefully Inspect the code for these.
2. Tests should have descriptive names for what they test (long names are good) **and** a docstring comment describing the test.


