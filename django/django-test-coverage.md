## Test Code Coverage

How thorough are your tests?  
One way is to measure the percentage of statements
that are exercised (run) by your unit tests,
called "**code coverage**".

To runs tests on a Django project with code coverage,
do the following.

1. [Install coverage package](https://coverage.readthedocs.io/en/coverage-4.4.2/install.html) using:
```
pip install coverage
```
2. Use `coverage` to run your Python code.  In the Django Polls tutorial project, run:
```
coverage run manage.py test polls -v 2
```
    You will see the usual unit test output on the console.  The flag `-v 2` is a "verbosity" option for coverage to request additional output.
3. View the coverage report as plain text:
```
coverage report
```
4. Create HTML pages containing detailed information:
```
coverage html
```
5. View the file `htmlcov/index.html` in your web browser.

## Configure Coverage

You can configure what files are checked by `coverage` using
a `.coveragerc` file in your project directory, as described
in the [Coverages Docs][coverage-docs].

In the Django Polls tutorial, I used:
```
[run]
# measure branch coverage
branch = True
# don't measure python standard library (this is the default)
cover_pylib = False
# omit uninteresting stuff
omit =
    /usr/*
    mysite/*   # the main application dir contains only configuration
    info/*     # the info app is just for testing
    # TODO: omit unit test files and directories
    # TODO: omit migrations

# explicitly include the main apps
include =
    polls/*
```

## Code Coverage for Java Projects

The most popular Java code coverage tools (still being maintained) are:

* [Clover](https://www.atlassian.com/software/clover) by Atlassian
* [JaCoCo](https://www.jacoco.org/jacoco/) - the web page mentions Eclipse but JaCoCo works with any Java project, not just Eclipse.
* IntelliJ IDEA has a built-in coverage tool for Java

## Reference

[Coverage Documentation][coverage-docs]

[coverage-docs]: https://coverage.readthedocs.io/en/v4.5.x/ "coverage.py documentation"
