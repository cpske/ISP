---
title: Schedule
navigation_order: 1
---

*This is an overview and may change. Details and weekly assignments will be posted on Google Classroom.*

### Links

* [http://bit.ly/isp2020-scores](http://bit.ly/isp2020-scores) scores for some assignments
* Scores for Google Classroom assignments (forms) are posted individually on Google Classroom
* [http://bit.ly/isp2020-ku-polls](http://bit.ly/isp2020-ku-polls) evaluations for KU Polls 
* [http://bit.ly/isp2020-projects](http://bit.ly/isp2020-projects) list of team projects and feedback

### Week 1

* Introduction to course
* Introduction to software process
* Exercise on processes
* Complete [Sign-up form](https://forms.gle/fh9SqvmA9yPh1ur6A) if you haven't done it yet
* Github Classroom review and practice
* Skill assessment quiz - concepts and coding. Requires Github.

### Week 2 (17 Aug)

* Scrum
* Version Control & Git - understanding git repos
* Common git use scenarios
* Git branches
* Git practice

### Week 3 (24 Aug)

* **Preparation:** install netcat or ncat on your computer
* Intro to HTTP Protocol
* HTTP in Action: manually enter HTTP requests using netcat or ncat
* Git Remotes
* Git Merging and Conflict Resolution
* Assignment: vision and requirements for KU Polls

### Week 4 (31 Aug)

* Web app and web framework overview - general structure and operation
* Intro to Django
* Homework: KU Polls first iteration (Django Polls tutorial)
  - Create an Iteration Plan
  - Use a task board on Github
  - Design the UI pages
  - Domain Model for Polls app - `Question` and `Choice` classes
  - Development work on a git branch (iteration1)
* Github Flow for managing work in git
  - if not enough time, this is for self-learning
  - online questions in Google Form

### Week 5 (7 Sep)

* No class meeting due to Songkran
* Review progress on KU Polls iteration 1 (online)
* Start background work and proposal for course team project.

### Week 6 (14 Sep)

* Unit testing!
* Introduction to Database
* Improvements to KU Polls
* Separate configuration from code
* Assignment: KU Polls iteration 2
* Assignment: Unit testing

### Week 7 (21 Sep)

* Unit testing in Django - how to test models, views, and UI
* Introduction to ORM
* Code Coverage tools for Python
* Review

### Midterm 28 Sep - 4 Oct

* Exam is 27 Sep (Sunday) rooms 202 and 203. Times: 9:00-12:00 and 13:00-16:00.
* Covers everything so far.
* Coding part will emphasize **unit testing** and **code quality**.

### Week 8 (5 Oct)

* Agile - Agile values, principles, and the practices.
  - values and mindset, not a software process
* Code Quality: coding style and coding convention.
* Comment style in Python 
  - there are 3 common standards for how to document parameters and returns
  - you can use either the Python standard or Google's standard (more concise)
  - use Type Hints in code to document data types instead of writing the data types in comments
  - Read this:  https://realpython.com/documenting-python-code/
* Style checking tools
  - pylint
  - flake8
  - how to configure flake8. But its *better* to fix your code than configure special rules.
  - pylint and/or flake8 can be used inside an IDE, including Eclipse, Pycharm, and VS Code
  - the standard tool for Java is CheckStyle.  KU even has its own checkstyle rules (on the skeoop.github.io site).
* Exericse: perform style checking on BankAccount code (`bank_account` and `money`) until pylint gives you a 10.0 score.
* Continuous Integration
* CI Exercise: 
  - Python:  demo-pyci
  - Java: demo-ci
* Guidelines for Team Projects

Assignment:
1. Apply flake8 to KU Polls and fix all problems
   - use flake8 config to exclude code that is not yours (migrations, django packages, virtual envs)
2. Add CI to KU Polls

### Week 9

* Review: CI assignment
* Code Quality
* What is "good code"?  What goals, problems, and forces motivate what is considered desirable (characteristics) in code?
* Specific principles and practies for good code
* Visible metrics or characteristics
* Intro to Refactoring 
  - https://cpske.github.io/ISP/refactoring/Refactoring.pdf
  - Reading: 
* Pizzashop refactoring exercise https://github.com/ISP19/pizzashop

### Week 10

* Refactoring


### Week 11

* More Refactoring - higher level refactorings involving structure of classes, and refactorings for creating objects

### Unscheduled

* Guidelines and Practices for Writing Better Code
* Refactoring
