---
title: Feedback on Quiz 4
---

## Problem 1. Fix Data Clump in Borrowing Constructor

a) Define a Patron class in `patron.py`.
```python
@dataclass
class Patron:
    patron_id: str
    name: str
    email: str
```

b) In Borrowing:
```python
def __init__(self, item: LibraryItem, patron: Patron,  
                   checkout_date: date|str = None):
    self.item = item
    self.patron = patron
    if checkout_date:
        ...
```

c) In `main.py`:
```python
patron = Patron(patron_id, patron_name, patron_email)
# or
patron = Patron("1234", "Edward Snowden", "snowden@protonmail.com")

# then
borrowing = library.checkout(item, patron, checkout_date=checkout_date)
```

### Bad Code for Patron

1. Writing lots of code instead of using a dataclass (waste of time):
   ```python
   class Patron:
       """A Patron who borrows Item from the library information."""
   
       def __init__(self, patron_id: str, patron_name: str, patron_email: str):
           self.__patron_id = patron_id
           self.__patron_name = patron_name
           self.__patron_email = patron_email
   
       @property
       def patron_id(self):
           return self.__patron_id
   
       @property
       def patron_name(self):
           return self.__patron_name
   ```
2. Forgetting `@dataclass` decorator. This class has **class attributes** and **no constructor**, not **instance attributes**.
   ```python
   class Patron:
       patron_id: str   # Class attribute
       name: str        # Class attribute
       email: str       # Class attribute
   ```
3. Using `id` as an attribute. We covered this many times in class. **Pay attention**.
   ```python
   @dataclass
   class Patron:
       id: str          # Shadows built-in id() function
       name: str        
       email: str      
   ```
4. Writing a constructor in a dataclass. Waste of time and violates reason to use dataclass.
   ```python
   @dataclass
   class Patron:
       patron_id: str
       name: str        
       email: str

       def __init__(self, patron_id, name, email):  # don't do this
    ```
5. Using Edward Snowden as default values. This changes code usage and creates a *latent error*:
   ```python
   @dataclass
   class Patron:
       patron_id: str = "1234"
       name: str = "Edward Snowden"   
       email: str = "snowden@protonmail.com"
   ```
   Latent error: what if someone omits email address when creating a new Patron?
   ```python
   patron2 = Patron("1235", "George Bush")
   ```
   The email address of patron2 is `snowden@protonmail.com`.

6. Writing Patron as an Enum.  This library can have **only one** Patron:
   ```python
   class Patron(Enum):
       """An enum class for Patron"""
       patron_name = "Edward Snowden"
       patron_id = "1234"
       patron_email = "snowden@protonmail.com"
   ```   
7. Writing Patron as a `dict`.  The solution to Data Clumps is to use an object, not a `dict`.
   ```python
   patron = {patron_name = "Edward Snowden", patron_id = "1234", ... }
   ```

### Incomplete Fix for Data Clump 

The `Borrowing` class should *Preserve the Whole Patron Object*, **not this**:
```python
class Borrowing:
    def __init__(self, item: LibraryItem, patron: Patron, checkout_date = None):
        self.patron_id = patron.patron_id
        self.patron_name = patron.patron_name
        self.patron_email = patron.patron_email
        self.item = item
```

## Problem 2. Fix Data Clump in Library.checkout

Use `patron` instead of patron attributes as parameter.
```python
    def checkout(self, item: LibraryItem, patron: Patron, checkout_date: date):
```

## Problem 3. Replace Type Code with State/Strategy or Subclasses in LibaryItem.

Replace **values** of BOOK, AUDIO, VIDEO (1, 2, 3) with assignment to objects.

> The Strategies or Subclasses **must contain behavior** for **due date** and **overdue fee**.
> Refactoring is incorrect if these classes are just data containers.

Using Strategies/Subclasses as data containers introduces two new "code smells": *Data Containers* and *Feature Envy*. That is bad refactoring.

| Problem                                             | Deduction |
|-----------------------------------------------------|-----------|
| **Common Error**: Removed the constants BOOK, AUDIO, VIDEO | none |
| Strategy/Subclasses are just data containers        |  -50%     |
| Encapsulates `due_date` or equiv but not `late_fee` |  -20%     |
| Encapsulates `late_fee` but not `due_date` or equiv |  -20%     |
| Did not remove `BOOK = 1`, etc.                     |  -20%     |
| Methods are static                                  |  -20%     |
| Classes are not subclasses                          |  -10%     |
| Class names violate naming convention (e.g. BOOK)   |  -10%     |
| Classes have an `int` type code attribute           |  -10%     |
| Code still has `if...elif` using item types         |  -100%    |
| Enums instead of classes (no credit)                |  -100%    |

