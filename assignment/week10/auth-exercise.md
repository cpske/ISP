---
title: Add Authentication to the Todo Application
---

Using the Todo app from the midterm exam, add the ability for each
user to have his own todo list.

The steps are:

1. Remove the upstream URL from the Git repository.
2. Add "users" to the Todo application.
   - 2.1 Add Django's built-in authentication. Create a login template.
   - 2.2 Modify todo index view to show the authenticated user. Add links to login and logout.
   - 2.3 For other views, require login to access
3. Modify the domain model so a user owns a collection of "todo".
   - 3.1 Modify models and run migrations.
   - 3.2 Review the "todo" form. Modify it needed.
5. Modify the code to use the domain model.

### 1. Remove the git upstream URL

So you don't accidentally "push" to the exam repository (penalty if you do).
```
git remote remove origin
```

### 2.1 Add Django's built-in authentication

This part is described step-by-step in either of these docs:

* My [Django Authentication summary](https://cpske.github.io/ISP/django/authentication)
* MDN's [Django Tutorial: User authentication](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication) part 8 of their excellent Django tutorial!

### Add one or two local users so you can test login and logout.

Do this using the Django shell (`manage.py shell`):
```python
from django.contrib.auth.models import User
# choose your own username, email, and password
user = User.objects.create_user(
          'username', 
          email='email@some.domain', 
          password='password')

# set other User attributes (at least first name)
user.first_name = "Harry"
user.last_name = "Hacker"
user.save()
```

**Evaluation**: when you finish this you should be able to 

1. login at http://localhost:8000/accounts/login/  and be redirected to Todo index
2. logout at http://localhost:8000/accounts/logout/ and be redirected to a logout page.

### 2.2 Update Views and Templates to Use Authentication

In the todo index page, 
- if user is authenticated then show his name in the heading line, and show list of todo
- also add a "Logout" link so user can logout
- if not authenticated, don't show todo. 

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

To perform an authentication test inside a view:
```python
def someview(request, ...):
    user = request.user
    if user.is_authenticated:
        do something
    else:
        do something_else
```

### 2.3 Require login to access the 'add' and 'done' views

A user must be authenticated to add a todo or change status of a todo.

Use **decorators** on the view methods to require login.

(Wasn't that *easy*?)

**Evaluation**:  As an unauthenticated user
     
1. If you navigate to /todo/ it shows a message that you need to login (with hyperlink)
2. If you navigate to /todo/add/ it redirects to the login page
3. If you navigate to /todo/id/done/ it redirects to the login page

### 3. Revise Domain Model & Views

We want each user to have his own list of Todo.  Draw a UML diagram for this.

We need to

1. update the Todo model and run a migration
2. (maybe) update the TodoForm in `forms.py` 
3. modify the add view to set the user after the form data is submitted
4. modify the index view so it only shows the todos for the logged in user
5. modify the 'done' view so user can only mark his own Todo as 'done'

### 3.1 Update the Todo model. 

This is just like Question - Choice in KU Polls.
The User class is in `django.contrib.auth.models`.
```python
class Todo(models.Model):
    description = models.CharField(...)
    done = models.BooleanField(...)
    user = models.ForeignKey(django.contrib.auth.models.User,
        null=True,
        blank=True,
        on_delete=models.CASCADE)
        )
```

create and run a migration.

### 3.2 Update `TodoForm` in `forms.py`.  

You should check the form after modifying the related model class.
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

### 3.3 Modify `add_todo` so the current user owns the Todo

This method is invoked when a user submits the TodoForm.
The method sets the user attribute of the todo and the done flag.

```python
@login_required
def add_todo(request):
    """Add a new todo. Should be invoked via POST method."""
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # create a todo from the form so we can set
			# specific attributes
            todo = form.save(commit=False)
            todo.user = request.user
            todo.done = False
            todo.save()
            messages.success(request, 
                f"Added \"{request.POST['description']}\"" )
            return redirect('todo:index')
        else:
            ... # same as original code
```

### 3.4 In the `todo_index` view, display only todo owned by the current user

Filter the todos to that the `todo_list` only contains todo owned by the current user, using `request.user`.

You only need a small change to the code. Try to do it yourself.

### 3.5 Modify the "done" view tp verify user owns the todo

In the `done_todo` view, the user must be authenticated and he must be the owner of the todo he is trying to modify.

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
This code uses the Django Messages framework to pass a message to a page template.  Messages is *much easier* than adding a message to the context.


## Forms and Form Processing

The Todo app uses a Form to handle HTML form input for a todo.

The MDN Django Tutorial [Part 9: Working with Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms) explains how to use forms.
They have a diagram of the flow in processing a form:

![Form processing flow-chart](https://mdn.mozillademos.org/files/14205/Form%20Handling%20-%20Standard.png)
