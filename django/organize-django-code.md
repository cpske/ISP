---
title: Separate Django models, views, tests into Multiple Files
---

The default organization of a Django "app" is for all model classes
to be defined in a single file named `models.py`.

This has a couple of drawbacks:

1. as models grow, its harder to read and navigate.

2. on a team, merge problems and conflicts. Many feature branches may change the models in different ways. 

[Divide Models into Multiple Files](#divide-models-into-separate-files)

[Divide Views and Tests into Multiple Files](#divide-views-and-tests)

[Cookiecutter Templates Project](https://cookiecutter.io/templates)
and [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django)
have more ideas on project setup and organization.



## Divide App Code into Multiple Files

Here is an example for the 'polls' app:

```
     BEFORE                      AFTER
polls/                      polls/
    __init__.py                 __init__.py
    apps.py                     apps.py
    forms.py
    models.py                   models/
                                    __init__.py
                                    question.py
                                    choice.py
                                    vote.py
    tests.py                    tests/
                                    __init__.py
                                    test_question.py
                                    test_choice.py
                                    test_vote.py
                                    test_views.py
    views.py                    views/          (views is optional,
                                    index.py    depending on complexity)
                                    detail.py
                                    results.py
```

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

Split `models.py` into separate files for each class, and put each file in a subdirecory named `models`:

```
ku-polls/
    manage.py
    polls/
       models/
           __init__.py
           question.py
           choice.py
           vote.py
```

The goals are:

1. No change to other code! The other code can refer to models the same way as before. 

2. (This one may no longer be an issue.) Django migrations needs to locate the models and associate them with the correct database table.  And we don't want to change the database table names.
   - The default table names are `polls_question`, `polls_choice`, etc.


**Step 1.  Create a `models` dir and `models/__init__.py`**

The code in `__init__.py` is critical to making the models *package* look like the models *module*. 

```python
# in models/__init__.py
from .question import *
from .choice   import *
from .vote   import *
```
If you want to be **specific** (as Google Python Style Guide recommends) use:

```python
from .question import Question
from .choice   import Choice
from .vote     import Vote
```

**Step 2.  Split models.py into separate files for each class**

For example, `Choice` class should be in `models/choice.py`.

**Step 3. Modify Imports in Model Classes**

Inside of Choice, you may need a relative import for other models:

```python
from .question import Question

class Choice(models.Model):
```

**Optional Step. Meta-class Information for Database Table Names**

This `Meta` class information may not be necessary in current 
versions of Django.

According the [wiki page][splitting-model-data], the Django code has been modified to detect this automatically.  When I tried this in 2020 (Django 3.x), the Meta class info was not necessary.  For Django 2.2, the Meta class *was* needed. 

The issue was:

Django creates a table for each model class using a table name in the form `app_classname`, such as `polls_question`.  When the model class is in a subfolder, it would deduce the app name incorrectly and misname the tables.

To preserve the default table names,
you add a `class Meta` inside **each** model class with these 2 values: 

* `db_table` = name of the database table
* `app_label` = name of the "app" for this table

```python
# File: polls/models/question.py
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=80)
    ...
    
    class Meta:
        """
        For models into separate files, specify table name and app name.
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


## Reference

[Cookbook - Splitting Models across multiple files][splitting-data-models] from the Django [code wiki][django-code-wiki]. (2011)

[splitting-data-models]: https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles

[django-code-wiki]: https://code.djangoproject.com/wiki/
