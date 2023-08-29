---
title: KU Polls Iteration 1
---

You will learn Django and implement KU Polls using the [Django Tutorial][django-tutorial].
The assignments for the next 3 weeks will add to this code, so don't fall behind.

The Requirements for this iteration are:

1. Display a list of poll questions with multiple-choice answers.
2. Visiter can select a poll question and vote for a choice. His vote is added to the total.
3. Visitor can see total votes for each choice in a poll.
4. Each poll has a publication date (start date) & is visible only on or after this date.
5. Poll questions and choices can be added or changed using the admin interface.

Features not implemented in this iteration:

- we will not implement any authentication and, as a result, will not track who has replied to which poll question. 
- hence, a user cannot change a previously submitted poll choice, although he can submit another choice

## Assignment 

The code you will produce for this iteration matches the [Django Tutorial][django-tutorial].

1. Create a wiki page named "Iteration 1 Plan" page in your `ku-polls` wiki. Your "Iteration 1 Plan" should have these sections:
   - **Goal** for the iteration
   - **Milestone**, a concrete, visible indicator of progress.
   - **Features** to implement and other major work (but not tasks)
   - **Acceptance Criteria** - how to evaluate the result?

2. Create a Github **Project** with a Table View all tasks. 
   - Define columns and fields you want.
   - In the Project settings, define a field named `Iteration`. Each task should be assigned to an Iteration.
   - Then, in your Task Board for each iteration you can **filter** only the tasks whose iteration value is the one you want.
   - Add Product Backlog of features to implement

3. Create a **Task Board** named "Iteration 1" in your Project.
   - Add tasks for work to do in this iteration.
   - In Iteration 1 you will write code following the Django Tutorial, so you may define tasks like "Implement tutorial part 1", "Implement tutorial part 2", ..., 
   - Other work you must do: "Add Good Poll Questions", "Review work and merge into main"
   - Convert "tasks" to "issues". Most tasks *should* be issues, but you may have some "housekeeping" tasks that are not issues in the repo.

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

5. Create a Branch and use Github Flow.
   - Create a branch named **iteration1** and do your work on this branch.

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
   - No boring, trivial questions like "How are you?", "What's your favorite color?"

9. Do not include `db.sqlite3` in your repository.  Instead, export your polls data to a file named **data/polls-v1.json**.  Here's is how:
   ```
   # in your "ku-polls" repository, enter:
   mkdir data
   python manage.py dumpdata --indent=2 -o data/polls-v1.json polls
   ```
   Include `data/` and `data/polls-v1.json` in your git repository.

10. When you finish and test everything, open a **Pull Request** to merge.    
   Then, take a break.  Afterwards, review your own work, and **merge** branch `iteration1` into `master`. It should be a simple "fast forward" merge.


### Suggestions

- Do **not use copy and paste** when doing the tutorial. You learn **better** by actually typing it yourself!  Typing engages your senses and forces you to *remember* what you just read.

- The tutorial converts function-based views to class views.  It is OK to leave some function-based views, but you should try class views -- they can do a lot more.
- Part 7 of the tutorial (customizing the admin interface) is useful but not required.

### Optional: Improve Appearance

You can add CSS styling to pages, add a graph of the poll results, and other stylistic improvements.

### Optional: Improve Security

Everyone will do this in Iteration 2, but if you are security-conscious then do this now.

The Django `settings.py` file contains sensitive information that you should not commit to Github.  Right now, the only sensitive value is `SECRET_KEY`:

```python
# File: mysite/settings.py

SECRET_KEY = 'some-random-secret-key'
```

For security, the value of the `SECRET_KEY` should not be in a separate file and not committed to git. 

You can do this in 4 steps:

1. Install the `python-decouple` package: `pip install python-decouple`
2. Add `python-decouple` to your `requirements.txt` file on a separate line.
3. Edit `mysite/settings.py` and define `SECRET_KEY` as an environment variable:
   ```python
   from decouple import config

   SECRET_KEY = config('SECRET_KEY', default='fake-secret-key') 
   ```
4. Create a file for externalized data. It is named `.env` in the project's root directory (not the mysite directory) and contains this:
   ```
   # contents of .env
   SECRET_KEY = your-actual-secret-key-without-quotation-marks
   ```
   The `.env` file should not be committed to git.

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
       settting.py
       urls.py
       etc.
   polls/               
```

More complex projects *do use subdirs* as shown above, but please don't do that in this assignment.

Your Github repository should also contain:

- `iteration1` branch merged into master or main
- at least 1 Pull Request, now closed
- "KU Polls" Project in the "Projects" tab
- Github Issues for work in Iteration 1, now closed.
- "Iteration 1" task board in the "KU Polls" Project.  All (or most) tasks should be "Done".

## References

[Import and Export Data](https://cpske.github.io/ISP/django/data-import-export) in Django. How to save data from your database to a file, and load the data again later.  This lets you recreate the database on another computer or switch to a different database (e.g. switch from SQLite to Postgresql).

[Learn about Github Project Boards](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

[Documenting your Projects on Github](https://guides.github.com/features/wikis/). 

[django-tutorial]: https://docs.djangoproject.com/en/4.1/intro/tutorial01/

### Evaluation Criteria

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
   - code should include a `db.sqlite3` file containing your questions
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
