## UML Exercises

These exercises use Java notation for code.
In Python some methods would be different, and you can have

1. Draw a UML class diagram of the Student class.
    
    A Student has a firstname, lastname, studentID, and email.
|Method   |Description   |
|---------|--------------|
|Student(String first,String last)|Constructor for a new student. ID is assigned automatically.  |
|setEmail(String email)| Set the email. |
|setId(Long studentId) | Set the student id. |
|boolean equals(Object other)|Test if two Students have same value.|
|String toString() | Get a string representation of this Student.|

We don't show "get" methods since they are pretty obvious and usual. Adds clutter to the diagram without conveying using info.

2. Draw a UML class diagram of the Course class.
    A Course has a course ID (courseId) and a bunch of enrolled students.
    A Course may have a max number of students, otherwise enrollment is unlimited.
    You must infer the return type of some methods.
    The methods are:

|Method   |Description   |
|---------|--------------|
|Course(String id)|Constructor for a new course.  No limit on enrollment. |
|Course(String id, int max)|Constructor for a new course with max allowed enrollment. |
|getCourseId()   |Get the course number.   |
|setMaxEnrollment()|Get the max enrollment. |
|Student[] getStudents()|Get enrolled students.|
|boolean addStudent(Student)| Enroll a student. Returns true if succeeds.|
|boolean removeStudent(Student)| Remove a student from course. Returns true if student is removed. false if no matching student.|
|getNumberEnrolled() | Return number of enrolled students.|
