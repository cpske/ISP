## Project Homepage Updates

Update the home page (README.md) of your Github repository to
include the following information, in this order.

1. Description of the project.  At least one paragraph.

2. Links to documents
   a. Link to iteration plans.  When someone clicks on this link it should actually show a list of iteration plans (if you have one doc per iteration) or directly open the iteration plan (if all in one document).  Just linking to the wiki is not good enough.
   b. Link to task board.
   c. Link to issues (for most projects this is the Github issue tracker)

3. Instructions to Install and Run Application Locally (see below)

## Write Better Iteration Plans

Iteration Plans should be clear about the work to be done, time estimates, and goal of the iteration.
Many iteration plans reviewed so far need improvement.  Revise your **current** (this week's) iteration plan so that:

1. Goals are clearly stated and precise.  Goals should be something the app can **do**, or some characteristic it **possesses**.
    * functional ("doing") goal:  a user can authenticate himself and view list of current polls.
    * non-functional goal: app is deployed to AWS EC2, and accepts simultaneous user logins.
    * Poorly written goals: "Implement basic UI", "Connect Django to React", "Separate data into categories" (a task not a goal, and its too vague -- *what* data?), "make index page" (also a task)
2. Tasks are clearly stated and specific.  Tasks are something for a person to do.  Avoid tasks that are too broad or vague.

## Descriptive Tasks with Time and Team Member

Many tasks are poorly written. The descriptions are vague, lack detail, don't contain time estimates (or actual time for "done" tasks), or the name of person performing the task.

1. Tasks should be added to task board during the iteration planning meeting. New unplanned tasks can be added during the iteration.
2. Task names should be clear and specific.  Use the body of task item to provide additional information.
3. Tasks should have an estimated time, and completed tasks should have the actual time spent.  For learning, it is good to be honest about actual time spent and compare the estimated and actual times.

| Poor task description |  Reason |
|-----------------------|---------|
| *Add more unit tests*   | Too vague, not specific, and too broad. |
| *CI*                    | Not something to do. Better: "Setup CI using Travis." |
| *Hotfix security*       | Fix *what*? Why is it a "hotfix" (you haven't deployed app yet). |


## Better and More Unit Testing

Projects I reviewed have very little unit testing.
Your unit tests should generally contain **more lines of code** than your
model and controller classes combined, since unit tests have to test several cases.

1. Write good unit tests for all methods that involve any non-trivial logic.
   * You don't need to test trivial get-set methods or simple constructors.
2. All tests should have a descriptive name for what they test (long names are good) **and** a comment describing the test.
3. Write tests for persistence (database storage) operations. 
   * Suggest use an in-memory database for speed and consistent test environment. In-memory databases are recreated each time the database is started you will have a consistent test environment. You also need to recreate the schema each time (e.g. run the Django `manage.py migrate` command in your tests). SQLite, H2, HSQLDB all provide in-memory databases.  [SQLite in-memory databases](https://www.sqlite.org/inmemorydb.html)
5. Test controllers (Django "views") correctly handle both valid and invalid requests.  Test for unauthorized request of an operation that requires authorization.

## Instructions How to Install and Run Locally

Write instructions so that someone else in the class can install your application on
their computer, configure it, and run it locally.

Instructions should include:

1. Required software and how to install it.  For Python or Scala, just provide a link to the official download site. 
2. For Django, Play, and Flask frameworks if they can be easily installed from command line then show the command to run, e.g. `pip install django` otherwise, provide link to the framework's install instructions.
3. Steps needed to configure the application for running.  This includes 
   * cloning your project from github
   * editing a configuration file or two (give example what to do)
   * initializing the database schema and adding initial data to the database.
4.  Please **do not** require someone install a database like MySQL or PostgreSQL.  Use a lightweight database, such as SQLite for Python projects or H2 for Play (whatever is included with Play).
5. How to run the application and verify its working.

## Your Peers with Validate Your Instructions

Other students will be assigned to follow your instructions and run your app.