---
title: KU Polls Iteration 1
---

You will learn Django and implement KU Polls using the [Django Tutorial][django-tutorial].
The assignments for the next 3 weeks will add to this code, so don't fall behind.

The features to implement in this iteration are:

1. Display a list of poll questions with multiple choices.
2. Visiter can select a poll question and select ("vote") for a choice. His vote is added to the total for that choice.
3. Visitor can see total votes for each choice in a poll.
4. Each poll has a publication date (start date) & is visible only on or after this date.
5. Poll questions and choices can be added or changed using the admin interface.

Features not implemented in this iteration:

- we will not implement any authentication and, as a result, will not track who has replied to each poll question. 
- a user cannot change a previously submitted poll choice, although he can submit another choice ("vote")

## Assignment 

The code you will produce for this iteration matches the [Django Tutorial][django-tutorial].

1. Create a wiki page named "`Iteration 1 Plan`" page in your `ku-polls` wiki. Add a link to this page in **Home**.
2. Your "Iteration 1 Plan" should have these sections:
   - **Goal** for the iteration
   - **Milestone**, a concrete, visible indicator of progress. More than one milestone is fine.
   - **Features** to implement and other **major work** but not detailed tasks (put those on the task board)
   - **Acceptance Criteria** - how to evaluate the result?

2. Create a Github **Project** for KU Polls. (You may have done this during the project inception.)

3. In the Project, create a *Task Board* named "**Iteration 1**".
   - Task Board should have at least 3 columns for task status (Backlog or Todo, In Progress, Done). 
   - Add tasks for work to do in Iteration 1. See below for example tasks.
   - Better: create a **table** in your Github Project named "Backlog". Add tasks to the Backlog. Then create an Iteration 1 task board that shows selected tasks from the backlog.
   - Convert "tasks" to "issues" so they are also shown in the Issue Tracker. Tasks for development work *should* be issues, but you may have some "housekeeping" tasks that are not issues. For example, editing the links is README.md.

4. Create the Django project directly in the `ku-polls` repo that you clone from Github -- not in a subdirectory.  Be careful how you create the project to avoid creating an extra subdirectory.  Do this:
   ```
   git clone https://github.com/xxxxxx/ku-polls
   chdir ku-polls
   # create a Django project HERE (.) and put config files in a subdir named mysite (no hyphen)
   django-admin startproject mysite .
   ```
   - OK to use a different name for the config dir (mysite) but it should be a valid Python package name (no hyphen) and **not** `polls` which will be an "app" within the project.
   - Verify: Your `ku-polls` repository should look like this:
     ```
     .gitignore
     manage.py             # this file is created by django
     mysite/               # config directory is created by django
     README.md
     requirements.txt
     ```

5. Create a git branch named **iteration1** and do your work on this branch.

6. **Push to Github** after you finish **each part** of the Django tutorial, e.g.
     ```
     git checkout -b iteration1
     ...(do tutorial part 1, test it, and add the files)
     git commit -m "Implement tutorial part 1"
     git push
     # repeat for part 2, part 3, ... all in iteration1 branch
     ```

7. Implement parts 1 - 6 of the [Django Tutorial][django-tutorial].
   - Please read the tutorial *carefully*. There is a lot of info in the text.

8. Add at least **2 interesting poll questions** to your app, and **delete** the boring "What's up?" question.
   - No trivial, boring questions like "How are you?" or "What's your favorite color?"

9. Do not include `db.sqlite3` in your Github repository.  Instead, export your polls data to a file named **data/polls-v1.json**.  Here's is how:
   ```
   # in your "ku-polls" repository, enter:
   mkdir data
   python manage.py dumpdata --indent=2 -o data/polls-v1.json polls
   ```
   Include `data/` and `data/polls-v1.json` in your git repository.

10. When you finish and test everything, open a **Pull Request** to merge.    
    - Then, take a break.  *Really*.

11. After a break, review your own work, then:
    - **merge** branch `iteration1` into `master` (or `main`). It should be a simple "fast forward" merge.
    - **close** the Pull Request on Github. There are several ways to do this.
    - *Note:* Github can merge the branch and close the Pull Request with a single click. You must "pull" master to your local repo.

### Suggestions

- Do **not use copy and paste** when doing the tutorial. You learn **better** by typing it yourself!  Typing engages your senses and forces you to *remember* what you just read.

- The tutorial converts function-based views to class views.  It is OK to leave some function-based views, but you should try class views -- they can do a lot more.
- Part 7 of the tutorial (customizing the admin interface) is not required, but useful. Implement it if you like.

### Example Tasks

Here are example tasks with a description.  If you want, you can split these into smaller tasks and/or use more descriptive titles.

| Task Title                | Description              |
|---------------------------|---------------------------|
| Initialize Django application and polls app |Implement tutorial part 1. Initialize Django application and a "polls" app with a simple page template, define URLs. Learn the Django project structure and how to use the 'manage.py' script.|
| Implement tutorial part 2 |Initialize database, create models for polls app, learn how to use Django interactive shell to interactively explore models by running python commands. Learn to use Django admin interface.   |
| Implement tutorial part 3 |Create pages for list of polls, poll details, and results view, and write logic for them. Learn Django template syntax. |
| Implement tutorial part 4 |Create a form for the polls detail (voting) page. 'Done:' user can view choices for a poll, select and submit a choice, and see his vote in included in the results. |
| Implement tutorial part 5 |Learn how to perform tests using the Django interactive shell. Write unittests for models and views. |
| Add CSS styling and stylesheet |Implement tutorial part 6. Add CSS stylesheet and page styles. Learn how to use static files in Django. |
| Add Polls Questions       |Add 2 interesting polls with multiple choices.        |
| Create Data Fixture       |Export polls data to a file. 'Done': polls data can be imported to a new database and are shown in the app. |
| Review and Test Code      |Open a PR and Review all code. Verify code is documented and uses standard Python coding style. All unit tests pass. |
| Merge Branch              |Merge `iteration1` branch into main/master and close the Pull Request. |


