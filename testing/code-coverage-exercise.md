---
title: Code Coverage Exercise
---

Install the Python `coverage` package and use it to analyze how
much of the Auction class was exercised by your unit tests.

### Install Coverage

1. [Install coverage package](https://coverage.readthedocs.io/en/coverage-5.5.x/install.html).  The instructions are different for each OS, so read the instructions.
In many cases you just type
    ```
    pip install coverage 
    ```

2. Check the installed version of coverage and read the list of command line uses:
    ```bash
    coverage --version
    coverage help
    ```
    The commands you'll probably use most are:
    ```bash
    coverage run some_program.py    # run a program with code coverage reporting
    coverage report                 # view coverage report as text
    coverage html                   # create an html report
    coverage erase                  # delete data and report from previous run
    ```

3. Use `coverage` instead of `python3` to run a program and gather data on what statements in the program are executed.    
   Do this for unit tests to see how much of the target code (code being tested) is actually executed using your tests.  Enter:
   ```bash
   coverage run -m unittest auction_test.py
   ```
   or use auto-discovery to run all files named something\_test.py:
   ```bash
   coverage run -m unittest discover -p "*_test.py"
   ```

4. View the coverage report as plain text:
    ```
    coverage report
    ```

5. Create HTML pages containing detailed information with links:
   ```
   coverage html
   ```
   The output is put in subdirectory `htmlcov`.    
   Open the file `htmlcov/index.html` in a web browser. You can click on any file name to see what statements were "covered" during the run.

## Configure Coverage

You can configure what files are analyzed by `coverage` using
a `.coveragerc` file in your project directory, as described
in the [Coverages Docs][coverage-docs].

One useful option is to request "branch coverage", to count how completely "if - else ..." branches are executed.

For code that uses a library or framework, you want to **exclude** the library or framework from coverage analysis, since it's not useful and distorts the results.

For Django projects you want to exclude migrations, settings.py, manage.py, static files, and anything else you don't write unit tests for.

In the Django Polls tutorial, I used:
```bash
[run]
# measure branch coverage
branch = True
# don't measure python standard library (this is the default)
cover_pylib = False
# omit uninteresting stuff
omit =
    __init__.py
    /usr/*
    mysite/*       # the main application 
    */migrations/* # omit migrations
    */tests.py     # omit unit test files and directories
# explicitly include the main app
include =
    polls/*

# exclude some methods we don't test from the report and stats
[report]
exclude_lines =
    def __str__    # example
    def __repr__   # example
```

## How Many Unit Tests Are Enough?

Consider this example of computing the discount for a Sale:
> If the sale total is at least 1,000 Baht, give customer a 50 Baht discount.    
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

How many test cases do we need to thoroughly test this code? 

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

1. We might have unit tests that test for "Platinum" customer discounts and the 50 Baht discount, but not both.  We might miss the cases where both discounts apply.
2. We might miss an unclear requirement: *what if a platinum customer buys 1,020 Baht?*  
  - Should he get both discounts?  
  - Which discount should be applied first? (the total discount will be different!)


## CodeCov for Automated Coverage Analysis

[Codecov.io](https://codecov.io) is an online code coverage service
that integrates with CI pipelines, including Travis-CI and Circle-CI.

For Python projects, Codecov.io uses the Python "coverage" package
to perform the actual coverage analysis.

To get started, go to [codecov.io](https://codecov.io) and register using your Github ID.  Give Codecov access to the project(s) you want it to pull and analyze.  It is similar to the way you give Travis permission to pull and build a project.
Then modify your `.travis.yml` file to perform coverage analysis and send the data to codecov.io.

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

We installed `codecov` as a package in the "install" phase rather than adding it to requirements.txt.  That's becuase codecov is only needed for CI, not for running our app in production.

[Example Python Project](https://github.com/codecov/example-python) has example and explanation of configuring your project for codecov.

## Code Coverage for Java Projects

The most popular Java code coverage tools (still being maintained) are:

* [Clover](https://www.atlassian.com/software/clover) by Atlassian
* [JaCoCo](https://www.jacoco.org/jacoco/) - the web page mentions Eclipse but JaCoCo works with any Java project, not just Eclipse.  JaCoCo computes complexity and reports how much "complexity" was tested or missed.
* IntelliJ IDEA has a built-in coverage tool for Java

---

## Resources

* Python [Coverage Documentation][coverage-docs]
* [Introduction to Code Coverage][dzone-code-coverage] on DZone has example using Javascript and links to some popular code coverage tools.
* [Linting Python in VS Code][vscode-python-linting]: How to use Pylint, Flake8, etc. in VS Code

For Java:

* [JaCoCo][jacoco] a code coverage tool for Java.
* [OpenClover](https://openclover.org) code coverage and source analysis for Java based on Clover.
* [Comparison of Code Coverage Tools](https://confluence.atlassian.com/clover/comparison-of-code-coverage-tools-681706101.html) on Atlassian (owner of Clover code coverage tool) compares features of some Java tools, including the free open-source tools JaCoco, JCov, and PIT.

[coverage-docs]: https://coverage.readthedocs.io/ "coverage.py documentation"
[dzone-code-coverage]: https://dzone.com/articles/an-introduction-to-code-coverage "An Introduction to Code Coverage"
[jacoco]: https://www.eclemma.org/jacoco/
[wikipedia-cyclomatic]: https://en.wikipedia.org/wiki/Cyclomatic_complexity
[vscode-python-linting]: https://code.visualstudio.com/docs/python/linting
