
## Plan - Do - Evaluate

* Plan the work - write iteration plan, create polls app and "scope out" the work, create tasks
* Do the tutorial in parts - commit each of 7 parts
* Evaluate - review what you learned

## Practice Good Iterative Development

Software engineers must manage their own time.

There were 2 weeks to complete this iteration,
so after 1 week you should have made some progress.

You should perform assignment the way you would work
on a real project.

I checked work twice:

* Wednesday, 9 Sep (day 9 of iteration)
  - complete Vision, Iteration Plan, Project board, `iteration1` branch with some work
* Sataurday, 12 Sep (last day of iterattion)
  - nearly finished work on `iteration1` branch
  - most tasks on Project board In Progress or Done

## Work First, Plan Later

Some students wrote the iteration plan **after** doing all the work.


## Common Mistakes

1. Commiting `.DS_Store` files, SQLite database file, and IDE files (`.idea`, `.vscode`).
2. Add extra layer of directories
3. `.gitignore` in subdirectory - it is useless there
4. README has bad or missing links to docs, formatting poor.

## Repository has extra layer of directories

Many students created a repo with an extra layer of directory.
The instructions for this assignment stated not to do that.  

Their repo contains:
```
.gitignore
README.md
mysite/
          mysite/
          polls/
          manage.py
```
should be (as shown by example in the assignment):
```
.gitignore
README.md
mysite/
polls/
manage.py
```

On some projects, creating an extra layer of directories may be OK.
The team would have to decide on that.  I don't see any
advantage to that for Django projects.

Create Django project **in the current directory** instead of a new subdirectory:
```
  django-admin startproject mysite .       <-- last argument is "." (period)
```
