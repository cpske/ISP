## Refactoring Practice

Make improvements in the pizza and pizzashop files by refactoring. 

Use your IDE's *refactoring commands* to do the refactoring whenever possible. 
Try not to manually edit the code -- unless the IDE refactoring doesn't do what you want or you want to correct formatting & comments.

## Starter Code

Starter code for this assignment is on Github Classroom.  Your repo will contain these source files:
```
pizza.py     - code for Pizza class
pizzashop.py - create and order some pizzas. Run this to verify the code works.
main.py      - code to order some pizzas
```

## What to Submit

1. Perform each refactoring and **commit** the result as a separate commit. 

When done, push all your code to Github.  

There should be at least 7 commits: 6 refactorings and one modification to add a "jumbo" pizza size.

### Problem Description

This application creates and orders pizza.
A pizza has a size and toppings.  The price depends on the size and number of toppings:

| Pizza Size  | Base Price | Price per Topping |
|-------------|:----------:|:------------:|
| small       | 120        | 20           |
| medium      | 200        | 20           |
| large       | 280        | 20           |
  
For example, a large pizza with two toppings:
```python
pizza = Pizza('large')
pizza.addTopping("mushroom")
pizza.addtopping("pineapple")
print("The price is", pizza.getPrice(), "Baht")
'The price is 320 Baht'
```

## Goal: Refactor to Improve the Code

We want to make these code improvements:

1. Type safety and error checking: Replace string literals with named constants.
2. Readability: Rename methods to use the Python naming convention.
3. Better Cohesion & Encapsulation: Move misplaced code to a better place (Extract Method and then Move Method).
4. Polymorphism & Extensibility: Replace "switch" (`if` ... `elif` ... `elif`) with object behavior.


### The #1 Rule of Refactoring: Passing Tests

Before refactoring you should have unit tests that cover all the code you plan to change, **and** the tests all pass.

We don't have unit tests, but the "main" block in `pizzashop.py` provides visual tests and checks prices.

### Refactor 1. Replace String Literals with Named Constants

> Use Named Constants instead of Literals in Code.

In the Pizza class replace the strings "small", "medium", and "large" with named constants `SMALL`, `MEDIUM`, and `LARGE`.  Use your IDE's refactoring feature:

1. In the Pizza class, select 'small'.
   - VSCode: right click -> Refactor -> Extract Variable. Enter the name SMALL.
   - Pycharm: right click -> Refactor -> Introduce Constant, enter the name SMALL. Press ENTER or **Preview** for better results.
   - Pydev: Refactoring -> Extract local variable and enter SMALL.

2. Do the same thing for "medium" and "large".

3. Did the IDE replace "small" with SMALL **everywhere** in pizza.py?      
   What we *want* are top-level or class constants (not local variables), like this:
   ```python
   SMALL = 'small'
   MEDIUM = 'medium'
   LARGE = 'large'

   class Pizza:
       def __init__(self, size: str) -> None:
           if not size in (SMALL, MEDIUM, LARGE):
               raise ValueError("Unrecognized pizza size")
           self.size = size
           self.toppings: list[str] = []  # In Python 3.8 use List[str]

        def getPrice(self) -> float:
            if self.size == SMALL:
                ...
   ```
   In my tests, none of the IDE did a complete job of replacing strings with named constants.

4. If the IDE didn't do a complete replacement, then fix the code manually: move SMALL, MEDIUM, and LARGE to global scope and manually replace all occurences in `pizza.py`.

5. Did the IDE change the sizes in `pizzashop.py`?
   If not, edit `pizzashop.py` and replace size strings with named constants:
    ```python
    from pizza import *

    if __name__ == "__main__":
        pizza1 = make_pizza(SMALL, ...)
        ...
        pizza2 = Pizza(MEDIUM)
        ...
        pizza3 = make_pizza(LARGE, ...)
    ```    
    
6. Test: Run `pizzashop.py`. Verify the results are the same.

