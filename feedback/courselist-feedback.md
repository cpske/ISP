---
title: Feedback on Courselist Refactoring Problem
---

This is feedback on how the courselist problem graded.

| File                      | Point Value |
|:--------------------------|-------------|
| courselist.py             |      14     |
| enrollment.py             |  3 + 1 bonus|
| test_gpa.py               |      5      |
| Total                     |      22     |


In your `courselist.py` and `enrollment.py` files on Github, 
I added numbered comments for each of the refactoring items described below.
You can view the comments on Github, but please do not "push" anything
to the repository.

For example, if you got item #1 and #2 correct there will be comments like this:
```python
##1 correct
##2 correct
def compute_gpa(self):
    ...
```

### Refactoring in courselist.py

7 items worth **2 points** each.

1. `compute_gpa(self)` computes and returns the GPA for the entire course list. 
   - should not print anything
   - returns the gpa of the entire courselist, not just one course.
   - no parameters other than `self`

2. `compute_gpa(self)` calls `e.grade_points()` to get grade points for Enrollment `e` (you may have a different method name)
   - does not directly access `grade_point` enum
   - does not print anything

3. `get_total_credits(self)` sums and returns the earned credits for the course list.
   - does not print anything
   - returns the earned credits for the entire course list, not just one enrollment
   - no parameters other than `self`
   - OK use a different method name, but method name should be descriptive of what it actually does

4. `print()` does NOT compute the GPA itself. 
   - prints the list of courses using a loop
   - after the loop, calls `compute_gpa` and `get_total_credits`; does NOT compute the gpa or credits itself. 
   - must NOT call `compute_gpa` or `earned_credits` inside the loop over enrollments

5. `print()` replace `e.course.course_id` with `e.course_id` and add `course_id()` as a method or property in Enrollment.
   - OK to use a different name for `e.course_id`.
   - Wrong: copy `course.course_id` to an attribute in Enrollment

6. `compute_gpa` uses `e.has_grade()` instead of checking the grade directly.
   - Wrong: writing `if e.has_grade() and e.grade in Enrollment.grade_point` which is a duplicate test. The point of refactoring was to eliminate directly testing the grade.

7. remove duplicate code for find course from `add_course` & `drop_course`
   - 1 point for making a change in `drop_course` but not in `add_course`.
   - The most efficient solution is simply to call `get_enrollment`.
     ```python
     def drop_course(self, course_id) -> bool:
         enrollment = self.get_enrollment(course_id)
         if enrollment and not enrollment.grade:
             # can drop this course
             self.enrollments.remove(enrollment)
             return True
         return False
     
     def add_course(self, course) -> bool:
         if self.get_enrollment(course.course_id):
            # cannot enroll twice in same course
            return False
        self.enrollments.append(Enrollment(course))
        return True
     ```
   - If you wrote a new method to search for enrollment, then you must also move the try-except from `drop_course` and `get_enrollment` to the new method. 
   - No credit for simply moving the "next" expression to a new method without try-except. That forces all methods that call your method to write a try-except in their code, which is a form of logic coupling.  The `find_enrollment` or `get_enrollment` should handle all the logic for its job. The StopIteration exception is a detail of the implementation, so `find_enrollment` should handle the exeption. 
     ```python
     def find_enrollment(self, course_id) -> Enrollment:
         try:
             return next(e for e in self.enrollments if e.course_id == course_id)
         except StopIteration:
             # course_id not found in enrolled courses
             return None
     ```
   - Writing a new method is not a good solution. It does exactly the same thing as `get_enrollment`, as you can see in the code above.


### Refactoring in enrollment.py 

Each of these is worth 1 point.  Bonus 1 point for careful coding in 2nd item.

1. Move `grade_point` dictionary from Course to Enrollment.
   - It should be a **class attribute** like it was in Course. Not an instance attribute (in constructor) or a global variable.
   - 1/2 point if `grade_point` is instance attribute (in constructor).

2. `grade_points(self)` (or other method name) returns grade points for this enrollment.
   - should return a single floating point value for the grade points, or 0.
   - No parameter for grade. No credit if have a grade parameter on this method.
   - **Bonus 1 pt:** if check that the grade is in the `grade_point` dictionary before trying to access it:
   ```python
   # in Enrollment class
   def grade_points(self):
       if self._grade in Enrollment.grade_points:
           return self._course.credits * Enrollment.grade_points[self._grade]
       return 0.0
   ```
   - OK to implement this as a property.

3. `has_grade(self)` - True if has a grade in grade_point.
   - No parameter for grade.  Enrollment already knows the grade.
   - Must return **boolean**, not a number or a grade!
   ```python
   def has_grade(self):
       return self._grade in Enrollment.grade_point
   ```

### Unit tests is `test_gpa.py`

Worth 5 points: 1 point for each correct test case plus 1 point for correctly using unittest (not pytest).

To get credit, you must test that Courselist correctly computes the GPA by calling some method. 
- No credit for calling `courselist.print()` and then checking the value of a `gpa` attribute as a side effect.  Why?
  1. you should test behavior, not attributes which should be treated as private
  2. Courselist should not have a `gpa` attribute. It should compute the GPA as needed and only expose the method that computes the gpa.
  3. Having a `gpa` attribute means that sometimes the GPA is wrong! Consider this: 
     - you set the grade for some course in the courselist.
     - you then get the gpa.
     - since you didn't call `print()` or `compute_gpa()` or whatever, the `gpa` attribute has not been updated to incorporate the grade you just added.
     - requiring a caller to invoke some method before accessing some other value is called *temporal coupling* and often causes errors in software.

### Names of Accessors (`get_something`) and Properties (`something`)

A property is like a synthetic or computed attribute.  To the caller, it looks like an attribute of the object.

Property names should **not** be prefixed with "get".

| Property Name      | Accessor Method Name      |
|--------------------|---------------------------|
| `course_id`        | `get_course_id()`         |
| `grade_points`     | `get_grade_points()`      |

This makes it easier to **read** your code and easier to write using your code:

```python
## Using a property
total_points = sum(e.grade_points for e in self.enrollments)

## Using an accessor method
total_points = sum(e.get_grade_points() for e in self.enrollments)
```

If you apply this rule consistently, it will help reduce syntax errors.

### Examples of a Property for a Computed Attribute

In Enrollment, `grade_points` is an example of what could be a computed attribute. You compute the grade points for the enrollment whenever it is called. That way, `grade_points` always uses the current value of the grade.

Another example: a Sale consists of a bunch of items that a customer is buying. Sale computes the total price of the items whenever we invoke `sale.total` (a property), but Sale does not have a `total` attribute (that would be error-prone).

## Invoking Instance Method as a Class Method

In Enrollment, if you have a `has_grade` method like this:
```python
class Enrollment:

    def has_grade(self):
        return e._grade in Enrollment.grade_points
```
then this is an **instance method**. The behavior is associated with an object, and the result is different for different objects.  

You should invoke it by writing:
```python
if e.has_grade():
    # do something
```
but Python will let you invoke it using the class name and explicitly passing the object reference:
```python
# DON'T write code like this

if Enrollment.has_grade(e):
    # do something
```
in other O-O languages this syntax is illegal. Even though Python allows it, it is misleading and not O-O programming style.  Please avoid this.
