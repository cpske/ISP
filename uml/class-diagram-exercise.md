---
title: UML Class Diagram Exercise
---
Exercise: Create a UML Class Diagram

1. Draw a UML class diagram of the code below, including
   - attributes, methods, and data types
   - relationships using the correct arrow type
   - **multiplicity** on associations
   - use standard UML notation
   - *don't* show visibility (+, -, ~)

```python
class Person:

    @classmethod
    def validate_citizen_id(cls, citizen_id: str) -> bool:
        """True if a citizen id is valid. Uses a checksum formula."""
        # code omitted
        pass

    def __init__(self, first_name: str, last_name: str,
              citizen_id: str):
        # code omitted

    def set_birthday(self, birthdate: date):
        self.birthday = birthdate

    def get_birthday(self):
        return self.birthday


class Student(Person):
    """A person studying at an educational institution."""
    pass


class CourseList:
    """Courses that a student is enrolled in."""

    def __init__(self, student: Student):
        self.student = student
        # courselist consists of enrollments, not courses
        self.courses: List[Enrollment] = []

    def add_course(self, course: Course):
        enroll = Enrollment(self.student, course)
        self.courses.add(enroll)

    def credits(self) -> int:
        """compute and return the total credits enrolled."""
        return sum(e.course.credits for e in self.courses)

# Course & Enrollment contain only attributes and standard
# methods for __eq__, __repr__, and __str__.
# Instead of writing boring code, use a dataclass.
# It automatically generates constructor, __str__, __eq__, __repr__
from dataclasses import dataclass, field

@dataclass
class Enrollment:
    # the attributes of an enrollment
    student: Student
    course: Course
    # field() is how to specify a default value & behavior
    grade: str = field(compare=False, default=' ')

    # Auto-generated constructor:
    #def __init__(self, student, course, grade=' '):

    def __str__(self):
        """Override the default string of dataclass."""
        return f"{self.course.id} grade {self.grade}"


@dataclass(frozen=true)  # make Course objects immutable
class Course:
    id: str        # course id
    description: str
    credits: int
```

2. Suppose we make `CourseList` *Iterable* as shown below.  Add this to the class diagram.
   - Show *Iterable* as an interface with an `__iter__` method
   - CourseList *implements* Iterable
   - Types like Iterable satisfy the intention of an interface, which is to *separate the specification of a behavior from it's implementation*, even though they aren't called "interfaces" in Python.
 

```python
from typing import Iterable, Iterator

class CourseList(Iterable[Enrollment]):

    def __iter__(self) -> Iterator[Enrollment]:
        """Return an iterator for enrollments in this courselist."""
        return iter(self.courses)
```

Submit your diagram to the assignment on Google Classroom. If you embed your diagram in a Google doc it is easier for instructor to give comments.

---

## Iterable & Iterator

In Python, [Iterable][Iterable-refs] and [Iterator][Iterator-refs] are **types** (in the `typing` package) with
implementations as *abstract base classes* in the `collections.abc` package.

In Java, C#, and other languages, *Iterable* and *Iterator* are *interfaces*.
Since an **interface** is a specification for some behavior without an implementation,
Python *types* are conceptually like *interfaces*.

[Iterable-refs]: https://docs.python.org/3/search.html?q=Iterable
[Iterator-refs]: https://docs.python.org/3/search.html?q=Iterator
[iterable]: https://docs.python.org/3/library/typing.html?highlight=iterable#typing.Iterable
[iterator]: https://docs.python.org/3/library/typing.html?highlight=iterator#typing.Iterator

[Iterable][iterable] is used extensively in Python, even though you may rarely
call it explicitly.   

What kind of object can you use in each of these statements?
```python
for x in ___?what?___:
    do something with x
```
or 
```python
[foo(x) for x in ___?what?____ if predicate(x)]
```
or
```python
sorted_values = sorted(?what?)
```
In all three cases, you can use anything that is *Iterable*.


[Iterable][iterable] A class is *Iterable* if it's instances create an Iterator (for some sequence) when you invoke `iter(object)`.
- `CourseList(Iterable)` means CourseList implements Iterable.
- `Iterable[X]` means the iterators created by this Iterable returns objects of type X.
- `CourseList(Iterable[Enrollment])` means CourseList is Iterable and the Iterator returns Enrollment objects.

[Iterator][iterator] is a type that *iterates* over a sequence of values each time `next()` is called.
> list, set, dict, and strings are all Iterable.
> ```python
> s = "Strings are iterable"
> it = iter(s)
> next(it)
> 'S'
> next(it)
> 't'
> next(it)
> 'r'

### Python Syntax for Subclass, Implements, & Mixin

In Python, the same notation is used for inheritance, typing, and mixins:
```python
from collections.abc import Sized, Callable

class Subclass(Parent, Sized, Callable):
    """A class that is a subclass of Parent,
    and also has the Sized and Callable behavior.
    """
```
