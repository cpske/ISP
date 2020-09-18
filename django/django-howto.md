## Django `manage.py shell` runs IPython

In the Django Tutorial part 2, they explain how to interactly
test your models:
```
python manage.py shell

Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
IPython 6.4.0 -- An enhanced Interactive Python. Type '?' for help.
In [1]: 
```

when I do this, some the commands don't work as in the tutorial.
Others on the web have the same problem. Appears to be due to IPython
instead of Python.  `manage.py help shell` shows that there
is an option `-i {ipython|python|bpython}`.

Choose `python` and it works:
```
./manage.py shell -i python
```

## Run manage.py as a script

On MacOS and Linux, you can execute Python scripts like commands.
The shell will examine the first line of the script to see what
to invoke.  If the first line starts with "#!" then the rest of the
line defines the command to run.  In my case:
```bash
#!/usr/bin/env python3
```

You also need to make the script executable (`chmod a+x manage.py`).
Then you can run it by typing:
```
./manage.py runserver
```

## Adding a Constructor to a Model Class

I tried adding a contructor to the `polls.models.Question` class
so I could set question text as first parameter.
But this breaks the object-creation ability of the ORM in Django.

Searching the web, I found:
> Django expects the signature of a model's constructor to be 
> `(self, *args, **kwargs)`, or some reasonable facsimile. 
> Changing the signature to something has broken it.

and from the Django docs:

> You may be tempted to customize the model by overriding 
> the `__init__` method. If you do so, however, take care 
> **not to change the calling signature** as any change may 
> prevent the model instance from being saved.

So its better to not override and either use:

1. Named parameter:
```python
>>> q = Question(question_text="What?")
```
2. Define a static factory method:
```python
class Question(models.Model):
    # A static (class) method
    @classmethod
    def create(cls, question, date=datetime.now()):
       return cls(question_text=question, pub_date=date)
```
and then type:
```python
>>> q = Question.create("What's up?")
```

## Many Ways to use Redirect

This article has good explanation of different ways to redirect in Django:

https://realpython.com/django-redirects/

## Manage Static Files with WhiteNoise

[WhiteNoise](http://whitenoise.evans.io/en/stable) is a Python package that allows web apps (including Django) to serve their own static content without a lot of overhead.

To install, just use:
```
pip install whitenoise
```
and add it to your requirements.txt.

For Django, in `settings.py` add WhiteNoise after Django SecurityMiddleware and before all others:
```python
MIDDLEWARE = [
   'django.middleware.security.SecurityMiddleware',
   'whitenoise.middleware.WhiteNoiseMiddleware",
   ...
   ]

# Optional, for permantently cachable files and compression add:
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

Also specify `{apphome}/staticfiles` as location of static content:
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

And in templates, use the `{\% static "file" \%}` tag:
```html
{\% load static \%}
<img src="{\% static "images/button.jpg" \%}" alt="button" />
```

## Read Database URL from Envvar (dj-database-url)

[dj-database-url](https://github.com/kennethreitz/dj-database-url) parses a single environment variable named DATABASE_URL and returns a dictionary of values as expected in settings.py:
```python
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
```
and in the environment:
```python
export DATABASE_URL="postgres://admin:password@hostname:port/mydatabase"
```
The syntax for the [URL schema][dj-database-schema] is:
```python
database://user:password@host:port/databae_name
# for SQLite
sqlite:///database_path
```

[dj-database-url]:https://github.com/kennethreitz/dj-database-url
[dj-database-schema]:https://github.com/kennethreitz/dj-database-url#url-schema


## Django Questions

### urls.py and `path()`

The Django URL Dispatcher gets routing information by sourcing a file named `urls.py`.
There is a top level `urls.py` in your project and each app typically has its own `urls.py` for its localized URLs.  The file looks like:
```python
from django.urls import include, path

urlpatterns = [
    path(r'^$', index, name="homepage"),  # main landing path
    path(r'polls/', include('polls.urls')),
]
```

According to the [Django Tutorial, Part 1](https://docs.djangoproject.com/en/2.1/intro/tutorial01/), the `path()` function has 4 parameters:
```python
path( route, view, kwargs, name )
"""
   route - a regular expression that is matched to the path of an incoming Http request
   view - a view function to handle the HttpRequest, or an `include` of another urls file.
   kwargs - keyword arguments, passed as a dictionary to the target view.
   name - a name for the URL
"""
```

## Django and MySQL

After running "pip install mysqlclient" or "pip install pymysql" 
you may still get the following error when using a MySQL database:
```
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
```

A solution that works is, in your project top directory (where the settings.py and top-level urls.py are), edit `__init__.py` and add:
```python
import pymysql
pymysql.install_as_MySQLdb()
```



