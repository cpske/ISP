---
title: Evaluation of the Appointment Booking System Tests
---

### Correction for Common Errors

During testing, I made corrections for the following errors:

| Error | Description |
|-------|-------------|
|  E1   | Hard coded appointment dates ("9/27/2021") in tests, so when tests are run at a later date they all fail! |
|  E2   | Tests rely on `appointment.__eq__` method which does not exist |
|  E3   | Student modified Appointment class or BookingSystem class |
| other | If syntax or semantic errors that cause tests to fail, count those errors and "@skip" tests. |


### Code Coverage

I performed code coverage using Python 3.6 and the `coverage` package. I used the original `booking_system.py` as target code.

Code Coverage **excluded** these methods and classes, which were not the main target of your testing:
```
parse_date
validate_id
Appointment class
```
Hence, code coverage measures how much of the important code in BookingSystem is covered by tests.

### Running Tests 

I ran tests using the original `booking_system.py` and 8 alternate codes.

- For variant 0 (original code) **all tests should pass**.
- For variant 1 (alternate implementation) **all tests should pass**.
- For variant 2 - 8 **at least one test should fail**.
- When testing the original `booking_system.py`, if any tests **failed** then those tests are not useful (false positives).  Hence, I **removed those tests**  using `@unittest.skip` before testing Variants 1 - 8.


 Variant  | Description                                             
----------|:----------------------------------------------------
 0        | Same as BookingSystem code in exam. All tests should **pass**.
 1        | Test using alterate implementation of BookingSystem. All tests should **pass**.
 2        | BookingSystem doesn't completely fill daily capacity (off by 1).
 3        | BookingSystem overbooks appointments (more than capacity per date).
 4        | BookingSystem ignores the requested date and chooses the date itself.
 5        | A Person can create more than one Appointment.
 6        | A Person can create appointment more than 7 days in the future.
 7        | Person cannot cancel an appointment. It stays in the BookingSystem.
 8        | BookingSystem creates appointment with person name and id in reversed fields (programmer error).

### Evaluation Procedure

1. Verify that student did not modify BookingSystem or Appointment.
2. Run tests using original BookingSystem with code coverage. Tests should all pass.
3. If tests fail because of hard-coded appointment dates (E1), then mock `today` to be 27/9/2021 and run again.
4. If test code uses a mix of hard-coded dates ('27-9-2021') and `date.today()` for date, then use `freezegun` to mock `datetime.date.today()` to a fixed value.
5. If tests rely on `appointment.__eq__` (E2) then add "eq" to appointment.py and rerun tests..
6. If any tests fail when using the original correct code, count the failures and remove those tests using `@skip` or `@skipIf`.
7. Run tests using code variants 1 - 8.


### Feedback on Code 

Some poor coding practices seen in the exam:

1. Don't call `setUp` from within tests.  unittest calls `setUp` automatically before each test:
   ```python
   def test_create_appointment(self):
       """Test can create appointment on unspecified day."""
       self.setUp()   <-----# Don't write this. It is called automatically.
       ...
   ```

2. Accessing attributes of BookingSystem in tests.  You should test the **specification** (behavior), not the implementation. Tests should NOT access attributes of BookingSystem.
   ```python
   def test_create_appointment(self):
      appt = self.bs.create_appointment('1234567890', 'Appointee")
      self.assertEqual(appt, bs.schedule[self.today][0] )    <----# Don't use attributes
   ```
   The alternate implementation (Variant 1) does not have a `schedule` attribute.

3. Redundant string constants instead of using a local variable. This makes tests hard to read.    
   Poor:
   ```python
    def test_cancel_appointment(self):
        """Cancel an appointment should remove it's booking details"""
        bs = BookingSystem(1)
        bs.create_appointment('1111111111', 'Pat', '29/09/2021')
        bs.remove_appointment('1111111111')
        # Semantic Error on 2nd line
        self.assertEqual(None, bs.find_appointment_for_id('1111111111')
                             ,bs.find_bookings_for_date('29/09/2021')) <-- error
   ```
   * redundant string '1111111111'
   * hardcoded date -- test will fail on a future date
   * long statement in assertEqual
   * Semantic error in assertEqual: what are you trying to compare?    
   Better:
   ```python
   def test_cancel_appointment(self):
       bs = BookingSystem(1)
       id = '1111111111'
       date = datetime.date.today()
       appt = bs.create_appointment(id, 'Pat', date)
       self.assertNotNone(appt, "could not create an appointment")
       # should return the appointment that is removed
       self.assertSame(appt, bs.remove_appointment(id))
       # should not have any appointment now
       self.assertEqual(None, bs.find_appointment_for_id(id))
       # no appointment in the schedule, either
       self.assertEqual([], bs.find_bookings_for_date(date))
   ``` 

4. Long lines. Line length should not exceed 80 chars.

5. Tests should not rely on string form of Appointment.    
   Poor:
   ```python
   def test_create_appointment(self):
      appt = self.bs.create_appointment('1111111111', 'Pat', '29/09/2021')
      self.assertEqual(str(appt), "Pat [1111111111] on 29/09/2021") <--- brittle
   ```
   This is a **brittle test**. It's easy to break by a small change in code.    
   Better:
   ```python
   def test_create_appointment(self):
      id = '1111111111'
      date = datetime.date.today()
      appt = bs.create_appointment(id, 'Pat', today)
      self.assertNotNone(appt)
      self.assertEqual(date, appt.date)
      self.assertEqual(id, appt.person_id)
      self.assertEqual('Pat', appt.name)
   ```

6. Don't modify the code under test!

   - Two students modified `booking_system.py` or `appointment.py`.
   - You should not modify code under test.
   - If you need to change something in the code under test, try (a) mock it, (b) write a method in your test class to do what you want.

   Example: *write an equal for appointment*   

   ```python
   # call this method from your tests to assert appt1 == appt2

   def assertAppointmentEqual(self, appt1, appt2):
       # test if same reference or both are None
       if appt1 == appt2: return 
       # compare attributes
       self.assertEqual(appt1.person_id, appt2.person_id)
       self.assertEqual(appt1.name, appt2.name)

   ```

