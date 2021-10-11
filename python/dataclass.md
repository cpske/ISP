---
title: Dataclasses
---

Python 3.7 added "dataclasses" to make it easier 
to construct simple classes that just contain data values.

Here is an example, for a Person who has a name (string) and birthday (datatime.date):

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    birthday: str
```

When you write this, Python automatically generates:
* `__init__(name, birthday)` constructor
* `__str__`  that returns "Person(name={name}, birthday={birthday})"
* `__repr__` that returns same thing as `__str__`
* `__eq__(other)`  that is true only if **all** the attibutes of `self` and `other` are equal

```python
>>> p = Person("Jones", "1/1/1960")
>>> q = Person("Jones", "1/1/1960")  # distinct objects with same attributes
>>> print(p)                         # calls p.__str__()
Person(name='Jone', birthday='1/1/1960')
>>> p                                # calss p.__repr__()
Person(name='Jone', birthday='1/1/1960')
>>> p.name = "Indiana"               # attributes are mutable
>>> p
Person(name='Indiana', birthday='1/1/1960')
```

There are several options you can specify:

```python
@dataclass(init=True, repr=True, eq=True, order=False, frozen=False)
class Person:
    ...
```
The means are
| option       | meaning               |
|:-------------|:----------------------|
| init=        | generate an `__init__` method? Default True. |
| repr=        | generate a `__repr__` method? Default True. |
| eq=          | generate an `__eq__` method? Default True. |
| frozen=      | make attributes immutable (read-only)? Default False. |
| order=       | add ordering methods? Default False. |

If we wanted Person to be immutable, we could write:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str
    birthday: str

>>> p = Person("Peewee", "1/1/1960")
>>> p.name = "Jones"
dataclasses.FrozenInstanceError: cannot assign to field 'name'
```
