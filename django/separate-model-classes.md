---
title: Separate Model Classes into Individual Files
---

The default organization of a Django "app" is for all model classes
to be defined in a single file named `models.py`.

This has a couple of drawbacks:

1. As you application grows this file becomes large and harder to read or navigate.

2. When working with a team, different team members will add models using different branches of the git repo.  Merging these branches may produce conflicts.  
   - Even without conflicts, every time you change one model class the file needs to me merged.

## Separate Model classes into Separate Files

Using the Django polls app as an example

```python
from django.db import models

class Question(models.Model):
    question_text = models.TextField(max_length=80)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=80)
    votes = models.IntegerField(default=0)
```

our project organization would look like this:
```
ku-polls/
    manage.py
    polls/
       __init__.py
       apps.py
       forms.py
       models.py
       tests.py
       views.py
```

We will split `models.py` into separate files for each class, and put all models in a subdirectory named `models`.  The project will look like this:

```
ku-polls/
    manage.py
    polls/
       __init__.py
       apps.py
       forms.py
       tests.py
       views.py
       models/
           __init__.py
           question.py
           choice.py
```

Some extra code is needed to address one or two issues:

1. We want the other code to refer to models the same way as before.  That is, we want to be able to write:
   ```python
   from polls.models import Question
   from lists.models import Choice
   ```

2. This one may no longer be an issue. Django migrations needs to locate the models and associate them with the correct database table.  And we don't want to change the table names.
    - The default table names are `app_model` such as `polls_question` lists_todo` and `lists_todolist`.

## 1. New code for `models/__init__.py`

So that other code can still use "`from polls.models import Question`" we want to make the models package look like a single module.  
In  `models/__init__.py` write:

```python
# in models/__init__.py
from .question import *
from .choice   import *
```
If you want to write specific imports (as Google recommends) write:

```python
from .question import Question
from .choice   import Choice
```

Inside of Choice, you may also need a relative import:

```python
from .question import Question

class Choice(models.Model):
```

## 2. Meta-class Information for Database Table Names

This `Meta` class information may not be necessary in current versions of Django.

According the [wiki page][splitting-model-data], the Django code has been modified to detect this automatically.

In 2020, I tried using separate model classes (as above) without this "Meta" information -- migrations worked and the table names are what you would expect. 
In an earlier test using Django 2.2.2, the Meta class *was* needed for correct table names in the database.

The issue was:

Django creates a table for each model class using a table name in the form `app_classname`, such as `polls_question`.  When the model class is in a subfolder, it would deduce the app name incorrectly and misname the tables.

To fix this (which you can still use to change the default table names),
you would add a `class Meta` inside each model class with these 2 values: 

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
        For models split into separate files, specify table name and app name.
        See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "polls_question"
        app_label = "polls"
```

Similarly for the Choice class in file `models/choice.py`.

## Separating Views and Tests

Separating views is just like separating models, but you can combine several view functions in one file if you prefer.  The real benefit is separate views for different "features" so your team can work on features in branches without merge conflicts.

Separating tests is even easier.  You can use an empty `__init__.py` file in the `tests/` folder, because nothing needs to import tests.

You should name test files using Django's naming convention, so they will be autodiscovered.  For example:
```python
    manage.py
    polls/
       __init__.py
       apps.py
       forms.py
       models/
           __init__.py   (import model classes into this file)
           question.py
           choice.py
       tests/
           __init__.py   (file can be empty)
           test_question.py
           test_voting.py
           test_views.py
       views/
           __init__.py   (import views into this file)
           index_view.py
           details.py
           results.py
```


## Reference

[Cookbook - Splitting Models across multiple files][splitting-data-models] from the Django [code wiki][django-code-wiki]. (2011)

[splitting-data-models]: https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles

[django-code-wiki]: https://code.djangoproject.com/wiki/
