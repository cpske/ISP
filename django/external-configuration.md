---
title: Separate Configuration Data from Code
---

* [The Problem](#the-problem)
* Basic Solution using Python built-in commands to access environment
* General solution using `python-decouple`
* Django-specific solution using `django-environ`
* [Properties in Java](#java-properties)
 
## The Problem

A typical Django `settings.py` file contains confiuration data such as:

```
SECRET_KEY = 'AElek13407aseasej39'
DEBUG = True
TIME_ZONE = 'Asia/Bangkok'   # you didn't write 'UTC', or did you?

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

1. sensitive information is included in code.  Anyone with access to the application code can steal it.
2. If committed to Github, anyone on the web can steal the sensitive data and abuse it.
3. It's difficult to change. For Django, it may be fairly easy, but for other apps (configuration spread over many files) or Java (configuration buried in Java source code not distributed with the app) it's much harder and easy to miss something.
4. If you put your Google Cloud, AWS, or Azure credentials into a file committed to Github, you may face a large **credit card bill** when someone steals them and uses your account to do Bitcoin mining.

### The Solution

A standard practice in programming is to separate configuration data from code.

This is also one of the Heroku [12-Factor App][12-factor-app] characteristics.

For security, it's also necessary to remove sensitive credentials and protect them.

## Using Environment Variables

In Python, one way to handle configuration values is to use **environment variables**.  The Python `os.getenv()` command returns the value of an environment variable:

```
print("Hello, ", os.getenv("USERNAME"));
# on Windows use HOMEPATH instead of HOME
print("Your home directory is ", os.getenv("HOME"));
```

In a Django `settings.py` we can write:
```
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = bool(os.getenv('DEBUG', 'False'))
TIME_ZONE = os.getenv('TIME_ZONE', 'UTC')

STATIC_URL = os.getenv('STATIC_URL','/static/')
```

and then set environment variables for each of these names.
In Bash you can write:
```
SECRET_KEY=AElek13407aseasej39
DEBUG=True
TIME_ZONE='Asia/Bangkok'
```
Put these values into a file and then load them into your shell's environment
before starting the web app.

For example, if we save them in a file named `config.sh`,
then type:
```
# read config values. In some shells, type "." instead of "source"
cmd> source config.sh  
# start the web app with configuration values now in the environment
cmd> python manage.py runserver
```

Most PaaS services, like Heroku, provide a way of setting env-variables
before running your web application.

You should provide **sensible defaults** in case an env-variable is not set.  
In the above example, the default value for `DEBUG` is False,
and the default value of static URL is '/static/'.

Environment variables can still pose a security risk: 
a bad guy may find a way to read environment variables.

In Django, if DEBUG=True and an error occurs, Django prints debugging output in the browser window **including environment variables**.

## Packages for externalizing Configuration Data

There are some Python packages that provide a nice alternative to using environment variables for configuration data:


* **python-decouple** - package for reading configuration data from a file or environment variables.  It can return values other than Strings (such as boolean or a dictionary) by specifying a `cast` parameter.

* **dj-database-url** - package to parse a Database URLs in standard notation (a string) and return a Django DATABASE_ENGINE dictionary.

* **django-environ** - similar to `python-decouple`, but specific to Django. 
  - Can parse a database URL into the Django setting DATABASES dictionary format.
  - Has convenience methods for converting other attributes to the data types used in Django's settings.py.

Comparing these, `django-environ` has convenience methods for converting strings to Django setting data types. `python-decouple` is more general-purpose and has better documentation.


## python-decouple for External Configuration Data

`python-decouple` is a general purpose module for externalizing configuration data. Hence, it is worth knowing and you can use it in Django, too.

* Module description: https://pypi.org/project/python-decouple/
* Example: https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html 

```
pip install python-decouple
```

**Usage:**
`config(var, default=value, cast=type_or_function)` Reads data from first of: (1) an environment variable, (2) .ini or .env file, (3) default value. `cast=` specify the type of value returned (default is string) such as `cast=bool` or `cast=int`.

Format of a `.env` file
```
# variables and their values -- you can add comment lines like this one
DEBUG=True
TEMPLATE_DEBUG=True
SECRET_KEY=ARANDOMSECRETKEY
DATABASE_URL=mysql://myuser:mypassword@myhost/mydatabase
```

Configuration in a `settings.ini` file (alternative to .env file):

```
# this is a comment
[settings]
DEBUG=True
SECRET_KEY=ARANDOMSECRETKEY123
DATABASE_URL=mysql://myuser:mypassword@myhost/mydatabase
```

### Using decouple in Django `settings.ini`

```
from decouple import config
# optional: module to parse database engine config from a single variable
from dj_database_url import parse as db_url

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')

DATABASES = {
     # use cast=db_url requires package dj-database-url
     'default': config('DATABASE_URL', 
                    default='sqlite:///'+BASE_DIR+'db.sqlite3',
                    cast=db_url
                ),
     } 
}
```

### How to Use Alternate Configuration Files with `python-decouple`

Decouple can read configuration file from a file other than `.env` or `settings.ini`.  This is explained at the end of the python-decouple docs page.

To read values from a file named `local.env` (instead of `.env`), 
create a new `decouple.Config` object using `RepositoryEnv('/path/to/env-file')`.  Notice that you **don't** import `config` in this case.
```
from decouple import Config, RepositoryEnv

ENV_FILE = '/opt/envs/my-project/local.env'
myconfig = Config(RepositoryEnv(ENV_FILE))

# use the Config.get() method in the same way you would use config('var').
# decouple.config uses the get() method internally, 
SECRET_KEY = myconfig.get('SECRET_KEY')
```

## `django-environ`

This package is an alternative to `python-decouple`.  Use `pip` to install it.

Put your properties in a `.env` file, same format as with `python-decouple`; **however**, it seems that this file needs to be your config directory (same directory as `settings.py`) rather than the application's top-level directory.

It can also get values from environment variables, just like `python-decouple`.

Example `settings.py`:
```python
import environ

env = environ.Env()
env.read_env()

SECRET_KEY = env('SECRET_KEY', default='dumb-secret-key')
DEBUG = env.bool('DEBUG', default=False)

DATABASES = {
    # read 'DATABASE_URL' and raises ImproperlyConfigured exception if not found
    'default': env.db(),
    }
```

Docs: https://django-environ.readthedocs.io/en/latest/    
Source: https://github.com/joke2k/django-environ 

## Java Properties

In Java, a standard technique is to put configuration data in a Java Properties
file. Java has a `java.util.Properties` class that can parse a properties file
and create a key-value map of the properties, that you can use in code.
In OOP (Programming 2) we used a Properties file for the Coin Purse.

A properties file is plain text like this:
```
# the default currency
purse.currency = Baht
# name of default withdraw strategy
purse.strategy = purse.strategy.GreedyWithdraw

# Example JDBC properties
jdbc.url = jdbc:h2:file:/path/file.db
```
As the example shows, property names (like `purse.capacity`) may include a period, and string values (like Baht) are **not** surrounded by quotes, even if they contain spaces.

In code, you would load and use properties like this:
```java
InputStream in = new FileInputStream(PROPERTIES_FILENAME);
Properties props = new Properties();
props.load(in);

// get a property
String url = props.get("jdbc.url");
// get a property. If it's not found, use a default value (Baht).
String currency = props.get("purse.currency", "Baht");
```
I usually create a `PropertyManager` or `ConfigManager` class to manage properties.

## References 

* python-decouple: https://pypi.org/project/python-decouple/
* https://stackoverflow.com/questions/43570838/how-do-you-use-python-decouple-to-load-a-env-file-outside-the-expected-paths
* django-environ: https://django-environ.readthedocs.io/en/latest/, Source: https://github.com/joke2k/django-environ 
* Javadoc for `java.util.Properties` explains how to use Properties in Java

[12-factor-app]: https://12factor.net/

### Questions

1. Suppose you have a `SECRET_KEY` in your project's `.env` file and also a `SECRET_KEY` environment variable?  Which value has precedence? (that is, which value will be used)
   - This situation could occur when running your app on Heroku.

2. Suppose that you have a `.env` file **and** a `settings.ini` file,  which one will python-decouple use?  Will it look for a named variable in both files?

3. How would you **test** decouple.config?
