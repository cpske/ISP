---
title: Authentication in Django
---

Django provides an authentication system, which you can combine with your own forms (UI) and different authentication "backends".

Django's authentication provides for user login, logout, sign-up, and password reset.  It consists of:

* **User** and **Group** models that store user info
* **views** (url handlers) and Forms for login, logout, changing password, and others
* **session middleware** to associate users with sessions
* **decorators** (for your view code) to require login or validate authorization before a view can be used.
* **password validators** for things like minimum password length


[Django Auth Docs][django-user-auth] has details with examples.
The [MDN Django Auth Tutorial][mdn-auth-tutorial] is a good introduction.


## Steps to Use Authentication in Django

- [Enable Authentication](#enable-authentication)
- [Add Default Redirects for KU Polls](#add-default-redirects-for-ku-polls)
- [Create a Template for Login](#create-a-template-for-login)
- [Add User Greeting to a Templates](add-user-greeting-to-a-template) and a link to login
- [Require Login in Views](#require-login-in-views) a user most login to vote

6. Add authentication checks in your views. For example, require that a visitor be logged in order to access some view(s).

### Enable Authentication

1. In your site's `settings.py` file check that `INSTALLED_APPS` includes `django.contrib.auth`
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',        <--- Authentication app
       ...
   ]
   ```

2. If you add `django.contrib.auth` to settings.py, you need to run **makemigrations** and **migrate** to create database tables for User and Group.

3. In `settings.py` you need two middleware components. Usually these are included by default:
   ```python
   MIDDLEWARE = [
       ...
       # SessionMiddleware manages sessions spanning multiple requests
       'django.contrib.sessions.middleware.SessionMiddleware',
       # AuthenticationMiddleware associates a user with session and requests
       'django.contrib.auth.middleware.AuthenticationMiddleware',
       ...
   ]
   ```

3. Enable at least one **authentication backend** to authenticate users.   
   The "ModelBackend" provides standard password-based authentication:
   ```python
   AUTHENTICATION_BACKENDS = [
       # username/password authentication
      'django.contrib.auth.backends.ModelBackend',  
   ]
   ```

4. In your site `urls.py` file, add the `auth` views. By convention, `accounts/` is the prefix for these URLs:
   ```python
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('accounts/', include('django.contrib.auth.urls')),  <-- auth views
       ...,
   ]
   ```
   `django.contrib.auth.urls` defines several URLs. The most important ones to get started are:
   ```python
   accounts/login/                  [name='login']
   accounts/logout/                 [name='logout']
   ```

5. Each `auth.urls` view requires a form named `form`.  You need to provide a **template** for each view to display the form and send results back to the view.
   ```
   URL                  View        Template
   /accounts/login      login       templates/registration/login.html
   /accounts/logout     logout      templates/registration/logged_out.html
   This url and view is not provided by Django:
   /signup              signup      templates/registration/sign_up.html
 

### Add Default Redirects for KU Polls

After a user "logs in", what page should he be shown?

The default is redirect to `/accounts/profile`, which does not exist.

After a user logs in, redirect the browser to the polls index.

1. In `settings.py` specify a default redirect page:
   ```python
   LOGIN_REDIRECT_URL = '/polls/'    # after login, show list of polls
   LOGOUT_REDIRECT_URL = '/'         # after logout, direct to where?
   ```

2. **Alternative: Use URL names** instead of *hard-coding* the `/polls/` URL, you can use a URL name (from urls.py):
   ```python
   LOGIN_REDIRECT_URL = 'polls:index'  # after login, show list of polls
   ```

**Note:** If the login `request` object contains a `next` key, the Django login view will redirect to the URL specified by `next` instead of the default redirect.


### Create a Template For Login 

Optionally also create a "Logged Out" or "Sign up" template.

6. Create directories `templates` and `templates/registrion` in your application top-level folder:
   ```
   ku-polls/
       mysite/
       polls/
       templates/             <--- new directory (maybe)
           registration/      <--- new directory
   ```

7. In `mysite/settings.py` include the templates directory:
   ```python
   TEMPLATES = [
       {
           # old way: 'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'DIRS': BASE_DIR / "templates")],
           'APP_DIRS': True,
           ...
       }
   ]
   ```

8. Create a `login.html` template in `templates/registration`
   ```
   ku-polls/
       templates/
           registration/
               login.html       <--- create this
               logged_out.html  <--- (do this later)
   ```
   The simplest login template is:
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
   {# If you have a password_reset template, then add a link here #}
   </body>
   </html>
    ```
   {% endraw %}
   Nicer Page Template: rendering the form as an html table looks nicer than paragraphs.  You can replace `form.as_p` with this:
   {% raw %}
   ```html
     <table>
     {{ form.as_table }}
     </table>
    ```
   {% endraw %}

9. **Test it.** Start the Django server and navigate to `localhost:8000/accounts/login/`.
   - It should show a Login form.

10. [Create a user](#create-a-user).  Here is how to create a user with the Django interactive shell. This code creates is a user named "harry" with password "hackme22".
   ```bash
   $ python manage.py shell

   from django.contrib.auth.models import User

   # username and email fields are required, others are optional.
   # Use named parameters to avoid errors.
   user = User.objects.create(username='harry', 
                              email='harry@hackerone.com',
                              first_name="Harry")
   user.set_password("hackme22")
   user.save()
   ```

Django also has a `User.objects.create_user()` method where you can specify the password as a named parameter.

11. **Login as this User**.


### Add User Information to a Template

Show the username in your templates. If a user is not logged in, then add a link to Loginl
- If you have a global `base` template, add it there.

Inside HTML templates access user information, such as:
{% raw %}
```
{{ user }}                     - reference to user object, never null
{% if user.is_authenticated %} - true if user is logged in
{{ user.username }}            - the user login name or empty string
{{ user.first_name }}          - may be an empty string 
```
{% endraw %}

In your `base` template or your polls `index` template, 
greet the user or ask him to login:
{% raw %}
```html
{% if user.is_authenticated %}
   Welcome back, {{ user.username }} 
{% else %}
   Please <a href="{% url 'login' %}?next={{request.path}}">Login</a>
{% endif %}
```
{% endraw %}

In the login link we added a **query parameter**: {% raw %}`?next={{request.path}}`{% endraw %}

The `next=path` tells Django's login view that after login to come back to this page.  Otherwise, it will redirect him to the default page (in settings.py).

**Note:** This only works if your `login.html` template *also* passes `next` to the Django login view. See the code above.


### Require Login in Views

You can require a user to login to access some views.  In KU Polls, 
we require a user to login before voting.

There are 3 ways to do it.

1. **`@login_required`** annotation for view methods.
   ```python
   from django.contrib.auth.decorators import login_required

   @login_required
   def vote(request, question_id):
       """Vote for a choice on a question (poll)."""
   ```

2. **Mixin** for class-based views.
   ```python
   from django.contrib.auth.mixins import LoginRequiredMixin

   class DetailView(LoginRequiredMixin, generic.DetailView):
       """Class based view for viewing a poll."""
       model = Question
       template_name = 'polls/detail.html'
   ```

3. **Code**.  The `request` parameter **always** contains a `user` attribute, even if no one is logged in.
   ```python
   def vote(request, question_id):
       """Vote for a choice on a question (poll)."""
       user = request.user
       if not user.is_authenticated:
          return redirect('login')
   ```

---

### Create a User

You can use these methods in a Python function or the Django shell.

**User.objects.create\_user** convenience method:

```python
from django.contrib.auth.models import User

# Use named parameters to avoid errors.
# username and email fields are required, others are optional.
user = User.objects.create_user( 'username', 
          email='email@some.domain', 
          password='password')

# set optional attributes
user.first_name = "Harry"
user.last_name = "Hacker"
user.save()
```

**User.objects.create**:
```
user = User.objects.create(username='username', 
                           email='email@some.domain') 
user.set_password("secret")
user.first_name = "Harry"
user.save()
```

Other ways to create users are:

- add a registration or "sign-up" page to your app
- using the admin interface
- use a data fixture and `manage.py loaddata` to read the file


### Adding a "Sign-up" Page

In most apps it is better to use OAuth than to let users create local
accounts.  If you do need to let people create accounts, here is an
example of how.

1. In your project `urls.py` file add a "signup/" url:
   ```python
   urlpatterns = [
      ...
      path('accounts/', include('django.contrib.auth.urls')), 
      path('signup/', views.signup, name='signup')
   ]
   ```

2. Create a view to handle the `signup` URL.  Put this `views.py` in the same directory as `urls.py` (e.g. mysite).  Add this function in `views.py`.
   ```python
   from django.shortcuts import render, redirect
   from django.contrib.auth import login, authenticate
   from django.contrib.auth.forms import UserCreationForm
   
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
       return render(request, 'registration/signup.html', {'form':form})
   ```
   An important thing here is that the view uses Django's UserCreateForm, and passes this form to the template for rendering.

3. Create a `signup.html` form.  This form is rendered by `signup()` (above) in response to a GET request (GET /signup). In `templates/registration/signup.html` write:
   {% raw %}
   ```html
   {% extends 'base.html' %}

   {% block content %}
   <h2>Register</h2>
   <form method="POST">
       {% csrf_token %}
       <table style="padding: 2ex;">
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
   If you don't have a global `base.html` for your templates, then omit the "extends", "block", and "endblock" statements.



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


### LoginRequired Mixin to Require Login for Class-based Views

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

[User Authentication and Permissions](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication) in the  MDN Django Tutorial, Part 8. This tutorial is very good, with more explanation than the Django official tutorial.

William Vincent [Django Sign Up Tutorial][signup_tutorial] shows another way of implementing a "Sign Up" view as a separate app.  He uses a class-based view for sign-up which is very simple.

William Vincent [Login/Logout Tutorial][auth_tutorial] has same info as this doc but also uses a `base.html` to structure page templates.


[django-user-auth]: https://docs.djangoproject.com/en/4.1/topics/auth/
[mdn-auth-tutorial]: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
[auth_tutorial]: https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/
[signup_tutorial]: https://wsvincent.com/django-user-authentication-tutorial-signup/

