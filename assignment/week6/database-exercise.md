---
title: Database Practice
---

Use a database browser to browse the structure of your Django-polls database.

Preferred: use [DBeaver](https://dbeaver.io/) GUI app to interact with almost any database, including Sqlite. Can draw ER diagrams. Home: <https://dbeaver.io/>

If you have a problem with DBeaver, other tools that work are:

- [Sqlitebrowser](https://sqlitebrowser.org/) free GUI app to browse SQLite database. https://sqlitebrowser.org/, but doesn't draw ER diagram.
- **sqlite3** - command line tool included with SQLite. Don't need to install anything, but has only command line interface. You use SQL commands to view or modify the database.
  - See below for how to use sqlite3 to view a database.

The Django polls database file is `db.sqlite3` in your django-polls directory.
---

## Questions

1. The Django Polls database contains many tables.  Which tables contain the data for your "polls" app?


2. What are the **fields** in the database table for "choice"?


3. Draw an ER or UML class diagram for how to relate a "choice" to a "question".


4. In order to join a "question" to it's "choices", there **must** be a field in one of those tables that refers to the `id` field of the other table.  This is called a *Foreign Key*.  What field in what table is used to relate a question and its choices?  (Write your answer as `tablename.fieldname`.)


5. Suppose we create a Django app named "store" and the "store" has model classes named Product and Sale.  What would be the names of the tables in the database?



## Part 2. Django Code

> In the following questions use a query expression to retreive
> Model objects from the database.
> Use the Django shell to try your answers.
> See [Making Queries][making_queries] for syntax of querying.

1. Write a Python function (as if part of the Django polls app) to count all the votes for poll for an `id` (id=1, 2, ...).
   ```python
   def vote_count(id):
       """Return total votes for a given poll. id is poll id"""
       # Hint: get the question from the database 
       #       Easiest is use Question.objects.get(...) 
       # question has a choice_set attribute that is a set of choices
       # for that question.

   ```

2. Write a method using Django query statements to find all polls where the question contains some specific text.  Use `Question.objects.filter(...)` or similar query statement instead of fetching all objects.
   ```python
   def find_polls_for_text(text):
       """Return list of Question objects for all polls containing some text"""
       # Hint: Question.objects.filter( expression )
       # and use the relations question_text__contains or __icontains 

   ```

---

### Using `sqlite` or `sqlite3` Command Line Tool

`sqlite` or `sqlite3` command line app is part of the SQLite package. 
You can use it to view or change a database, and issue SQL commands.

* Commands beginning with "." are commands to sqlite, e.g. `.help`
* Other commands are SQL
* Examples:
  ```
  cmd> sqlite3  db.sqlite3
  sqlite> .help                         (show help message)
  sqlite> .tables                       (show tables)
  sqlite> .schema --indent polls_choice (show structure of a table)
  sqlite> .mode column                  (print query results in columns)
  sqlite> SELECT * FROM polls_choice;   (SQL query, must end in semi-colon)
  sqlite> .exit
  ```

---
### Reference

*Making Queries* in the Django documentation: 
[https://docs.djangoproject.com/en/2.2/topics/db/queries/][making_queries]

[making_queries]: https://docs.djangoproject.com/en/2.2/topics/db/queries/

