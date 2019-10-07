Continuous Integration Demo
============================

This project demonstrates use of Travis CI to build and test a Python project.  To do this, you first need a git repo with a remote on Github.

### Setup

1. Download `demo-pyci.zip`.
2. Change to a directory where you store projects (but **not** inside another git repo) and unpack the zip file.  This will create a subdir like this:
    ```
    demo-pyci/
        README.md
        stats.py
        stats_test.py
    ```
3. Change dir to `demo-pyci` and do:
   - create a git repository
   - add all 3 files
   - create and add a .gitignore file for Python projects.  You should *at least* ignore `__pycache__` dirs.
   - commit everything to the git repo
4. Create a public `demo-pyci` repository on Github and
   - add it as remote for your local demo-pyci repo
   - push everything to Github

## Run the Tests Locally - One test should FAIL

Run the tests yourself to verify the code (almost) works.
We will then "script" this command for Travis to run for us.

Run the unit tests using auto-discovery (so you don't
need to the name of the test file) using:
```bash
  python -m unittest discover -p "*_test.py"
```
The `-p "*_test.py"` defines a **pattern** for unit test files.
If you wanted files *beginning* with "test_" you would use
`-p test_*.py`.

It should run 3 tests and one test fails.

**Don't fix it**  We want a failure so you can see how Travis notifies you.

## Add Travis-CI for Automatic Testing

[Travis-CI](https://travis-ci.com) is a continuous integration server for building, testing, and deploying software projects.  It works with many lanaguages and integrates easily with Github.

1. Create a Travis account on travis-ci.com using Github authentication.
   - When you connect your Travis account to Github, a dialog will ask which Github projects you want to allow Travis to access.
   - You can grant access to specific projects or all projects. The next step (here) shows how to grant access to a project at any time.
2. On Github, in your Personal Settings page, select Applications. Choose "Travis" and add the project you want to Travis to test.  
    - If you already gave Travis access to all your repos, skip this step.
    - Otherwise, grant access to the `demo-pyci` project.
3. In your local repository, add a Travis Configuration file named `.travis.yml` that describes your project.  Here is a simple `.travis.yml` for this project:
    ```
    language: python
    
    python: "3.6"
    
    # don't clone more than necessary
    git:
      depth: 1
    
    # Install dependencies
    install:
      - pip install -r requirements.txt
    
    # script to run tests. Can also use make, e.g. "make test"
    script: 
      - python -m unittest discover -p "*_test.py"
    ```
    This project doesn't require any add-on modules (requirements.txt is empty), so we could omit the `install:` section, but it is shown as example.
4. Add your `.travis.yml` file to the git repo, commit it, and push to Github.
5. Next go to https://travis-ci.com/your_githubid/demo-pyci.  You should see Travis pull, build, and run the project.

## Become Familiar with the Travis Web Interface

Your Travis home pages shows    
Left Side:
* your repositories that Travis is monitoring
* status of recent "builds"

Right Side (details for one repo selected on left side):
* Current build and screen showing console log
* Branches that Travis is monitoring and building (if any)
* History
* Pull Requests - Travis knows about Pull Requests!

Your Job Log screen will look something like this:
![travis build log](travis-build-demo-pyci.png)

Some parts of the log are collapsed ("Build System Information").  Click to expand and see how much work Travis is doing for you!

### Travis runs Python apps in a virtualenv. 

The "Build system information" section of Travis Job Log
shows that Travis uses a virtualenv to run Python projects,
and uses `pip` and `requirements.txt` to add required packages.

## Adding a Badge to your Project README.md

Add a Travis status notification at the top of your README.md file, called a "badge".  It looks like this:    
[![Build Status](https://travis-ci.com/jbrucker/demo-pyci.svg?branch=master)](https://travis-ci.com/jbrucker/demo-pyci)

The Markdown for this is:
```markdown
[![Build Status](https://travis-ci.com/your_acctid/demo-pyci.svg?branch=master)](https://travis-ci.com/your_acctid/demo-pyci)
```
In markdown `![text msg](/path/imagename)` includes an image in a page. That is wrapped inside another `[text](url)` markup to put the image into a clickable link (link to `url`).

Teams uses "badges" for many things, so when someone visits the Github repo they immediately see the project status.

## Fix the Bug and Watch Travis Rebuild your Project

1. Fix the bug in `stats.py`.  It is supposed to throw a `ValueError` when there is no data.  
2. Run the tests locally. They should all pass.
3. Commit and push your fix.
4. Visit your Travis page again.  It may take a minute or two to pull the new code, but you should see it rebuild the project and everything passes.
5. Visit your project on Github.  Does the "badge" show the project passing?
  
## Travis for Neanderthals 

Another way to "build" and test Python projects is the
venerable (ancient) GNU Make utility.

Make is a build system configured using a `Makefile` that defines relationships between targets and dependencies, along with commands to run. 
You can use "make" to build almost any kind of project.  Make is used to compile the Linux operating sytem, MySQL (from source code), books written using LaTeX, and more.

To use "make" in your project, in `.travis.yml` write:
```
script:
  - make test
```
you must provide a Makefile with a `test` target that runs your tests.
There's really no benefit to this for Python, unless you really love make.

------
### Reading

You should read and understand these short documents:

[Travis Getting Started Guide](https://docs.travis-ci.com/user/tutorial/)

[Building a Python Project](https://docs.travis-ci.com/user/languages/python/) with Travis CI. 


