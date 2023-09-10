---
title: Authentication in Django
---

Django provides an authentication system, which you can combine with your own forms (UI) and different *authentication backends* -- like username/password or OAuth.

The Django authentication model includes:

* **User** and **Group** models that store user info
* **Views** and **Forms** for login, logout, changing password, and more
* **session middleware** to associate users with requests
* **decorators** (for your view code) to require login or validate authorization
* **password validators** for things like required minimum password length

[Django Auth Docs][django-user-auth] has details with examples.
The [MDN Django Auth Tutorial][mdn-auth-tutorial] is a great introduction.


## How to Use Authentication in KU Polls

- Step 1. [Enable Authentication](#enable-authentication)
- Step 2. [Add Default Redirects for KU Polls](#add-default-redirects-for-ku-polls)
- Step 3. [Create a Template for Login Page](#create-a-template-for-login-page)
- Step 4. [Add User Greeting to a Templates](add-user-greeting-to-a-template) and a link to login
- Step 5. [Require Login in Views](#require-login-in-views) a user most login to vote

- Extra Material: 
[Create a Sign-up Page for New Users](#create-a-sign-up-page-for-new-users),
[Access User Information in a View](#access-user-information-in-a-view),
[How to Create Users](#how-to-create-users),
[Resources](#resources)


### Enable Authentication

1. In your site's `settings.py` file verify that `INSTALLED_APPS` includes `django.contrib.auth` (add it if necessary):
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',        <--- Authentication app
       ...
   ]
   ```

2. If you added `django.contrib.auth` to settings.py, you need to run **makemigrations** and **migrate** to create database tables for User and Group.

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
       # username & password authentication
      'django.contrib.auth.backends.ModelBackend',  
   ]
   ```

4. In your site `urls.py` file, add the `auth` urls. By convention, `accounts/` is the prefix for these URLs:
   ```python
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('accounts/', include('django.contrib.auth.urls')),  <-- auth views
       ...,
   ]
   ```
   `django.contrib.auth.urls` defines several URLs. The most important ones to get started are:
   ```python
   accounts/login/                  name='login'
   accounts/logout/                 name='logout'
   ```

5. Each `auth.urls` has a **view** that provides a **form** named `form`.  You need to provide a **template** for each view to display the form and send results back to the view.
   ```
   URL                  View        Template
   /accounts/login      login       templates/registration/login.html
   /accounts/logout     logout      templates/registration/logged_out.html
   ```

### Add Default Redirects for KU Polls

After a user "logs in", what page should he be shown?

The default is redirect to `/accounts/profile`, which does not exist.

In `settings.py` specify defaults for login and logout.  Two syntaxes:

1. Specify the default redirect page as a path:
   ```python
   LOGIN_REDIRECT_URL = '/polls/'    # after login, show list of polls
   LOGOUT_REDIRECT_URL = '?'         # after logout, direct to where?
   ```

2. **Use URL names** instead of *hard-coding* paths.  This is better:
   ```python
   LOGIN_REDIRECT_URL = 'polls:index'  # after login, show list of polls
   LOGOUT_REDIRECT_URL = 'login' 
   ```

**Note:** If the login `request` object contains a `next` key, the Django login view will redirect to the URL specified by `next` instead of the default redirect.

### Create a Template For Login Page

6. Create directories named `templates` and `templates/registration` in your application top-level folder:
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
           'DIRS': [BASE_DIR / 'templates'],
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
    {# If you have a sign-up page, then add a link here #}
   </body>
   </html>
    ```
   {% endraw %}
   Nicer Page Template: you can render the form as an html table. You can replace `form.as_p` with this:
   {% raw %}
   ```html
     <table>
     {{ form.as_table }}
     </table>
    ```
   {% endraw %}

9. **Test it.** Start the Django server and navigate to `localhost:8000/accounts/login/`.
   - It should show a Login form.

10. [Create a user](#create-users).  Here is how to create a user with the Django interactive shell. This code creates is a user named "harry" with password "hackme22".
    ```bash
    $ python manage.py shell

    from django.contrib.auth.models import User

    # username field is required, others are optional.
    # Use named parameters to avoid errors.
    user = User.objects.create(username='harry', 
                              email='harry@hackerone.com',
                              first_name="Harry")
    user.set_password("hackme22")
    user.save()
    ```
    See below for other ways to create users.

11. **Test it:** Login as this User.


### Access User Information in a Template

Show the username in your templates. If a visitor is not logged in, then show a link to Login.
- If you have a global `base` template, add this to the base template.

Inside page templates access user information, such as:
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

The `next=path` tells Django's login view that after login to come back to this page.  Otherwise, it will redirect him to the default `LOGIN_REDIRECT_URL`.    
(*`next` only works if your `login.html` template also passes `next` to the Django login view function.*)


### Require Login in Views

You can require a user to login to access some views.  In KU Polls, 
we require a user to login in order to vote.

1. Before your `vote` view add the `@login_required` **annotation**:


   ```python
   from django.contrib.auth.decorators import login_required

   @login_required
   def vote(request, question_id):
       """Vote for a choice on a question (poll)."""
   ```

2. **Test it**. If you are **not** logged in, when you try to submit a vote you should be directed to the login page.


**Two Other Ways** to require login in views:

1. For a class-based views use the `LoginRequired` **Mixin**.
   ```python
   from django.contrib.auth.mixins import LoginRequiredMixin

   class DetailView(LoginRequiredMixin, generic.DetailView):
       """Class based view for viewing a poll."""
       model = Question
       template_name = 'polls/detail.html'
   ```

2. **Use Python Code**.  The `request` parameter always contains a `user` attribute, even if no one is logged in.
   ```python
   def vote(request, question_id):
       """Vote for a choice on a question (poll)."""
       user = request.user
       if not user.is_authenticated:
          return redirect('login')
   ```

---

Extra Material


### Create a Sign-up Page for New Users

These steps describe how to enable visitors to create their own local account.
In most apps it is better to use OAuth so that visitors can login using
their Google, Github, Facebook, etc., account.  
Enabling OAuth is *suprisingly easy* to do in Django.

To enable visitors to create a local account:

- define a url for a "Sign up" page
- create a view to handle this page
- create a page template for the sign-up page
 

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
               # get named fields from the form data
               username = form.cleaned_data.get('username')
               # password input field is named 'password1'
               raw_passwd = form.cleaned_data.get('password1')
               user = authenticate(username=username,password=raw_passwd)
               login(request, user)
              return redirect('polls')
           # what if form is not valid?
           # we should display a message in signup.html
       else:
           # create a user form and display it the signup page
           form = UserCreationForm()
       return render(request, 'registration/signup.html', {'form': form})
   ```
   The important thing here is that the view uses Django's UserCreationForm, and passes this form to the template for rendering.  `UserCreationForm` provides code to validate and clean input data.

3. Create a `signup.html` template containing a sign up form.  The `signup` view (above) renders this template when the user visits /signup, and re-renders the page if a POST request finds any problems in the form data.    
   In `templates/registration/signup.html` write:
   {% raw %}
   ```html
   <h2>Register</h2>
   <form method="POST">
       {% csrf_token %}
       <table style="padding: 2ex;">
       {{ form.as_table }}     {# this line shows the sign-up form #}
       <tr>
       <td colspan="2">
       <button type="submit">Register</button>
       </td>
       </tr>
       </table>
   </form>
   ```
   {% endraw %}

The important parts of this template are 
- render the form: `form.as_table`
- POST submits the form back to the same URL that the request came from (since there is no `action=...` parameter)

---

### How to Create Users

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

**User.objects.create** method:
```
user = User.objects.create(username='username', 
                           email='email@some.domain') 
user.set_password("secret")
user.first_name = "Harry"
user.save()
```

Other ways to create users are:

- add a registration or "sign-up" page to your app
- the admin interface
- use a data fixture and `manage.py loaddata` to read user data from a file

---

### URLs in Django's `auth` Application

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

to use these views you must create a template for each in a folder named `templates/registration`.  
The templates should have the same name as the view: the `login` view 
expects a template named `login.html`.  The login view encapsulates its data in a Form named `form`,
so in your `login.html` template do something like this:
{% raw %}
```html
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


## Django's Password Validators

Django provides a collection of *validators* for authentication data.   
They are defined in `settings.py`, usually:
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
These password requirements are good but sometimes annoying. You can customize them. 

Look at the constructors for the password validator classes in the file `django/contribe/auth/password_validation.py`.  Each constructor has some named parameters. You can specify parameter values to customize the validators.

| Validator                | Constructor Parameters     |
|:-------------------------|:---------------------------|
| MinimumLengthValidator   | `min_length=0`             |
| UserAttributeSimilarityValidator | `user_attributes=[...],max_similarity=0.7` |
| CommonPasswordValidator  | `password_list_path=path-to-file` |
| NumericPasswordValidator | none |

`NumericPasswordValidator` checks if a password is purely alphanumeric (disallowed).  If you want to allow alphanumeric passwords, comment out the validator.


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

