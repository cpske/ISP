## Movie Rental Refactoring

This refactoring example is from [Chapter 1][refactoring_pdf] of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains code translated from the original Java version.

The runnable `main.py` creates a customer and prints a statement.

The [PDF from Chapter 1][refactoring_pdf] explains the 
motivation for each refactoring and how to do it.  Please read it.


### Notes on Python Version

In Python, the refactoring are the same as Fowler's Java version, but some details are different.

Variable names use the Python convention (`total_charge`) instead of Java camelcase names, and in some places I omitted the "get" (`rental_price` instead of `get_rental_price`).

## Instructions

Before and after each refactoring you should **run the unit tests**.

* method names should use Python naming convention

Perform each of these refactorings:

1. *Extract Method for price calculation*.  In Customer.statement() extract the code that calculates the price of each rental.
   - Make it a separate method. Fowler calls it `amountFor` but a Pythonic name would be `amount_for` or `rental_price(rental)`. 

2. *Move Method*. After extracting the method for price calculation (above) of a rental,
Fowler observes that the method uses information about the rental but not about the customer.  Hence, the method should be in the `Rental` class instead of `Customer` class. 
   - Move the method to the `Rental` class. A good IDE refactoring tool can do this for you.
   - After moving the method, verify that the method is referenced correctly in code.  The `rental` parameter is not needed (in Python, rental is now `self`).
    - write a unit test for this method in `rental_test.py`.

3. *Rename Method*. If you are using the method name `amount_for` or `amountFor`, then rename it. Fowler uses `getCharge` but "charge" could be confused with a credit card "charge". I suggest `rental_price(self)`.

4. *Replace Temp Variable with a Query*.  Instead of assigning `charge = rental.getCharge()` (Python: `charge = rental.rental_price()`) and using `charge` in the code, directly invoke `rental.getCharge()` (Python: `rental.rental_price()`) wherever it is needed. 
   - This eliminates the local variable `charge` but results to multiple method calls for the same thing.

5. *Extract Frequent Renter Points*. Repeat the steps you performed above for rental charge to frequent renter points in `statement`. 
   - Since the calculation of renter points depends only on information in a Rental, move this calculation to the Rental class as a new method named `rental_points`.
   - In `customer.statement()` call this method.
   - Write a unit test in `rental_test.py` to verify your new method computes frequent renter points correctly.

6. *Extract Method to compute total charge*. Move the computation of *total* price from `statement` to a separate method in `customer`.  `statement` calls this method to get the total amount.
   - `statement` calls this method only **once** to get the total charge.
   - eliminate the temp variable `total_amount`.
   - write a unit test for this new method in `customer_test.py` to verify the total charge for a collection of rentals is correct.

7. *Extract Method to compute total rental points*. Instead of computing total rental points in `statement`, write a separate method to compute and return it (just like for total rental charge).
   - eliminate the temp variable `frequent_renter_points` and instead call this method.
   - write a unit test for this new method in `customer_test.py` to verify the total renter points is computed correctly