**Commit** your work with the message "`replace strings with named constants`".

### Refactor 2. Rename Method

1. In Pizza, `getPrice` is not a Python-style name.  Refactor to rename it to `get_price`.
    - VSCode: right-click on method name, choose "Rename Symbol"
    - Pycharm: right-click, Refactor -> Rename, **Preview** changes.
    - Pydev: "Refactoring" menu -> Rename

2. Did the IDE **also** rename `getPrice` in `order_pizza()` and "main" (in pizzashop.py)?

3. **Test**: Run `pizzashop.py` and verify the output is the same as original code.

**Commit** your work with the message "`rename getPrice in Pizza`".

### Refactor 3. Rename Method, again

In Pizza, rename `addTopping` to `add_topping`.  

- Repeat the same steps as above.
- Verify name was changed everywhere
- Test: run pizzashop.py
- **Commit** with a descriptive commit message


## Refactor 4. Extract Method and Move Method

> Perform refactorings in small steps. 
> In this case, we extract a method first, then move it to a better place.

In pizzashop, `order_pizza` creates a string `description` for a pizza.  
That is a poor location for this because:

1. the pizza description may be needed in other parts of the application
2. it relies on information about a Pizza that the Pizza knows.

Therefore, it should be the Pizza's job to describe itself.  

This is known as the *Information Expert* principle.

Apply the *Extract Method* refactoring, followed by *Move Method*.

1. **Select** all these statements in `order_pizza` that create the description:
   ```python
    description = pizza.size
    if pizza.toppings:
        description += " pizza with "+ ", ".join(pizza.toppings)
    else:
        description += " plain cheeze pizza"
    ```

2. **Extract Method** to `describe(pizza)`
   - VS Code: right click -> Refactor -> 'Extract Method'. Enter `describe` as the method name. 
   - PyCharm: right click -> Refactor -> Extract -> Method and enter `describe` as the method name.
   - PyCharm correctly suggests that "pizza" should be parameter, and it returns the description. (correct!)
   - PyDev: Refactoring menu -> Extract method.  PyDev asks you if pizza should a parameter (correct), but the new method does not return anything.  Fix it.
   - Update Comments (All IDE): after refactoring, move the comment line from `order_pizza` to `describe` as shown here:
    ```python
    def describe(pizza):
        # A description of the pizza such as 'small pizza with mushroom'
        description = pizza.size
        if pizza.toppings:
            description += " pizza with "+ ", ".join(pizza.toppings)
        else:
            description += " plain pizza"
        return description
    ```
    NOTE: Forgetting to update comments is a common problem in refactoring. Be careful.

3. **Move Method:** The code for `describe()` should be in the Pizza class (as explained above).    
   Select the entire `describe` function. Does the IDE "Refactoring" menu have a "Move Method" refactoring?
   - None of the 3 IDE do this correctly (in my tests), so I moved it manually.
   - Select the `describe(pizza)` method in pizzashop.py and CUT it (edit -> cut).
   - PASTE the method into the Pizza class.
   - Rename the parameter name from "pizza" to "self" (Refactor -> Rename): `def describe(self)`
   
4. **Rename Method:** In `pizza.py` rename `describe(self)` to `__str__(self)`. You should end up with this:
    ```python
    # In Pizza class

    def __str__(self):
        """A description of the pizza such as 'small pizza with mushroom'."""
        description = self.size
        if self.toppings:
            description += " pizza with "+ ", ".join(self.toppings)
        else:
            description += " plain cheese pizza"
        return description
    ```

5. Back in `pizzashop.py`, modify the `order_pizza` to get the description from Pizza:
    ```python
    def order_pizza(pizza):
        description = str(pizza)           <----- invoke pizza.__str__()
        print("Order:", descripton)
        print("Price:", pizza.get_price())
    ```

6. **Test**: Run pizzashop.py.  Fix any problems until it works as before.

7. **Commit** your work with a descriptive commit message.


