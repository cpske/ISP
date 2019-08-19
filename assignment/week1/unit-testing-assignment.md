# Unit Testing

There are two parts to this assignment. The first part is to test a single function.  The second part is writing a Fraction class and test its methods.
Starter code is provided in the Github Classroom assignment.

## Clone The Project from Github Classroom

1. Accept the assignment by going to the URL given in class.

2. Wait for Github to create a repository for you.

3. Clone the repository (command to do this is shown on Github).  If you are using the HTTPS protocol with Git, the command will be similar to this:

```
(change to a directory where you store projects in. NOT the Desktop!)
cd workspace

(clone the repository)
git clone https://github.com/ISP19/unittesting-your_github_id.git unittesting
```
The last argument (`unittesting`) is the name you want git to use for your local copy.  If you don't specify this, git uses the same name as the remote repo (`unittesting-your_github_id`).


## What to Submit

Commit your work to Github classroom. You should have these files:

| File             | Description   |
|:-----------------|:--------------|
| README.md        | Describe your test cases |
| listutil.py      | Code for `unique` including docstring and doctest |
| listutil_test.py | Unit tests for `unique` and `average` |
| fraction.py      | Code for Fraction class |
| fraction_test.py | Unit tests for Fraction |

## Problem 1. listutil

The starter code for `listutil.py` describes the `unique` function.

1. Write the code for `unique`.  See below for examples.
2. In README.md write a table of test cases to thoroughly test the code. You should test:
   * **borderline cases**, such as a list with 0 or 1 elements
   * **typical cases**, such as a list with a few duplicates or **no** duplicates
   * an **impossible case** where the method should not work. 
   * **extreme case**, such as a very large list
3. Write the tests using Python unittest.  The test file should be `listutil_test.py`.  Each test case is a separate method.
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
>>> lst = [1,2,2,4,[1,2,3],1]
>>> unique(lst)
[1, 2, 4, [1,2,3]] 
```


## Example Python unittest for Unique

```python
import unittest
from listutil import unique
 
class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual( ['hi'], unique(['hi']) )
 
if __name__ == '__main__':
    unittest.main()
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
You do this by defining special methods in your class:

| Operator Syntax | Method invoked        |
|:----------------|:----------------------|
| f + g           | `__add__(f,g)`        |
| f - g           | `__sub__(f,g)`        |
| f * g           | `__mul__(f,g)`        |
| -f              | `__neg__(f)`          |
| f == g          | `__eq__(f,g)`         |

When you write `f+g`, python invokes `__add__(self,g)` where `self=f`.
Each of these methods returns a **new** Fraction, except `__eq__` which returns boolean.
For example:
```python
class Fraction:

    def __add__(self, frac: Fraction):
        """Add two fractions and return the sum as a new Fraction"""
        numerator =        # compute numerator of self + frac
        denominator =      # compute denominator of self + frac
        return Fraction(numerator, denominator)
```

3. Write these methods in the Fraction class:

<table border="1" align="center">
<tr>
<th>Method Name</th> <th>Meaning</th>
</tr>
<tr valign="top">
<td align="left"> 
__init__(num,denom=1)
</td>
<td align="left"> 
Constructor sets fraction numerator and denominator in proper form. Default value of denominator is 1.
</td>
</tr>
<tr valign="top">
<td align="left">
__add__(self,frac)
</td>
<td align="left">add fractions self and frac </td>
</tr>
<tr valign="top">
<td align="left">
__mul__(self,frac)  
</td> 
<td align="left">multiply fractions `self` and `frac` </td> 
</tr>
<tr valign="top">
<td align="left">
__str__(self)
</td>
<td align="left">fraction as a string </td>
</tr>
<tr valign="top">
<td align="left"> 
__eq__(self,f)
</td>
<td align="left"> 
test if two fractions have same value, `self == f` 
</td>
</tr>
</table>

4. The constructor should always store a Fraction in **proper form**.  This means:
    * numerator and denominator have no common factors
    * denominator is always positive or zero. 
    * Fraction(3,0) has numerator=1 and denominator=0.
    * Hint: Python has a function `math.gcd()` you can use to remove the greatest common denominator. `math.gcd(a,b)` is always positive unless `a` and `b` are both 0. 
5. `__str__` should return fraction as a string, such as "2/3" or "4" (if fraction has denominator 1 then print it as integer).
6. `__eq__` is true if fractions have the same value.
    * Example:  `Fraction(3,4) == Fraction(-9,-12)` should be `true`.
    * If constructor always stores fractions in proper form, then this method is trivially easy. 
7. Write **unittests** for all methods, including the constructor.


### Example Test Cases in README.md

You must design your own test cases -- more than shown here.

### Tests for unique

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list  |
| argument not a list    |  throws exception   |


