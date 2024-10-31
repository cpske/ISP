---
title: Feedback on Movie Rental Refactoring
---

## Don't Use Loops for Simple Sums

Agile Programming Tip: *Code Expressively*

This code does not clearly show the **intent**:
```python
    def total_amount(self):
        """Calculate the total charge of all the rentals."""
        total = 0
        for rental in self.rentals:
            total += rental.get_price()
        return total
```

Compare to this:
```python
    def total_amount(self):
        """Calculate the total charge of all the rentals."""
        return sum(rental.get_price() for rental in self.rentals)
```

This code clearly show the *intent* to to sum the rental prices.
Easier to read.

More than 1/2 of the class wrote loops like this.

*Please learn to use Python fluently.*


## Duplicate constants

Don't create 2 constants that refer to the same thing.
It is confusing, makes code harder to maintain (what if
you a DOCUMENTARY pricing rule?), and error-prone.

```python
from pricing import REGULAR, NEW_RELEASE, CHILDREN

class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    REGULAR = REGULAR
    NEW_RELEASE = NEW_RELEASE
    CHILDRENS = CHILDREN
```
