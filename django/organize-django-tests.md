---
title: Organize Unit Tests in Django
---

When you create a new app, Django creates `models.py`, `views.py`, and `tests.py` file for the app.
Putting all your models, views, or tests in one file is usually 
not a good idea, especially on a team project with many people working 
on different features.

A better way is to **divide your code** into multiple files.  
For the Polls tutorial, the structure for tests would be:
```listing
polls/
    __init__.py
    apps.py
    models.py
    urls.py
    views.py
    tests/
        __init__.py
        test_question.py
        test_choice.py
        test_views.py
```

Similarly for models and views.

- [Reorganize Tests](#reorganize-tests)
- [Reorganize Models](#reorganize-models)


### Reorganize Tests

**1. Put your tests in a folder named `tests`**

In your "app" directory create a folder named `tests`.
For the Django Polls tutorial, the folder would be `polls/tests`.
In the tests folder create an empty `__init__.py` file so that folder is a package (Python doesn't require this but unittest discovery does).

**2. Move `tests.py` to the `tests` folder**

**3. Divide your tests based on target or type**

Separate `tests.py` into `test_question.py` (tests for Question),
`test_views.py`, etc.
Since Choice is closely tied to Question, its OK to test both Question
and Choice in one file.

You may also divide tests based on *type of behavior* you want to test, such as `test_authorization.py`.

The Django test runner looks for files named `test_something.py` by default. It should automatically discover your test files.

For the tests you wrote in the Polls tutorial, divide the tests
into separate files based on what is tested:
```listing
polls/
    tests/
        __init__.py        - this can be an empty file
        test_question.py   - tests of Question model
        test_choice.py     - tests of Choice model
        test_views.py      - tests of views
```

and then delete `tests.py` or rename it so it won't be run, e.g. 'old-tests.py'.

**4. Modify imports in test files**

Since the tests are now in their own package, you will need
to modify the imports in your tests.

Old Import:
```python
# OLD: this won't work
from .models import Question, Choice, Vote
```
New Import:
```python
# NEW: import from named package
from polls.models import Question, Choice, Vote
```

**5. Run the Tests and Verify They Work**

Run `manage.py test app_name` and verify that it discovers all tests, e.g.
```
python manage.py test -v 2 polls
```
The `-v 2` is optional; it displays one line for each test method run.


### Reorganize Models

You can refactor your models classes into individual files, instead of putting them all in `models.py`.  

This is described in [Divide Models and Views into Separate Files](organize-django-code).
