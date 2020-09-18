---
title: Import and Export Data in Django 
---

You can import and export data in your project's database.
Useful for:

* creating a backup
* transferring data to a different database, such as when switching to a different server or different database.
* creating initial data for others who install and use your app

## Using Django dumpdata and loaddata

The `manage.py` interface to [django-admin][django-admin] has a `dumpdata` command to export part or all of your application database data to a file.  There are many useful options described in the [django-admin dumpdata][django-admin] documentation.

Create a dump of the "polls" models in JSON format, and output to the console:
```bash
python manage.py dumpdata --indent=2 polls
```
The output is in JSON format. The `--indent=2` option requests formatted, easy-to-read output.

`manage.py` also has a `loaddata` command to import data from a JSON file.

For import, the Django convention is to look for data in a `fixtures` directory inside an "app" directory such as `polls/fixtures`.
To dump data to a file named `seed.json` in our polls app, use:
```bash
mkdir polls/fixtures          (if directory doesn't exist)
python manage.py dumpdata --indent=2 -o polls/fixtures/seed.json polls
```
The `-o outputfile` option specifies a file to receive dump data, the `polls` parameter means dump only data for the polls app.

Edit `polls/fixtures/seed.json` to remove any unwanted data.

To load the data into a fresh, empty database use:
```bash
python manage.py loaddata seed.json
```
Django will look in every app's `fixtures` directory for files named `seed.json`, and import the data into the database.

See the [django-admin][django-admin] docs for more dumpdata and loaddata options.


### Creating Initial Data for Others to Use

To create initial data to distribute with your project, you need to
do a little more work.

1. Use `manage.py dumpdata -o init.json polls` to create a data file.
2. Edit the file to remove excess poll questions and choices, and **set the vote counts** to zero.
3. Put the data file in directory `polls/fixtures`.
4. **Test it** on a fresh install of your project!

> Real Developers test everything.  Don't *assume* it will work.

When someone installs your Django Polls project he won't have a database,
so he needs to run:
```bash
python manage.py migrate
python manage.py loaddata init.json   (or whatever filename you choose)
```

## Using a Migration instead of "manage.py loaddata"

You can create a migration file to load initial data into the database.
This makes it easier for others to install your app, since they
only need to run `manage.py migrate`.  

There's a good description and example in
[Data Migrations][data-migrations] on RealPython.com.

### Challenge for Hackers

Can you write a data migration (in Python) do read a JSON file
created by `dumpdata` and load it into the database?

That would give you both the simplicity of initializing data using a migration, 
and convenience of having data in a separate file you can easily modify.

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
