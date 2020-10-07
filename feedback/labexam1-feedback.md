---
title: Feedback on Bank Account Test
---

## False Positives and False Negatives

**False Positive**: a test fails even though the code under test is correct.
- this implies the code is incorrect but actually it is correct
- usually correctable by comparing the test to the specification for how the code *should* behave

**False Negative**: the code contains an error, but the tests all pass.
- fail to detect an error in code
- may result in releasing defective code to customers
- may cause other parts of code to fail, and waste time finding the cause of failure

Both "False Positive" and "False Negative" are defects in testing.    

If a test case is "False Positive" then the test may be useless:
```
def test_balance(self):
    self.account.deposit(Money(1000))
    self.assertEqual(self.account.balance, 900)  # always fails
```

So, you need to identify and fix any False Positives.

> False Positive and False Negative in medical tests.
> 
> A false positive means the test indicates you have a condition even though you do not.    
> A false negative means the test "passes" (you don't have the condition) even though you do.
>
> Which is worse?    
> Compare these, and consider the consequences of a false positive or false negative.
>
> * A test whether you have the Covid-19 virus.
> * A test whether you have the Covid-19 antibodies to protect against the Covid-19 virus.


## How I Tested

I used 2 BankAccount classes:

1. A correct BankAccount class, according to the specification.
2. A BankAccount containing 7 different errors which are activated using an environment variable. Only 1 error is active at a time.

I tested for errors that a competant programmer might realistically make.
Many of these are "edge" cases or failure to match the specification.

The defects are:

| BUG  | Description                      |
|------|:---------------------------------|
|  1   | `available` is computed incorrectly when there are pending checks (the exam starter code has this bug) |
|  2   | can't withdraw exactly the available balance |
|  3   | `clear_check(check)` never raises exception (fails silently)  |
|  4   | can deposit Money with a value of 0        |
|  5   | can deposit the same Check more than once  |
|  6   | if try to withdraw too much, withdraw returns None without raising ValueError |
|  7   | value of a deposited check is not included in balance until check clears |
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
   * Any tests that do not test BankAccount I marked as `\@skip`.
   * Retest and correct until all tests pass.

4. Record any semantic or syntax errors.

5. Run tests using the defective BankAccount code: run the tests multiple times using each of the bugs above.
   * Record which cases the defect was detected.
   * Student needs to detect 6 out of 7 defects for full credit.

## Scoring

<table border="1">
<tr>
  <th align="left">Criterion</th>
  <th align="left">Score</th>
</tr>
<tr valign="top">
  <td>
  Test using Correct BankAccount<br>
  (Test for False Positives)
  </td>
  <td>
  20  all tests pass <br/>
  14  one test fails <br/>
  7   two tests fail <br/>
  0   more than two tests fail <br/>
  </td>
</tr>
<tr valign="top">
  <td>
  Code Coverage
  </td>
  <td>
  10  coverage &ge; 89% <br/>
  7   coverage 80% - 88% <br/>
  4   coverage 70% - 79% <br/>
  0   coverage below 70%
  </td>
</tr>
<tr valign="top">
  <td>
  Test using Defective BankAccount <br/>
  Six Different Defects Tested
  </td>
  <td>
  10 points for each defect detected <br>
  Full score 60 points
  </td>
</tr>
<tr valign="top">
  <td>
  Semantic and Syntax Errors <br/>
  </td>
  <td>
  10 no errors <br/>
  &nbsp;5 one error <br/>
  &nbsp;0 two or more errors
  </td>
</tr>
<tr valign="top">
  <td>
  <b>Total</b>
  </td>
  <td>
  <b>100</b>
  </td>
</tr>
</table>

## Not a Test of BankAccount

Any test that does **not** test the BankAccount class was marked as `\@skip`:

```python
@unittest.skip("Not a test of BankAccount")
def test_cannot_deposit_zero(self):
    with self.assertThrows(ValueError):
        Money(0.0)
```

1. This does not test BankAccount.deposit(). Test name is misleading.
2. The spec doesn't say anything about the behavior of Money itself.
3. Even if the test works, the BankAccount deposit() method must separately verify that `money.value > 0`.  Why?
   - Because a **subclass** of Money **may** permit value = 0.
   - The code for the Money class could change -- don't rely on it.

## Test Always Fails Due to Logic Error

This will *always* fail.

```python
def test_deposit_check(self):
   acct = BankAccount("test account")
   acct.deposit(Check(800))
  
   self.assertEqual(acct.available, 800)
   self.assertEqual(acct.available, 700)
```

For a test that always fails I either comment out the failing assert or mark the entire test as `\@skip`.

## Syntax and Semantic Errors

These are errors where Python prints an error message when 
it encounters the error, or the error will cause the code to fail at
the particular statement.

Therefore, any programmer should be able to fix these error him/herself.

Before evaluating student code using the buggy BankAccount class,
I had to correct or remove all syntax and semantic errors.

These are examples of actual errors in student code:

```python
acct = BankAccount("test account")
acct.deposit(1000)                      # param should be Money or subclass of Money
self.assertEqual(acct, "test account")  # can't compare BankAccount and string

self.assertIs(acct.balance, 1000.0)     # semantic error (see below)

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
To compare **values** use `assertEqual(a, b)`.
