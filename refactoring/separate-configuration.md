---
title: Separate Configuration from Code
---

It's a good practice to separate data from code, such as:

* configuration data, e.g. relative path to a directory for images
* constants that may change, such as URLs you use
* sensitive values including logins, auth tokens, and (of course) passwords

This makes code easier to modify, maintain, and makes it more secure.

These values can be read from a configuration file, a Properties file (Java), or environment variables.

Class presentation: [Separate Configuration from Code](Separate-config-from-code.pdf)    
My write-up for Django: [Externalize Configuration](../django/external-configuration)

### Django Example

A Django project has many configuration values in a file named `settings.py`,
which includes:
```python
SECRET_KEY = '1234abhc@#9848'
DEBUG = False
ALLOWED_HOSTS = ['localhost', '.ku.ac.th']
```

These values really should not be stored in code and you may want to change
them depending on how you deploy your Django project.

We can create a file named `.env` (not committed to git) that contains:
```shell
# configuration values - don't commit this to git
SECRET_KEY = 1234abhc@#9848
DEBUG = False
ALLOWED_HOSTS = localhost, .ku.ac.th
```

Then use python-decouple to read these values in `settings.py`:
```python
from decouple import config, Csv

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool, default=False)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost', cast=Csv())
```

For Python, there are many packages that do this. Here are two:

* [python-decouple][python-decouple] - flexible and general-purpose. Reads values from environment or a file. Good documentation.
* [django-environ][django-environ] - similar to python-decouple, adds convenience methods for converting values to the formats used in Django's `settings.py`.
* [list of Django configuration packages][django-configuration] if you don't like either python-decouple or django-environ

## Java Properties

In Java, a standard practice is to put configuration data in a Java Properties
file. The `java.util.Properties` class can parse a properties file
and create a key-value map of the properties that you can use in code.
You can also use `Properties` to modify properties and write them a file.
In OOP (Programming 2) we used a Properties file for the Coin Purse.

A properties file is plain text like this:
```shell
# the default currency
purse.currency = Baht
# name of default withdraw strategy
purse.strategy = purse.strategy.GreedyWithdraw

# Example JDBC properties
jdbc.url = jdbc:h2:file:/path/file.db
```

As the example shows, property names (like `purse.capacity`) may include a period, and string values (like Baht) are **not** surrounded by quotes, even if they contain spaces.
It's standard practice to use hierarchial names with "." in them (like "jdbc.url" instead of "url") to avoid name collisions.

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
I usually create a singleton `PropertyManager` or `ConfigManager` class to manage properties,
including discovering and loading a properties file.

Another class, ResourceBundle, is similar to Properties and allows you to have locale-specfic versions of properties. 
To learn about Properties, see:

* [Properties][properties-api] in Java API docs
* [Using Properties][using-properties] from my [OOP in Java][OOP] course

[properties-api]: https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Properties.html
[using-properties]: https://skeoop.github.io/properties/Using-Properties
[OOP]: https://skeoop.github.io/

[python-decouple]: https://pypi.org/project/python-decouple/
[django-environ]: https://django-environ.readthedocs.io/en/latest/
[django-configuration]: https://djangopackages.org/grids/g/configuration/
