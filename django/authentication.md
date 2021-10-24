---
title: Authentication in Django
---

Django includes an authentication system, which can be combined with your own forms and authentication "backends".

Django's authentication "app" provides support for user login, logout, sign-up,
and password reset.  
It provides:

* **User** and **Group** models that store user info
* **views** (url handlers) and Forms for login, logout, changing password, and others
* **session middleware** to associate users with sessions
* **decorators** to require login or validate authorization before accessing views
* **password validators** for things like minimum password length

The [MDN Django Tutorial][mdn-auth-tutorial] is a good introduction and 
[Django Auth Docs][django-user-auth] have details with examples.

### Steps to Use Authentication in Django

1. Enable the `auth` app, middleware, and authentication backends in `settings.py`.
2. Run migrations if necessary (usually it is not).
3. Add urls for login, logout, etc., in `urls.py`.
4. Add templates for login and logout.  You don't have to do much because Django provides forms.
5. Add authentication checks in your views, such as checking that a visitor is logged in or has permission to perform an action (based on group membership).

## Enable and Use Authentication

1. In your site's `settings.py` file check that `INSTALLED_APPS` includes `django.contrib.auth`
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       ...
   ]
   ```
   - When you add `django.contrib.auth` to a project, you need to **makemigrations** and run **migrations** to create database tables for User and Group.

2. In `settings.py` you need two middleware applications. Usually these are included by default:
   ```python
   MIDDLEWARE = [
   ...
   # SessionMiddleware manages sessions spanning multiple requests
   'django.contrib.sessions.middleware.SessionMiddleware',
   # Associates users with sessions and requests
   'django.contrib.auth.middleware.AuthenticationMiddleware',
   ...
   ]
   ```

3. (**This seems to be the default**) You need at least one **authentication backend** to authenticate users.  The standard password-based backend included with Django is:
   ```python
   AUTHENTICATION_BACKENDS = (
       # username/password authentication
      'django.contrib.auth.backends.ModelBackend',  
   )
   ```
   You can add OAuth authentication by adding the social-auth package or allauth package as another authentication backend. 

4. Include the Django auth views in your URLs. By convention, use `accounts/` as the prefix for these URLs:
   ```python
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('accounts/', include('django.contrib.auth.urls')),
       ...,
   ]
   ```
   `auth.urls` adds several URLs (see below). The most important ones to get started are:
   ```python
   accounts/login/                  [name='login']
   accounts/logout/                 [name='logout']
   ```

5. The `auth.urls` module maps each URL to a view provided by Django. Each view uses a form named `form`.  You need to provide a **template** for each view, to display the form and send results back to the view.
   - Django expects the templates to be in a `registration` folder, and each template has the same name as the view:
     | view  | template (you provide)  |
     |-------|-------------------------|
     | login | login.html              |
     | logout | logged_out.html (called after logout) |
6. Create a `templates` directory in your application top-level folder (`ku-polls/templates`) and enable it in `settings.py` as follows: 
   ```python
   TEMPLATES = [
       {
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           ...
       }
   ]
   ```
  - Also create a `templates/registration` directory.

7. Create a `login.html` template.  Its location should be:
    ```
    project_dir/
        templates/
            registration/
                login.html
                logged_out.html
                ...
    ```
    A basic login template is:
    {% raw %}
    ```html
    <html>
    <body>
    <h2>Login</h2>
    <form method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <p>
      <button type="submit">Login</button>
      </p>
      <input type="hidden" name="next" value="{{next}}"/>
    </form>
    {# If you have written a password_reset template, then add #}
    <p>
    <a href="{% url 'password_reset' %}">Forgot password?</a>
    </p>
    </body>
    </html>
    ```
    {% endraw %}

8. Test this by starting the Django server and navigating to `localhost:8000/accounts/login/`.
   - To create a user who can login see [Create a User Interactively](#create-a-user-interactively) below.

9. After you login at `/accounts/login/`, Django by default redirects you to `/accounts/profile`.  This is usually **not** what you want.    
   To specify a default redirect page after login, in `settings.py` set (this is for the todo app):
    ```python
    LOGIN_REDIRECT_URL = '/todo/'    # KU-Polls: use '/polls/'
    ```
   - If the login request contains a field named `next`, the auth login view will redirect to the URL specified by `next` instead of the default.  That's why there is a hidden field named `next` in the form above (it preserves the value of next from the previous redirect).

10. You can logout by navigating to `/accounts/logout/` but you need a page to redirect to *after* logout.  There are 2 solutions:
    - create a logout page at `/templates/registration/logged_out.html`
    - in `settings.py` set: `LOGOUT_REDIRECT_URL = 'some-existing-view`` (this is usually better)

11. For the **todo** app: Create a logout template located in `/templates/registration/logged_out.html`:
    {% raw %}
    ```html
    <html>
    <body>
    <h2>Logged out</h2>
    <p>
    Want something todo? 
    <a href="{% url 'login'%}">Login again</a>
    </body>
    ```
    {% endraw %}
    - For **KU Polls**: redirect to the polls index page (or page of your choice)
   

### Next Steps

Once you enable login and logout, the next things to do are:

1. [Access user information in views](#access-user-information-in-views) and [templates](#access-user-information-in-templates).
2. Use a decorator to [require login to access a view method]().
   - a simple and reliable way to enforce authentication


### URLs Provided by Django's `auth` Application

Django's `auth` app provides views for each of these URLs:
```python
accounts/login/                  [name='login']
accounts/logout/                 [name='logout']
accounts/password_change/        [name='password_change']
accounts/password_change/done/   [name='password_change_done']
accounts/password_reset/         [name='password_reset']
accounts/password_reset/done/    [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/             [name='password_reset_complete']
```
to use these views you must create a template for each in a folder named `registration`.  
The templates should have the same name as the views: the `login` view 
expects a template named `login.html`.  The login view encapsulates its data in a Form named `form`,
so in your `login.html` template do something like this:
{% raw %}
```
<form method="POST">
  {% csrf_token %}
  <table style="padding: 2ex;">
  {{ form.as_table }}
  </table>
  <button type="submit">Login</button>
  <!-- if your app redirects user to login before accessing some pages, then next contains return url -->
  <input type="hidden" name="next" value="{{next}}" />
</form>
```
{% endraw %}


### Create a User Interactively

You can create a user in code or using the Django shell.
Normally you would use a web Form to add users,
but for prototyping you may want to create a demo user.
In the Django shell (`python manage.py shell`) enter:

```python
from django.contrib.auth.models import User

# The username and email fields are required, others are optional.
# Use named parameters to avoid errors.
user = User.objects.create_user( 'username', 
          email='email@some.domain', 
          password='password')

# set other User attributes (optional)
user.first_name = "Harry"
user.last_name = "Hacker"
user.save()
```


## What is a User?

When you enable the `django.contrib.auth` app and apply migrations, Django will
add database tables for User (`auth_user`), Group (`auth_group`), Permissions (`auth_permissions`) and tables for relations between these.

The model classes in `django.contrib.auth` are:

| Class   | Description      |
|:--------|:-----------------|
| User    | User with first_name, last_name, password, email, id, and date_joined |
| Group   | Group with an id and name. |
| Permission | Permission with id, codename, and permission name. |



### Use a Decorator to Require Login to Access a View

To require a user login before accessing a view, use a `@` decorator:
```python
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login/') 
def vote(request, question_id):
    """Vote for one of the answers to a question."""
    user = request.user
```
The default login_url is `/accounts/login/` so you can **omit it**.
The decorator also sets the `next` field so the user will be redirected
to the same view after logging in.

### Use LoginRequired Mixin to Require Login for Class-based Views

For class-based views use a *mixin* to require authentication:
```python
from django.contrib.auth.mixins import LoginRequiredMixin

class EyesOnlyView(LoginRequiredMixin, ListView):
    # this is the default. Same default as in auth_required decorator
    login_url = '/accounts/login/'
    rest of your view code
```
> **Mixin** is a design style or design pattern where
> functionality from multiple classes is combined into another
> class.  That is, behavior is "mixed in".

### Access User Information in a Template

Inside HTML templates access information about a user using:
{% raw %}
```
{{ user }}                     - reference to user object, not null
{% if user.is_authenticated %} - true if user is logged in
{{ user.username }}            - the user login name or empty string
{{ user.first_name }}          - may be empty string if not set in model
```
{% endraw %}
For example, to greet a user or ask him to login:
{% raw %}
```html
{% if user.is_authenticated %}
   Welcome back, {{ user.username }}
{% else %}
   Please <a href="{% url 'login' %}">Login</a>
{% endif %}
```
{% endraw %}
But, in the above code after logging in the user will be redirected to the default LOGIN_REDIRECT_URL.  To cause the browser to come back to this page after login, append the `next=` query parameter to the login URL:
{% raw %}
```
{% if user.is_authenticated %} 
    Welcome back, {{ user.username }}
{% else %}
    Please <a href="{% url 'login'%}?next={{request.path}}">Login</a>
{% endif %}
```
{% endraw %}
This example shows that you can access the `request` object inside a template, too.

**Note:** This only works if your `login.html` template *also* passes `next` to the Django login view.  You should include a *hidden field* in the template for the `next` field.


### Access User Information in a View

The logged in user is saved as part of the *session* and included in the `request` object (HttpRequest), which is passed to every view.

```python
@login_required
def vote(request, question_id):
    """Vote for one of the answers to a question."""
    user = request.user
    print("current user is", user.id, "login", user.username)
    print("Real name:", user.first_name, user.last_name)
```

### Django Redirects for Login and Logout

The Django `auth` login and logout views will redirect the browser after login or logout.
Specify where to redirect a user after login or logout in `settings.py`:
```python
LOGIN_REDIRECT_URL = '/todo/'
LOGOUT_REDIRECT_URL = '/todo/'
```
Instead of a hard-coded URL, you can use the name of a view.  If the URL does not contain a '/' then Django will look for a named view.  If you have a view named '`home`' then use:
```python
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
```

For a particular `login` or `logout` request, you can specify where to redirect the browser using the `?next=url` query parameter.  For example:
{% raw %}
```
Please <a href="{% url 'login'%}?next={{request.path}}">Login</a>
```
{% endraw %}

### Signing Up a New User

The Django `auth` app has a UserCreateForm with validators that impose some strict criteria on passwords and prevent duplicate usernames.  But you have to provide
your own view (controller) and template to use this form.

In my polls app, I added the view right to top-level urls.py file:
```python
# mysite/urls.py
...
from . import views

urls = [
    ...,
    path('accounts/', include('django.contrib.auth.urls')),  # Django auth app
    path('signup/', views.signup, name='signup'),
    ]
```
and in `mysite/views.py` define a "signup" method that handles both GET and POST requests.  A GET request returns a sign-up form.  

A POST request validates the form data.  If it is valid, then `form.save()` causes the user data to be saved to the Users table (auth_users).  This shows how
forms can simplify code by encapsulating (and inheriting) common actions for
accepting, validating, and saving data.
{% raw %}
```python
def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('password')
            user = authenticate(username=username,password=raw_passwd)
            login(request, user)
            return redirect('polls')
        # what if form is not valid?
        # we should display a message in signup.html
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
```
{% endraw %}

Finally, we need a template for sign-up.  As shown in the above view code,
we inject the UserCreationForm object as a variable named `form`.
You can put the template anywhere you like. As shown in the `render()` function call in the view, I put mine in a subdirectory of `templates/` named `registrations`.  That is, BASE_DIR/templates/registion/signup.html.

A simple user sign-up template is:
{% raw %}
```html
{% block content %}
<h2>Register</h2>
<form method="POST">
    {% csrf_token %}
    <table>
    {{ form.as_table }}
    <tr>
    <td colspan="2">
    <button type="submit">Register</button>
    </td>
    </tr>
    </table>
</form>
{% endblock %}
```
{% endraw %}

The important parts of this template are a) render the form `{{form.as_table}}`
and b) POSTing the form back to the correct URL.  Since the &lt;form method='POST'&gt; block doesn't specify an action, the default action is to send it back to the same URL the page came from.

