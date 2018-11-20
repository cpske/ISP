## Separate Configuration Data from Code

A typical Django `settings.py` file contains confiuration data such as:

```
SECRET_KEY = 'AElek13407aseasej39'
DEBUG = True
TIME_ZONE = 'UTC'

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

A recommended practice in programming is to separate configuration constants from code.

Its also important to remove passwords and private credentials from code.

## Techniques

In Java, a standard technique is to put configuration data in a Java Properties
file.  In OOP (Programming 2) we used a Properties file for the Coin Purse.
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

In Django, one way to handle configuration values is to use **environment variables**.  In `settings.py` we could write:
```
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
TIME_ZONE = os.getenv('TIME_ZONE')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'polls',
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
        'PORT': '5432',
	}
}
STATIC_URL = os.getenv('STATIC_URL','/static/')
```
and then set environment variables before running the application.
Most PaaS services, like Heroku, provide a way of setting env-variables
before running your web application.

If you use this technique, you should provide sensible defaults in case
some env-variable is not set.  For example, the default value of `DATABASE_HOST	 is '127.0.0.1' and default static URL is '/static/'.

Environment variables can pose a security risk: a bad guy may find a way to read environment variables.  In Django, if DEBUG=True and an error occurs, Django prints debugging output in the browser window **including environment variables**.

There are two Python packages that provide a nice alternative to using environment variables.

* **python-decouple** - package for reading configuration data from a file or environment variables.  It also returns values other than Strings (such as boolean or a dictionary).
* **dj-database-url** - package to parse a Database URLs in standard notation and return a Django DATABASE_ENGINE dictionary.


## python-decouple for External Configuration Data

* Module description: https://pypi.org/project/python-decouple/
* Example: https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html 
the examples show how to use decouple with Heroku and Travis-CI.

```
pip install python-decouple
```

**Usage:**
`config(var, default=value,cast=type_or_function)` Reads data from first of: (1) environment variable, (2) .ini or .env file, (3) default value. `cast=` enables you to specify the type of value returned, such as `cast=bool` or `cast=int`.

### Configuration in a `.env` file
```
# variables and their values
DEBUG=True
TEMPLATE_DEBUG=True
SECRET_KEY=ARANDOMSECRETKEY
DATABASE_URL=mysql://myuser:mypassword@myhost/mydatabase
```

### Configuration in `settings.ini` file

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
# optional: parse database engine config from a single variable
from dj_database_url import parse as db_url

DEBUG = config('DEBUG', default=False, cast=bool)

DATABASES = {
  # to use cast=db_url requires package dj-database-url
  'default': config('DATABASE_URL', 
                    default='sqlite:///'+BASE_DIR+'db.sqlite3',
                    cast=db_url
             ) 
}

SECRET_KEY = config('SECRET_KEY')
```

### How to Use Alternate Configuration Files

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

### References 

* https://pypi.org/project/python-decouple/
* https://stackoverflow.com/questions/43570838/how-do-you-use-python-decouple-to-load-a-env-file-outside-the-expected-paths


### Questions

1. Suppose that you have a `.env` file **and** a `settings.ini` file,  which one will python-decouple use?  Will it look for a named variable in both files?

2. Suppose you have a `SECRET_KEY` in your project's `.env` file and also a `SECRET_KEY` environment variable?  Which value has precedence? (that is, which value will be used)

3. How would you **test** decouple.config?
