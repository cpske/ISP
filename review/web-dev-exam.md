## Topics on Web Programming Exam

In the programming exam, you will implement a simple web
application using Django, Flask, or Play Framework.

The application will probably include the following:

1. A Model class whose instances are saved to a database.
2. A form for users to input values to create a new instance of the Model.
3. Some validation of form data.
4. A screen that shows a list of all, or recent, model instances.
5. Some application logic applied to the model, such as displaying a summary report of model data.
6. Unit tests for the model and controllers.

It *may* include:

* A second Model class that is related to the first.

## Example

A Course Record application for a student, which records courses he has taken, semester, grade received, and credits for each course.

* The input form would be a screen for inputting a new Course.
* Data validation of input data would be validating that fields are not empty, credits is non-negative, and grade is valid.
* The list screen shows all courses, sorted by semester taken.
* The logic would be to compute the student's GPA.
* A unit test would be that the course list controller. Another unit test would be to test that GPA is computed correctly for several cases (e.g. withdraw with 'W' then retake the course).

A second Model class could be for course descriptions, so that the student doesn't have to manually input course data (id, description, credits). 

## Django

To implement this kind of app in Django, it is helpful to know how to use Django Forms, and how to write your own validators for Form fields.

