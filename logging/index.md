---
title: Logging
---

Logging is an essential part of a professional application.
Logging is required by law for some kinds of applications,
such as financial and medical applications.

Presentation [Introduction to Logging](Logging.pdf)

## Logging in Python

[Python Logging Howto](https://docs.python.org/3/howto/logging.html) basic & advanced tutorials (not really advanced).

[Logging in Python](https://realpython.com/python-logging/) on RealPython.com

[Python Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook)


## Logging Practice

[Logging Practice](logging-practice) exercise

## Logging in Django

Django extends the Python logging module.
You can configure logging in your Django `settings.py` file.

You can also configure logging for a specific "app" in the `app.py` file, 
which is described in the second article below.  
But it's usually better to configure logging in `settings.py`.
Logging configuration done in `app.py` or any other file may
go unnoticed when you try to modify logging at a later time.

* [Django Logging, The Right Way](https://lincolnloop.com/blog/django-logging-right-way/) clear explanation with examples
* [Disabling Error Emails in Django](https://lincolnloop.com/blog/disabling-error-emails-django/) explains how to remove default loggers in Django
* [Logging](https://docs.djangoproject.com/en/3.1/topics/logging/) in the official Django docs


## Configure Python Logging in Code

This function contains examples of configuring Python logging in code,
using a FileHandler, Formatter, and StreamHandler.

For simple logging configuration, it much easier to use `basicConfig`
instead of this.

```python
def configure():
    """Configure loggers and log handlers."""
    # write all messages to a file.
    # For a real app, use a configurable absolute path to log file.
    filehandler = logging.FileHandler("demo.log")
    filehandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
    filehandler.setFormatter(formatter)
    # add the handler to the root logger, it will handle all log msgs
    root = logging.getLogger()
    root.setLevel(logging.NOTSET)
    root.addHandler(filehandler)

    # Define a console handler for messages of level WARNING or higher
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    formatter = logging.Formatter(fmt="%(levelname)-8s %(name)s: %(message)s")
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)
```


## Logging Services

You can use a **logging service** to receive, monitor, analyze, and store logs.

Commercial web sites can generate hundreds of megabytes (or more!) of log info every day.  Those logs need to be filtered, scanned for suspicious activity or error messages, and summarized.  Logging services do this. 

Logging Services also aggregate logs from many machines or many apps. A busy web service may have several hosts running the same application to provide faster responses. A logging service will combine logs from many hosts.

Some logging services are:

* [Loggly](https://loggly.com) log analysis and monitoring. Log monitoring service used by Pizza Hut :-).
* [Sentry](https://sentry.io) has a free "developer" tier and toolkits to make it easy to send you app logs to Sentry.

