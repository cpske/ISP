---
title: UML Class Diagram Exercise
---

Draw this diagram on paper.

Do your own work & please *do not* look at your neighbor's work.

### 1. Draw a UML class diagram of the code below

Include in your diagram:
- attributes, methods, and data types
- parameters on methods
- return type on all methods. If a method return None, don't show anything.
- relationship between Person and Student, using correct type of arrow.
Don't Show:
- *don't show* visibility (+, -, ~)
- *don't show* `self` parameter (its not an actual parameter in object invocation)
- *don't show* attributes & methods in subclass that are inherited from parent class but not overridden


```python
class Person:

    @classmethod
    def validate_citizen_id(cls, citizen_id: str) -> bool:
        """True if a citizen id is valid. Uses a checksum formula."""
        # code omitted
        pass

    def __init__(self, first_name: str, last_name: str,
                 citizen_id: str):
        self.first_name = first_name
        self.last_name = last_name
        self.citizen_id = citizen_id

    def set_birthday(self, birthdate: date):
        self.birthday = birthdate

    def get_birthday(self):
        return self.birthday


class Student(Person):
    """A person studying at an educational institution."""
    pass
```


### 2. Add these classes to your UML Class Diagram

Show:
- relationships using the correct arrow type
- **multiplicity** on associations
- use standard UML notation, not Python notation.
  A Python `list[str]` is written as `str[*]` in UML.
- show `{readOnly}` after read-only (immutable) attributes

Don't Show:
- *don't show* implementation details like `dataclass` or `field()`
- *don't show* attributes & methods in subclass that are inherited from parent class, but not overridden

```python
class CourseList:
    """Courses that a student is enrolled in."""

    def __init__(self, student: Student):
        self.student = student
        # courselist consists of Enrollments for the student's courses
        self.enrollments: List[Enrollment] = []

    def add_course(self, course: Course):
        #TODO verify that student is not already enrolled in this course
        enroll = Enrollment(self.student, course)
        self.enrollments.add(enroll)

    def credits(self) -> int:
        """compute and return the total credits enrolled."""
        return sum(e.course.credits for e in self.enrollments)

# Course & Enrollment contain only attributes and standard
# methods for __eq__, __repr__, and __str__.
# Use a 'dataclass' to auto-generate standard code.
# Dataclass automatically generates constructor, __str__, __eq__, __repr__
from dataclasses import dataclass, field

@dataclass(frozen=true)  # Course attributes are immutable (read-only)
class Course:
    """A course in the university catalog."""
    # the attributes of a course
    course_id: str
    description: str
    credits: int
    # Dataclass auto-generates this constructor:
    #def __init__(self, course_id, description, credits):

    # Dataclass auto-generates these methods: 
    # __str__ and __eq__

@dataclass          # attributes are mutable
class Enrollment:
    """Enrollment represents a student taking a course, and records his grade."""
    student: Student
    course: Course
    # field() is how to specify a default value & behavior
    # field is an implementation detail, don't show it in UML
    grade: str = field(compare=False, default=' ')

    # Dataclass auto-generates this constructor:
    #def __init__(self, student, course, grade=' '):

    def __str__(self):
        """Override the default string of dataclass."""
        return f"{self.course.course_id} grade {self.grade}"
```

### 3. Discussion

3.1 In `Course` why name the course ID as `course_id`.  Why not just use `id`?
```python
class Course:
    id: str         # "id" means the course id number (obviously)
```

3.2 Why is `course_id` declared as `str`?  Shouldn't it be an `int`?
```python
class Course
    course_id: int
```

3.3 (Design Pattern) Why have separate classes for `Course` and `Enrollment`?  If we move the `grade` parameter to `Course`, then we can eliminate the `Enrollment` class.

---

### UML Quick Reference

Visual Paradigm Class Diagram Tutorial <https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/>

