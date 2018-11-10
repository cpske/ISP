## Test Code Coverage

How thorough are your tests?  One way is to check how many
statements are exercised (run) by your unit tests,
called "code coverage".

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


[Coverage Documentation][coverage-docs]

[coverage-docs]: https://coverage.readthedocs.io/en/v4.5.x/ "coverage.py documentation"

