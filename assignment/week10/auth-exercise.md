---
title: Add Authentication to the Todo Application
---

Using the Todo app from the midterm exam, add the ability for each
user to have his own todo list.

The steps are:

1. Remove the upstream URL from the Git repository.
2. Add Django's built-in authentication. Create a login template.
3. Modify todo index view to show the authenticated user. Add links to login and logout.
4. Modify the domain model so a user owns a collection of "todo".
5. Modify the code to use the domain model.

### 1. Remove the git upstream URL

So you don't accidentally "push" to the exam repository (penalty if you do).
```
git remote remove origin
```

### 2. Add Django's built-in authentication

This part is described step-by-step in either of these docs:

* My [Django Authentication summary](https://cpske.github.io/ISP/django/authentication)
* MDN's [Django Tutorial: User authentication](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication) part 8 of their excellent Django tutorial!

You should add one or two local users so you can test login and logout.    
```python
from django.contrib.auth.models import User
# choose your own username
user = User.objects.create_user(
          'username', 
          email='email@some.domain', 
          password='password')

# set other User attributes (optional)
user.first_name = "Harry"
user.last_name = "Hacker"
user.save()
```

**Evaluation**: when you finish this you should be able to 

1. login at http://localhost:8000/accounts/login/  and be redirected to Todo index
2. logout at http://localhost:8000/accounts/logout/ and be redirected to a logout page.

### 3. Update Views and Templates to Use Authentication

In the todo index page, show the user name and only show a list of "todo" if user is authenticated.

Template variables you can use are:
{% raw %}
```html
{{user.first_name}}
{{user.last_name}}

{% if user.is_authenticated %}
   show his todo list with his name in heading line
{% else %}
   ask him to login
{% endif %}
```
{% endraw %}
In a view, to get the URL for the login (or logout) page use
{% raw %}
```html
<a href="{% url 'login' %}">Login</a>
```
{% endraw %}

In your views, add some decorators or "if" tests so that:

* must be authenticated to access the 'add' view
* for the index view, your choice: either require login or render an empty todo_list when visitor is not authenticated.

Recall from the slides that the way to use a decorator is:
```python
@login_required
def someview(request, ...):
```

and to perform an authentication test inside a view:
```python
def someview(request, ...):
    user = request.user
    if user.is_authenticated:
        do something
    else:
        do something_else
```

**Evaluation**:  As an unauthenticated visitor,
     
1. If you navigate to /todo/ it either shows a message that you need to login (with hyperlink), or redirects to login page
2. If you navigate to /todo/add/ it redirects to the login page
3. If you navigate to /todo/id/done/ it redirects to the login page

### 4. Revise Domain Model & Views

We want each user to have his own list of Todo.  Draw a UML diagram for this.

We need to

1. update the Todo model and run a migration
2. (maybe) update the TodoForm in `forms.py` 
3. modify the add view to set the user after the form data is submitted
4. modify the index view so it only shows the todos for the logged in user
5. modify the 'done' view so user can only mark his own Todo as 'done'

4.1 Update the Todo model. This is just like Question - Choice in KU Polls.
The User class is in `django.contrib.auth.models`.
```python
class Todo(models.Model):
    description = models.CharField(...)
    done = models.BooleanField(...)
    user = models.ForeignKey(django.contrib.auth.models.User,
                  null=True,
                  blank=True,
                  on_delete=models.CASCADE))
```

create and run a migration.

4.2 Update `TodoForm` in `forms.py`.  This may not be needed, but you should check the
form after modifying the model.
In this form, the user can set only the todo `description`. The Todo app automatically
sets `done=False` and sets the user.

In `forms.py`:
```python
class TodoForm(forms.ModelForm):
  
    class Meta:
        model = Todo
        fields = ['description'] # the fields to show in form
        exclude = ['done', 'user']
        # custom labels for input fields
        labels = {
            'description': "Description of todo",
        }
```

4.3 When the logged in user submits a todo, it invokes the `add_todo` method.
This method sets the user attribute of the todo and the done flag.

```python
@login_required
def add_todo(request):
    """Add a new todo. Should be invoked via POST method."""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # create a todo from the form so we can set specific attributes
            todo = form.save(commit=False)
            todo.user = request.user
            todo.done = False
            # should log this action
            todo.save()
            messages.success(request, 
                f"Added \"{request.POST['description']}\"" )
            return redirect('todo:index')
        else:
            ... # same as original code
```

4.4 In the `todo_index`, you should filter the todos to that the `todo_list` only contains todo owned by the current user.  Try to do it yourself.

4.5 Modify the "done" view.  
The user must be authenticated and own the todo he is trying to modify.
```python
#todo: require login to access this view
def done_todo(request, todo_id: int):
    """Mark a todo as done, then redirect back to the index page."""
    try:
        todo = Todo.objects.get(id=todo_id)
    except ...
        # same as original code

    # the user must own this todo to modify it
    if todo.user == request.user:
        todo.done = True
        todo.save()
        messages.success(request, f"Todo {todo.id} marked as done")
    else:
        messages.error(request, f"Todo {todo.id} doesn't belong to you")
    ...
```


### Forms and Form Processing

The MDN Django Tutorial [Part 9: Working with Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms) explains how to use forms.
They have a diagram of the flow in processing a form:

![Form processing flow-chart](https://mdn.mozillademos.org/files/14205/Form%20Handling%20-%20Standard.png)
