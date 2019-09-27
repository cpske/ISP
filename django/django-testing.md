## Organize Unit Tests

When you create a new app, Django creates a `tests.py` file for the app.
However, putting all your tests in one file is probably not a good idea.

A better approach is to divide your tests into multiple files.  
For the Django Polls tutorial, the recommended structure for tests would be:
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
```python
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

## Django TestCase

Django has its own TestCase class which you should usually use
instead of Python's `unittest.TestCase`. 
See the Django docs "Testing" section (under "Development Process" in online docs).

You can use Python's `unittest.TestCase` if your tests don't 
interact or change the database.  The Django TestCase uses
transactions and flushing the database, which makes it slower.

Django has 4 test classes:

* `django.test.SimpleTestCase`
* `django.test.TestCase` the usual superclass for your tests
* `django.test.LiveServerTestCase` like TestCase but also starts the Django web server before tests and stops it after tests.
* `django.test.TransactionTestCase` I'm not sure why you'd use this.

## Django Client (`django.test.Client`)

This class has functionality for retrieving a page, without using an HTTP server.  For example:

```python
import django.test.TestCase

class MyTest(django.test.TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertIn('<title>My Home Page</title>', html)

        # This only works if response is retrieved using self.client
        self.assertTemplateUsed(response, 'polls/home.html')
```
django.test.Simple

## Reference

This StackOverflow page has additional information about organizing tests:
[Organizing Django Unit Tests](https://stackoverflow.com/questions/5160688/organizing-django-unit-tests/20932450#20932450)

[Testing in Django - Part 1: Best Practices](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/) example using this test organization. Article also describes use of `coverage` for code coverage and Selenium for UI testing.
