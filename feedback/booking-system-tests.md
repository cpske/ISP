---
title: Python Semantics & Design Exercise
---

In the Appointment Booking System exam, some students wrote tests like this:

```python
def test_find_appointment(self):
    self.booking_system.create_appointment("1234567890","Bookie","2021-9-28")
        self.assertEqual(self.booking_system.find_appointment_for_id("1234567890"), Appointment('1234567890', 'Bookie', '28/09/2021'))
```

### Coding Style

1. Suggest improvements to this code, based on Python coding style guide.

2. Suggest improvments based on writing readable code.

### Semantics

`assertEqual` always fails.  There are 2 reasons.  Find BOTH.

**Hint:** 
Compare the handling of `date` in `BookingSystem.create_appointment` and
`Appointment` constructor.

### Design

Suppose that you can modify BookingSystem and Appointment.

What changes would you make and **why**?

There are several changes to this code that would improve:

* Consistency

* Convenience

* Type Checking (for readability & static checking)