8. *Replace Conditional Logic with Polymorphism* (Fowler, p. 28).  In `Rental.rental_price` (Fowler's name is `getCharge`) there is a long `if ... elif ... elif` to compute the rental charge using the Movie price code. In the Java version, it is a `switch` statement.  We can replace this with *polymorphism*.    
   Do this in **three steps**.
   - Step 1: make the Movie class compute its own frequent renter points. Rental calls `movie.frequent_renter_points(days)` to get the value.
   - Step 2: replace price code constants with a hierarchy of `PriceStrategy` objects. Fowler calls the superclass `Price`. Since this is the *Strategy Pattern*, let's call it PriceStrategy. *See below for details*.
   - Step 3: Movie *delegates* the computation of renter points to the PriceStrategy object.
   - Replace the constant for price code with a PriceStrategy object.
   - In Fowler's article, this is a long refactoring because he first uses inheritance (Movie subclasses) and then explains why that's a poor solution.
   - This refactoring uses the principle "*Prefer composition over inheritance*".

   - You define an interface (e.g. PriceStrategy) and concrete implementations for RegularPrice, ChildrensPrice, and NewReleasePrice. The strategy interface also computes frequent renter points using a separate method.


9. *The Missing Refactoring*.  In the final code the `Customer` class still needs a *Move Method* refactoring to remove some unrelated behavior, in my opinion.  
   - What do you think?
   - What method should move?

10. *Misplaced Responsibility*?  Is the Movie class responsible for anything that, conceptually, belongs in the Rental class?


### Define a PriceStrategy Hierarchy

In Java, you would define an Interface for `PriceStrategy` and then define concrete implementations for RegularMovie, NewRelease, and ChildrensMovie.

Python does not require creating an interface for a strategy, but for clarity or to make the Python version match the Java version, you can create an abstract superclass (`PriceStrategy`) for the interface and abstract methods (or methods that return 0).  `RegularMovie`, `NewRelease`, etc., extend  `PriceStrategy` and implement the methods.

```python
from abc import ABC, abstractmethod

class PriceStrategy(ABC):
   """Abstract base class for rental pricing."""

    @abstractmethod
    def frequent_renter_points(self, days: int) -> int:
        pass

    @abstractmethod
    def rental_price(self, days: int) -> float:
        pass
```

Each concrete price strategy implements the abstract methods:
```python
class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def frequent_renter_points(self, days):
        """New release rentals get 1 point per day rented."""
        return days
    
    def rental_price(self, days):
        #TODO return rental price for a new release
```

These classes don't have any *state* so we can share instances between Movies.  In `Movie` you could replace the pricing constants with:
```python
class Movie:
    # pricing strategies
    NEW_RELEASE = NewRelease()
    REGULAR = RegularMovie()
    CHILDRENS = ChildrensMovie()
```

There may be more elegant ways than this.

### Define an Enum for PriceStrategy

Another way to implement a Strategy in Python is to use an Enum. 
- Each member of the enum is one concrete pricing strategy (normal, childrens, new\_release).
- Each enum member has a dict named `values`, which you define when you declare the enum memmber.  Here's a naive example of assigning fixed values for "price" and "frp":
```python
from enum import Enum

class PriceCode(Enum):
   # these are the members (instances) of the enum
   new_release = { "price": 3, "frp": 2 }
   normal = {"price": 2, "frp": 1 }

   def rental_price(self, days):
      return self.value["price"]*days
   
   def frequent_renter_points(self, days):
      return self.value["frp"]
```

You can assign an Enum member to a variable, and then invoke its methods:
```python
price_code = PriceCode.new_release
print("Rental price for 4 days:", price_code.rental_price(4))
# prints 12  (3*4)
```

- You can define functions as the enum values using lambdas.  Each enum member defines it's own function for pricing and frequent renter points.
```python
from enum import Enum

class PriceCode(Enum):
    new_release = {"price": lambda days: 3.0*days, 
                    "frp": lambda days: days
                  }
    normal = { ... }
    ...

    def rental_price(self, days: int) -> float:
        """Return rental price for a given number of days."""
        pricing = self.value["price"]  # a lambda
        return pricing(days)
```

Whether you use an Enum or an abstract base class with subclasses for each price strategy, the code for Movie will be similar. The important part is that Movie *delegates* computation of price and renter points to the PriceCode or PriceStrategy instead of using an `if ... elif ...` block.





## Resources

* [Refactoring, First Example][refactoring_pdf] extract from Martin Fowler's *Refactoring* book. 
* [Refactoring slides from U. Colorado](https://www.cs.colorado.edu/~kena/classes/6448/s05/lectures/lecture19.pdf) step-by-step instructions for Java version of this example, including UML class diagrams of progress.

[refactoring_pdf]: https://cpske.github.io/ISP/refactoring/Refactoring-movierental.pdf