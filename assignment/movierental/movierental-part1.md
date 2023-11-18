---
title: Movie Rental Refactoring Part 1
---

## Description

This is a well-known refactoring problem from [Chapter 1][refactoring_pdf] of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

The application creates a statement showing the movie rentals by a customer, along with the total price and "frequent renter points" earned.

In the application, a **Customer** rents **Movies**. A **Rental** object records the `movie` and `days_rented`.  The rental `price` of a Movie is based on its **price code** such as "New Release", "Children's Movie", or "Regular". The price code also determines the **frequent renter points** earned for a Rental.

The Customer class has a `statement` method that creates a formatted statement containing the details of each rental along with total amount and total points earned, and returns the statement as a string.

`main.py` creates a customer, rents some movies, and prints a statement.

## Assignment

This assignment contains a Python translation of the original Java version.

The [PDF from Chapter 1][refactoring_pdf] explains the 
motivation for each refactoring and how to do it.  It is helpful to read it.

### Changes in the Python Version

In Python, the refactoring are the same as in Fowler's Java version, but some details are different.

- Variable names use the Python naming convention (`total_amount`) instead of Java camelcase names (`totalAmount`), and no leading underscore.
- Instead of `getCharge()` (Java) use `get_price()`
- Instead of `getFrequentRenterPoints()` (Java) use `get_rental_points` (Note "rental" instead of "renter")
- Instead of `Price` for strategies (p. 29) use `PriceStrategy`


## Instructions

Before *and* after each refactoring you should **run the unit tests**.

Perform these refactorings:

1. *Extract Method for rental price calculation*.  In `Customer.statement()` extract the code that calculates the price of one rental.
   - Make it a separate method. Fowler calls it `amountFor` but a Pythonic name would be `get_price(rental)`. 

2. *Move Method*. After extracting the method for price calculation (above),
observe that the method uses information about the rental but not about the customer.  Hence, the method should be in the `Rental` class instead of the `Customer` class. 
   - Move the `get_price` method to the `Rental` class. 
   - The `rental` parameter is now `self`.
   - After moving the method, verify that the method is referenced correctly in code.  Customer should call `rental.get_price()`.
    - write a unit test for this method in `rental_test.py`.

3. *Replace Temp Variable with Query* (*aka* "Inline Temp").  In `statement()`, instead of assigning `charge = rental.get_price()` (Java: `charge = rental.getCharge()`) and then using `charge`, directly invoke `rental.get_price()` wherever it is needed ("Inline Temp"). 

4. *Extract Frequent Renter Points*. Repeat the steps you performed above for rental price to frequent renter points in `statement`. 
   - The calculation of renter points depends only on information in a Rental, so move this calculation to the Rental class. Name the new method `rental_points`.
   - In `customer.statement()` call this method.
   - Write a unit test in `rental_test.py` to verify your new method computes frequent renter points correctly.

5. *Extract Method to compute total charge*. Move the computation of *total amount* from `statement` to a new, separate method in `Customer`.  `statement` calls this method to get the total amount.
   - `statement` calls this method **only once** to get the total amount. Not inside a loop!
   - eliminate the temp variable `total_amount`.
   - write a unit test for this new method in `customer_test.py` to verify the total charge for a collection of rentals is correct.

6. *Extract Method to compute total rental points*. Instead of computing total rental points in `statement`, extract a method to compute and return it -- just like for total rental price (above).  Define a `get_rental_points` method in `Rental`.
   - eliminate the temp variable `frequent_renter_points` and instead call this method **one time**.
   - write a unit test for this new method in `customer_test.py` to verify the total renter points is computed correctly.

