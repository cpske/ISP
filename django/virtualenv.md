## Running Python Apps in a Virtual Environment

You can run Python apps in a *virtual environment* that contains a separate, stand-alone copy of Python and all the Python add-ons that the application requires.

A virtual environment lets you configure and test apps in a stable
environment that **isolates the app** from other Python stuff on your computer.  
When installing and testing other people's apps, 
you can install the application's dependencies in its own virtualenv
without modifying your own Python installation.    
And, you can delete the virtualenv when you are done using the app.

A big problem in development is that code runs differently (or not at all!) 
on different computers due to differences in the version of Python and 
the add-ons installed.

Even on your *own machine*, an app may stop working when you upgrade
Python or add-on packages.

Using a virtual environment eliminates most of these problems.


### Installing Virtualenv

Python has a package named [virtualenv][virtualenv].
It is included in some Python distrubutions, otherwise install it using `pip`.

> Note: if you want to install pip and virtualenv **globally** (instead of your personal python packages dir) then run these commands as root or admin.

On Linux/MacOS the commands are usually `python3` and `pip3`; on other systems just `python` and `pip`.

1. Make sure your `pip` is up-to-date:
    ```bash
    python3 -m pip install --upgrade pip3
    python3 -m pip --version
    # Check consistency. This should be the same thing.
    pip3 --version
    ```
2. Install virtualenv.
    ```
    python3 -m pip install virtualenv
    ```
    or invoke pip directly:
    ```
    pip3 install virtualenv
    ```

### Using Virtualenv

The basic workflow is like this. 

1. Create a virtualenv directory named `env` inside the project directory. You can use any name instead of "env".
   ```bash
   cd /some/directory/django-polls
   virtualenv env
   ```
2. Activate the virtualenv using the `activate` script. On Linux/MacOS and bash shell, you *source* this script, meaning to run it in your current shell. Use the "." command or "source" command.
    ```bash
    .  env/bin/activate
    ```
    or:
    ```
    source env/bin/activate
    ```
    On Microsoft Windows:
    ```
    env\Scripts\activate
    ```
    When virtualenv is activated it prepends `(env)` to your shell prompt so you know it is active.
3. (First time only) Install requirements from `requirements.txt`:
    ```bash
    (env)cmd>  pip install -r requirements.txt
    ```
    Requirements are installed only in the virtual env directory (`env`).
4. Run the app or do whatever you want:
    ```bash
    (env)cmd>  python3 manage.py runserver
    ```
5. Exit the virtualenv using `deactivate`.  
You can also exit by closing the shell window.
    ```bash
    (env)cmd>  deactivate
    ```

After initial setup, to run the app just "activate" the virtualenv and run the app.

### Exclude virtualenv files from Git!

Add the virtualenv directory to your `.gitignore` file and **don't commit virtualenv directories** into git.

---
## virtualenvwrapper

[Vrtualenvwrapper][virtualenvwrapper] is an add-on for virtualenv to improve management of virtualenvs and makes them easier to use, esp. if you are working on multiple projects. Many developers love it.

However, the basic "virtualenv" may be better
for preparing a venv configuration to run on a cloud service.

## Pipenv

[Pipenv][pipenv] is a newer package that fixes some virtualenv problems of dependency mismatch, improves the management interface, and has a consistent interface on all OS (including Windows). "Under the hood" pipenv uses virtualenv for the virtual environment. 

---
### References

* [Installing packages using pip and virtualenv][virtualenv] has complete instructions for using virtualenv on Windows, MacOS, and Linux/Unix.
* [Virtualenvwrapper][virtualenvwrapper] docs describe what is does and how to use it.
* [Pipenv documents][pipenv] the official documentation and [Github Site][pipenv-github].
* [Pipenv: A guide to the new packaging tool][pipenv-guide] on RealPython explains the dependency conflicts that can arise with virtualenv and requirements.txt.

[virtualenv]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
[pipenv]: https://pipenv.kennethreitz.org/en/latest/install/
[pipenv-github]: https://github.com/pypa/pipenv
[pipenv-guide]: https://realpython.com/pipenv-guide/
[virtualenvwrapper]: https://virtualenvwrapper.readthedocs.io/en/latest/
