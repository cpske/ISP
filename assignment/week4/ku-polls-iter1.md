---
title: KU Polls Iteration 1
---

## Assignment 

Perform iteration 1 of the KU Polls application.

The code for this iteration matches what's in the Django tutorial.

1. Create an "Iteration 1 Plan" page in your `ku-polls` wiki. It should include:
   - **Goal** for the iteration
   - **Features** to implement (discussed in class)
   - Tasks; or write the tasks in your task board to avoid redundancy
   - **Acceptance Criteria** - when is the work done?
   - **Retrospective** - record useful lessons learned, observations, and plan for improving your process

2. Create a **task board** using Github projects.
   - Click the `Projects` tab in your `ku-polls` repo to create a project.
   - Task board is for tasks in this iteration.
   - Record your tasks and their status. 
   - Task board should have at least 3 columns: To do (Backlog), In Progress, Done.
   - Each task should have short title and a description.
   - It's up to you how to define tasks.  Looking at the work in the Django tutorial may give some ideas.

3. Create a branch named `iteration1` and do your work on that branch.
   - Push to Github after finishing each part of the Django tutorial. 
   - Don't wait until your done everything to push to Github!
   - When everything is done and passes both unit tests and interactive tests, merge `iteration1` into `master` and push to Github.

4. Implement all parts of the [Django Tutorial][django-tutorial]
   - Don't use copy and paste when doing the tutorial. Type everything yourself. 
   - In some parts of the tutorial they convert method-based views to class views.  It is OK to leave some views as method-based views, providing you have the same functionality.

5. Add at least 2 interesting questions to your polls application, and delete boring "What's up?" question from the tutorial.
   - "Interesting" is subjective, but avoid stuff like "How are you?", "What's your favorite color?".

You can add some optional embellishments, such as a graph of the results or styling uusing Bootstrap, etc.

## Optional: Improve Security

The Django `settings.py` file contains some sensitive information that you should not commit to Github.  Right now, the only sensitive value is `SECRET_KEY`:

```python
# File: mysite/settings.py

SECRET_KEY = 'some-random-secret-key'
```

In Iteration 2 we'll implement *Externalizing Configuration Data*,
but for **good security**, you may want to do it now.  It's easy.

On the ISP github.io site, the topic "Externalize Configuration" describes how
to put configuration data in a separate file and *easily* use the data in `settings.py`.  With either package, your settings.py would look like this:

```python
SECRET_KEY = env('SECRET_KEY') 
```
You can also specify a default value, in case the data file (`.env`) is missing:
```python
SECRET_KEY = env('SECRET_KEY', default='missing-secret-key') 
```

The data file (`.env`) is not committed to git.


## What You Should Have

When you are done, you git repository should look like this:
```
    .gitignore
    manage.py
    README.md
    requirements.txt     <-- Optional. List of required Python packages.
    mysite/              <-- where application settings.py and urls.py are
    polls/               <-- the polls "app" code and templates
    templates/           <-- global templates and admin app custom templates
```

Your working copy will look like this:
```
ku-pulls/                <-- your LOCAL directory, NOT part of git repo.
    .gitignore
    db.sqlite3           <-- your WORKING COPY, but NOT committed to git repo.
    manage.py
    README.md
    requirements.txt     <-- Optional. List of required Python packages.
    mysite/              <-- where application settings.py and urls.py are
    polls/               <-- the polls "app" code and templates
    templates/           <-- global templates and admin app custom templates
```

The configuration directory can have a name different from `mysite`,
such as `config`.  But avoid using `ku-polls` (confusing with `polls`).

Your README file should contain links to
* Vision Statement
* Requirements
* Iteration 1 Plan

## References

[Learn about Github Project Boards](https://docs.github.com/en/github/managing-your-work-on-github/about-project-boards) - for this assignment, be sure to use a project board linked to your `ku-polls` repository.

[django-tutorial]: https://docs.djangoproject.com/en/3.1/intro/tutorial01/
