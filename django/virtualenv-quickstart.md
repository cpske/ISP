## Virtualenv Quickstart

Your `python` and `pip` commands may be different from those shown here.

```
# update pip and install virtualenv
cmd>  python3 -m pip --upgrade pip3
cmd>  python3 -m pip install virtualenv

# create a virtualenv for one project
cmd>  cd /someplace/django-polls
cmd>  virtualenv env

# activate the virtualenv by reading a script
# some shells use "." instead of "source"
cmd>  source env/bin/activate 

# install packages into this virtualenv
(env)cmd>  pip3 install -r requirements.txt

# run python inside this virtualenv
(env)cmd>  python3 manage.py runserver

# exit the virtualenv
(env)cmd>  deactivate
```

This example created a directory named `env` for the project virtual environment files.
You can delete the directory anytime, but you don't need to.

## Don't Commit the `env` Directory to Git!

Add the `env` directory (or whatever name you use) to `.gitignore`
and update .gitignore in your repo.  **Don't commit virtualenv dirs** to git.

## More Info

Read [Using Virtualenv](virtualenv) for a better understanding.    
Or read the official docs [Installing packages using pip and virtualenv][virtualenv].

[virtualenv]: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
