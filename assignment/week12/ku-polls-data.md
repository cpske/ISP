---
title: Create a Data Fixture for KU Polls Iteration 3
---

In KU Polls iteration 3 you added users and modified the polls models.

Please create user and polls data so TAs and others can run your polls app.

Use one of these choices to make the changes:

- work on `iteration3` branch, then merge it into `master` (best choice and easy if you have already merged iteration3 into master)
- work directly on `master`, assuming you **already** merged iteration3 into master

Steps:

1. Your app should have at least 2 users (not superusers) who can login, for testing.  If you don't have two users, add them before continuing. Use names "demo1" and "demo2".
   - From Iteration 1 you should already have 2 interesting poll questions with multiple choices. 

2. In your README.md add a section "Running KU Polls" and write the names of the users and their passwords.  For example:
   ```
   ## Running KU Polls

   Users provided by the initial data (users.json):

   | Username  | Password    |
   |-----------|-------------|
   | demo1     | Vote4me!    |
   | demo2     | Vote4me2    |
   ```

3. Create a `fixtures` directory inside the `polls` directory:
   ```
   mkdir polls/fixtures
   ```
   - **Windows Users:** use "\" instead of "/" in path (Windows **worst** mistake), or use the Bash shell
   - `fixtures` is Django's standard location for application data

4. Now your KU Polls project should have this structure:
   ```
   ku-polls/
           polls/
                fixtures/
   ```
5. Use the "dumpdata" command to create two JSON files containing "polls" data and "users" data:
   ```
   python3 manage.py dumpdata --indent 2 -o polls/fixtures/polls.json polls
   python3 manage.py dumpdata --indent 2 -o polls/fixtures/users.json auth 
   ```
   - **Don't forget** the last argument: `polls` or `auth`.  
   - If you forget the last argument (the "app" name), then "dumpdata" will dump ALL the database tables, including Django's migrations and settings. This will make the dumpdata useless.
   - The "-o" argument means "output" (where to write the data).

6. Add to Git: `README.md` (revised) and `polls/fixtures/*.json`.    
   Two ways to do this:
   - Add to `iteration3` branch, then merge into `master`, **or**
   - Add directly to `master`

7. Push your updates to Github.


## Initialize Polls Data in a New Installation

When someone installs your application in a new location,
the person should be able to recreate the database using:

```
python3 manage.py migrate
python3 manage.py loaddata users polls
```

As shown above, you should "loaddata" for `users` before `polls`, since the polls data refers to users.


---

### References

- [Import and Export Data in Django](https://cpske.github.io/ISP/django/data-import-export)
- [Providing initial data for models](https://docs.djangoproject.com/en/3.2/howto/initial-data/) from the official Django Docs.
