## Django Users and Authentication

### Django Configuration for Users and Authentication

For authentication of users you need at least one authentication "backend" application.
The standard app included with Django is:
```python
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # username/password authentication
)
```

After adding this backend you need to run **migrations** to update the database schema.

To validate user password, add one or more PASSWORD_VALIDATORS.

You also need two middleware applications for interface to your python code.

```python
MIDDLEWARE = [
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ...
    ]
```

### Creating a User

```python
from django.contrib.auth.models import User

user = User.objects.create_user('username', 'email@some.domain', 'password')

# set other attributes
user.first_name = "Joe"
user.last_name = "Hacker"
user.save()
```

### Require Login to Access a View

1. Using a decorator

from django.contrib.auth.decorators import login_required

```python
@login_required
def some_view(request):
```

this redirects the user to a login url, specified by the `LOGIN_URL`
variable in `settings.py`.  The default is:
```
LOGIN_URL = '/accounts/login/'`
```

2. Using a Mixin on class-based views.

For a class-based view, use:

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class MyView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'   # this is the default
```

3. Getting the logged in user in a view. (Requires AuthenticationMiddleware)

```python
@login_required(login_url='/accounts/login/') 
def vote(request, question_id):
    """Vote for one of the answers to a question."""
    user = request.user
    print("current user is", user.id, "login", user.username)
    print("Real name:", user.first_name, user.last_name)
```



### Assignment

1.  What database tables does the django.contrib.auth "backend" add to your database?  
    - perform the migration and then use a database browser to view the schema
2.  What is the name of the table containing user names and hashed passwords?
3.  What fields are in the "users" database table?
    - by default, when you register a new user it only requires a username and password.  
