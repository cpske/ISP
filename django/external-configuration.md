---
title: Separate Configuration Data from Code
---

* [The Problem](#the-problem)
* Basic Solution using Python built-in commands to access the environment
* General solution using `python-decouple`
* Django-specific solution using `django-environ`
 
## The Problem

A typical Django `settings.py` file contains configuration data such as:

```
SECRET_KEY = 'AElek13407aseasej39'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '158.108.0.0']
TIME_ZONE = 'Asia/Bangkok'   # you didn't write 'UTC', did you?

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'polls',
        'USER': 'admin',
        'PASSWORD': 'mint2840',
        'HOST': '127.0.0.1',
        'PORT': '5432'
     }
}
# for cloud deployment
STATIC_URL = 'https://storage.googleapis.com/ske-polls/static/'
```

The problems with this are:

1. Anyone with access to this code can **steal sensitive information**.
2. If committed to Github, anyone on the web can steal the info and abuse it.
3. It's difficult to change. In Django it may be fairly easy, but for other apps (configuration spread over many files) or Java (configuration in Java source code not distributed with the app) it's much harder to change and easy to miss something.
4. If you put your Google Cloud, AWS, or Azure credentials into a file on Github, you may face a large **credit card bill** when someone steals them and uses your account for Bitcoin mining.

### The Solution

A standard practice in programming is to **separate configuration data from code**.

This is also recommended in Heroku's [12-Factor App][12-factor-app] guide.

Put sensitive data in a separate file that is *not* committed to Github.

## Basic Way: Using Environment Variables

*This section shows the basic idea and works, but I recommend using [Decouple](#python-decouple) instead.*

In Python, you can store configuration values as **environment variables**.  The Python `os.getenv()` command returns the value of an environment variable:

```python
import os
# Get the user's login name from the environment
>>> os.getenv("USERNAME")
'user'                # if you are logged in as "user"
# on Windows use HOMEPATH instead of HOME
>>> os.getenv("HOME")
'/home/user'          # typical home directory on Linux
>>> os.getenv("foo")
                      # returns nothing for undefined envvar
>>> os.getenv("foo", "default")
'default'             # returns a default value for undefined envvar
```

In Django's `settings.py` we can use the environment to get
sensitive variables and include default values:

```python
SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
DEBUG = bool(os.getenv('DEBUG', 'False'))
TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')
```

Create a shell script (Bash, Zshell, or Windows batch file) to set these environment variables.
This script *should not* be part of your Git repository.

For bash you can write:
```shell
SECRET_KEY=AElek13407aseasej39
DEBUG=True
TIME_ZONE='Asia/Bangkok'
```
in MS Windows use:
```shell
SET SECRET_KEY=AElek13407aseasej39
SET DEBUG=True
SET TIME_ZONE='Asia/Bangkok'
```
Save these lines in a file ("shell script") such as `config.sh`.

Before starting the web app, you load their values into the environment:
```shell
# read config values. In some shells, type "." instead of "source"
cmd> source config.sh  
# now start the Django app 
cmd> python manage.py runserver
```

PaaS services like Heroku provide a way to specify environment variables like this.

You should provide **sensible defaults** in case an env-variable is not set.  
In the above example, the default value for `DEBUG` is False.

Environment variables can still pose a security risk: 
a bad guy may find a way to read environment variables.

In Django, if DEBUG=True and an error occurs, Django prints debugging output in the browser window **including environment variables**.

## Packages to Externalize Configuration

Two Python packages provide nice solutions to externalize
configuration data (you only need one of them!)

* **python-decouple** - reads configuration data from a file or environment variables.  It can return values as any data type (not just Strings) by specifying a `cast`.
  - General purpose module (can use on any project)

* **django-environ** - similar to `python-decouple`, but specific to Django. 
  - Has convenience methods for converting other attributes to the data types used in Django's settings.py.
  - Can parse a database URL into the Django DATABASES setting format.

* **dj-database-url** - package to parse a Database URLs in standard notation (a string) and return a Django DATABASE_ENGINE dictionary. Use this with `python-decouple`.

## python-decouple

This is a general purpose module for externalizing configuration data.

* Module description: https://pypi.org/project/python-decouple/
* Example: https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html 

```
pip install python-decouple
```

**Usage:** `config(var, default=value, cast=type_or_function)`     
Reads data from first of: (1) an environment variable, (2) .ini or .env file, (3) default value.     
`cast=` specify the type of value returned (default is string) such as `cast=bool` or `cast=int`.

Format of a `.env` file
```
# variables and their values -- you can add comment lines like this one
DEBUG=True
TEMPLATE_DEBUG=True
SECRET_KEY=ARANDOMSECRETKEY
DATABASE_URL=mysql://myuser:mypassword@myhost/mydatabase
ALLOWED_HOSTS='localhost,.herokuapp.com'
```

Instead of `.env` you can use a `settings.ini` file, which contains named sections.

```
# this is a comment
[settings]
DEBUG=True
SECRET_KEY=ARANDOMSECRETKEY123
DATABASE_URL=mysql://myuser:mypassword@myhost/mydatabase
ALLOWED_HOSTS='localhost,.herokuapp.com'
```

### Using decouple in Django's `settings.py`

In your site's `settings.py` file:
```python
from decouple import config, Csv

# optional module to parse database configuration from a single database URL
from dj_database_url import parse as db_url

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=Csv())

DATABASES = {
     # use cast=db_url requires package dj-database-url
     'default': config('DATABASE_URL', 
                    default='sqlite:///'+BASE_DIR+'db.sqlite3',
                    cast=db_url
                ),
     } 
}
```

### Database URLs for dj-database-url

The above example shows how to use a single environment variable (`DATABASE_URL`) and the dj-database-url function `parse` to create all the values in a Django dictionary.

This is a lot simpler than using separate variables for database name, url, username, and password.  The format for the URLs in shown on <https://github.com/jacobian/dj-database-url>.

Here are a few common ones by example

| Database | URL                      |
|:---------|:-------------------------|
|SQLite    | sqlite:///db.sqlite3     |
|Postresql | postgres://user:password@localhost/mydatabase |
|MySql     | mysql://user:password@localhost/mydatabase |

`user` and `password` are the database user (defined in the database manager) that has permission to read/write the database for your app.
For migrations, this user needs permission to alter the schema and create tables, too.

If the database is running on another host, use that instead of "localhost" (of course), and if the database manager is listening on a non-standard port then specify it after the hostname, such as:

```
postgres://appuser:secret@server.ku.th:12345/mydatabase
```

### How to Use Alternate Configuration Files with `python-decouple`

Decouple can read the configuration from a file other than `.env` or `settings.ini`.  This is explained at the end of the python-decouple docs page.

To read values from a file named `local.env` (instead of `.env`), 
create a new `decouple.Config` object using `RepositoryEnv('/path/to/env-file')`.  Notice that you **don't** import `config` in this case.
```python
from decouple import Config, RepositoryEnv

ENV_FILE = '/opt/envs/my-project/local.env'
myconfig = Config(RepositoryEnv(ENV_FILE))

# use the Config.get() method in the same way you would use config('var').
# decouple.config uses the get() method internally, 
SECRET_KEY = myconfig.get('SECRET_KEY')
```

But, changing `settings.py` partially negates the benefit of using decouple.
I think a better way is to keep multiple something.env files and
copy the one you want to `.env`.

## Using django-environ

This package is an alternative to `python-decouple`.  
Use `pip` to install it.

Put properties in a `.env` file in same format as used by `python-decouple`; 
**but**, it seems that this file must be your config directory (same directory as `settings.py`) rather than the application's top-level directory.

`django-environ` can also get values from environment variables, just like `python-decouple`.

Example `settings.py`:
```python
import environ

env = environ.Env()
env.read_env()

SECRET_KEY = env('SECRET_KEY', default='dumb-secret-key')
DEBUG = env.bool('DEBUG', default=False)

DATABASES = {
    # read 'DATABASE_URL' and raise ImproperlyConfigured exception if not found
    'default': env.db(),
    }
```

## References 

* python-decouple: <https://pypi.org/project/python-decouple/>
* <https://stackoverflow.com/questions/43570838/how-do-you-use-python-decouple-to-load-a-env-file-outside-the-expected-paths>
* django-environ: <https://django-environ.readthedocs.io/en/latest/>, Source Code: <https://github.com/joke2k/django-environ>
* Java API doc for `java.util.Properties` explains how to use Properties in Java

[12-factor-app]: https://12factor.net/

### Questions

1. Suppose you have a `SECRET_KEY` in your project's `.env` file and also a `SECRET_KEY` environment variable?  Which value has precedence? (that is, which value will be used)
   - This situation could occur when running your app on Heroku.

2. Suppose that you have a `.env` file **and** a `settings.ini` file,  which one will python-decouple use?  Will it look for a named variable in both files?

3. How would you **test** your externalized configuration using either python-decouple or django-environ?
