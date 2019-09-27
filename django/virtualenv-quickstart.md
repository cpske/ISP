## Virtualenv Quickstart

Your `python` and `pip` commands may be different from those shown here.

```bash
# update pip and install virtualenv
cmd>  python3 -m pip --upgrade pip3
cmd>  python3 -m pip install virtualenv

# create a virtualenv for one project
cmd>  cd /someplace/django-polls
cmd>  virtualenv env

# activate the virtualenv using "activate" script
# some shells use "." instead of "source"
cmd>  source env/bin/activate 

# install packages into this virtualenv (only once)
(env)cmd>  pip3 install -r requirements.txt

# run app inside this virtualenv
(env)cmd>  python3 manage.py runserver

# exit the virtualenv
(env)cmd>  deactivate
```

This example created a directory named `env` for the project virtual environment files.
You can delete the directory anytime, but you don't need to.

## Don't Commit the `env` Directory to Git!

Add the "env" directory (or whatever name you use) to `.gitignore`
and update .gitignore in your git repo.    
**Don't commit virtualenv dirs** to git.

**Note**: The `env` directory **is totally unrelated** to the `.env` file used by python-decouple.

## More Info

Read [Using Virtualenv](virtualenv) for a better understanding.    
Or read the official docs [Installing packages using pip and virtualenv][virtualenv].

[virtualenv]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