The best solution is to use *Strategies*, which is recommended by:

> *Prefer composition over inheritance.*

```python
AUDIO = AudioItem()
BOOK = BookItem()
VIDEO = VideoItem()

class ItemType():
    @abstractmethod
    def due_date(self, checkout_date: datetime.date) -> : datetime.date:

    @abstractmethod
    def late_fee() -> int:

class BookItem(ItemType):
    def due_date(self, checkout_date):
        return checkout_date + timedelta(days=14)

    def late_fee(self, days_overdue):
        return max(0, 10*(days_overdue - 3))
```

### Error: Classes for ItemTypes are Just Data Containers

> Classes, especially *Strategies*, are about **behavior**.

If you write code like the example below, there is no reason to create separate classes!
You could use a single DataClass with 3 attributes and initialize
them via the constructor -- must simpler!
```python
# Strategy should not be just a data container
class Book(ItemType):
    def __init__(self):
        self.borrowing_period = 14
        self.grace_period = 3
        self.fine_per_day = 10
```

## Problem 4. Replace Conditional with Polymorphism in `Borrowing.due_date`

```python
class Borrowing:
    def due_date(self):
        return self.item.item_type.due_date(self.checkout_date)
```

This is not polymorphism. `due_date` is doing the calculation itself, and always doing it the same way.

```python
class Borrowing:
    def due_date(self):
        return self.checkout_date + \
               timedelta(self.item.item_type.borrowing_period)
```

> No Polymorhphism, No Credit.

| Problem                                             | Deduction |
|-----------------------------------------------------|-----------|
| Code contains `if ... elif ...` testing the type    |  -100%    |
| `due_date` is not fully polymorphic                 |  -20%     |
| (Borrowing or LibraryItem computes it itself)       |           |
| `late_fee` is not fully polymorphic                 |  -20%     |
| (Borrowing or LibraryItem or Library) computes it itself) |     |


Exception: OK if item types are subclasses of `LibraryItem` and
`LibraryItem.due_date` or `LibraryItem.late_fee` use the template
method pattern with data from subclasses.

### Why So Picky About This?

One class should be completely responsible for a particular behavior. Avoid dividing the behavior 
between classes.

There is no reason to have ItemTypes provide the *data* to compute the overdue fee, but Borrowing actually *compute* the fee using that data.  Simpler and more flexible to have each ItemType compute its own fee.

Example:  Suppose the library implements a new rule:    
"*The overdue fee on audio will be limited to a max of 100 Baht*".

Now the formula for audio overdue fees is different from the formula for other items.

Having ItemTypes compute their own overdue fee is consistent with the Information Expert principle:

> *Information Expert: Assign a responsability to the object that has the information needed to carry out the responsibility*.

In this case, the ItemTypes know their own grace period and fine rates.

## Problem 5. Fix Magic Number

Replace max items value 4 with a **global** or **class level** constant.

| Problem                                             | Deduction |
|-----------------------------------------------------|-----------|
| Local constant instead of class or global constant  |  -50%     |
| Constant name is not uppercase                      |  -10%     |

## Problem 6: Fix *Feature Envy* in Library `is_overdue`

Move this method to the `Borrowing` class.

| Problem                                             | Deduction |
|-----------------------------------------------------|-----------|
| Library has `is_overdue` that *delegates* to Borrowing  |  -20% |
| Reason: `Library.is_overdue` has no purpose         |           |
| Move `is_overdue` to top-level function in `utils`  |  -100%    |
| Reason: This simply moves *Feature Envy* to utils.  |           |

## Problem 7: Extract Method and Apply Polymorphism in Library `return_item`. 

Extract a polymorphic method to compute the late fee.
The calculation should be implemented in the ItemTypes for Audio, Book, and Video.

To simplify code and avoid call chain, create a method in Borrowing that is a facade:
```python
class Borrowing:

    def late_fee(self):
        days_overdue = (utils.today() - self.due_date()).days
        return self.item.late_fee(days_overdue)
```

