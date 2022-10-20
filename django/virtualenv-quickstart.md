## Virtualenv Quickstart

Your `python` and `pip` commands may be named `python3` and `pip3`.

If you have `virtualenv` installed you can use `virtualenv` instead of `python -m venv`.  According to developers, "virtualenv" is more efficient.

```bash
# create a virtual envronment for django-polls project
cmd>  cd /someplace/django-polls
cmd>  python -m venv env 

# Activate the virtual env using "activate" script
# some shells use "." instead of "source"
# Windows: enter 'env\Scripts\activate' (no "source")
cmd>  source env/bin/activate 

# install packages into this virtual environment (only once)
(env)cmd>  pip3 install -r requirements.txt

# run app inside this virtual environment
(env)cmd>  python3 manage.py runserver

# when finished, exit the virtual environment 
(env)cmd>  deactivate
```

This example created a directory named `env` for the project virtual environment files.    
To delete the virtual envirionment, delete the `env` directory.

## Don't Commit the `env` Directory to Git!

Add the "env" directory (or whatever name you use) to `.gitignore`
and update .gitignore in your git repo.    
**Don't commit** virtualenv directories to git.

**Note**: The `env` directory is unrelated to the `.env` file used by python-decouple.