### Optional: Improve Security

Everyone will do this in Iteration 2, but if you are security-conscious then do this now.

The Django `settings.py` file contains sensitive information that you should not commit to Github.  The only sensitive value now is `SECRET_KEY`:

```python
# File: mysite/settings.py

SECRET_KEY = 'some-random-secret-key'
```

For security, the value of the `SECRET_KEY` should never be committed to Github!
Instead, specify it in a separate file that is not committed to git.

Do this in 4 steps:

1. Install the `python-decouple` package: `pip install python-decouple`
2. Add `python-decouple` to your `requirements.txt` file on a separate line.
3. Edit `mysite/settings.py` and define `SECRET_KEY` as an environment variable:
   ```python
   from decouple import config

   SECRET_KEY = config('SECRET_KEY', default='fake-secret-key') 
   ```
4. Create a file for the config data. The file is named `.env` in the project's root directory (not the mysite directory) and contains this:
   ```
   # contents of .env
   SECRET_KEY = your-actual-secret-key-without-quotation-marks
   ```
   The `.env` file should not be committed to git, but its good to add a `sample.env` file to git so other users know what info they need to put in the file, e.g.
   ```
   # sample.env
   # Specify your Django secret key here. No quotation marks.
   SECRET_KEY = bogus-secret-key
   ```

For details, see [Externalize Configuration](https://cpske.github.io/ISP/django/external-configuration) on the ISP github.io site. 


## What To Submit

Your Github repository should look like this:
```
.gitignore
manage.py
README.md
requirements.txt     <-- List of required Python packages
data/
    polls-v1.json    <-- polls data from your database
mysite/              <-- where application settings.py and urls.py are
    settting.py
    urls.py
    etc.
polls/               <-- the polls "app" code and app templates
    admin.py
    migrations/
    models.py
    templates/
    tests.py
    views.py
    etc.
templates/           <-- global templates
```

*Wrong*: the Django project should not be in a subdirectory of your Github repo.    
This is incorrect:
```
.gitignore
README.md
requirements.txt
ku-polls/         <-- Wrong: django project in a subdir of your repo
    manage.py
    mysite/
    polls/               
```

More complex projects *do use subdirs* as shown above, but please don't do that in this assignment.

## Work to Submit

Your Github repository should contain:

- `iteration1` branch merged into master or main
- a Pull Request, now closed
- "KU Polls" Project in the "Projects" tab
- "Iteration 1" task board in the "KU Polls" project & tasks for all work.
- Tasks for the work in Iteration 1 have descriptions and are now done.
- Well formatted, descriptive README.md with links to wiki files.
- Wiki containing pages: "Home", "Vision and Scope", "Project Plan", "Requirements", and "Iteration 1 Plan"

## References

[Import and Export Data](https://cpske.github.io/ISP/django/data-import-export) in Django. How to save data from your database to a file, and load the data again later.  This lets you recreate the database on another computer or switch to a different database (e.g. switch from SQLite to Postgresql).

[Learn about Github Project Boards](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

[Documenting your Projects on Github](https://guides.github.com/features/wikis/). 

[django-tutorial]: https://docs.djangoproject.com/en/4.1/intro/tutorial01/

### Evaluation Criteria (May be Revised)

1. Github Flow (3)
   - repo has `iteration1` branch with all your work.
   - `iteration1` has been merged into `main` (or `master`).
   - a Pull Request to merge iteration1 into main and PR is **closed**.

2. Project and Tasks: (3)
   - Project is shown on repo "Projects" tab **and** there - Has a Project with tasks for work done. (1pt)
   - Project has an "Iteration 1" task board with several tasks. (Tasks can be named "Implement tutorial part n" n=1..6, "Create Good Poll Questions", etc) (1pt)
   - All tasks (or almost all) are "Done". (1pt)

3. Running App with 2 Good Questions
   - we will clone either "main" or "iteration1"
   - after running migrations, we can import your poll questions & choices using:
     ```
     python manage.py loaddata data/polls-v1.json
     ```
   - code runs and shows 2 good questions. No trivial questions like "What is your favorite color?" or "What's up?".
   - Penalty for not removing dumb "What's Up?" question.

4. Tests
   - Code has at least 5 unit tests and the tests are not redundant.     
     2 points = tests all pass    
     1 point = some tests fail or fewer than 5 tests
     0 point = no tests or they all fail
   ```
   python manage.py test polls
   ```

5. Code Quality based on eximation of `polls/models.py`
   - 1 point: `polls/models.py` contains descriptive docstring comments, including module, class, and method comments.
   - No credit for: `"""The Question class.""" or other trivial, uninformative comment.
   - 1 point for layout: 1 blank line between **every** method. **2 blank lines** between classes. 
   - No point if even one instance of methods/classes not separated by blank line.

```python
# No credit - missing docstrings and missing blank line before `was_published` method
class Question(models.Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField(...)
    def was_published_recently(self):
        ...

    def __str__(self):
        return str(self.question_text)
```
