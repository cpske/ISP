## Python Review (Done After the Github Warm-up)

1. Why use **properties** instead of just exposing an object's attributes?
   - What Object-oriented principle do properties use?
   - Code to expose attributes:
     ```python
     class Money:
         def __init__(self, value, currency):
             self.value = value
             self.currency = currency
     ```
   - Code to use properties in place of attributes: 
     ```python
     class Money:
         def __init__(self, value, currency):
             self.__value = value
             self.__currency = currency
    
       @property
       def value(self):
            return self.__value
    ```

2. How do you add *type hints* to the constructor to indicate that
   `value` should be `float` and `currency` should be `str`?

3. Methods like `__eq__` and `__str__` are called **magic methods**.    
   Why?

4. We invoke `__eq__` by writing `a == b` where `a` and `b` refer to some object with an `__eq__` method.
   - How do we invoke `__str__`?

5. Suppose we want to be able to add Money objects like this:
   ```python
   m1 = Money(5, 'Baht')
   m2 = Money(20, 'Baht')
   sum = m1 + m2
   print(sum)
   25 Baht
   ```
   - What method should we write? 
   - What parameter(s) does this method need?

6. Write the code for the "add" method and test it on your computer. 
   - in `money_test.py` there are 2 "skipped" tests for add.  Remove the `@pytest.mark.skip` annotation to use the tests.
   - run pytest until your code passes. 

7. It does not make sense to add money with different currencies:
   ```python
   m1 = Money(10, 'Baht')
   m2 = Money(20, 'USD')
   m1 + m2
   THIS IS NONSENSE
   ```
   - What should we do if someone tries to add Money with different currencies?
   - What should we do if someone tries to add Money to something that is not Money (like a float or string)?
   - TODO: Modify your "add" method to raise exception if currencies are different.
   - TODO: Modify "add" to raise exception of the parameter is not an instance of Money. Use `isinstance(obj, Classname)` to test it.

8. Commit and push your work:
   - Commit changes with a **descriptive** git comment (-m)
   - Software Process: Always write a **descriptive** comment when you commit work, such as "*completed `__add__` method and unit tests*".
   - Push to Github

9. Go to Github and observe that it automatically runs your pytests.  The tests should all pass.


### What to Submit

Push your revised `money.py` and `money_test.py` to Github.


### Magic Methods


Write or complete these methods:

| Method      | Description                   |
|:------------|:------------------------------|
| `__add__`   | Add two objects and return result as a new object. (3) |
| `__gt__`    | Test `self > other`. For Money, first compare currencies, then the value. |
| `__ge__`    | Test `self >= other`. True if `self > other` or `self == other`. |
| `__str__`   | Return string representation. |
| `__mul__`   | Multiply 2 objects and return result as a new object. `a * b` invokes `__mul__(a,b)`. |
| `__rmul__`  | Multiply 2 objects where "self" is on the right of multiply sign. `a * b` invokes `__mul__(b,a)` in the class of `b`. |



![Money UML class diagram](../../images/money2.png)