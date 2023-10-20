---
title: Separate Django models, views, tests into Multiple Files
---

When you create a new app, Django creates `models.py`, `views.py`, and `tests.py` files for your code.
Putting all your models, views, or tests in the same file is usually 
not a good idea, especially on a team project with many people working 
on different features.

A better way is to **divide your code** into multiple files.  
For example, if we separated tests into individual files the
structure might be:
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

- [Divide App Code into Multiple Files](#divide-app-code-into-multiple-files) shows the structure
- [Reorganize Models](#reorganize-models) how to refactor models into a `models` package
- [Reorganize Tests](#reorganize-tests) how to refactor tests

[Cookiecutter Templates Project](https://cookiecutter.io/templates)
and [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
have more ideas on project setup and organization.


## Divide App Code into Multiple Files

Here is an example for the 'polls' app:

```
     BEFORE                AFTER
polls/                polls/
    __init__.py           __init__.py
    apps.py               apps.py
    forms.py              forms.py
    models.py             models/
                              __init__.py
                              question.py
                              choice.py
                              vote.py
    tests.py              tests/
                              __init__.py
                              test_question.py
                              test_choice.py
                              test_vote.py
                              test_views.py
    views.py              views/            (*) 
                              index.py
                              detail.py
                              results.py
```
`(*)` dividing views may not be needed if the file is small.

To the rest of your application, the code looks the same!
When you finish, you'll still be able to use `from models import Question` exactly as in the original code. Similarly for views and tests.


## Divide Models into Separate Files

Using the Django polls app as an example

```python
from django.db import models

class Question(models.Model):
    # code for Question class
    ... 

class Choice(models.Model):
    # code for Choice class
    ... 
```

1. In the `polls` app, create a subdirectory named `models`. This will be a Python "package".

2. Separate the code in `models.py` into one file for each class, such as `models/question.py`, `models/choice.py`, `models/vote.py`.
   ```
   polls/
        models/
            __init__.py
            question.py
            choice.py
            vote.py
   ```
3. To make the models package *look like* the original models *module*, you need some code in `__init__.py`.  This is critical to making the change transparent to your other code and to Django migrations.
   ```python
   # in models/__init__.py
   from .question import Question
   from .choice   import Choice
   from .vote     import Vote
   ```
   If there is anything else in `models` that other parts of your code need to import, add those imports to `__init__.py` as well.

4. Modify Imports in the Model Classes.
   Inside of choice.py, you need a relative import for other models:
   ```python
   from .question import Question
   ```
   and similarly for any other imports. Add imports to each model file.

5. Run your tests.  Do they still pass?


**Optional: Meta-class Information for Database Table Names**

This `Meta` class information is not necessary in Django 3.x and newer, but it *used* to be required. Its included for reference (may be useful in other situations).

This [wiki page][splitting-model-data] states that Django code has been modified to automatically detect when models are in a package.  When I tried this in 2020 (Django 3.x), the Meta class info was not necessary.  For Django 2.2, the Meta class *was* needed. 

The issue was:

Django creates a table for each model class using a table name in the form `app_classname`, such as `polls_question` and `polls_choice`.  When the model class is in a subfolder, it would infer the app name incorrectly and misname the tables.

To preserve the default table names,
you would add a `class Meta` inside **each** model class with 2 values: 

- `db_table` = name of the database table
- `app_label` = name of the "app" for this table

```python
# File: polls/models/question.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=80)
    ...
    
    class Meta:
        """
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "polls_question"
        app_label = "polls"
```

Similarly for other models.


## Divide Views and Tests

Dividing views is just like dividing models, but you can combine several view functions in one file if you prefer.  The real benefit is separate views for different "features" so your team can work on features in branches without merge conflicts.

Separating tests is easy!  You can use an empty `__init__.py` file in the `tests/` folder, because nothing else needs to import tests.

You should name test files using Django's naming convention, so they will be autodiscovered.  For example:

```python
    manage.py
    polls/
       tests/
           __init__.py     (this file can be empty)
           test_question.py
           test_voting.py
           test_views.py
       views/
           __init__.py     (import views into this file)
           index_view.py
           details.py
           results.py
```

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


## Reference

[Cookbook - Splitting Models across multiple files][splitting-data-models] from the Django [code wiki][django-code-wiki]. (2011)

[splitting-data-models]: https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles

[django-code-wiki]: https://code.djangoproject.com/wiki/
