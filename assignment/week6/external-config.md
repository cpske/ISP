---
title: Improvements to your Django Project
---


Item 3 should be on a separate branch, test it,
and when you're sure its working then merge into master.

1. Structure your README.md file so it contains the following sections and information.  You can have other information in addition to this.
    ```
    ## Django Polls Application
    (describe the application in good English.)

    ## Requirements

    This application requires
    * Python 3.6 or newer
    * Python packages as in [requirements.txt](requirements.txt), including Django

    ## Installation

    1. Clone the repository from Github.
    2. Enter the following commands to initialize database tables:
       ```
       write the command(s) here
       ```
    3. Import sample polls questions and choices:
       ```
       python3 manage.py loaddata polls.json 
       ```

    ## How to Run

    write brief instructions for how to run the application
    you should tell the reader what URL he should enter in his browser, too


2. Create a `requirements.txt` file listing the Python packages your project depends on, including Django.  This file is used by many services to create a virtual environment for your application. **Do not** include unnecessary packages.
    ```
    # packages needed by this application
    Django >= 3.1.0
    python-decouple 
    ```

3. Add the `python-decouple` package to your system and use it to **externalize configuration values** in `settings.py` to an external file.
    - use a git branch for your work, named `externalize-config`
    - add the dependency on `python-decouple` to `requirements.txt`
    - externalize confidential data (SECRET_KEY) and settings likely to change, like DEBUG. Put the values in a `.env` file in the base directory of your project.
    - when using `config( )` to externalize values, supply sensible default values so the app can still be run even if user doesn't have a `.env` file. E.g. the default for DEBUG should probably be False.
    - after testing that it works, merge this branch into master

4. (Optional) Use the `dj-database-url` package for clean database URLs.
