---
title: Project Installation Instructions in README
---

Most open-source software projects include instructions to install, configure, and run the software.

## Instructions How to Install and Run Locally

Write instructions how to install, configure, and run your application locally.
Include them in README.md.  If instructions are long, you can use a separate file (INSTALL.md) and refer to that file in README.md.

The instructions should be sufficient for **anyone** to install, configure, and run your application on their own computer.

Instructions should include:

1. Prerequisite (required) software.  For Python, just state the required version of Python (not how to install it, which is documented on Python.org).  The user can go find Python him/herself.
2. How to clone your project.
3. Brief text description of important software that will be used, just as Django and sqlite.  These are included in `requirements.txt` so no separate installation is required.
4. Instructions for setting up a virtual environment (virtualenv). You can use `pipenv` as alternative, if you prefer.
5. Steps needed to configure the application for running.  This includes 
   - sample configuration file for env variables read by python-decouple or django-environ 
   - any necessary renaming or editing of the configuration file (give example what to do)
   - running migrations
   - adding initial data to the database
6. Use a lightweight database by default, e.g. sqlite.
   - the database settings should be part of the externalized data, so that if someone *wants* to switch to a different database then they can do it without editing settings.py
7. How to start the application and verify it is working.

### Provide Local User Accounts as Initial Data

Since others will be running the project on their machine, OAuth authentication may not work. (The user won't have your OAuth secrets.)

So, of OAuth doesn't work then you should provide at least one local user account as part of the initial data ("fixture").  Be sure to include the initial username and password in your instructions for running the app.

### Don't Commit Your Virtualenv to Github!

A user should be able to create his own virtualenv from your requirements.txt.

It's both inefficient and error-prone to include the contents of a virtualenv on Github. It may not run on the target machine, or may contain out-of-date packages.


## Your Peers with Validate Your Installation Instructions

Other students will be assigned to follow your instructions and run your app.


## Evaluation 

If, after exactly following your instructions, the application does not run according to the written instructions then the team gets 0 credit for this assignment.

Points deducted for these errors:

* Poor English or inconsistent English. This includes sentence structure and punctuation.
* Poor formatting of instructions.
* Unnecessary or overly stringent requirements. An example is stating that you require Python 3.8 when actually it works fine using Python 3.6 or 3.7.
* Missing dependencies.  Your app should run in a Python virtualenv, hence all dependencies should be in `requirements.txt`, including Django! 

## Resources

[How to use virtualenv](/ISP/django/virtualenv) and my [Quickstart](/ISP/django/virtualenv-quickstart).

[Providing Initial Data for Models](https://docs.djangoproject.com/en/3.1/howto/initial-data/) from the Django documentation.

Django [Data Import-Export](/ISP/django/data-import-export) my write-up.


