## Running Python Apps in a Virtual Environment

You can run Python apps in a *virtual environment* that contains a separate, stand-alone copy of Python and the Python add-ons that the application requires.

A virtual environment lets you configure and test apps in a stable
environment that **isolates the app** from other Python stuff on your computer.  
This solves several problems:
- you want to install and run someone else's app on your computer, without changing the Python packages on your computer
- you want to verify that your app can run on someone else's computer (may not have the same Python packages as yours)
- you want to have multiple different Python "environments" or Python versions 

Using a virtual environment solves most of these problems.

### Creating a Virtual Environment

There are several commands for creating a virtual environment:
- `python -m venv`
- virtualenv (Python package)
- pipenv (another Python package)

In this write up we will use the builtin `venv` module.  It has less functionality than the virtualenv or pipenv packages, but is good enough.

1. Create a virtual env directory named `env` **inside** a project directory. You can use any name instead of "env" ("env" and "venv" are typical names):
   ```bash
   cd /some/directory/django-polls
   python3 -m venv  env 
   ```
   This creates an `env` subdirectory with structure like this:
   ```
   env
   env/bin
   env/include
   env/lib
   env/share
   ```
   The `env/bin` directory contains python, python3, pip, and pip3 commands.  But they aren't on your shell's "path" until you "activate" the virtual env.
2. Start the virtual environment by "sourcing" the `activate` script. In a Bash or Zshell (Linux, MacOS, or Windows with git-bash installed), type:
    ```bash
    source env/bin/activate
    ```
    or:
    ```
    . env/bin/activate
    ```
    On Microsoft Windows:
    ```
    env\Scripts\activate
    ```
    When the virtual env is activated it prepends `(env)` to your shell prompt so you know it is active.  
    ```
    (env) cmd>
    ```
3. (First time only) Install requirements *inside* the virtual environment:
    ```bash
    (env) cmd>  pip install -r requirements.txt
    ```
    Requirements are installed only in the virtual env directory (`env`).
4. Run the application or do whatever you want:
    ```bash
    (env) cmd>  python3 manage.py runserver
    ```
5. Exit the virtualenv using `deactivate`.  
You can also exit by closing the shell window.
   ```bash
   (env) cmd>  deactivate
   ```

After initial setup, to run the app just "activate" the virtualenv and run the app.

### Exclude virtual environment directories from Git!

Add the virtualenv directory (`env`) to your `.gitignore` file and **don't commit** virtualenv directories into git.

---

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
