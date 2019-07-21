## Refactoring Django Models to use Separate Classes

The default organization of a Django "app" is for all model classes
to be defined in a single file named `models.py`.

This has a couple of drawbacks:

1. As you application grows this file becomes large and harder to read or navigate.

2. When adding new features on a team, different team members may add models (using different branches of the git repo).  Merging these branches may produce conflicts.  
    - Even without conflicts, every time you change one model class the file needs to me merged.

## Splitting Mdoels into Separate Files

Suppose we have a todo-list application (as in *TDD in Python*) with a `lists` app and two model classes:

```python
from django.db import models

class Todo(models.Model):
    text = models.TextField(default="", ...)
    done = models.BooleanField(default=False)
    # each todo belongs to a todo list
    todo_list = models.ForeignKey('TodoList', on_delete=models.CASCADE,
           null=True, blank=True)

class TodoList(models.Model):
    name = models.CharField(default="", max_length=48, unique=True)
```

our project organization would look like this:
```
list-project/
    manage.py
    lists/
       __init__.py
       apps.py
       forms.py
       models.py
       tests.py
       views.py
       templates/
           (templates for web pages)
```

We will split `models.py` into a separate class for each model and put each class-file in a subdirectory named `models`.  Our project will look like this:

```
list-project/
    manage.py
    lists/
       __init__.py
       apps.py
       forms.py
       tests.py
       views.py
       models/
           __init__.py
           todo.py
           todo_list.py
       templates/
           (templates for web pages)
```

Some extra code is needed to address two issues:

1. Django migrations needs to locate the models and associate them with the correct database table.  And we don't want to change the table names.
    - The default table names are `app_model` such as `lists_todo` and `lists_todolist`.
2. We don't want to change our code that refers to models.  In the default configuration (all models in models.py) we would write:
```python
from lists.models import Todo
from lists.models import TodoList
```
we want that to stay the same!

## 1. Meta-class Information for Django

In each model class add a `Meta` class to specify the app and database table.

* `db_table` - name of the database table
* `app_label` - name of the "app" for this table

```python
# File: models/todo_list.py
from django.db import models

class TodoList(models.Model):
   '''
    A TodoList is a named collection of related todos,
    typically all owned by one person.
    '''
    name = models.CharField(default='', max_length=40, unique=True)
    
    class Meta:
        """For models split into separate files, these two variables must be set.
           See https://code.djangoproject.com/wiki/CookBookSplitModelsToFiles
        """
        db_table = "lists_todolist"
        app_label = "lists"
    
    def __str__(self):
        return self.name
```

Similarly for the Todo class (in file `models/todo.py`).


## 2. New code for `models/__init__.py`

So that our views can use "`from list.models import Todo`" (without naming the actual file containing the Todo class) add code to `models/__init__.py`:

```python
from .todo_list import TodoList
from .todo import Todo
```
The Django wiki page doesn't have a "." in `from .todo_list` for relative import, but in my test the dot is needed.