7. *Replace Conditional Logic with Polymorphism* (Fowler, p. 28).  In `Rental.get_price` (Java: `getCharge`) there is a long `if ... elif ... elif` to compute the rental price by testing the Movie price code. In the Java version, this is a `switch` statement.  Replace this with *polymorphism*.    
   Do this in **three steps**.
   - Step 1: make the Movie class compute its own rental price and rental points. Rental calls `movie.get_rental_points(days)` and `movie.get_price(days)`.
   - Step 2: *Replace Switch with Polymorphism* (Page 29). Replace price code constants with a hierarchy of `PriceStrategy` objects. Fowler calls the superclass `Price`. Since this is the *Strategy Pattern*, let's call it PriceStrategy. *See below for details*.
   - Step 3: Movie *delegates* the computation of rental price and rental points to the `PriceStrategy` object.
   - Replace the constants for price code with PriceStrategy objects.
   - In Fowler's article, this is a long refactoring because he first uses inheritance (Movie subclasses on page 28) and then explains why that's a poor solution.
   - This refactoring uses the principle: "*Prefer composition over inheritance*".
   - Details of [How to Implement a Price Strategy](#how-to-implement-price-strategy) are given below

8. Missing or Incorrect Refactorings?

   - In the final code, do you see anything that *still* needs refactoring, based on the refactoring signs ("code smells") or design principles?
   - Do you think any of the refactorings are wrong?
   - Share your ideas on Discord and we will discuss them after this assignment. 
   - If there is not much contribution on Discord, then it will be a quiz instead of a discussion.


### How to Implement Price Strategy

There are two ways:

- [Define a Price Strategy Hierarchy](#define-a-pricestrategy-class-hierarchy) as in the Java version.  This is the most flexible approach since strategy objects can contain complex methods.

Another way, which we used in the Pizzashop exercise, is to use an enum.  This is simpler but not as flexible as strategy objects:

- [Define an Enum for Price Strategy](#define-an-enum-for-pricestrategy) where each Enum member implements the strategy methods as lambdas.  This only works if the strategies are simple enough to be implemented as lambda expressions.

Whether you use strategy classes or an Enum, the code for Rental will be similar. The important part is that Rental (or Movie) *delegates* computation of price and rental points to the PriceStrategy instead of using `if ... elif ... elif ...`. 

This is the refactoring "*Replace Switch with Polymorphism*", implemented using the *Strategy Pattern*.


#### Define a PriceStrategy Class Hierarchy

In Java, to apply the Strategy Pattern you define an Interface for the strategy (`PriceStrategy`) and then define concrete implementations of the interface, such as RegularPrice, NewRelease, and ChildrensPrice.

Python does not require an interface for the strategy, but for clarity, documentation, and type checking you can create an abstract base class (`PriceStrategy`) as the interface with abstract methods that subclasses must implement.  `RegularPrice`, `NewRelease`, etc., extend  `PriceStrategy` and implement these methods.

```python
from abc import ABC, abstractmethod

class PriceStrategy(ABC):
   """Abstract base class defines methods for rental pricing."""

    @abstractmethod
    def get_price(self, days: int) -> float:
        """The price of this movie rental."""
        pass

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """The frequent renter points earned for this rental."""
        pass
```

Each concrete price strategy implements the abstract methods:

```python
class NewRelease(PriceStrategy):
    """Pricing rules for New Release movies."""

    def get_rental_points(self, days):
        """New release rentals get 1 point per day rented."""
        return days
    
    def get_price(self, days):
        #TODO return rental price for a new release
```

The strategy objects don't save any *state* so we can share one instance among many Movies.  In the file containing the strategies create one instance of each strategy and use it in place of the constants in Movie:

```python
class PriceStrategy(ABC):
    ...

class NewRelease(PriceStrategy):
    ...

class RegularPrice(PriceStrategy):
    ...

# Define instances of the strategies as named constants
NEW_RELEASE = NewRelease()
REGULAR = RegularPrice()
CHILDREN = ChildrensPrice()
```
Python requires the instances be created *after* the class definition.

#### Make the Price Strategies be Singletons

We need only one instance of each Strategy class, since they do not have any state.

By carefully writing a Singleton `__new__` method in the base class, each child class will be a Singleton.

```python
class PriceStrategy(ABC):
    _instance = None

    @classmethod
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(PriceStrategy, cls).__new__(cls)
        return cls._instance
```

You should verify that (a) instances of NewRelease, ChildrensMovie, and RegularMovie are *not* the same, (b) all instances of RegularMovie *are* the same object.


#### Define an Enum for PriceStrategy

Another way to implement a Strategy in Python is to use an Enum. 

- The Enum defines the methods required by the strategy
- Each member of the enum is one concrete pricing strategy (regular, childrens', new release).
- Each enum member has a dict named `value`, that you define when you declare the enum member. 

The price of rentals is a function of days rented, frequent rental points is also a function of days rented.  Hence, each enum member needs its own *functions* for these, and we don't want to use `if ... elsif ... ` logic.  That is error-prone and not extensible.

(If anyone does that, they will get ZERO credit.)

But, you can define `lambda` expressions for the rental price and rental point functions:


```python
from enum import Enum

class PriceStrategy(Enum):
    NEW_RELEASE = {"price": lambda days: 3.0*days, 
                    "frp": lambda days: days
                  }
    REGULAR_PRICE = { ... }
    ...

    def get_price(self, days: int) -> float:
        """Return rental price for a given number of days."""
        pricing = self.value["price"]  # a lambda
        return pricing(days)
```


### UML Class Diagram

![UML of Final Code](movierental-part1-uml.png)

If you use an *enum* the structure would be:

![UML of Code using Enum](movierental-part1-enum-uml.png)



## Resources

* [Refactoring, First Example][refactoring_pdf] extract from Martin Fowler's *Refactoring* book. 
* [Refactoring slides from U. Colorado](https://www.cs.colorado.edu/~kena/classes/6448/s05/lectures/lecture19.pdf) step-by-step instructions for Java version of this example, including UML class diagrams of progress.

[refactoring_pdf]: https://cpske.github.io/ISP/refactoring/Refactoring-movierental.pdf
