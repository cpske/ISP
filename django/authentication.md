---
title: Authentication in Django
---

Django provides an authentication system, which you can combine with your own 
templates (UI) and different *authentication backends* -- like username/password or OAuth.  You can also customize things like password requirements.

Django `django.contrib.auth` app includes:

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
- Step 4. [Add User Greeting to a Template](#add-user-greeting-to-a-template) and a link to login
- Step 5. [Require Login in Views](#require-login-in-views) a user most login to vote.  *Only one line of code!*

Exercises
- 1. In the polls index, add a link to Logout if the user is logged in.
- 2. Define a base page template for your pages.  Put the greeting and login/logout links in the base template instead of duplicating them on every page.

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

5. Each `auth.urls` has a **view** that provides a **form** named `form`.  You need to write a **template** for each view to display the form and send results back to the view.
   ```
   URL                  View Name   Your Template
   accounts/login/      login       templates/registration/login.html
   accounts/logout/     logout      templates/registration/logged_out.html
   ```

### Add Default Redirects for KU Polls

After a user "logs in", what page should he be shown?

The default is redirect to `/accounts/profile`, which does not exist.

In `settings.py` specify defaults for login and logout.  Two syntaxes:

1. Specify where to redirect after login or logout:
   - You can use a *path* like `LOGIN_DIRECT_URL = '/polls/'`, but using a url name is better.
   ```python
   LOGIN_REDIRECT_URL = 'polls:index'  # after login, show list of polls
   LOGOUT_REDIRECT_URL = 'login'       # after logout, return to login page
   ```

**Note:** If the login `request` object contains a `next` key, the Django login view will redirect to the URL specified by `next` instead of the default redirect.

#### Does it Work?

- Rerun tests.  They should still pass.

- Start server and visit <http://localhost:8000/accounts/asdfasdfasdfasdf/> with `DEBUG=True`. It should show a listing of `/accounts/` URLs.

- Visit the login page: <http://localhost:8000/accounts/login/>.  What does the error message tell you?

### Create a Template For Login Page

6. Create directories named `templates` and `templates/registration` in your application top-level folder:
   ```
   ku-polls/
       mysite/
       polls/
       templates/             <--- new directory (maybe)
           registration/      <--- new directory for login template
   ```

7. In `mysite/settings.py` include a global templates directory:
   ```python
   TEMPLATES = [
       {
           # old way: 'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'DIRS': [BASE_DIR / 'templates'],   # <--- global templates
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
     <tr>
     <td colspan="2"><button type="submit">Login</button> </td>
     </tr>
     </table>
    ```
   {% endraw %}

9. **Test it.** Start the Django server and navigate to `localhost:8000/accounts/login/`.
   - It should show your Login form.

10. Create a user.  Here is how to create a user with the Django interactive shell.
    ```bash
    $ python manage.py shell

    from django.contrib.auth.models import User

    # username field is required, others are optional.
    # Use named parameters to avoid errors.
    user = User.objects.create(username='harry', 
                               email='harry@hackerone.com')
    user.set_password("hackme2")
    # first_name is optional
    user.first_name = "Harry"
    user.save()
    ```
    See below for other ways to [create users](#how-to-create-users).

11. **Test it:** Login as this user.

12. **Unit tests:** You should write unit tests for authentication.
    - Example tests: [`test_auth_user.py`](../assignment/ku-polls/test_auth_user.py)
    - Copy the tests into your `polls/` directory to use them.

### Add User Greeting to a Template

KU Polls should show some text so a user knows that he is logged in.

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

The `next=path` tells Django's login view to redirect back to this page after the user logs in.  Otherwise, it will redirect him to the default `LOGIN_REDIRECT_URL`.    
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

1. For a class-based view use the `LoginRequired` **Mixin**.
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
          # or, so the user comes back here after login...
          return redirect(f"{settings.LOGIN_URL}?next={request.path}")
   ```

See: [Limiting access to logged-in users](https://docs.djangoproject.com/en/stable/topics/auth/default/#limiting-access-to-logged-in-users) in the Django docs.


## Logout

Django (as of version 5.1) does not allow invoking the `logout` view using the GET method.  It requires POST.

This means you need a `<form>` that submits a POST request to logout.
To add a "logout" button to a template, you could use:
{% raw %}
```html
{% if user.is_authenticated %}
   <form action="{% url 'logout' %}" method="post"> 
   {% csrf_token %} 
   <button type="submit">Log Out</button> 
   </form>
{% endif %}
```
{% endraw %}


There may be other work-arounds for this.
---

## Extra Material


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
              return redirect('polls:index')
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

### Access User Information in a View

The logged in user is saved as part of the *session* and included in the `request` object (HttpRequest), which is passed to every view.

```python
def vote(request, question_id):
    """Vote for one of the answers to a question."""
    user = request.user
    print("current user is", user.id, "login", user.username)
    print("Real name:", user.first_name, user.last_name)
```


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

---

### How to Create Users

You can use these methods in a Python function or the Django shell or in code:

1. **User.objects.create\_user** convenience method:

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

2. **User.objects.create** method:
   ```
   user = User.objects.create(username='username', 
                              email='email@some.domain') 
   user.set_password("secret")
   user.first_name = "Harry"
   user.save()
   ```

3. Add a registration or "sign-up" page to your app.

4. Use the admin interface

5. Create a data fixture (JSON file) containing user info and `manage.py loaddata` to read the data from a file.

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

to use these views you must create a template for the view you want in a folder named `templates/registration`.  
The templates should have the same name as the view name: 
the `login` view expects a template named `login.html`.
The login view encapsulates its data in a Form named `form`,
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


[django-user-auth]: https://docs.djangoproject.com/en/5.1/topics/auth/
[mdn-auth-tutorial]: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
[auth_tutorial]: https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/
[signup_tutorial]: https://wsvincent.com/django-user-authentication-tutorial-signup/

