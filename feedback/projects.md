---
title: Feedback on Projects
---

## 1. Use What You Learn

In KU Polls iteration 2 you learned how to separate configuration data
from code, which is a good practice for **any** software.

Are teams applying it to their projects?

| Project            | External configuration? | Secret settings on Github?  |
|:-------------------|------------------|:----------------------------|
| Covid19 Tracker    | No               | SECRET KEY, OAuth secrets   |
| DEK-COM            | No               | SECRET KEY                  |
| EveHolder          | django-environ   | none                        |
| Sleep Helper       | No               | SECRET KEY                  |
| JIX                | No               | SECRET KEY, OAuth secrets   |
| KU-Hub             | decouple         | none                        |
| Kvent              | decouple         | none [see Note]             |
| Noxus              | No               | SECRET KEY                  |
| Real Estate Rental | No               | SECRET KEY, OAuth secrets   |
| TELLING            | No               | SECRET KEY                  |
| TEWMA              | No               | SECRET KEY                  |
| Your Fitness Pal   | No               | SECRET KEY                  |


### Secure Development

The software industry unanimously recommends:

> Security must be part of the development process, not added at the end.

Apply basic security practices from the start. 
Think about security during code reviews, too.

If your `SECRET_KEY` has been exposed, you can generate a new one.

**Note**: Kvent `settings.py` has: 

```python
ALLOWED_HOSTS = ['*']
DEBUG = config('DEBUG', default=True)
```

You should add `ALLOWED_HOSTS` to the external config so you can use
different values for development and production. Restrict ALLOWED\_HOSTS 
in a development environment. You should be careful that `DEBUG`
is False on a deployed server, since `DEBUG=True` can be used to discover 
environment variables (your secrets). 

Hence, the safe default is `False`.

## 2. Better and More Tests Needed

Projects I reviewed have very little unit testing.

Unit tests generally contain **more lines of code** than your model and controller 
classes combined, since unit tests have to test several cases.

1. Write good unit tests for all methods that involve any non-trivial logic.
   * Test important behavior, not just methods.
   * Not necessary to test trivial methods or simple constructors. Carefully Inspect the code for these.
2. Tests should have descriptive names for what they test (long names are good) **and** a docstring comment describing the test.



