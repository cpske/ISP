# Authentication using Django's django.contrib.auth app

Django's authentication "app" provides basic support for user login, logout, sign-up,
and password reset.  It also provides basic model for storing using info in a database table.

1. In your site's `settings.py` file check that INSTALLED_APPS includes `django.contrib.auth`
    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        ...
    ]
    ```
2. In your site's `urls.py` enable Django's auth URLs.  By convention, use `accounts/` in URL mapping
    ```python
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('accounts/', include('django.contrib.auth.urls'),
        ...,
    ]
    ```

Django's `auth` app provides views for each of these URLs:
```python
accounts/login/ [name='login']
accounts/logout/ [name='logout']
accounts/password_change/ [name='password_change']
accounts/password_change/done/ [name='password_change_done']
accounts/password_reset/ [name='password_reset']
accounts/password_reset/done/ [name='password_reset_done']
accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/reset/done/ [name='password_reset_complete']
```
to use these views you must create a template for each in a folder named `registration`.  
The templates should have the same name as the views, so the `login` view 
expects a template named `login.html`.  The login view encapsulates its data in a Form named `form`,
so in your `login.html` template do something like this:
```html
<form method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Login</button>
  <!-- if your app redirects user to login before accessing some pages, then next contains return url -->
  <input type="hidden" name="next" value="{{ next }}" />
</form>
```

## What is a User?

When you use the `django.contrib.auth` app and apply migrations, it will
add database tables for User (`auth_user`), Group (`auth_group`), Permissions (`auth_permissions`) and tables for many-to-many relations between these 
(a User may have many permissions and many users may have the same permission).

We can refer to Users in our apps.  For the Polls app, we want to associate
a User with votes so that one user can only vote once for each poll.
We may also allow a user to change this choice in a poll.

The model classes in `django.contrib.auth` are:

| Class   | Description      |
|:--------|:-----------------|
| User    | User with first_name, last_name, password, email, id, and date_joined |
| Group   | Group with an id and name. |
| Permission | Permission with id, codename, and name. |

### Getting the Logged-in User

You can check if a user is authenticated in HTML templates and in views.
In a template use:
```html
{% if user.is_authenticated %}
   Welcome back, {% user.username %}
{% else %}
   Please <a href="{% url 'login' %}">Login</a>
{% endif %}
```

If your app has a navbar on the left side you might use offer context-senstive
login-logout links:
In a template use:
```html
{% if user.is_authenticated %}
   <a href="{% url 'logout' %}">Logout</a>
{% else %}
   <a href="{% url 'login' %}">Login</a>
{% endif %}
```
In `settings.py`, specify where to redirect a user after login or logout:
```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```
Instead of a hard-coded relative URL, you can use the name of a view as defined in urls.py, i.e. if you have a view named 'home' then use:
```python
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
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

Finally, we need a template for sign-up.  As shown in the above view code,
we inject the UserCreationForm object as a variable named `form`.
You can put the template anywhere you like. As shown in the `render()` function call in the view, I put mine in a subdirectory of `templates/` named `registrations`.  That is, BASE_DIR/templates/registion/signup.html.

A simple user sign-up template is:
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
The important parts of this template are a) render the form `{{form.as_table}}`
and b) POSTing the form back to the correct URL.  Since the &lt;form method='POST'&gt; block doesn't specify an action, the default action is to send it back to the same URL the page came from.


William Vincent has a
[Django Sign Up Tutorial][signup_tutorial] that shows another way of implementing a "Sign Up"
view as a separate app.  He uses a class-based view for sign-up which is very simple.



## Resources

[auth_tutorial]: https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/
[signup_tutorial]: https://wsvincent.com/django-user-authentication-tutorial-signup/
