## Code Coverage

How thorough are your tests?    
Do your unit tests really test *all* the code?

**Code Coverage** is a measure of how much of your source code
is tested or "exercised" by unit tests. Code coverage measures how many
functions, methods, statements or lines of code, and branches are tested.

## Python Code Coverage

The [coverage package](https://coverage.readthedocs.io/en/coverage-4.4.2/) is a useful
tool for measuring Python code coverage.

Coverage works will unit tests of all Python apps, but this example refers to testing Django projects.

To runs tests on a Django project with coverage, do the following.

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

### 100% Code Coverage Does Not Mean Tests are Perfect

You can have 100% code coverage and still miss defects.
Here are a couple of cases and examples.

* Both code and unit tests neglect some Use Cases.
  * Example: in Django polls tutorial, a user can manually submit a vote for a choice that doesn't exist.  Our code and tests don't check for invalide choices.
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

[coverage-docs]: https://coverage.readthedocs.io/en/v4.5.x/ "coverage.py documentation"

[dzone-code-coverage]: https://dzone.com/articles/an-introduction-to-code-coverage "An Introduction to Code Coverage"

[jacoco]: https://www.eclemma.org/jacoco/