## Django's Annoying Password Validators

Django provides a collection of *validators* for authentication data.   They are usually:
```python
# settings.py
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```
The password requirements are good but sometimes annoying. You can customize them. Look at the constructors for the validator classes (above) in the file `django/contribe/auth/password_validation.py`.  Each constructor has some named parameters. You can specify a value for those named parameters

| Validator                | Constructor Parameters     |
|:-------------------------|:---------------------------|
| MinimumLengthValidator   | `min_length=0`             |
| UserAttributeSimilarityValidator | `user_attributes=[...],max_similarity=0.7` |
| CommonPasswordValidator  | `password_list_path=path-to-file` |
| NumericPasswordValidator | none |

`NumericPasswordValidator` checks if a password is purely alphanumeric (disallowed).  If you want to allow alphanumeric passwords, comment out the validator.


Don't copy this!  It's for example only.
```python
# if you copy this, you are an idiot

```

---

### Resources

[Django User Authentication System](https://docs.djangoproject.com/en/2.2/topics/auth/default/) https://docs.djangoproject.com/en/2.2/topics/auth/default/.

[User Authentication and Permissions](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication) in Mozilla Django Tutorial, Part 8. This tutorial is very good, step-by-step, with more explanation than the Django official tutorial.

William Vincent [Django Sign Up Tutorial][signup_tutorial] that shows another way of implementing a "Sign Up" view as a separate app.  He uses a class-based view for sign-up which is very simple.

William Vincent [Login/Logout Tutorial][auth_tutorial] has same info as this doc but also uses a `base.html` to structure page templates.


[django-user-auth]: https://docs.djangoproject.com/en/2.2/topics/auth/
[mdn-auth-tutorial]: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
[auth_tutorial]: https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/
[signup_tutorial]: https://wsvincent.com/django-user-authentication-tutorial-signup/


