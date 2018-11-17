## Organize Unit Tests

When you create a new app, Django creates a `tests.py` file for the app.
However, putting all your tests in one file is probably not a good idea.

A better approach is to divide your tests into multiple files.  
For the Django Polls tutorial, the recommended structure for tests would be:
```
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
        

### 1. Put your tests in a folder named `tests`

For the Django Polls tutorial, the folder would be `polls/tests`.
Inside the folder create a `__init__.py` file so that folder is a package.
An empty file is OK.

### 2. Name your test files `test_*.py`

By default, the Django test runner looks for files named `test_something.py`.
This is **not the standard naming** for Python unit tests (should be something_test.py), but it will enable tests to run without more configuration.

Since the tests are now in their own package, you may need
to modify the `import` statements in your tests.  
For example:
```
# OLD: this won't work
from .models import Question, Choice

# NEW: import from named package
from polls.models import Question, Choice
```

### 3. Move Existing tests from `tests.py` to files in `tests/` Directory

Move your tests from `tests.py` to files with descriptive names,
and then **delete** tests.py.

### 4. Run the Tests

Run `manage.py test app_name` and it will "discover" all tests
in the app_name/tests folder, e.g.:
```
python manage.py test polls
```


## Reference

This StackOverflow page has additional information about organizing tests:
[Organizing Django Unit Tests](https://stackoverflow.com/questions/5160688/organizing-django-unit-tests/20932450#20932450)

[Testing in Django - Part 1: Best Practices](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/) example using this test organization. Article also describes use of `coverage` for code coverage and Selenium for UI testing.
