## Code Coverage

How thorough are your tests?    
Do your unit tests really test *all* the code?

**Code Coverage** is a measure of how much of your source code
is tested or "exercised" by unit tests. Code coverage measures how many
functions, methods, statements or lines of code, and branches are tested.

## Python Code Coverage

The [coverage package][coverage-docs] is a 
tool for measuring Python code coverage.  It measures how much of your
code is executed when a program is run.

[Coverage][coverage-docs] works with unit tests on any Python app, including Django.  To integrate code coverage with a CI server (like Travis-CI) use the online service [CodeCov](https://codecov.io).

To runs tests on a project with coverage, do the following.

1. [Install coverage package](https://coverage.readthedocs.io/en/coverage-4.5.x/install.html).  The instructions are different for each OS, so read the instructions.
In some cases you just type
    ```bash
    pip install coverage 
    ```
2. Check the installed version of coverage and read the list of command line uses:
    ```bash
    coverage --version
    coverage help
    ```
    The commands you'll probably use most are:
    ```
    coverage run some_program.py
    coverage report    # view results
    coverage html      # create html report
    coverage erase     # delete old reports
    ```
2. Use `coverage` to run your Python code.  To create a coverage report for your fraction testing assignment you need a test runner.  Its easy to add a "main" block to `fraction_test.py`:
    ```python
    if __name__ == '__main__':
        unittest.main(verbosity=2)
    ```
    Then run the tests with coverage:
    ```
    coverage run fraction_test.py
    ```
    You will see the usual unittest output on the console.  
3. View the coverage report as plain text:
    ```
    coverage report
    ```
4. Create HTML pages containing detailed information with links:
   ```
   coverage html
   ```
   and view the file `htmlcov/index.html` in a web browser. You can click on any file name to see what statements were "covered" during the run.

## Configure Coverage

You can configure what files are analyzied by `coverage` using
a `.coveragerc` file in your project directory, as described
in the [Coverages Docs][coverage-docs].

When using a library or framework, you usually want to **exclude** the library or framework from coverage analysis, to avoid distorting the results (and its not useful anyway).

For Django projects, you want to migrations, settings.py, manage.py, static files, and anything else you don't write unit tests for.

In the Django Polls tutorial, I used:
```
[run]
# measure branch coverage, too
branch = True
# don't measure python standard library (this is the default)
cover_pylib = False
# omit uninteresting stuff
omit =
    /usr/*
    mysite/*   # the main application 
    # TODO: omit unit test files and directories
    # TODO: omit migrations
# explicitly include the main app
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

How many test cases do we need to thoroughly test the code? That is, how many calls to `total(sale)`?

**Cyclomatic Complexity** is a measure of the complexity of a method, class, or package.  For a method, cyclomatic complexity is the number of different paths of execution through the method.

A simple formula for computing it is:
```
   complexity = #branches - #decision_points + 2
```
The complexity score is usually a bound for the number of tests needed to cover every path.  [Wikipedia][wikipedia-cyclomatic] has more details and examples.

### 100% Code Coverage Does Not Mean Tests are Perfect

You can have 100% code coverage and still miss defects.
Here are a couple of cases and examples.

* Both code and unit tests neglect some Use Cases.
  * Example: in Django polls tutorial, a user can manually submit a vote for a choice that doesn't exist.  Our code and tests don't check for invalid choices.
* A method has multiple conditional branches, and not all combinations are tested.
  * See the example below.

This is an e-commerse app.  Sales with value over 1,000 Baht get a 50 Baht discount, and Platinum customers always get a 3% discount.
What happens if a Platinum customer has a purchase of over 1,000 Baht?

```java
import pos.model.Sale;
import pos.model.Customer;

class Register {
    private static final PLATINUM_DISCOUNT = 0.03;

    public double computeTotalWithDiscount(Sale sale) {
        double total = sale.getTotal();
        Customer customwe = sale.getCustomer();
        if (customer.isPlatinum()) {
            total -= PLATINUM_DISCOUNT*total;
        }
        else if (total > 1000.0) {
            // everyone gets this discount
            total -= 50.0;
        }
        return total;
    }
}
```
* We might have unit tests that test for "Platinum" customer discounts and the 50 Baht discount, but not both.  We might miss the cases where both discounts apply.
* We might also miss some unclear requirements: what if a platinum customer buys 1,020 Baht?  
    - Should he get both discounts?  
    - Which discount should be applied first? (the discount will be different)


## CodeCov for Automated Coverage Analysis

[Codecov.io](https://codecov.io) is an online code coverage service
that integrates with CI pipelines, including Travis-CI and Circle-CI.

For Python projects, Codecov.io uses the Python "coverage" package
to perform the actual coverage analsys, so you still need "coverage" in your project.

To get started, go to [codecov.io](https://codecov.io) and register using your Github ID.  Give Codecov access to the project(s) you want it to pull and analyze.  It is similar to the way you give Travis permission to pull and build a project.

You can add or remove projects later by going into your Setting page on Github, look for the Codecov app, and add/remove projects.  This is the same procedure as adding Travis-CI to a Github project.

### Invoke Codecov from the Command Line

You can send your coverage reports directly to codecov.io from your own computer.  To do this you need a few things.

1. Install the `codecov` package.
    ```
    pip install codecov
    ```
2. Run "coverage" to create coverage data:
   ```
   coverage run your_python_tests.py
   ```
3. Get your CODECOV_TOKEN from codecov.io and add it as an environment variable:
   ```
   export CODECOV_TOKEN="02468aef00-1234..."
   ```

4. Send the coverage data to codecov.io:
   ```
   codecov
   ```
   You can combine steps 3 and 4 into a simple bash script.

Then go to your project page on codecov.io and see the results.

Once you know how Codecov works, you can easily add it to your Travis-CI configuration file and let Travis do the work for you.

### Integrate Codecov in a Travis-CI Build

To add Codecov to your CI build, add it to your `.travis.yml` file.

You need to change and add a few things in your travis config file.  There is more than one way to do this, so please read about on the web.  This is just one example.

```yml
install:
  - pip install codecov

script:
  - (run your unit tests with "coverage" to generate code coverage data)

after_success:
  - codecov
```

We installed `codecov` as a package in the "install" phase rather than adding it to requirements.txt.  That's becuase codecov is only needed for CI, not for production.

[Example Python Project](https://github.com/codecov/example-python) has example and explanation of configuring your project for codecov.

## Code Coverage for Java Projects

The most popular Java code coverage tools (still being maintained) are:

* [Clover](https://www.atlassian.com/software/clover) by Atlassian
* [JaCoCo](https://www.jacoco.org/jacoco/) - the web page mentions Eclipse but JaCoCo works with any Java project, not just Eclipse.  JaCoCo computes complexity and reports how much "complexity" was tested or missed.
* IntelliJ IDEA has a built-in coverage tool for Java

## Resources

* Python [Coverage Documentation][coverage-docs]
* [Introduction to Code Coverage][dzone-code-coverage] on DZone has example using Javascript and links to some popular code coverage tools.
* [Comparison of Code Coverage Tools](https://confluence.atlassian.com/clover/comparison-of-code-coverage-tools-681706101.html) on Atlassian (owner of Clover code coverage tool) compares features of some Java tools, including the free open-source tools JaCoco, JCov, and PIT.
* [JaCoCo][jacoco] is a code coverage tool for Java.

[coverage-docs]: https://coverage.readthedocs.io/ "coverage.py documentation"

[dzone-code-coverage]: https://dzone.com/articles/an-introduction-to-code-coverage "An Introduction to Code Coverage"

[jacoco]: https://www.eclemma.org/jacoco/

[wikipedia-cyclomatic]: https://en.wikipedia.org/wiki/Cyclomatic_complexity

