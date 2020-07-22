---
title: Improvements to your Django Project
---

You can do items 1 and 2 on the master branch.
Item 3 should be on a separate branch, test it,
and when you're sure its working then merge into master.

1. Structure your README.md file so it contains the following.  You can have other information, but include at least this:
    ```
    ## Django Polls Application
    (describe the application.  Try to use good English.)

    ## Requirements

    This application requires
    * Python 3.6 or newer
    * Python add-on packages as in [requirements.txt](requirements.txt), including Django

    This app was developed and tested using Python 3.6.6 and Django 2.2.5 running on Windows XP, but any operating system with the required software installed should work.

    ## How to Run

    (how to run the application, briefly)
    1.
    2.
    3.
    ```

2. Create a `requirements.txt` file listing the Python packages your project depends on, including Django.  This file is used by many services to create a virtual environment for your application.
    ```
    # this is a comment line
    Django >= 2.1.2
    ```

3. Add the `python-decouple` package to your system and use it to **externalize configuration values** in `settings.py` to an external file.
    - use a git branch for your work, named `externalize-config`
    - add the dependency on `python-decouple` to `requirements.txt`
    - externalize confidential data (SECRET_KEY) and settings likely to change, like DEBUG. Put the values in a `.env` file in the base directory of your project.
    - when using `config( )` to externalize values, supply sensible default values so the app can still be run even if user doesn't have a `.env` file. E.g. the default for DEBUG should probably be False.
    - after testing that it works, merge this branch into master

4. (Optional) Use the `dj-database-url` package for clean database URLs.
