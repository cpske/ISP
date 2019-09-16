## Improvements to yur Django Project

1. Structure your README.md file so it contains the following.  You can have other information, but include at least this:
    ```
    ## Django Polls Application
    (describe the application)

    ## Requirements

    The application requires
    * Python 3.6 or newer
    * Django 2.1.2 or newer
    * Python add-on modules as in [requirements.txt](requirements.txt)

    ## How to Run

    (how to run the application, briefly)
    ```

2. Create a `requirements.txt` file listing the Python modules your project depends on, including Django.  This file is used by many services to create a virtual environment for your application.
    ```
    # this is a comment line
    Django >= 2.1.2
    ```

3. Add the `python-decouple` package to your system and use it to **externalize configuration values** in `settings.py` to an external file.
    - add the dependency (python-decouple) to `requirements.txt`
    - use a git branch for your work, named `externalize-config`
    - externalize confidential data (SECRET_KEY) and settings likely to change, like DEBUG. Put the values in `.env`
    - after testing that it works, merge branch into master

4. (Optional) Also use `dj_database_url` package for clean database URLs.
