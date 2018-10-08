## Install Django

1. Download using instructions on official download page at [www.djangoproject.com/download/](https://www.djangoproject.com/download).
    - You need Python 3.5 or newer and the "pip" command (part of Python).

2. Recommend you also download the HTML documents and **bookmark** in your browser: [Django 2.1 HTML docs](https://docs.djangoproject.com/m/docs/django-docs-2.1-en.zip).    
   Django [documentation](https://docs.djangoproject.com/en/2.1/) page has links to other formats (PDF, ePub, online).

3. Implement the [Tutorial App](https://docs.djangoproject.com/en/2.1/intro/).

### Python

* If you *don't* have Python installed, get it from [https://www.python.org/downloads/](Python Downloads).  For Ubuntu Linux, use `apt-get` to install as a package instead of downloading a tarball.

* If you already have Python, use `python --version` to check your version. If you don't have 3.5 or newer, you should upgrade.

* Ubuntu users: Ubuntu comes with both Python 2.7 and 3.x.  You can control which one is invoked when you type `python`.  You want Python 3.x.


## Learning Django

* [Getting Started](https://www.djangoproject.com/start/) on the Django project site.
* [Django Tutorial](https://docs.djangoproject.com/en/2.1/intro/) and [Docs](https://docs.djangoproject.com/en/2.1/) on Django Project site.  Chapter 1 and 2 are easy to read and explain a lot.
* Mozilla [Django Web Framework](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) detailed tutorial, on Mozilla MDN site.
  - Setting up a Django development environment. Instructions for MacOS X, Windows 10, and Ubuntu.
  - LocalLibrary sample project, with many parts.
* [TDD with Python](https://www.obeythetestinggoat.com) web development with Django and Test Driven Development.  Thai highly recommends this and says "fun book to read".
* [Django Tutorials and Courses](https://hackr.io/tutorials/learn-django) link collection on Hackr.io.

* (Old) [The Django Book](https://djangobook.com) the online book is out-of-date (covers Django 1.x), but the Python tutorials may be useful.

## Videos

* [Django Crash Course](https://www.youtube.com/watch?v=D6esTdOLXh4) on Youtube (1:08:00).
   - Django is MTV framework. "V" is "View controller" or "business logic layer" (I don't agree with "business logic" part). "T" is "template" or the presentation layer.
   - Video includes boring instructions to install Python, XAMPP on Windows. 
   - You don't need "phpmyadmin" or MySQL.  For learning, the the use SQLite database.
   - **Don't use MySQL root user for database access.** Bad habit and lazy.

## Learning Python

Python is easy to learn and fun to program. 

* [Dive into Python 3](http://www.diveintopython3.net/) - Django recommends.
* [Python Tutorial](https://docs.python.org/3/tutorial/) on Python official site.
* Many excellent online courses, tutorials, books to choose from.

To write Django code you need to understand basic O-O concepts and how to use classes and objects in Python.

## Testing and Test-Driven-Development

* [Obey the Testing Goat](http://www.obeythetestinggoat.com/) apply TDD to Django and Python. Thai calls it "fun to read and ingrain TDD practices".  Example: write a test to verify that Django is correctly installed **before** you install Django.
* [Test-Driven Development with Python](http://www.obeythetestinggoat.com/) - scroll down for chapters.  Individual [pages](http://www.obeythetestinggoat.com/pages/book.html).
* [Testing and Django](https://pyvideo.org/pycon-us-2012/testing-and-django.html) video presentation by Carl Meyer (47 minutes). Very useful, fast-paced talk. [Slides](https://github.com/carljm/django-testing-slides) and [code gist](https://gist.github.com/carljm/1450104).
 

## Django Deployment

For any web app, you need a place to deploy it.

* [Django on Google Cloud](https://cloud.google.com/python/django/) overview of deployment options for Google Cloud.
* [Deploy a Python Web App on Amazon AWS](https://aws.amazon.com/getting-started/projects/deploy-python-application/) includes a sample Django app.
* There are several Youtube tutorials for deploying Django on AWS EC2.
* Heroku: Heroku has a Platform as a Service (Paas) with a free tier.  The Mozilla Django turial describes how to deploy to Heroku.


## Notes About Django

### Compared to Other Frameworks

* Highly opinionated.  Django has a fixed project layout, fixed templating system, and much else.  Other frameworks like Flask and Pyramid give you more flexibility.
* Easy to get started and rapid development. "Opinionated" also means it provides a lot of boiler plate code and its easy to learn how to complete the parts.

* `settings.py` includes SECRET_KEY (for encrypting session data). **Don't save this on Github.**
* Admin interface: /myproject/admin
* Creating an admin user: `python manage.py createsuperuser --username=foo --email=foo@gmail.com`. It will prompt for a password (cannot be all numeric).

* Other Highly Ranked Python Frameworks: Flask, Pyramid (includes Pylons), CherryPy, and Turbo Gears.
