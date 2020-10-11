---
title: Refactoring
---

Contents:
* [Refactoring](#refactoring)
* [Separate Configuration from Code](#separate-configuration-from-code)

## Refactoring

Refactoring refers to modifying the structure of existing code to improve it,
without changing the functionality.

Some things we will cover:

* signs that code needs refactoring -- sometimes called "code smells", a term I *dislike*
* what does "improve code" mean?  Software principles provide objective guides.
* guide lines for when and how to refactor
  - code should be working before refactoring
  - you must have tests before refactoring
  - refactor is small steps and only one at a time 
  - test the result of each refactoring and commit it before doing the next refactoring
* common refactorings, with names
* refactoring Python and Java using an IDE. 
  - Eclipse, IntelliJ (aka PyCharm), and Netbeans provide good refactoring tools 
  - VS Code can perform some refactoring, but not as good as the IDE above

### Presentation Slides

[Intro to Refactoring](Refactoring.pdf)    
[Refactoring Signs and Patterns](Refactoring-Patterns.pdf)      

### Refactoring Signs and Symptoms

How to know when you should refactor code?
Good lists with description and examples, are:

* [Code smells](https://blog.codinghorror.com/code-smells/) at CodingHorror.com
* Chapter 3 of *Refactoring* by Martin Fowler
* [Chapter 24](/ISP/resources/Refactoring - Code Complete.pdf) of *Code Complete 2* by Steve McConnell has a long list

Common signs:

1. Duplicate code - same computation performed in multiple places
2. Long Method - is a method doing more than one thing?
3. Large Class - symptoms are a class with many instance variables, or many methods, esp. methods that don't seem essential to the class's primary responsibility
4. Long parameter list - a method with many parameters
5. Divergent Change - when you try to change one bit of functionality you have to change code in several different methods
6. A method uses members of another class more than the members of it's own class. (*Members* means attributes and methods.)
7. Complex expressions make it hard to understand purpose of code.
8. Switch statements - the code uses a "switch" or "if ... else if ... else if ..." to control variable based on the value of a variable, with one "case" or "if" per alternative. Consider replacing this with polymorphism.
9. "*Three strikes, refactor*" - if you find yourself writing (almost) the same thing 3 times, then refactor it.


### Refactoring Goals

The goal is to create "better" code with the same functionality as the original.  In most cases, the interface remains unchanged.

So, what is good code?

(If I wrote it here, it would be duplication, which is *poor* code. But to get you started ...)

1. High cohesion within a class or module.  

2. Good encapsulation with limited API. (Low coupling.) You can make changes to the implementation of one part without needing to change others.

3. Each piece of information is represented only once in code.

### Refactoring Exercises

1. [Pizzashop refactoring exercise](https://github.com/ISP19/pizzashop)     
2. [Movie Rental refactoring problem](https://github.com/jbrucker/movierental) from Martin Fowler's presentation and article
3. Read about refactoring (below) and create your own refactoring exercise for other students

### More about Refactoring

[JeremyBytes](http://www.jeremybytes.com/Demos.aspx) has material on refactoring as part of "Clean Code".

[Introduction to Refactoring](http://www.math.uaa.alaska.edu/~afkjm/csce401/handouts/refactoring.pdf) PDF has many refactorings with short Java examples -- easy to read.

[Refactoring Techniques](https://refactoring.guru/refactoring/techniques) lots of them

[Refactoring Guru](https://refactoring.guru/refactoring)

[Refactoring in IntelliJ](https://www.jetbrains.com/help/idea/tutorial-introduction-to-refactoring.html#5db90) explains how to do it in IntelliJ, with examples of common refactorings.
 


---

## Separate Configuration from Code

It's a good practice to separate data from code. Such as:

* configuration data, e.g. relative path to a directory for images
* constants that may change, such as URLs you use
* sensitive values including logins, auth tokens, and (of course) passwords

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
