---
title: Feedback on Movie Rental Refactoring
---

## Don't Use Loops for Simple Sums

Agile Programming Tip: *Code Intently and Expressively*

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

This code more clearly shows the *intention* is to sum the rental prices.

More than 1/2 of the class wrote a `for` loop.

*Please use Python fluently.*


## Replace Type Code with Strategy and Replace Conditional with Polymorphism

You should remove the named constants in Movie:
```python
class Movie:
    # Delete these 
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDRENS = 2
```

These are *type codes* and the refactoring is to replace them with something more useful.

Instead define constants that refer to strategy objects:
```python
NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()   # better: 'CHILDRENS' as in original
```

You are not using polymorphism if you leave the named constants (1, 2, 3) in Movie 
and write code like this:
```python
class Movie:

    def get_price_strategy(self):
        """Return a PriceStrategy based on the price_code."""
        if self.price_code == self.NEW_RELEASE:
            return NEW_RELEASE
        elif self.price_code == self.CHILDRENS:
            return CHILDREN
        elif self.price_code == self.REGULAR:
            return REGULAR
```
it is just moving the `if ... elif ... elif` from one place to another.

Movie is still **coupled** to the fixed rental categories, which we are trying to eliminate.

And the duplicate constants are **confusing**.

## No Duplicate Constants, Either

Do not create 2 constants that refer to the same thing.
It is confusing and makes code harder to maintain and test. 

What if you add a DOCUMENTARY rental type? You'd need to add another duplicate constant to Movie, too, for consistency.

Some students defined named constants for strategies 
in a `pricing` module (correct),
but then define duplicate constants in Movie:

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

There is no benefit to this, and it's just more code to maintain.

Get rid of these constants so that Movie is not *coupled* to the specific rental categories. Only `pricing` needs to know them.
