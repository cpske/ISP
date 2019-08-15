# Unit Testing

There are two parts to this assignment. The first part is to test a single function.  The second part is writing a Fraction class and test its methods.
Starter code is provided in the Github Classroom assignment.

## Clone Your Project from Github Classroom

1. Accept the assignment by going to the URL given in class.

2. Wait for Github to create a repository for you.

3. Clone the repository (command to do this is shown on Github).  If you are using the HTTPS protocol with Git, the command will be similar to this:
```
# change to a directory where you store projects in (NOT the Desktop!)
cd workspace

# clone the repository
git clone https://github.com/ISP19/unittesting-your_github_id.git unittesting
```
Notice the last argument (`unittesting`). That's the name you want git to create for your local copy.  If you omit this, it will be named `unittesting-your_github_id`.


## What to Submit

Commit your work to Github classroom. You should have these files:

| File             | Description   |
|:-----------------|:--------------|
| README.md        | Describe your test cases |
| listutil.py      | Code for `unique` including docstring and doctest |
| listutil_test.py | Unit tests for `unique` |
| fraction.py      | Code for Fraction class |
| fraction_test.py | Unit tests for Fraction and gcd |


## Problem 1. listutil

The starter code for `listutil.py` describes the `unique` function.

1. Write the code for `unique`.  See below for examples.
2. In README.md write a table of test cases to thoroughly test the code. You should test:
   * **borderline cases**, such as a list with 0 or 1 elements
   * **typical cases**, such as a list with a few duplicates or **no** duplicates
   * an **impossible case** where the method should not work. 
   * **extreme cases**, such as a huge list
3. Write the tests using Python unittest.  The test file should be `listutil_test.py`.
4. Run the tests until your code passes them all.

Examples: `unique(list)` returns a list containing unique elements `list`, in the same order as their first occurence in `list`.  That is, `unique` removes duplicate elements. 
```python
>>> lst = ['b', 'a', 'a', 'c', 'b', 'a']
>>> unique(lst)
['b', 'a', 'c']
>>> lst = [5,5,5,5,5,5,5]
>>> unique(lst)
[5]
>>> unique( [] )    # empty list
[ ]
# unique does not do a recursive scan of embedded lists
>>> lst = [1,2,2,4,[1,2,2,4],1]
>>> unique(lst)
[1, 2, 4, [1,2,2,4]] 
```

## Problem 2. Fraction and FractionTest

The Fraction class and *operator overloading* will be discussed in class.

Write a Fraction class that performs exact arithmetic using fractions.
Here are some examples:
```python
>>> from fraction import Fraction
>>> f = Fraction(2,3)   # = 2/3
>>> g = Fraction(1,12)  # = 1/12
>>> sum = f + g         # = 2/3 + 1/12 = 9/12 = 3/4
>>> sum                 # invokes sum.__str__()
3/4
>>> f * g               # 2/3 * 1/12 = 1/18
1/18
>>> two = Fraction(2)   # default denominator is 1. Same as Fraction(2,1)
>>> two + f
8/3
>>> two * g
1/6
>>> f = Fraction(8,-20) # fractions should be stored in standard form
>>> f
-2/5
```

Python lets you define operators like +, -, \*, /, and unary minus (-f) methods for your own classes, called *operator overloading*. You can also overload relational operators like `a==b`, `a<b`, `a>=b`.
You do this by defining special methods, namely:

| Operator Syntax | Method invoked        |
|:----------------|:----------------------|
| f + g           | `f.__add__(g)`        |
| f - g           | `f.__sub__(g)`        |
| f * g           | `f.__mul__(g)`        |
| -f              | `f.__neg__()`         |
| f == g          | `f.__eq__(g)`         |

Each of these methods returns a **new** Fraction, except `__eq__` which returns boolean.
For example:
```python
class Fraction:

    def __add__(self, frac: Fraction):
        numerator =        # compute numerator of self + frac
        denominator =      # compute denominator of self + frac
        return Fraction(numerator, denominator)
```
When you write `f+g`, python invokes `__add__(f,g)`, that is `self=f`.

1. In the Fraction class, first write a *class method* named `gcd` that returns the greatest common divisor of two integers.
    * The `gcd` is always positive, even if `a` and/or `b` is zero or negative!
    * See starter code for documentation.
    * Use Euclid's algorithm to compute GCD efficiently. **Don't** use a for loop.
2. **Test-Driven Development:** Tests for `gcd` are given in the starter code!  To apply TDD: first write a gcd that always returns 1.  The tests will fail.  Then write code to make the tests pass. Code - test - code - test...
3. Write these methods in the Fraction class:

| Method Name         | Meaning               |
|:--------------------|:----------------------|
| `__add__(self,g)`   | add two fractions, `f+g` |
| `__mul__(self,g)`   | multiplication, `f*g`    |
| `__str__(self)`     | show fraction as a string |
| `__eq__(self,g)`    | test for equality, `f == g` |
| `Fraction(num,denom=1)` | constructor          |
3. The constructor should always store a Fraction in **proper form**.  This means:
    * numerator and denominator have no common factors (use `gcd`)
    * denominator is always positive or zero. For example, Fraction(3,0) has denom=0.
4. Write unittests for all methods, including the constructor.


### Example Test Cases in README.md

You must design your own test cases -- more than shown here.

### Tests for unique

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list  |
| argument not a list    |  raises Invalid


### Example Python unittest

```python
import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_single_item(self):
        self.assertListEqual( ['hi'], unique['hi'])
        self.assertListEqual( ['x'], unique['x','x','x','x','x',x'])
 
if __name__ == '__main__':
    unittest.main()
```

The `FractionTest.py` file has more examples for testing gcd.
