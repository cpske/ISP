---
title: Database Practice
---

Use a database browser to browse
the structure of your Django-polls database.

Tools you are use are:

* sqlite3 - command line tool that is part of SQLite
* [Sqlitebrowser](https://sqlitebrowser.org/) free GUI app to browse SQLite database. https://sqlitebrowser.org/
* [DBeaver](https://dbeaver.io/) GUI app to interact with almost any database, including Sqlite. Written in Java (JRE included).
  - Can draw ER diagrams.
  - https://dbeaver.io/

The Django polls database file is `db.sqlite3` in your django-polls directory.


### Using `sqlite` or `sqlite3` command line tool

`sqlite` or `sqlite3` command line app is included with Sqlite package. 

* Commands beginning with "." are commands to Sqlite, e.g. `.help`
* Other commands are SQL
* Some examples:
  ```
  cmd> sqlite3  db.sqlite3
  sqlite> .help                         (show help message)
  sqlite> .tables                       (show tables)
  sqlite> .schema --indent polls_choice (show structure of a table)
  sqlite> .mode column                  (print query results in columns)
  sqlite> SELECT * FROM polls_choice;   (SQL query, must end in ;)
  sqlite> .exit
  ```


## Questions

1. The Django Polls database contains many tables.  Which tables contain the data for your "polls" app?
   ```
   sqlite> .tables
   ```

2. What are the **fields** in the database table for "choice"?

3. Explain or draw a diagram for how to relate a "choice" to a "question".

   > In the following questions use a query expression to retreive
   > Model objects from the database.
   > Use the Django shell to try your answers.
   > See [Making Queries][making_queries] for syntax of querying.

4. Write a Python function (as if part of the Django polls app) to count all the votes for poll for an `id` (id=1, 2, ...).
    ```python
       def vote_count(id):
          """Return total votes for a given poll. id is poll id"""
          # Hint: get the question from the database 
          #       Easiest is use Question.objects.get(...) 
          # question has a choice_set attribute that is a set of choices
          # for that question.

    ```

5. Write a method using Django query statements to find all polls where the question contains some specific text.  Use `Question.objects.filter(...)` or similar query statement instead of fetching all objects.
    ```python
       def find_polls_for_text(text):
          """Return list of Question objects for all polls containing some text"""        # Hint: Question.objects.filter( expression )
          # and use the relations question_text__contains or __icontains 

    ```

---
### Reference

*Making Queries* in the Django documentation: 
[https://docs.djangoproject.com/en/2.2/topics/db/queries/][making_queries]

[making_queries]: https://docs.djangoproject.com/en/2.2/topics/db/queries/