And in Book:
```python
class Book(ItemType):

    def late_fee(self, days_overdue: int):
        return max(0, 10*(days_overdue - 2))
```


Only 1 object should compute the late fee. It is low cohesion and "feature envy" for Borrowing to compute the late fee using data from the item, like this:
```python
class Borrowing:

    def late_fee(self):
        days_overdue = (utils.today() - self.due_date()).days
        fee = self.item.fee_per_day*(days_overdue - self.item.grace_period)
        return max(0, fee)
```
20% deduction for this.

Also a 20% deduction for invoking non-static method like this:
```
    return Borrowing.late_fee(self.borrowing)
```
This is both non-OO style and not Pythonic way of invoking instance methods.
You should simply write `self.borrowing.late_fee()`.

## Problem 8: Replace Nested Conditional with Guard Clauses

Instructions:

> Replace Nested Conditional with Guard Clauses.
> Handle the easy cases first to eliminate nested "if".

> When you finish refactoring `return_item`, the only "if" statements should be Guard Clauses. 
> No nested "if" and no "else".

Refactorings to apply:

1. Replace conditional with Guard Clause
2. Remove test `if borrowing.is_overdue`. Instead, method that computes late fee simply returns 0 if not overdue.
3. Call another method to compute the late fee and return the value

Final Result: Only 1 "if" statement for Guard Clause and no "else".

```python
class Library:

    def return_item(self, item_id):
        # Guard Clause
        if item_id not in self.checkouts:
            logging.error(
                f"Return of item {item_id} that is not checked out.""")
            raise ValueError(f"Item {item_id} is currently not checked out.")

        borrowing = self.checkouts[item_id]
        # remove item from the collection of checkout-out items
        del (self.checkouts[item_id])
        # Return the late fine. Returns 0 if item is not overdue.
        return borrowing.late_fee()
```

Errors & Deductions:

- Nested "if".  No points.
- Any "else" clause. No points.
- Invert use of Guard Clause: "good" case inside "if" block, then the error case. -50% deduction.
- Has extra "if" statement to test if item is overdue and "if" block contains multiple statements. -10% deduction.

### More Refactoring is Possible

```python
    def return_item(self, item_id):
        # Guard Clause
        ...

        borrowing = self.checkouts[item_id]
        del(self.checkouts[item_id])

        # compute the late fine
        days_overdue = borrowing.days_overdue()
        return borrowing.item.item_type.late_fee(days_overdue)
```
The last 2 statements can be improved.

The result of `borrowing.days_overdue()` is used only as argument to
`borrowing.item.item_type.late_fee()` which is also a "call chain" (undesirable).

Create a delegate method in borrowing to compute days overdue and hide the call chain (better encapsulation):
```
class Library:
    def return_item(self, item_id):
        # Guard Clause
        ...

        borrowing = self.checkouts[item_id]
        del(self.checkouts[item_id])
        
        # compute the late fine
        return borrowing.late_fee()
```
and in Borrowing:
```python
class Borrowing:
    def late_fee(self):
        days_overdue = self.days_overdue()  # returns 0 if not overdue
        return self.item.item_type.late_fee(days_overdue)
```

### Not a Guard Clause

This code does **not** use a Guard Clause, but its a partial improvement:
```
    def return_item(self, item_id):

        if item_id in self.checkouts:
            borrowing = self.checkouts[item_id]
            del (self.checkouts[item_id])
            return borrowing.late_fee()

        logging.error(f"Return of item {item_id} that is not checked out.""")
        raise ValueError(f"Item {item_id} is currently not checked out.")
```

### Catching Exceptions is Error-Prone and Less Readable

Using try - except is not a substitute for Guard Clause:

```python
    def return_item(self, item_id):
        try:
            borrowing = self.checkouts[item_id]
            del (self.checkouts[item_id])
            return borrowing.late_fee()
        except:
            logging.error(
                f"Return of item {item_id} that is not checked out.""")
            raise ValueError(f"Item {item_id} is currently not checked out.")

```
The "except" block catches all exceptions, including exceptions not intended
such as if `borrowing.late_fee()` raises an exception.

In addition, throwing and catching exceptions is slower than an "if" test
because Python must invoke extra code to "unwind the call stack".

The code is also **less readable**. When someone unfamiliar with the code
reads this, its not clear which statement in the block may raise exception
and the reason why.
