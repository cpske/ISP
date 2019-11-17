
[Python Collection Base Classes](https://docs.python.org/3/library/collections.abc.html) in the package `collections.abc`.
* Names of collections and the key methods they provide
* "abc" means Abstract Base Class

[Python `typing` Package](https://docs.python.org/3/library/typing.html)
* Names of type hints you can use to designate Python types


### Type Hints Applied to Classes

You can use type hints to convey the meaning of "*provides a behavior*".
In languages like Java or C-sharp this would be "*implements an interface*".

* A class named `MyIterable` has an `__iter__` method that can be used to create an iterator, or as the data source in a `for x in data` statement.

```python
from typing import Iterable, Iterator

class MyIterable(Iterable):
   ...

   def __iter__(self) -> Iterator:
      """This method should return an Iterator.
         Code that wants an iterator will call iter(obj)
         to create one.
      """
      pass
```

* If `MyIterable` returns an `Iterator` whose values are (say) `int`, you can aid type checking by specifying this using the notation `Iteratable[type]`:

```python
from typing import Iterable, Iterator

class MyIterable(Iterable[int]):
   def __init__(self):
       self.data = range(0,10)

   def __iter__(self) -> Iterator[int]:
      """This method should return an Iterator.
         Code that wants an iterator will call iter(obj)
         to create one.
      """
      # create an iterator from a range
      return iter(self.data)
```

* A class has a `__len__` method that returns the "length" or "size" of the object. In Python code, this means you can write `len(obj)`.  The `typing` package defines a `Sized` type for this:

```
from typing import Sized

class CourseList(Sized):
    """List of courses taken by a student"""

    def __init__(self, student_id):
        self.student_id = student_id
        self.courses = []

    def add_course(self, course: Course):
        self.courses.append(course)

    def __len__(self):
        return len(self.courses)
```

