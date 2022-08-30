---
title: KU Polls Iteration 1
---

You will learn Django and implement KU Polls using the [Django Tutorial][django-tutorial].
The assignments for the next 3 weeks will add to this code, so don't fall behind.

## Assignment 

The code you will produce for this iteration match the [Django Tutorial][django-tutorial].

The Requirement are as in the example project:
1. Display a list of poll questions
2. Visiter can select a poll question and vote for a choice. His vote is added to the total.
3. Visitor can see total votes for each choice in a poll.
4. Each poll has a publication date (start date) & is visible only on or after this date.
5. Administrator can add or modify poll questions and choices.

1. Create a wiki page named "Iteration 1 Plan" page in your `ku-polls` wiki. Include:
   - **Goal** for the iteration
   - **Features** to implement
   - **Milestone**, at least one
   - **Acceptance Criteria** - how to evaluate the result?

2. Create a **task board** named "Iteration 1" in your "KU Polls" Project (that you created in the lab).
   - Add tasks and features for this iteration.
   - Convert "tasks" to "issues" wherever it makes sense.
   - Suggestion: if you add an "Iteration" field to your Project (in Project Settings), you can assign tasks to an iteration (using the table view).  Then, in the "Iteration 1" project tab (view as task board) add a "Filter" so that only tasks with "Iteration" value of 1 are shown.

3. Use Github Flow.
   - Create a **git branch** named `iteration1` and do your work on this branch.
   - **Push to Github** when you finish **each part** of the Django tutorial. 

4. Implement parts 1 - 6 of the [Django Tutorial][django-tutorial].
   Your Django project code should be in the root directory of your `ku-polls` repository (which you have already created), not a subdirectory.    
   So, when you create the Django project do it like this (instead of as in the tutorial):
   ```
   # change directory to your ku-polls repository (Windows use chdir)
   cd ku-polls
   # create a Django project *here*.  The "." parameter means to create it in this directory.
   django-admin startproject mysite .
   # Show the files. Windows: "dir" any other OS: "ls"
   ls
   ```
   it should show:
   ```
   README.md    (file you cloned from Github repo)
   manage.py
   mysite       (directory)
   ```

5. Add at least **2 interesting poll questions** to your application, and **delete** the boring "What's up?" question.
   - no trivial questions like "How are you?", "What's your favorite color?"

6. Optional: add embellishments, such as a graph of poll results, a custom background, or CSS styling.

7. When you finish and test everything, open a **Pull Request** to merge, then review your own work, and **merge** branch `iteration1` into `master`. It should be a simple "fast forward" merge.


### Suggestions

- Do **not use copy and paste** when doing the tutorial. You learn **better** by engaging your senses -- that means typing it yourself! Typing also forces you to *remember* what you just read.

- The tutorial converts function-based views to class views.  It is OK to leave some views as function-based views, but you should try class views -- they can do a lot more.
- Part 7 of the tutorial (customizing the admin interface) is helpful but not required.

### Optional: Improve Security

Everyone will do this in Iteration 2, but if you are security-conscious then do this now.

The Django `settings.py` file contains sensitive information that you should not commit to Github.  Right now, the only sensitive value is `SECRET_KEY`:

```python
# File: mysite/settings.py

SECRET_KEY = 'some-random-secret-key'
```

For security, the value of the `SECRET_KEY` should not be in a file commited to Github.  

On the ISP github.io site, the topic [Externalize Configuration][] explains how
to put configuration data in a separate file and *easily* use the data 
in `settings.py`.  After that, your settings.py would look like this:

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='missing-secret-key') 
```

The data file (usually named `.env`) should not be committed to git.

[Externalize Configuration]: https://cpske.github.io/ISP/django/external-configuration


## What To Submit

When you are done, your Github repository should look like this:
```
    .gitignore
    manage.py
    README.md
    requirements.txt     <-- List of required Python packages, including Django
    mysite/              <-- where application settings.py and urls.py are
        settting.py
        urls.py
        etc.
    polls/               <-- the polls "app" code and templates
    templates/           <-- global templates and admin app custom templates
```

Wrong: your Github repo should not contain an extra level of directories.    
This is incorrect:
```
    .gitignore
    README.md
    ku-polls/            <-- Wrong: django project in a subdirectory
        manage.py
        mysite/
            settting.py
            urls.py
            etc.
        polls/               
```
You can use the subdirectory layout in other projects (if you want) but not this assignment.

README.md should contain a brief description of the app and links to wiki pages:

- Vision Statement
- Requirements
- Development Plan
- Iteration 1 Plan

Your Github repository should also contain:

- `iteration1` branch merged into master or main
- at least 1 Pull Request, now closed
- "KU Polls" Project in the "Projects" tab.
- "Iteration 1" task board in the "KU Polls" Project.  Most tasks should be "Done".
- Github Issues for work in Iteration 1, now closed

## References

[Learn about Github Project Boards](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

[Documenting your Projects on Github](https://guides.github.com/features/wikis/). 

[django-tutorial]: https://docs.djangoproject.com/en/4.1/intro/tutorial01/
