## Organize Unit Tests in Django

When you create a new app, Django creates a `tests.py` file for the app.
However, putting all your tests in one file is usually not a good idea.

In particular, on a team project with development done in git branches
you will have conflicts every time you merge a branch into master.

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

In your "app" directory create a folder named `tests`.
For the Django Polls tutorial, the folder would be `polls/tests`.
In the tests folder create an empty `__init__.py` file so that folder is a package (Python doesn't require this but unittest discovery does).

### 2. Move `tests.py` to the `tests` folder

And then divide it into several test files...

### 3. Name your test files `test_*.py`

The Django test runner looks for files named `test_something.py` by default.

For the tests you wrote in the Polls tutorial, divide the tests
into separate files based on what is tested:
```listing
polls/
    tests/
        __init__.py
        test_question.py   - tests of Question model
        test_choice.py     - tests of Choice model
        test_views.py      - tests of views
```

and then delete `tests.py` or rename it so it won't be run, e.g. 'test-orig.py'.

### 4. Modify imports

Since the tests are now in their own package, you will need
to modify relative imports in your tests.
For example:
```python
# OLD: this won't work
from .models import Question, Choice

# NEW: import from named package
from polls.models import Question, Choice
```

### 5. Run the Tests

Run `manage.py test app_name` and verify that it discovers all tests
in the app_name/tests folder, e.g.:
```
python manage.py test -v 2 polls
```
The `-v 2` is optional; it displays one line for each test method run.

## Refactor Models, too?

You can also refactor your `models.py` into a `models` directory and separate files for each class.  

Refactoring models requires some extra work is needed so that you don't need to rewrite your imports and so that Django migrations work.  This is covered in a separate write-up.
