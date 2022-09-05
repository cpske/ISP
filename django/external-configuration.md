---
title: Externalize Configuration Data in Python
---

* [The Problem](#the-problem)
* [The Solution](#the-solution)
* [Using Environment Variables](#using-environment-variables) is a basic solution and used by Heroku cloud services
* [Packages to Externalize Configuration](#packages-to-externalize-configuration), the best ones are:
  - [python-decouple](#python-decouple) a general purpose package 
  - [django-environ](#django-environ) specifically for Django
  - [dj-database-url](#database-urls-and-dj-database-url) for parsing database URL strings

 
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
        'PASSWORD': 'iamanidiot',
        'HOST': '127.0.0.1',
        'PORT': '5432'
     }
}
# for cloud deployment
STATIC_URL = 'https://storage.googleapis.com/ske-polls/static/'
```

The problems with this are:

1. Anyone with access to this code can **steal sensitive information**.
2. If committed to Github, anyone on the web can **steal the info**.
3. **Difficult to change** - an installer has to search for the data. In Django it may be fairly easy, but for other apps the configuration data may be spread over many files or may require recompiling the code (Java, C++, etc).
4. If you put your Google Cloud, AWS, or Azure credentials into a file on Github, you may get a **large credit card bill** when someone steals your credentials and uses your account (for crypto-mining).

## The Solution

A standard practice is to **separate configuration data from code**.

This is recommended in Heroku's [12-Factor App][12-factor-app] guide.

Put sensitive data in a separate file that is *not* committed to Github, or use environment variables.

## Using Environment Variables

*This is the basic idea and it works, but I recommend using [python-decouple](#python-decouple) instead.*

In Python, you can access values as **environment variables**.  The Python `os.getenv()` command returns the value of an environment variable:

```python
import os
# Get the user's login name from the environment. May be 'USERNAME' on Windows.
>>> os.getenv("USER")
'hacker'
# on Windows use HOMEPATH instead of HOME
>>> os.getenv("HOME")
'/home/hacker'
>>> os.getenv("foo")
                        # returns nothing for undefined env var
>>> os.getenv("foo", "default")
'default'               # returns a default value for undefined env var
```

We can use the environment to store sensitive data for a Django app.

1. Define variables and values in a bash or zshell script named `config.sh` (*not checked in* to Git):
   ```shell
   SECRET_KEY=AElek13407aseasej39
   DEBUG=True
   TIME_ZONE='Asia/Bangkok'
   ```

2. If using MS Windows use a ".bat" or Powershell script:
   ```shell
   SET SECRET_KEY=AElek13407aseasej39
   SET DEBUG=True
   SET TIME_ZONE='Asia/Bangkok'
   ```

3. In Django `settings.py` use `os.getenv()` to get the values:
   ```python
   import os
   SECRET_KEY = os.getenv('SECRET_KEY')
   DEBUG = bool(os.getenv('DEBUG', 'False'))
   TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')
   ```

4. Before starting Django, load these values into your shell's environment:
   ```shell
   cmd> source config.sh  
   ```
   In some shells, type ". config.sh" instead of "source"

5. Start Django.  It should use values from the environment variables!


Cloud services like Heroku let you specify environment variables as part of your app configuration.

You should provide **safe defaults** in case an env-variable is not set.  
In the above example, the default value for `DEBUG` is `False`.

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

This is a general purpose module to externalize configuration data.

- Module description: <https://pypi.org/project/python-decouple/>
- Example: <https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html>

```
pip install python-decouple
```

**Usage:** `config(var, default=value, cast=type_or_function)`

Reads data from either: (1) an environment variable, (2) .ini or .env file, (3) default value, in that order.    
`cast=` specify the type of value returned (default is string) such as `cast=bool` or `cast=int`.

Format of a `.env` file
```
# variables and their values -- add comment lines like this one
DEBUG=True
TEMPLATE_DEBUG=True
SECRET_KEY=ARANDOMSECRETKEY
DATABASE_URL=mysql://myuser:mypassword@myhost/mydatabase
ALLOWED_HOSTS=localhost,127.0.0.1,.herokuapp.com
```

Instead of `.env` you can use a `settings.ini` file, using a *section* named "settings". This is convenient if you have *other* packages that use the settings file format for configuration.

```
# this is a comment
[settings]
DEBUG=True
SECRET_KEY=ARANDOMSECRETKEY123
DATABASE_URL=mysql://myuser:mypassword@myhost/mydatabase
ALLOWED_HOSTS='localhost,.herokuapp.com'
```

### Using decouple in Django `settings.py`

In your `settings.py` file use:
```python
from decouple import config, Csv

# (optional) module to parse database configuration from a single database URL
from dj_database_url import parse as db_url

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', 
                       default='localhost,127.0.0.1', 
                       cast=Csv())

DATABASES = {
     # use cast=db_url requires package dj-database-url
     'default': config('DATABASE_URL', 
                    default='sqlite:///'+BASE_DIR+'db.sqlite3',
                    cast=db_url
                ),
     } 
}
```

### Database URLs and dj-database-url

It is common to specify a database location as a URL, such as `sqlite:///db.sqlite3`.
The above example uses `DATABASE_URL` to store this URL, and the dj-database-url function `parse` to "parse" the URL into the dict format Django expects.

This is much nicer than using separate variables for database name, path, username, and password.  

The format for database URLs in shown on <https://github.com/jacobian/dj-database-url>. Here are a few examples

| Database | URL                      |
|:---------|:-------------------------|
|SQLite    | sqlite:///db.sqlite3     |
|MySql     | mysql://user:password@localhost/mydatabase |
|Postresql | postgres://user:password@ec2-99a.com1.amazonaws.com:5432/d4ce432 |

`user` and `password` are the database user (defined in the database manager) that has permission to read/write the database for your app.
For migrations, this user needs permission to alter schema and create tables, too.

If the database is running on another host, use that hostname instead of "localhost" (of course), and if the database manager is listening on a non-standard port then specify it after the hostname, such as:

```
postgres://appuser:secret@server.ku.th:12345/mydatabase
```

### How to Use Alternate Configuration File with `python-decouple`

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

Specifying the env filename in `settings.py` goes against the goal of externalizing configuration.
I think a better way is to keep multiple something.env files and
copy the one you want to `.env`. 
*Or*, use an environment variable to specify the filename.

## django-environ

`django-environ` is similar to [python-decouplse](#python-decouple) 
but provides convenience methods for Django,
such as parsing a database URL, so you don't need [dj-database-url](#dj-database-url).

Put data in a `.env` file in the same format as used by `python-decouple`; 
**however**, it seems that this file must be your config directory (same directory as `settings.py`) rather than the application's top-level directory.

`django-environ` can also get values from environment variables, just like `python-decouple`.

Example `settings.py` using `django-environ`:
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
