## Exercises

Answer these questions by using a database browser to browse
the structure of your Django-polls database.

The Django polls database file is `db.sqlite3` in your django-polls directory.

Some apps you can use to answer these questions:

* `sqlite` or `sqlite3` command line app included with Sqlite.  
    - Commands beginning with "." are commands to Sqlite, e.g. `.help`
    - Other commands are SQL
    - Some examples:
    ```
    cmd> sqlite3  db.sqlite3
    sqlite> .help                         (show help message)
    sqlite> .tables                       (show tables)
    sqlite> .schema --indent polls_choice (show structure of a table)
    sqlite> .mode column                  (print query results in columns)
    sqlite> SELECT * FROM polls_choice;   (SQL query, must end in ;)
    sqlite> .exit
    ```
* [Sqlitebrowser](https://sqlitebrowser.org/) free GUI app to browse SQLite database.
* [DBeaver](https://dbeaver.io/) GUI app to interact with almost any database, including Sqlite. Written in Java (JRE included) and uses JDBC.

## Questions

1. The Django Polls database contains many tables.  Which tables contain the data for your "polls" app?

2. What are the **fields** in the table for poll "choices"?

3. What **field** in **which table** is used to count votes for a poll?

4. In the source code, a **Choice** object belongs to a **Question**. In the Polls database how can we relate a row in the "choice" table to a row in the "question" table?     
Write an SQL Join clause like    
"`City.country_code = Country.code`" (connects a City to a Country using the country's code).   
   
