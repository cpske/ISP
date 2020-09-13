---
title: Unit Testing
---

There are two parts to this assignment. 
1. Write a single function and some tests for the function.
2. Write unit tests for an Auction class.

Starter code is provided in the Github Classroom assignment.

## What to Submit

Commit your work to Github classroom. You should have these files:

| File             | Description   |
|:-----------------|:--------------|
| README.md        | Describe your test cases for `unique` |
| listutil.py      | Code for `unique` including docstring and doctest |
| listutil_test.py | Unit tests for `unique`, at least 3 tests |
| auction.py       | Code for Auction class (provided) |
| auction_test.py  | Your unit tests for Auction |

## Problem 1. listutil

The starter code for `listutil.py` describes the `unique` function.

1. Write the code for `unique(list)`.  
   - unique returns a new list containing the first occurence of each distinct element from the parameter list.
   - unique does not modify the parameter list.
2. In README.md write a table of test cases to thoroughly test the code. You should test:
   * **borderline cases**, such as a list with 0 or 1 elements
   * **typical cases**, such as a list with a few duplicates or **no** duplicates
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
>>> unique([ ])    # empty list
[ ]
# unique does not do a recursive scan of embedded lists
>>> lst = [1,2,2,4,[1,2,3],1]
>>> unique(lst)
[1, 2, 4, [1,2,3]] 
```
### Describing your test cases in README.md

Markdown has syntax for creating tables.  For example:

| Test case              |  Expected Result      |
|------------------------|-----------------------|
| empty list             |  empty list           |
| one item list          |  list with same item  |
| argument not a list    |  throws exception     |


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

## Problem 2. Auction

The Auction class is given in the starter code.

Write unit tests to verify that it confirms to the specification.
Try to identify any errors *specifically*, so someone running the
tests would know the probable cause of the error.

[Specification for Auction Class](AuctionTest.pdf)
