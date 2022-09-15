---
title: Feedback on Phone Log Testing Quiz
---

## How I Graded

1. Run your tests using a correct `PhoneLog` code.  All tests should pass.
   - If any tests fail, edit the test file and review the test code.
   - If the test is incorrect, mark it with `@unittest.skip`.
   - For the special case where student misunderstood trimming of spaces, fix the test.
   - Retest using the correct `PhoneLog` code until all tests pass.

2. Record any syntax or semantic errors in the scores sheet.
   - Fix 1 syntax or usage error that causes tests to fail or error.
   - If more than 1 syntax or usage error, the tests are wrong.

3. If the correct `PhoneLog` code passes all tests using student's original tests or tests edited to skip 1 test, then give credit for "Good Code Passes Tests". Otherwise, no credit.
   - Two exceptional cases were allowed. Both of these are **not** in the spec, but I commented out the specific test code for purpose of evaluation.
     1. Student test assumes a phone number containing non-numerics should raise a ValueError. (Only ValueError, not TypeError.)  
     2. Student test assumes that internal spaces are removed from phone numbers.

4. Run tests using 4 codes each containing a defect. Count how many defects were detected.

5. View the test code for correct use of `setUp`.
   - setUp should **not** contain assert statements -- those should be in tests.


## The Four Defects 

Your tests were run against 4 defective PhoneLog codes, 
each containing a mistake that a programmer might reasonably make.

1. When the PhoneLog is full to capacity, `record_call` always drops the oldest call *before* checking whether the received phone number is already in the call list.  Hence, is sometimes deletes a number unnecessarily.

2. `record_call` compares the phone number only to the *first* element in the phone log. Hence, it may end up recording the same number more than once.

3. Off-by-one error: if the phone log is full and a new phone number is passed to `record_call`, it is recorded without removing the oldest number from the phone log.    
   This sort of defect occurs a lot due to mistakes such as `if len(list) > capacity` instead of `if len(list) >= capacity`.

4. The code for checking an empty phone number is incorrect:
   ```python
   def record_call(self, phone_number):
       # this test for empty string but not a string containing space
       if not phone_number:
           raise ValueError("Phone number may not be empty or space")
   ```
   This sort of error is an example of misunderstanding Python semantics.


## Use Utility Methods for More Concise, Readable Tests

Consider this test:
```python
   def test_duplicate_call(self):
       self.phonelog.record_call("1111")
       self.phonelog.record_call("1112")
       self.phonelog.record_call("1111")
       # 1111 should be first with no duplicate
       self.assertListEqual(["1111", "1112"], self.phonelog.get_calls())
       # consecutive duplicates are not recorded
       self.phonelog.record_call("1111")
       self.assertListEqual(["1111", "1112"], self.phonelog.get_calls())
       # duplicate a call in the middle
       self.phonelog.record_call("3333")
       self.phonelog.record_call("4444")
       self.phonelog.record_call("3333")
       self.assertListEqual(["3333", "4444", "1111", "1112"], 
                            self.phonelog.get_calls())
```
a lot of verbose and duplicate code here -- and this is only **one** test. 
Is this more readable? 

```python
   def test_duplicate_call(self):
       receive_calls(self.phonelog, "1111", "1112")
       self.assert_phonelog_is(["1112", "1111"])
       receive_calls(self.phonelog, "1111")
       self.assert_phonelog_is(["1111", "1112"])

       # consecutive duplicates are not recorded
       receive_calls(self.phonelog, "1111")
       self.assert_phonelog_is(["1111", "1112"])

       # duplicate a call in the middle
       receive_calls(self.phonelog, "3333", "4444", "3333")
       self.assert_phonelog_is(["3333", "4444", "1111", "1112"]) 
```

In writing tests, when you see a lot of verbose, boilerplate code, consider
some utility methods or functions:
```python
class TestPhoneLog(unittest.TestCase):
    def setUp(self):
        self.phonelog = PhoneLog(5)

    def assert_phonelog_is(self, call_list):
        self.assertListEqual(call_list, self.phonelog.get_calls())


# function to receive calls
def receive_calls(phonelog, *phone_numbers):
    for num in phone_numbers:
        phonelog.record_call(num)
```


## Common Mistakes

1. Testing 2 statements in one `assertRaises` block. In class we discussed why this is incorrect.    
   This test will miss one of the four defects:
   ```python
   def test_empty_phone_number(self):
       phone_log = PhoneLog(10)
       with self.assertRaises(ValueError):
           phone_log.record_call("")
           phone_log.record_call("    ")
   ```

3. Tests print on terminal.  They should not.
   ```python
   def test_long_phonelog(self):
       ...
       print(self.phonelog.get_calls())   # Don't do this!
   ```

4. Misread the Specification: `receive_call` only trims leading/trailing space, not internal space.
   ```python
   def test_call_containing_space(self):
       self.phonelog.record_call("11 22")
       self.assertEqual("1122", self.phonelog.get_calls()[0])
   ```
   - no penalty for this (I fixed your code)
   - when you see that this test fails, you should reread the spec to make sure this is **really** a defect

5. Misread the Specification: there is no mention that phone number must contain only numeric characters or what PhoneLog will do in that case.  Should not expect a ValueError for `record_call("abc")` or `record_call("02-942-8555")`.
   - similar to previous defect

6. "Test to an Implementation" instead of "Test the Specification".    
   This code should not throw AttributeError
   ```
   phonelog.record_call(1234)
   ```
   - The specification doesn't state what `record_call` will do, so don't test it.
   - It's a usage error by the code *using* PhoneLog, not an error in PhoneLog code.
   - The exception which (logically) should be raised is TypeError, not AttributeError


## Uncommon Mistakes

1. A few **very long** tests instead of many short tests.
   - Each test should test for only one thing.
   - If a long test fails, it is hard to identify the root cause of the failure.
   - If there are any errors in the test, I omit it using `@unittest.skip`, so all the asserts in that test method are skipped!

2. Not prefixing test method names with `test_`.     
   This method is not a test and unittest will not run it:
   ```python
   def new_phonelog_is_empty(self):
       """A new phonelog should not contain any calls."""
       phonelog = PhoneLog(5)
       self.assertListEqual([], phonelog.get_calls())
   ```
