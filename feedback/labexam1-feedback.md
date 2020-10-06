---
title: Feedback on Bank Account Test
---

## False Positives and False Negatives

**False Positive**: a test fails even though the code under test is correct.
- this erroneously implies the code is incorrect
- usually correctable by comparing the test to the specification for how the code *should* behave

**False Negative**: the code contains an error, but the tests all pass.
- fail to detect errors in code
- can result in releasing defective code to customers

Both "False Positive" and "False Negative" are defects in testing.    

If a test case is "False Positive" then the test may be useless:
```
def test_balance(self):
    self.account.deposit(Money(1000))
    self.assertEqual(self.account.balance, 900)  # always fails
```

So, you need to fix False Positives before you can **really** test the code.

## How I Tested

I used 2 BankAccount classes:

1. A correct BankAccount class, according to the specification.
2. A BankAccount containing 6 different errors which are activated using an environment variable. Only 1 error is active at a time.

I tested for errors that a competant programmer might realistically make.
Many of these are "edge" cases or failure to match the specification.

The 6 errors are:

| BUG  | Description                      |
|------|:---------------------------------|
|  1   | `available` is computed incorrectly when there are pending checks (the exam starter code has this bug) |
|  2   | can't withdraw exactly the available balance |
|  3   | `clear_check(check)` never raises exception (fails silently)  |
|  4   | can deposit Money with a value of 0        |
|  5   | can deposit the same Check more than once  |
|  6   | if try to withdraw too much, withdraw returns None without raising ValueError |
|  0   | No active bugs. All methods work correctly. Used to verify the target code.  |

I also ran code coverage, using a `.coveragerc` file to *exclude* methods you were not expected to test:
```
# .coveragrc
branch = True
# omit uninteresting files. Only analyze bank_account.py
omit =
    *_test.py
    money.py
    check.py

[report]
# exclude these BankAccount methods from statistics
exclude_lines =
    def __str__
    def __repr__
    def account_name
```

## Test Procedure

1. Run the test code with code coverage using a correct BankAccount class (class has no defects and no extra code for latent defects).    
   All tests should pass.

2. Record code coverage result and how many tests failed or had errors.

3. Correct or comment out all failed tests in student's `bank_account_test.py`.
   * I corrected the first error reported by unittest, except semantic errors. 
   * For example, if a test asserts account.available is 400 and it should be 500, then I changed the assert value to 500.
   * For failures after the first one, I commented out the failing asserts. Just enough to make the test pass.
   * Also commented out syntax and semantic errors that cause tests to fail.
   * Retest and correct until all tests pass.

4. Record any semantic or syntax errors.

5. Run tests using the defective BankAccount code: run the tests 6 times using each of the bugs above.
   * Record which cases the defect was detected.
   * Student needs to detect 5 out of 6 defects for full credit.

## Scoring

<table border="1">
<tr>
  <th align="left">Criterion</th>
  <th align="center">Score</th>
</tr>
<tr valign="top">
  <td>
  Test using Correct BankAccount<br>
  (Test for False Positives)
  </td>
  <td>
  20  all tests pass <br/>
  15  one failure <br/>
  5   two failures <br/>
  0   more than two fail <br/>
  </td>
</tr>
<tr valign="top">
  <td>
  Code Coverage
  </td>
  <td>
  10  coverage &ge; 89% <br/>
  7   80% - 88% coverage <br/>
  5   70% - 79% coverage <br/>
  0   below 70%
  </td>
</tr>
<tr valign="top">
  <td>
  Test using Defective Code <br/>
  Number of Bugs Detected
  </td>
  <td>
  10 points per bug <br>
  Full score 50 points
  </td>
</tr>
<tr valign="top">
  <td>
  Coding Errors <br/>
  (Semantic and syntax errors)
  </td>
  <td>
  &nbsp;0 no errors <br/>
  -4 one error <br/>
  -8 two or more errors
  </td>
</tr>
<tr valign="top">
  <td>
  <b>Total</b>
  </td>
  <td>
  80
  </td>
</tr>
</table>

## Syntax and Semantic Errors

These are errors where either Python prints an error message when 
it finds the error, or the error will cause the code to fail.

Either way, a programmer should be able to fix them him/herself,
since a message is printed when the test is run.

These are examples of actual errors in codes:

```python
acct = BankAccount("test account")
acct.deposit(1000)                      # param should be Money or subclass of Money
self.assertEqual(acct, "test account")  # can't compare BankAccount & string

self.assertIs(acct.balance, 1000.0)     # semantically incorrect (see below)

with AssertionError(ValueError,"Have to Clear check first"):  # semantic error
    money = Money(1000)
    a.withdraw(money)                   # param should be float, not Money
```

`self.assertIs(a, b)` is used to test `a is b` (test for object identity).   
```python
>>> x = 1000.0
>>> y = 1000
>>> x is y
False
>>> y = 2 * 500.0   # y is float with the same value as x
>>> x is y
False
# what you should write is:
>>> x == y
True
```
To compare values use `assertEqual(a, b)`.

## Logic Error

This will *always* fail.

```python
def test_deposit_check(self):
   acct = BankAccount("test account")
   acct.deposit(Check(800))
  
   self.assertEqual(acct.available, 800)
   self.assertEqual(acct.available, 700)
```
