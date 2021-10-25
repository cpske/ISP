---
title: Evaluation of Unit Tests for the Appointment Booking System
---

### Correction for Common Errors

During testing, I made corrections for the following errors:

1. Hard coded appointment dates ("9/27/2021"), so when tests are run at a later date they all fail!
2. Tests rely on `appointment.__eq__` method which does not exist.
3. Student modified the Appointment class or BookingSystem class.

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

- For variant 0 and 1 **all tests should pass**.
- For variant 2 - 8 **at least one test should fail**.
- After testing the original `booking_system.py`, if any tests **failed** then those tests are not useful (they fail even when code is correct).  Hence, I **removed those tests**  using `@unittest.skip` before testing Variants 1 - 8.


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


