## Running Python Apps in a Virtual Environment

You can run Python apps in a *virtual environment* that contains a separate, stand-alone copy of Python and all the Python add-ons that the app requires.

This lets you configure and test apps in a stable
environment that isolates them from other Python stuff on your computer.  

A big problem in development is that
code runs differently (or not at all!) on different
machines due to differences in the version of Python and the add-ons installed.

This may even happen on *your own* computer if you change the version of Python you use!

Using a virtual environment mostly eliminates these problems.

### Virtual Environment is Good for Testing Other Apps

Using a virtual environment is great for testing other people's apps. 
Install and run the app in a virtual env so it does not change the configuration of your own system.  
All the app's dependencies are installed inside the virtual environment (a directory).  When you are done, just delete it!

### Installing Virtualenv

Python has a package named [virtualenv][virtualenv].
It is included in some Python distrubutions, otherwise install it using `pip`.

> Note: if you want to install pip and virtualenv **globally** (instead of your personal python packages dir) then run these commands as root or "admin".

On Linux/MacOS the commands are usually `python3` and `pip3`; on other systems just `python` and `pip`.

1. Make sure your `pip` is up-to-date:
    ```
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
   ```
   cd /some/directory/django-polls
   virtualenv env
   ```
2. Activate the virtualenv using the `activate` script. On Linux/MacOS and bash shell, you *source* this script, meaning to run it in your current shell, using the "." command or "source" command.
    ```
    .  env/bin/activate
    ```
    Some shells have a "source" command:
    ```
    source env/bin/activate
    ```
    On Microsoft Windows:
    ```
    env\Scripts\activate
    ```
    When virtualenv is activated it changes your shell prompt so you know you are working in a virtualenv.
3. (First time only) Install requirements from `requirements.txt`:
    ```
    (env)cmd>  pip install -r requirements.txt
    ```
    Requirements are installed only in the virtual env directory (`env`).
4. Run your app or do whatever you want:
    ```
    (env)cmd>  python3 manage.py runserver
    ```
5. Exit the virtualenv using `deactivate`.  
You can also exit by closing the shell window.
    ```
    (env)cmd>  deactivate
    ```
After initial setup, to run the app just "activate" the virtualenv and run the app.

### Exclude venv files from Git!

Add the virtualenv directory to your `.gitignore` file and **don't commit virtualenv directories** into git.

---
## virtualenvwrapper

[Vrtualenvwrapper][virtualenvwrapper] is an add-on for virtualenv to improve management of virtualenvs and makes them easier to use, esp. if you are working on multiple projects. Many developers love it.

However, the basic "virtualenv" may be better
for preparing a venv configuration to run on a cloud service.

## Pipenv

[Pipenv][pipenv] is a newer package that fixes some virtualenv problems of dependency mismatch, improves the management interface, and has a consistent interface on all OS (including Windows). "Under the hood" pipenv using virtualenv for the virtual environment. 

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