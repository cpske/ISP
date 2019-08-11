## Validating data in a web app

You should verfiy that input values has the expected and allowed values.
In a web app, you can validate input data:

* client side - using HTML form field validators or Javascript
* server side - in a Django `Form`, in a controller method, or a model

Where are the pros and cons of each?

### Client Side Validation

"User experience" is greatly improved by giving feedback before input
values are sent to the server.  Its also more efficient.

But, your application cannot *rely* on client-side validation because
a hacker can bypass (or edit) your web page and submit data directly,
without valiation.

### Server Side Validation

1. Django Forms
    You can write methods named `clean_property()` where `property` is an attribute of your model (e.g. `clean_name()`). Django will automatically call these methods.  If the data to "clean" is invalid, the method should raise (throw) a ValidationError.

    See Django docs for "Model" for details.

2. Code in a controller ("view").
   You can get data from a user request in a view method and raise exception or return an error status code.

3. Constraints specified in a model.
   There are a couple of ways you can validate data in a model class.  Most Django Field types have attributes you can set, such as:
```python
name = CharField(min_length=2, max_length=40, unique=True)
```
   This would require the value of name to be between 2 and 40 chars long, and no two objects in database table can have the same name.  



### Unit Test for Validation

Suppose we have a `Todo` class with a field `text` that contains a description of a "todo".  To ensure that we never save empty Todo items, we could include a requirement in the Todo model class:

```python
from django.db import models

class Todo(models.Model):
    text = models.TextField(default="", blank=False,
             help_text="Enter description of this todo")
    ...
```

Note: for `blank=False` to be applied you must invoke in code:
    todo.full_clean()


In the unit tests for Todo, use:

```python
import django.core.exceptions

def test_cannot_save_empty_todo(self):
    todo = Todo(text="")
    with self.assertRaises(django.core.exceptions.ValidationError):
        todo.save()
        # hack to force validation of blank=False on textfield
        todo.full_clean()
```

The "with block" runs a block of code.  You could also write:
```python
def test_cannot_save_empty_todo(self):
    todo = Todo(text="")
    try:
        todo.save()
        todo.full_clean()
        self.fail("todo.save should raise ValidationError")
    except self.assertRaises(django.core.exceptions.ValidationError):
        pass
```
