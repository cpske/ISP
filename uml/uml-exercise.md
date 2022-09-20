## UML Exercises

Draw a UML class diagram, including

- attributes, methods, and data types
- use standard UML notation
- relationships using the correct arrow type
- **multiplicity** on associations
- *don't* show visibility (+, -, ~)

```python
class Person:

    @classmethod
    def validate_citizen_id(cls, citizen_id: str) -> bool:
        """Check if a citizen id is valid. Uses a checksum."""
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
# Instead of a lot of boring code, use a dataclass.
from dataclasses import dataclass, field

@dataclass
class Enrollment:
    # the attributes of an enrollment
    student: Student
    course: Course
    # field() is how to specify a default value & behavior
    grade: str = field(compare=False, default=' ')

    # auto-generated: constructor, __eq__, __repr__,
    def __str__(self):
        """Override the default string of dataclass."""
        return f"{self.course.id} grade: {self.grade}"


@dataclass(frozen=true)  # make a course immutable
class Course:
    id: str        # course id
    description: str
    credits: int
```

2. Next we add an `__iter__` method to `CourseList`.  This makes a CourseList be *Iterable*.  Add this to the UML diagram
   - show Iterable as an *interface*. It's only method is `__iter__`.
   - CourseList implements Iterable
   - include a type parameter (Enrollment)
   - Iterable and Iterator are *types* in the Python `typing` package, which we will cover after the midterm
   - we will also review the *Iterator* design pattern after the midterm

```python
from typing import Iterable, Iterator

class CourseList:

    def __iter__(self) -> Iterator[Enrollment]
        return iter(self.courses)
```
2. Draw a Sequence Diagram
