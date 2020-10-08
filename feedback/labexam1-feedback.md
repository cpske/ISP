---
title: Feedback on Bank Account Test
---

## False Positives and False Negatives in Medical Tests

For a test that indicates if a person has the Covid-19 virus

* What is a *False Positive* result?

* What is a *False Negative* result?

* For a Covid-19 test, which error is more serious?

For a test that you have the Covid-19 antibodies to protect against the Covid-19 virus

* What is a *False Positive* result?

* What is a *False Negative* result?

* For a Covid-19 antibody test, which error is more serious?


## False Positives and False Negatives in Code Testing

**False Positive**: a test fails even though the code under test is correct.

- this implies the code is incorrect but actually it is correct
- can be verified and corrected by comparing the test code to the specification of how the code *should* behave

**False Negative**: the code contains an error, but the tests all pass.

- fail to detect an error in code
- the lack of **sensitivity** of the test can easily go unnoticed
- may result in releasing defective code to customers
- when the appication fails or produces wrong results, may require a lot of time to identify and locate the cause

Both "False Positive" and "False Negative" are defects in testing. 

A test that produces a "False Positive" may be useless:
```
def test_balance(self):
    self.account.deposit(Money(1000))
    self.assertEqual(self.account.balance, 900)  # always fails
```

So, you need to identify and fix any False Positives.


## How I Tested

I used 2 BankAccount classes:

1. A correct BankAccount class, according to the specification.
2. A BankAccount containing 7 different errors which are activated using an environment variable. Only 1 error is active at a time.

I tested for errors that a competant programmer might realistically make.
Some of these are "edge" cases where it is easy to make a coding error.

The defects are:

| BUG  | Description                      |
|:----:|:---------------------------------|
|  1   | `available` is computed incorrectly when there are pending checks (the exam starter code has this bug) |
|  2   | can't withdraw exactly the available balance (the starter code has this bug) |
|  3   | `clear_check(check)` never raises exception (fails silently)  |
|  4   | can deposit Money with a value of 0        |
|  5   | can deposit the same Check more than once  |
|  6   | if try to withdraw too much, withdraw returns None without raising ValueError |
|  7   | value of a deposited check is not included in balance until the check clears |
|  0   | No active bugs. All methods work correctly. Used to verify the target code.  |

I also ran code coverage while testing the *correct* BankAccount class.
I used a `.coveragerc` file to *exclude* methods you were not expected to test:
```
# .coveragrc
branch = True
# omit files that are not under test. Only analyze bank_account.py
omit =
    *_test.py
    money.py
    check.py

[report]
# exclude methods that are not explicitly being tested
exclude_lines =
    def __init__
    def __repr__
    def __str__
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
   * Commented out any syntax and semantic errors that cause tests to fail.
   * Any tests that do not test BankAccount I marked as `\@skip`.
   * Retest and correct until all tests pass.

4. Record any semantic or syntax errors.

5. Run tests using the defective BankAccount code: run the tests multiple times using each of the defects listed above.
   * Record which cases the defect was detected (a test fails or errors).
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
  14  one test fails (1 false positive)<br/>
  8   two tests fail (2 false positives)<br/>
  0   more than two tests fail <br/>
  </td>
</tr>
<tr valign="top">
  <td>
  Code Coverage
  </td>
  <td>
  20  coverage &ge; 85% <br/>
  19  coverage = 84% <br/>
  18  coverage = 83% <br/>
  ... <br/>
  1   coverage = 66% <br/>
  0   coverage &lt; 65%
  </td>
</tr>
<tr valign="top">
  <td>
  Test using Defective BankAccount <br/>
  Different Defects Tested One at a Time
  </td>
  <td>
  10 points for each defect detected <br>
  Full score is 60 points (6 defects)
  </td>
</tr>
<tr valign="top">
  <td>
  Semantic and Syntax Errors <br/>
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
  <b>100</b>
  </td>
</tr>
</table>

### Student Code Accuracy & Sensitivity

| Metric                 | Number |
|:-----------------------|--------|
| Test Coverage &ge; 90% (good) |   19   |
| Test Coverage 85%-89% (fair)|   12   |
| No False Positive      |   17   |
| One False Positive     |   19   |
| Two False Positive     |    5   |
| Detected Bug 1         |   29   |
| Detected Bug 2         |   14   |
| Detected Bug 3         |   15   |
| Detected Bug 4         |    9   |
| Detected Bug 5         |   13   |
| Detected Bug 6         |   42   |
| Detected Bug 7         |   41   |

### Top Testers

* Narawish
* Patiphan
* Sahanon
* Theetouch

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
   - In testing, I *did* allow Money(0) so tests of deposit(Money(0)) would work.

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
it encounters the error; usually the error will cause the code to fail at
the erroneous statement.

Therefore, any programmer should be able to fix these errors him/herself.

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

`assertIs(a, b)` is used to test `a is b` (test for object identity).   
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

Similarly, instead of testing `assertIs(math.isfinite(2), True)` it is better to write `assertTrue(math.isfinite(2))`.
