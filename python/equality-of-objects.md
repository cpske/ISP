---
title: Comparing objects
---

In the midterm exam there was an Appointment class with
structure as shown here:

<table border="1" width="40%">
<tr><th>Appointment</th></tr>
<tr><td>
name: str <br/>
person\_id: str <br/>
date: datetime.date 
</tr>
<tr>
<td>
__init__(person\_id, name, date) <br/>
__str__()
</td>
</tr>
</table>

A student asked "why does the following unit test fail?"
(I edited the code for clarity)
```python
def test_create_appointment(self):
    bs = BookingSystem(2)
    bs.create_appointment("1111111111", "Santa", "01/10/2021")
    bookings = bs.find_bookings_for_date("01/10/2021")

    self.assertEqual(bookings, [Appointment("1111111111","Santa","01/10/2021")])
```
the output is:
```
AssertionError: Lists differ:
[Appointment('1111111111', 'Santa', '01/10/2021')] != [Appointment('1111111111', 'Santa', '01/10/2021')]

First differing element is:
Appointment('1111111111', 'Santa', '01/10/2021')
Appointment('1111111111', 'Santa', '01/10/2021')
```

**Why?**    
It looks like the lists are same and the first element is same, too.

1. Can anyone explain why unittest thinks they are different?

2. What *Fundamental Characteristic of Objects* is being shown here?


**Hint**

Instead of `Appointment`, if we had lists of dates or strings, it would work!
```python
def test_list_of_dates(self):
    list1 = [datetime.date(2021,10,1), datetime.date(2021,12.31)]
    list2 = [datetime.date(2021,10,1), datetime.date(2021,12.31)]
    // this is NOT the best test method to use, but it works
    self.assertEqual(list1, list2)
```

Output:
```
PASS 
```





