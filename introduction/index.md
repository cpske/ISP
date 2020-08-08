---
title: Introduction to ISP
---

Monday 10:00-12:00 and 13:00-16:00

Individual Software Process (ISP) covers the fundamentals of software process,
focusing on the knowledge and skills to be an effective software developer -- either solo or on a team.

The goals are:

1. Gain knowledge, skills, and habits to be an effective developer -- either solo or on a team
2. Ability to write good quality, correct, maintainable code
3. Understand software process fundamentals and their purpose.


Topics are listed on the [course index page](/ISP/) on github.io.
Topics include

* Introduction to Software Process Models and the purpose of a defined process
* Iterative and incremental development
* Writing good code that's testable and maintainable
* Coding standard and documenting code
* Good developer habits, esp. attention to detail and continual learning
* Version control as part of a work flow
* Testing
* Design and code reviews
* Refactoring existing software
* Automation of tests and deployment
* Estimating, planning, and tracking your work
* Develop *faster* by automating repetitive work and following a process

"Good code" includes consistently using a coding convention, documenting code, writing code that is readable and testable, reviewing, and updating (refactoring) code when needed.

*01219346 Software Process &amp; Project Management*
covers software process in more depth.  This course is aimed at 
learning skills for developers to "*build the product right*".

### Presentation

[Introduction to Course](Introduction-to-Course.pdf)     
[8 Recommendations to Developers (PDF)](Jomzap-Recommendations.pdf) ([ODP](Jomzap-Recommendations.odp) by Jomzaap Sittipithaya (จอมทรัพย์ สิทธิพิทยา), SKE graduate, entrepreneur, and co-founder of Exzy Corp, from his presentation at KU.    
[Advise from TaskWorld](TaskWorld-Advise) by SKE grads working at TaskWorld (software firm in Bangkok)

## Course Organization

Monday 10:00-12:00 and 13:00-16:00.

* Weekly Online Meeting 10:00-12:00 via Google Meet
  - Do students prefer Google Classroom &amp; Google Meet or Microsoft Teams?
* Occasional Live Class in E204.  Announced in advance.
* Weekly Lab 13:00-16:00 (online, for now)
* Quiz some weeks
* Weekly Assigned Reading and Problems. You must do the reading.
* Small Team Software Project
* All material will be online

Platform we will use, at least to start:

* [Google Classroom](https://classroom.google.com) for announcements, assignments, and discussion.  **Join** using course code **f2xplp**.
* Github Classroom for some assignments and quizzes. 
[Complete this form](https://forms.gle/9PW1L9Hsmx6ygHR9A) (https://forms.gle/9PW1L9Hsmx6ygHR9A) to tell us your Github ID.  You will be invited to join the Github "ISP2020" organization.
* Course Material on [cpske.github.io/ISP/](https://cpske.github.io/ISP/). Material is organized by topic (not sequentially). Click on topic link for summary and learning path. Some material is optional.

> Students usually don't need this, but the Github Classroom URL is
> https://classroom.github.com/classrooms/68801168-isp-2020

### Effort and Commitment

Plan to spend about 12 hours per week on ISP.

* 4-5 hours on Monday, another 6-8 hours at other times.
* read assigned material each week
* do exercises and assignments yourself, submit on-time
* write and review code regularly
* ask TAs and instructors for help, instead of other students.
  - other students don't know any more than you do
  - asking for help on assignments often borders on cheating
* Team Project: mostly in 2nd half of course. This may require extra time.

**Online Education Requires Discipline & Commitment**    

Most learners don't complete online courses.  They fall behind 
or drop out.  
Successful online learners **commit time and effort** to continue the course.

Learning takes time and consistent effort. You need to plan
your time, make a commitment, and have discipline.

### Software You Need

* IDE such as Eclipse, IntelliJ IDEA, NetBeans, or VS Code
* Python 3.6 or newer, Java JDK 8 or 11
* Good text editor (something better than Notepad). IDE is OK, but slow for editing a single file.
* Git command line client. Git GUI is also useful (most IDEs include it)


### Why a Team Software Project?

In this course you will design, implement, and deploy a web application
in a team of approx. 4 people.  You can choose the project topic, 
subject to approval by instructor.

Part of the challenge of creating software is working effectively
as a team.  Many of the skills we study involve other people, 
and are intended to improve team work.

Hence, we need a *team* project to practice both individual and project-related skills.
The project is also an opportunity to learn the basics of HTTP, web frameworks, and web application development.

Last year's students say that the project is the most valuable part of the course.


### Not a Powerpoint Course

Powerpoint slides are an aid to presentation.
They don't contain much depth and missing some important material. 

You must read the assigned material and learn from hands-on work 
for a real understanding.

If you only study "slides", you won't learn much and probably won't
pass the course.


## Prerequisites

* Programming ability equivalent to Programming 1 and 2, including object-oriented programming
* Know how to write code in Java and Python
* Ability to use Git and Github

If you have not *at least* worked through Prog 2, then you should take Prog. 2 before enrolling in this course. No one without Prog 2 background has *ever* passed this course (when I teach it).

## Grading

Your grade is based on    
- *quizzes and exams*
- *assignments*
- *participation in class*
- *project work and use of good software process*

The project score is based on how well you apply a process and your consistent contribution.  The final product is only a small part of the project score.

The approximate grading scale is:

| Overall Score | Grade |
|:-------------:|-------|
| 85 - 100      |   A   |
| 80 - 85       |   B+  |
| 75 - 80       |   B   |
| 70 - 75       |   C+  |
| 65 - 70       |   C   |
| 60 - 65       |   D+  |
| 55 - 60       |   D   |
|  0 - 55       |   F   |

**Minimum Exam Average**: 
You must achieve an overall average exam score of at least 50% to pass.


## Teaching Assistants (TAs)

[Mai Norapong](https://github.com/MaiNorapong) 	`email("Mai","Norapong",2)`

[Pakanon Pantisawat](https://github.com/pknn1) `email("Pakanon","Pantisawat",1)`

TA email, in Python and Java:

```python
DOMAIN = "ku.th"

def email(firstname: str, lastname: str, nlast: int = 1) -> str:
    """Return the email address for a KU person"""
    # "\u0040" is Unicode for 'at' symbol
    return f"{firstname}.{lastname[0:nlast]}\u0040{DOMAIN}"

if __name__ == '__main__':
    print("Contact Mai ", email("mai","norapong",2));
    print("Contact Pakanon ", email("pakanon","pantisawat",1));
```
---
```java
/**
 * Return the Email address for a KU person. Works only for Thai names.
 * @param first person's first name
 * @param last  person's last name
 * @param nlast number of chars from last name to use
 * @return email address, of course
 */
public static String email(String first, String last, int nlast) {
    final String DOMAIN = "ku.th";
    var sb = new StringBuilder();
    sb.append(first)
      .append(".")
      .append(last.substring(0,nlast))
      .append("\u0040")    // Unicode for 'at' symbol
      .append(DOMAIN);
    return sb.toString();
}

// you could use String.format instead of StringBuilder
```

*Why obfuscate email addresses?* 

Bots scrape web pages for email addresses (and login credentials!)
to create databases for spam and phishing.
