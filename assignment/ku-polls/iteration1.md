---
title: KU Polls Iteration 1
---

## Assignment 

Perform iteration 1 of the KU Polls application.

The requirements and code for this iteration match the [Django Tutorial][django-tutorial].

1. Create an "Iteration 1 Plan" page in your `ku-polls` wiki. Include:
   - **Goal** for the iteration
   - **Features** to implement (discussed in class)
   - **Acceptance Criteria** - when is the work done? how will you test the code?

2. Create a **task board** using a Github Project.
   - Click the `Projects` tab in your `ku-polls` repo to create a Project.
   - Read about "Projects" and project boards on Github
   - Create an "Iteration 1" project for this iteration.
   - Task board (Project board) should have at least 3 columns: To do (Backlog), In Progress, Done. Github will create these columns if you choose a Kanban project.
   - Record your tasks and their status. 
   - Each task should have short title and a longer description.
   - You define your own tasks based on the Iteration Plan.  
     - Look at the work in the Django tutorial to get ideas what you need to do.

3. Create a **git branch** named `iteration1` and do your work on this branch.
   - **Push to Github** when you finish **each part of the Django tutorial**. 
   - Pushing work to Github regularly is a good habit and avoids losing work.

4. Implement at least part 1 - 6 of the [Django Tutorial][django-tutorial]
   - Do **not use copy and paste** when doing the tutorial. You will learn **much better** by typing everything yourself.  See how much you can enter without looking back at the tutorial text.
   - In the tutorial they convert function-based views to class views.  It is OK to leave some views as function-based views, provided that view provides the same functionality.
   - Read part 7 of the tutorial (customizing the admin interface); implementing this is recommended but not required.

5. Add at least **2 interesting poll questions** to your application, and **delete** the boring "What's up?" question from your polls.
   - please avoid uninteresting things like "How are you?", "What's your favorite color?".

6. Optional: add embellishments, such as a graph of poll results, a custom background, or CSS with Bootstrap.

7. After you finish and test everything, **merge** branch `iteration1` into `master` and push to Github.


## Optional: Improve Security

The Django `settings.py` file contains some sensitive information that you should not commit to Github.  Right now, the only sensitive value is `SECRET_KEY`:

```python
# File: mysite/settings.py

SECRET_KEY = 'some-random-secret-key'
```

In Iteration 2 we'll implement *Externalizing Configuration Data*,
but for **good security**, you may want to do this now.  

It's easy.

On the ISP github.io site, the topic [Externalize Configuration][] explains how
to put configuration data in a separate file and *easily* use the data 
in `settings.py`.  After that, your settings.py would look like this:

```python
SECRET_KEY = env('SECRET_KEY') 
```
You can also specify a default value, in case the data file (`.env`) is missing:
```python
SECRET_KEY = env('SECRET_KEY', default='missing-secret-key') 
```

The data file (`.env`) should not be committed to git.

[Externalize Configuration]: https://cpske.github.io/ISP/django/external-configuration


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
