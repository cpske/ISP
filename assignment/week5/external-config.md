## Improvements to your Django Project

You can do items 1 and 2 on the master branch.
Item 3 should be on a separate branch, test it,
and when you're sure its working then merge into master.

1. Structure your README.md file so it contains the following.  You can have other information, but include at least this:
    ```
    ## Django Polls Application
    (describe the application.  Try to use good English.)

    ## Requirements

    The application requires
    * Python 3.6 or newer
    * Django 2.1.2 or newer
    * Python add-on packages as in [requirements.txt](requirements.txt)

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
    - after testing that it works, merge branch into master

4. (Optional) Use the `dj-database-url` package for clean database URLs.
