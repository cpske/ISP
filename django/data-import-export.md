---
title: Import and Export Data in Django 
---

You can import and export data in your project's database.
Useful for:

* creating a backup
* transferring data to a different database, such as when switching to a different server or different database.
* moving the project to a different computer
* creating initial data for others who install your app

## Export Data using dumpdata

The `manage.py` script has a `dumpdata` command to export part or all of your application database to a file.  There are many useful options described in the [django-admin dumpdata][django-admin] documentation.

* You can specify which "apps" and which "tables" to dump
* The data is in JSON format, which is human readable. 

Create a dump of the "polls" models in JSON format. Output is to the console:
```bash
python manage.py dumpdata --indent=2 polls
```
The `--indent=2` option requests output indented 2 spaces per nesting level. Ifyou don't include ``--indent=xx` the output is very dense and hard to read.

There are 2 ways to output to a file:
```
# 1. redirect standard output to a file
python manage.py dumpdata --indent=2 polls > polls.json

# 2. use the -o option
python manage.py dumpdata --indent=2 -o polls.json polls 
```
**Don't forget the `polls` argument!**  If you omit it, then manage.py will dump all tables (including Django's own tables) which is not portable.


## Import Data Using loaddata

Import data into a database using:
```
python manage.py loaddata  polls.json
```
You can specify more than one data file.  Sometimes the order matters. For example, if the "polls" data refers to "users" (a user owns his votes) then you *might* need to create users before loading polls data. 
```
python manage.py loaddata users.json polls.json
```

If files are in a directory (e.g. `data/`, specify the path, too. For example
```
python manage.py loaddata data/users.json data/polls.json
```


## Creating a "Data Fixture"

Django calls the initial data for an "app" a **data fixture** and it looks for this data in an "app" subdirectory named `fixtures`.
For the `polls` app, the data fixture directory is `polls/fixtures`.

Suppose we want to create a start-up fixture named "seed".
The commands would be:
```
# create the fixtures directory (one time)
mkdir polls/fixtures
# export the polls data to seed.json
python manage.py dumpdata --indent=2 -o polls/fixtures/seed.json polls
```

Then edit `polls/fixtures/seed.json` to remove any unwanted data.

### Loading a Data Fixture

If you specify a filename *without a path*, Django will look in the "fixtures" directories of all apps for the file.

To load the data into a fresh, empty database use:
```bash
python manage.py loaddata seed.json
```

See the [django-admin][django-admin] docs for more dumpdata and loaddata options.

## Using Data as Part of Installation

When someone installs your Django Polls project (or you deploy it to a cloud service) there won't be a database.

So the installation process must run:
```bash
python manage.py migrate
python manage.py loaddata seed.json   (or whatever filename you choose)
```

### Challenge for Hackers: Use a Migration instead of "manage.py loaddata"

You can create a migration file to load data into a database.
This makes it easier for others to install your app, since they
only need to run `manage.py migrate`.  

There's a good description and example in
[Data Migrations][data-migrations] on RealPython.com.

Can you write a data migration (in Python) do read a JSON file
created by `dumpdata` and load it into the database?

---
## References

[Providing Initial Data for Models][django-initial-data] describes how to create initial data using a Migration or a "fixture". A "fixture" is a file containing data in JSON, XML, or Yaml format.

[Data Migrations][data-migrations] on RealPython.com describes how to create a data migration for initial data.
## Other Ways to Import and Export Data

You can also use the database's own import/export commands.
These are specific to each database and the output format may differ slightly.

Django [import-export](https://django-import-export.readthedocs.io/en/latest/index.html) add-on, with good documentation on ReadTheDocs.io.
This add-on gives you finer control over import and export.
The downside: adding another dependency to your project.

[django-initial-data]: https://docs.djangoproject.com/en/2.2/howto/initial-data/
[django-admin]: https://docs.djangoproject.com/en/2.2/ref/django-admin/
[data-migrations]: https://realpython.com/data-migrations/
