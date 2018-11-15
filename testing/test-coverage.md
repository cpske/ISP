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

## How Many Unit Tests Are Enough?

Consider this example of computing the discount for a Sale:
> If the sale total is at least 1,000 Baht, give a 50 Baht discount.
> If the customer pays using cash, then give a 2% discount.

```python
def total(sale):
    """Compute total price of a sale, including discounts."""
    total_price = sale.get_total()
    if sale.payment.type == PaymentType.CASH:
        total_price = 0.98*total_price
    if total_price >= 1000:
        total_price -= 50
    return total_price
```

How many test cases -- that is, how many different calls to total(sale) -- do we
need to thoroughly test this code?

**Cyclomatic Complexity** is a measure of the complexity of a method, class, or package.  For a method, cyclomatic complexity is the number of different paths of execution through the method.

A simple formula for computing it is:
```
   complexity = #branches - #decision_points + 1
```

JaCoCo (Java coverage tool) computes complexity and reports how much "complexity" was tested or missed.

## Code Coverage for Java Projects

The most popular Java code coverage tools (still being maintained) are:

* [Clover](https://www.atlassian.com/software/clover) by Atlassian
* [JaCoCo](https://www.jacoco.org/jacoco/) - the web page mentions Eclipse but JaCoCo works with any Java project, not just Eclipse.
* IntelliJ IDEA has a built-in coverage tool for Java

## Reference

[Coverage Documentation][coverage-docs]

[coverage-docs]: https://coverage.readthedocs.io/en/v4.5.x/ "coverage.py documentation"
