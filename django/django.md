---
title: Django
---

* Presentation: [Intro to Django](Intro-to-Django.pdf)
* [Install Django](#install-django)
* [Learn Django](#learning-django) two recommended tutorials and [videos](#videos)
* [Authentication](authentication) how to use Django's authentication framework
* [Authorization](authorization) how to use Django's permissions-based authorization
* [Deployment](django-deployment) to the cloud or a virtual server
* [Externalize Configuration](external-configuration) how to remove configuration data from your Django code.
* [Forms](forms) notes on Django's Form classes that automate the handling of HTML forms
* [Howto](django-howto) miscellaneous notes on problems I've encountered and their solution
* [Import and Export Data](data-import-export) save database data to a file and import the data file into a new installation of the app
* [Logging](logging) is an essential part of web apps
* [Messages Framework](messages-framework) is a clean, easy way to transfer error messages from a view (controller) to a page template, without using the context
* [Organize Unit Tests](test-organization) create a `tests/` directory containing multiple test files. More modular and scales better.
* [Put Models in Separate Files](separate-model-classes) how to use a `models` folder and separate files for model classes.
* [Virtualenv](virtualenv) and [Quickstart](virtualenv-quickstart) how to make you app more portable using a virtual environment. Many cloud services require this for Python apps.

---

## Install Django

1. Download using instructions on official download page at [www.djangoproject.com/download/](https://www.djangoproject.com/download).
    - You need Python 3.6 or newer and the "pip" command (part of Python).

2. Recommend you also download the Django documents as HTML and **bookmark** in your browser: [Django 3.1 HTML docs](https://docs.djangoproject.com/m/docs/django-docs-3.1-en.zip).    
   Django [documentation](https://docs.djangoproject.com/en/3.1/) page has links to other formats (PDF, ePub, online).

### Python

* You need Python 3.6 or newer. Get it from [https://www.python.org/downloads/](Python Downloads).  For Ubuntu Linux, use `apt-get` to install as a package instead of downloading it.

* If you already have Python, use `python --version` to check your version. If you don't have 3.6 or newer, you should upgrade.

* Ubuntu users: Ubuntu comes with both Python 2.7 and 3.x.  Be careful to use Python 3. On many systems the command is `python3`. Typing `python` may run Python 2.7.
  - In 2020, Python 2 will *finally* be retired! So this won't be necessary on newer systems. Try `python --version` to see if `python` is Python 3.x.


## Learning Django

* [Getting Started](https://www.djangoproject.com/start/) on the Django project site.
* [Django Tutorial](https://docs.djangoproject.com/en/2.1/intro/) and [Docs](https://docs.djangoproject.com/en/3.1/) on Django Project site.  It explains a lot.
* Mozilla [Django Web Framework](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) detailed tutorial, on Mozilla MDN site.
  - Setting up a Django development environment. Instructions for MacOS X, Windows 10, and Ubuntu.
  - LocalLibrary sample project, with many parts.
* [TDD with Python](https://www.obeythetestinggoat.com) web development with Django and Test Driven Development.  Thai highly recommends this and says "fun book to read".
* [Django Tutorials and Courses](https://hackr.io/tutorials/learn-django) link collection on Hackr.io.


### Videos

* [Django Crash Course](https://www.youtube.com/watch?v=D6esTdOLXh4) on Youtube (1:08:00).
   - Django is MTV framework. "V" is "View controller" or "business logic layer" (I don't agree with "business logic" part). "T" is "template" or the presentation layer.
   - Video includes boring instructions to install Python, XAMPP on Windows. 
   - You don't need "phpmyadmin" or MySQL.  Use the default SQLite database.
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

For a web app, you need a place to deploy it.

* [Django on Google Cloud](https://cloud.google.com/python/django/) overview of deployment options for Google Cloud.
* [Deploy a Python Web App on Amazon AWS](https://aws.amazon.com/getting-started/projects/deploy-python-application/) includes a sample Django app.
* There are several Youtube tutorials for deploying Django on AWS EC2.
* Heroku: Heroku has a Platform as a Service (Paas) with a free tier.  The Mozilla Django turial describes how to deploy to Heroku.


## Miscellaneous Notes About Django

* Django uses "*convention over configuration*". Django has a fixed project layout, fixed templating system, and "automates" a lot.  
  - Frameworks like Flask and Pyramid give you more flexibility. You have to write more code, but you may get a better understanding of what's going on.
* Django is easy to get started and rapid development.
* `settings.py` includes SECRET_KEY (for encrypting session data). **Don't save this on Github.**
* Creating an admin user: `python manage.py createsuperuser --username=foo --email=foo@gmail.com`. It will prompt for a password (cannot be all numeric).
  - For even better security, don't use "admin" as the username.
  - To access the Admin interface: http://localhost:port/admin
* Highly Ranked and Popular Python Frameworks: 
  - Flask
  - Pyramid (includes Pylons) 
  - CherryPy
  - Turbo Gears

### Web Services for Front-end Frameworks

If you use Angular, React, or Vue.js on the client-side of your application, 
these frameworks want to exchange data with the server side "back end" as web-service requests, 
rather than regular requests for a web page.  They typically use JSON format for data.

You can define web service URLs in Django to send and receive JSON or whatever the front-end wants,
but it *may* be simpler to add [Django REST Framework](django-rest-framework.org) to your project.

**Suggestion**: use a separate URL hierarchy for your web service URLs.  Using the Django Polls as an example, you may have:
```
/polls/            web interface to polls app
/polls/1/
/polls/1/results/
/api/polls/        RESTful web service interface
/api/polls/1/      get poll 1 details
/api/polls/1/vote/ post or put a vote
```


### Running a Django App using Gunicorn

    cd myproject
    gunicorn [--bind 0.0.0.0:8080] myproject.wsgi

Other options:

    --workers 3      # or: -w 3
    --daemon         # run in daemon mode. or: -d

[Gunicorn Docs](http://docs.gunicorn.org/en/stable)

Run a Django App with [Gunicorn](http://rahmonov.me/posts/run-a-django-app-with-gunicorn-in-ubuntu-16-04/), 
[Nginx](http://rahmonov.me/posts/run-a-django-app-with-nginx-and-gunicorn/),
and [Supervisord](http://rahmonov.me/posts/run-a-django-app-with-nginx-gunicorn-and-supervisor/) for Linux.
