---
title: Separate Django models, views, tests into Multiple Files
---

When you create a new app, Django creates `models.py`, `views.py`, and `tests.py` files for your code.
Putting all the models, views, or tests in a single file is usually 
not a good idea, especially on a team project with many people working 
on different features.

A better way is to **divide your code** into multiple files.  

For example, we can separate tests into individual files like this:
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
Then, if one developer writes new tests for questions it won't conflict with another developer's tests for views.

The following sections explain how to do this.

- [Divide App Code into Multiple Files](#divide-app-code-into-multiple-files) shows the structure
- [Separate Models](#separate-models) how to refactor models into a `models` package
- [Separate Tests](#separate-tests) how to refactor tests
- [Separate Views](#separate-views) how to refactor views

[Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
has more ideas on project setup and organization.


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
    views.py              views/
                              index.py
                              detail.py
                              results.py
```

All of these are **optional**. For example, you can divide models and tests but leave the views in a single file (so you can enjoy merge conflicts :-).

If you make the changes carefully, they are invisible to the rest of your
application and you won't need to change any imports.

You'll still be able to write `from models import Question` exactly as in the original code. 


## Separate Models

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

2. In `models/`, create one file for each model class and move the code to that file: `models/question.py`, `models/choice.py`, `models/vote.py`.
   ```
   polls/
        models/
            __init__.py
            question.py
            choice.py
            vote.py
   ```
3. To make the models package *look like* the original models *module* so we can write `from models import Question`, you need some code in `__init__.py`.  This is critical to making the change transparent to your other code and to Django migrations.
   ```python
   # in models/__init__.py
   from .question import Question
   from .choice   import Choice
   from .vote     import Vote
   ```
   If there is anything else in `models` that other parts of your code need to import, add those names to `__init__.py` as well.

4. Modify Imports in each Model Model Class.
   Inside of choice.py, you need a *relative import* for other models:
   ```python
   from .question import Question
   ```
   and similarly for any other imports. Add necessary imports to each model file.

5. Run your tests.  Do they still pass?


## Separate Views

Dividing views into separate files is just like dividing models, but you can combine several view functions in one file if you prefer.  
The real benefit is to separate views for different "features" so your team can work on features in branches without merge conflicts.

You will need imports in `views/__init__.py` to make the views look like a single module.

```
    polls/
       views/
           __init__.py     (import other views into this file)
           index_view.py
           details.py
           results.py
```

## Separate Tests

Separating tests is easy!  You can use an empty `__init__.py` file in the `tests/` folder, because nothing else needs to import tests.  You *will* need to modify the imports *inside* the test code.

You should name test files using Python's naming convention, so they will be autodiscovered.  For example: `test_question.py` and `test_voting.py`.

1. Put your tests in a folder named `tests`, e.g. `polls/tests`.

2. Move the `tests.py` file to the `tests` folder

3. Divide your tests into separate files based on target or type
   - Separate `tests.py` into `test_question.py` (tests for Question),
`test_index_view.py` (tests for a specific target), etc.
   - You can divide tests based on *type of behavior* you want to test, such as `test_authorization.py`.

4. Modify imports in the test code files

   Since the tests are now in their own package, you will need to modify the imports in your tests.

   Old Import in "tests.py":
   ```python
   # OLD: this won't work
   from .models import Question, Choice, Vote
   ```
   New Import:
   ```python
   from polls.models import Question, Choice, Vote
   ```

5. Run the Tests and Verify They Work

   - Run `manage.py test app_name` to verify that it discovers all tests.
   - Example: `python manage.py test -v 2 polls`



## Reference

[Cookbook - Splitting Models across multiple files][splitting-models] from the Django [code wiki][django-code-wiki]. (2011)

[splitting-models]: https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles

[django-code-wiki]: https://code.djangoproject.com/wiki/


## Not Necessary: Meta-class Information for Database Table Names

In Django before version 3, if you refactor model classes into a separate package, it would effect the default table names in the database.  
To prevent that, you can specify the table name in the class's "meta" information.

This is not necessary for Django 3 and newer, but its included here for reference.  It might be useful for other situations.

From this [Django wiki page][splitting-models], the issue was:

Django creates a table for each model class using a table name in the form `app_classname`, such as `polls_question` and `polls_choice`.  When the model class is in a subfolder, it would infer the app name incorrectly and misname the tables (e.g. `polls_models_question`).

To preserve the default table names, add a `class Meta` inside **each** model class with 2 values: 

- `db_table` = name of the database table
- `app_label` = name of the "app" for this table

```python
# File: polls/models/question.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=80)
    
    class Meta:
        """
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "polls_question"
        app_label = "polls"
```

Similarly for other models.
