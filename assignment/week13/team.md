---
title: Project Homepage Updates (Week 13)
---


## Better and More Unit Testing

Projects I reviewed have very little unit testing.

Unit tests generally contain **more lines of code** than your
model and controller classes combined, since unit tests have to test several cases.

1. Write good unit tests for all methods that involve any non-trivial logic.
   * Test important behavior, not just methods.
   * You don't need to test trivial methods or simple constructors.
2. Tests should have descriptive names for what they test (long names are good) **and** a docstring comment describing the test.


## Instructions How to Install and Run Locally

Write instructions so someone else in the class can install your application on
their computer, configure it, and run it locally.

Instructions should include:

1. Required software and how to install it.  For Python, just state the required version.  The user can go find it him/herself.
2. State which Django version is needed, but you don't need a install instruction since you can include Django in `requirements.txt`.
3. How to clone your project.
4. Instructions for installing packages.  Using a virtualenv is recommended. There are a few "virtualenv" tools to choose from including `virtualenv` and `pipenv`.
5. Steps needed to configure the application for running.  This includes 
   * editing a configuration file (give example what to do)
   * running migrations
   * adding sample data to the database, if needed
6.  Please **do not** require someone install a database like MySQL or PostgreSQL.  Use a lightweight database, such as SQLite for Python projects.
7. How to start the application and verify it is working.

### Your Peers with Validate Your Installation Instructions

Other students will be assigned to follow your instructions and run your app.
