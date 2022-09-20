## UML Exercises

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
    """Courses a student is enrolled in."""

    def __init__(self):
        # store enrollments, not courses
        self.courses: List[Enrollment] = []

    def add_course(self, course: Course):
        enroll = Enrollment(self, course)
        self.courses.add(enroll)

    def credits(self) -> int:
        """compute and return the total credits enrolled."""
        return sum(e.course.credits for e in self.enrollments)

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

> **Iterable:** A class is *Iterable* if it's instances create an Iterator (for some sequence) when you invoke `iter(object)`.
> `CourseList(Iterable)` means CourseList implements Iterable.
> `Iterable[X]` means the iterators created by this Iterable returns objects of type X.
> An **Iterator** is a type that *iterates* over a sequence of values each time next() is called.
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

---
3. Draw a Sequence Diagram of what happens when `Main.run` is invoked.
   - Use the "found" notation to show `run` is invoked. 
   - "found" is drawn as an arrow from the left side that points to the activation box for "run", with the word `run` on the arrow.

```python
class Money:
    def __init__(self, value: float, currency: str):
        self.value = value
        self.currency = currency

    def __add__(self, other: Money):
        if other.currency != self.currency:
            raise ValueError("Can't add different currencies")
        sum_value = self.value + other.value
        return Money(sum_value, self.currency)

class Main:
    def run(self):
        m1 = Money(50, "RMB")
        m2 = Money(20, "RMB")
        sum = m1 + m2
```