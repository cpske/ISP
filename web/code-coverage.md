## Code Coverage

Code Coverage is a measure of how much of your source code
is tested or "exercised" by unit tests. Code coverage measures how many
functions, methods, statements or lines of code, and branches are tested.

[Introduction to Code Coverage][dzone-code-coverage] on DZone has example using Javascript and links to some popular code coverage tools.

### 100% Code Coverage Does Not Mean Tests are Perfect

You can have 100% code coverage and still miss defects.
Here are a couple of cases and examples.

* Both code and unit tests neglect some use case.
  * Example: in Django polls tutorial, a user could manually submit a vote for a choice that doesn't exist.  Our code and tests might not check that for valid choices.
* A method has multiple conditional branches, and not all combinations are tested.
  * Example: in an e-commerce example, a "platinum card" member gets a 3% discount on all purchases.  Everyone gets a 50 Bath discount on a purchase of 1,000 Baht or more.  Is the following code correct?

```java
import pos.model.Sale;
import pos.model.Customer;

class Register {
    private static final PLATINUM_DISCOUNT = 0.03;

    public double computeTotalWithDiscount(Sale sale) {
        double total = sale.getTotal();
        Customer cust = sale.getCustomer();
        if (cust.isPlatinum()) {
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
    * We could have unit tests that test for "platinum" customer discounts and the 50 Baht discount, but not both.  We might miss the cases where both discounts apply.
    * We would also miss some unclear specification: what if a platinum customer buys 1,020 Baht.  Should he get both discounts?  Which discount should be applied first?


## Code Coverage Tools

[JaCoCo][jacoco] for Java. Other free tools are JCov and PIT.

## Resources

[dzone-code-coverage]: https://dzone.com/articles/an-introduction-to-code-coverage "An Introduction to Code Coverage"

[jacoco]: https://www.eclemma.org/jacoco/

* [Comparison of Code Coverage Tools](https://confluence.atlassian.com/clover/comparison-of-code-coverage-tools-681706101.html) on Atlassian (owner of Clover code coverage tool) compares features of some Java tools, including the free open-source tools JaCoco, JCov, and PIT.