### Refactor 5. Eliminate Temporary Variable *aka* "Inline Temp"

The code for `order_pizza` is now so simple that we don't need the `description` variable.  Eliminate it:
```python
    def order_pizza(pizza)
        print("Order:", str(pizza))        # or print("Order:", pizza)
        print("Price:", pizza.get_price())
```

**Test.** Run the pizzashop code. Verify the results are the same.

**Commit** this change with a descriptive commit message.


## Refactor 6. Replace 'switch' with Call to Object Method

This is the **most complex** refactoring, but it produces big gains in code quality!
- code is simpler
- enables static checking of pizza sizes
- can change prices and sizes without changing the Pizza class!

The `get_price` method has a block like this:
```python
if self.size == SMALL:
    price = ...
elif self.size == MEDIUM:
    price = ...
elif self.size == LARGE:
    price = ...
```
The pizza has to know the sizes and pricing rule for each size.
This makes the code complex and harder to change.

The O-O approach is to *encapsulate* size information so that pizza sizes know their own price.
We will define a new datatype for pizza sizes.

Python has an [Enum][enum] type for this.
An "enum" is a class with a fixed set of instances, which are static members of the class.  Each enum member has a **name** and a **value**.

[enum]: https://docs.python.org/3/library/enum.html?highlight=enum#enum.Enum

1. In `pizza.py` define an Enum named `PizzaSize`:
   ```python
   from enum import Enum

   class PizzaSize(Enum):
       # Enum members written as: name = value
       small = 120
       medium = 200
       large = 280

       def __str__(self):
           return self.name
   ```
2. **Test the Enum**:  Add a "main" block in `pizza.py` to test PizzaSize:
   ```python
   if __name__ == "__main__":
       # test the PizzaSize enum
       for size in PizzaSize:
           print(size.name, "pizza has price", size.value)
   ```

3. **Use descriptive names**: `size.value` does not convey it's meaning.  Add a `price` property to PizzaSize so the meaning is clearer:
   ```python
   # PizzaSize
       @property
       def price(self):
           return self.value
   ```
   and update your test code in "main":
   ```python
   if __name__ == "__main__":
       # test the PizzaSize enum
       for size in PizzaSize:
           print(size.name, "pizza has price", size.price)
    ```
      
4. **Replace "switch" with method call:** In `Pizza.get_price()`, eliminate the `if size == SMALL: elif ...` It is no longer needed.  The Pizza sizes know their own price.
   ```python
   def get_price(self):
       """Price of a pizza depends on size and number of toppings"""
       price = self.size.price + 20*len(self.toppings)
   ```

5. **Inline Temp**.  In `get_price`, eliminate the `price` variable. Compute and return the price in one line.

6. **Apply Type Safety**: Update the Pizza constructor
   - change the **type hint** on the `size` parameter
   - replace `if not size in ("small",...)` with a test for parameter type:
     ```python
     if not isinstance(size, PizzaSize):
         raise TypeError('size must be a PizzaSize')
     self.size = size
     ```

7. In `pizzashop.py` replace the constants SMALL, MEDIUM, and LARGE with `PizzaSize` members.

8. Test it.

9. **Commit** this change with a descriptive commit message.  This is a long commit, so use the commit editor to write a multi-line commit message.

### 7. Extensibility

Can you add a new pizza size *without changing* the Pizza class?

1. Define a "jumbo" size with a base price of 450 Baht.

   ```python
   class PizzaSize(Enum):
      ...
      jumbo = 450
   ```

2. In `pizzashop.__main__` add code to create a jumbo pizza and print it.

Does it work?

**Commit** this change.


## References

* [Refactoring.guru](https://refactoring.guru/refactoring) has many refactorings and description of when to use them.
* My [Refactoring](https://cpske.github.io/ISP/refactoring/) page has suggested resources.
* *Refactoring: Improving the Design of Existing Code* by Martin Fowler is the bible on refactoring.  The first 4 chapters explain the fundamentals.
