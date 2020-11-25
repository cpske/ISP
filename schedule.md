---
title: Schedule
navigation_order: 1
---

*This is an overview and may change. Details and weekly assignments are posted on Google Classroom.  You should do what is assigned on Google Classroom.*

### Links

* Scores for Google Classroom assignments (forms and docs uploaded to Classroom) are posted individually on Google Classroom
* <http://bit.ly/isp2020-scores> scores for other assignments, mostly coding
* <http://bit.ly/isp2020-ku-polls> evaluations for KU Polls 
* <http://bit.ly/isp2020-projects> list of team projects, scores, and feedback

### Week 1

* Introduction to course
* Introduction to software process
* Exercise: process description of an everyday process
  - [Write a Process Description for Everyday Project](/ISP/assignment/week1/general-process-exercise) 
  - [Submissions](https://classroom.google.com/u/1/c/MTM4MDk3MDY1NjM4/a/MTIyOTI1NjczMTM0/submissions/by-status/and-sort-name/all)
* Github Classroom review and practice accepting and doing an assignment.
* Skill assessment quiz - concepts and coding. Requires Github.

Assignment
* Complete [Sign-up form](https://forms.gle/fh9SqvmA9yPh1ur6A) for Github if you haven't done it yet
* [Install required software](/assignment/week1/signup-and-software)
* [Software Process Questions](https://docs.google.com/forms/d/e/1FAIpQLSd3FtoUtetMjd47M5TY9FYgK2TJvWwog44PzuEki6gFd3zsyQ/closedform) 
- [Software Process Homework](/assignment/week1/software-process-homework)

### Week 2 (17 Aug)

* Scrum
  - Watch [Scrum in Under 10 Minutes](https://www.youtube.com/watch?v=XU0llRltyFM) on Youtube
  - [Introduction to Scrum](/agile/scrum introduction) with links you should **read**
  - Read [Scrum Guide](https://www.scrumguides.org/scrum-guide.html) you should know, may be on quiz
* Version Control & Git - understanding git repos
* Common git use scenarios
* Git branches
* Git practice

Assignment
* Answer [Scrum Questions](https://docs.google.com/forms/d/e/1FAIpQLSccesC0cZCxaAmpOzgQ2EaOzYOZ9egDvrw54kUOwyFmqDJZeg/closedform) a Google Form
* Complete at least parts 1 & 2 of this tutorial: <https://learngitbranching.js.org/>
* Create a Github Repo of Git common usage with "how to" examples 
  - Starter code in Github Assignment: <https://classroom.github.com/a/q7wONzhR>

### Week 3 (24 Aug)

* **Preparation:** install netcat or ncat on your computer and TEST IT
  - <https://nmap.org/ncat/>
  - <https://eternallybored.org/misc/netcat/>
* Feedback on Week 1 assignments
* Intro to HTTP Protocol
* HTTP in Action: manually enter HTTP requests using netcat or ncat
* Git Remotes
* Git Merging and Conflict Resolution

Assignment
* [Command Line Basics](/assignment/week3/Command-Line-Basics.odt) you should know (nothing to submit) 
  - <https://drive.google.com/open?id=1igAYSBGdshgz1ESZOjcFwP0x-vCT-02CatdWEcVV7aQ&authuser=1>
* Add Git remote commands to your Git commands repo
  - [git-remote-commands](/assignment/week3/git-remote-commands)
* KU Polls write a vision and requirements 
  - [Assignment](/assignment/week3/ku-polls)
  - Background for Vision Statement: <https://cpske.github.io/ISP/assignment/ku-polls/vision>

### Week 4 (31 Aug)

* Quiz 1 (paper) and Quiz 2 (coding)
* Web app and web framework overview - general structure and operation
* Intro to Django
* Describe how to do KU Polls first iteration (Django Polls tutorial)
  - Create a wiki and how to refer to it in project README
  - Create a Project board (task board) and how to add issues as tasks
  - Using a task board on Github
  - Design the UI pages
  - Domain Model for Polls app - `Question` and `Choice` classes
  - Development work on a git branch (iteration1)
* Github Flow for managing work in git
  - if not enough time to cover in class then this is self-learning assignment

Assignment
* Github flow 
  - Read: https://cpske.github.io/ISP/git/index#github-flow
  - Questions on Github Flow: <https://forms.gle/HWLQ5retVNoquSJ38>
  - Copy of questions: https://cpske.github.io/ISP/assignment/week4/github-flow-questions
* KU Polls Iteration 1 (Django tutorial) - https://cpske.github.io/ISP/assignment/week4/ku-polls-iter1
  - submit work in your own `ku-polls` repo on Github.
  - use correct repo structure! No extra layer of directories.

### Week 5 (7 Sep)

* No class meeting due to Songkran
* Review progress on KU Polls iteration 1 (online)
* Start background work and proposal for course team project.

Assignment
* Work on KU Polls. Don't wait until due date to push code!
* (Not assigned in 2020) Questions about Agile coding based on PAD - agile-and-coding.md

### Week 6 (14 Sep)

* Django Review https://cpske.github.io/ISP/django/Django-review-1.pdf
* Unit testing https://cpske.github.io/ISP/testing/
  - link to slides in testing overview page on github.io
* Brief Introduction to Database
* Separate configuration from code - why and how
  - https://cpske.github.io/ISP/django/external-configuration
  - also called "externalize configuration", a 12-Factor App recommended practice
* Describe the Improvements to KU Polls for Iteration 2

Exercise
* Django Review Questions (answer online): https://forms.gle/zPuPzzt76QWboFZXA
* Database practice in class - view & describe schema and tables using sqlitebrowser or dBeaver
  - https://cpske.github.io/ISP/assignment/week6/database-exercise

Assignment
* Unit testing assignment to submit on Github Classroom 
  - <https://cpske.github.io/ISP/assignment/week6/unit-testing-assignment>
  - Auction class - AuctionTest.odt AuctionTest.pdf
  - Github Classroom assignment: <https://classroom.github.com/a/Tls2V5I9>
* [KU Polls Iteration 2](/assignment/ku-polls/iteration2.md)
  - add an `end_date` to polls, 
  - add methods `is_published`, `can_vote`
  - improve navigation by adding links to home page
  - add default landing page (redirect)
  - show all poll questions (not just 5)
* (Not assigned in 2020) Test another student's KU Polls - ku-polls-peer-testing.md

### Team Project

* Project Guidelines: <http://bit.ly/isp2020project-description>
* Proposal Template: <http://bit.ly/ISP-project-template>
* Project Spreadsheet: <http://bit.ly/ISP2020-projects> to submit your team and proposal link

### Week 7 (21 Sep)

* Testing in Django - how to test models, views, url dispatcher, and templates
  - https://cpske.github.io/ISP/testing/WebTesting.pdf
* Code Coverage tools for Python 
* Introduction to Object-Relational Mapping (ORM)
  - https://cpske.github.io/ISP/database/Persistence-and-ORM.pdf
* Review some past material and assignments

Exercise
* In class team exercise using Github Flow 
  - https://cpske.github.io/ISP/assignment/week7/kucafe-github-flow
  - team assignments in Google Docs spreadsheet (shown in class)
  - starter code (ku-cafe.zip) https://cpske.github.io/ISP/assignment/week7/ku-cafe.zip
* ORM Practice (optional) - interactively use Django's ORM commands to hack the U.S. presidential election
  - https://drive.google.com/open?id=10c6lLZwzyZU6UOKtw0zFUpIHLiWKPad2nOZpwarqHEE&authuser=1

Assignment
* Code Coverage: https://cpske.github.io/ISP/testing/code-coverage
* ORM modeling practice (optional) write Django models for a sales application 
  - https://cpske.github.io/ISP/assignment/orm/Modeling-Practice.pdf
  - Github Classroom Assignment: https://classroom.github.com/a/UOcT0BOr

### Midterm 28 Sep - 4 Oct

* Exam is 27 Sep (Sunday) rooms 202 and 203. Times: 9:00-12:00 and 13:00-16:00.
* Covers everything so far.
* Coding part will emphasize **unit testing** and **code quality**.
* Recommended OBS Video Settings: <https://drive.google.com/open?id=1xiDH6NImH0PAAZp5AUNWtJeLzlRSYoqiAOFE8wFS1vM&authuser=1>

### Week 8 (5 Oct)

* Code Quality, Coding Style, and Coding Standards
  - <https://cpske.github.io/ISP/code-quality>
  - coding style for Python (you learned this in Programming 1, I think)
* Comment style in Python 
  - there are 3 common standards for how to document parameters and returns
  - you can use either the Python standard or Google's standard (more concise)
  - use type hints to document data types instead of writing the data types in docstring comments on functions and methods
  - Read this:  <https://realpython.com/documenting-python-code/>
* Style checking tools, esp. pylint and flake8
  - <https://cpske.github.io/ISP/code-quality/code-quality-tools>
  - how to configure flake8. But it is *better* to fix your code rather than add special expections!
  - Pylint and/or Flake8 can be used inside an IDE, including Eclipse, Pycharm, and VS Code
  - the standard tool for Java is Checkstyle.  CPSKE has its own checkstyle rules.
* Automation and Continuous Integration
  - <https://cpske.github.io/ISP/automation/>

Exercise
* Perform style checking on BankAccount code (`bank_account` and `money`) until pylint gives you a 10.0 score. 
  - Also run flake8.
  - Push to **your own github account** (change the upstream)
* CI Practice - add Travis-CI and Codecov to demo-pyci
 - Instructions <https://cpske.github.io/ISP/automation/travis-demo-project>
 - Starter code <https://cpske.github.io/ISP/automation/demo-pyci.zip> 
* Guidelines for Team Projects

Assignment:
* Apply flake8 to KU Polls and fix all problems
   - use flake8 config file to exclude code that is not yours (migrations, django packages, virtual envs)
* Agile Practices (there will be quiz on this) 
  - Assignment: https://cpske.github.io/ISP/assignment/week8/agile 
  - Reading from *Practices of an Agile Developer* (read some "Tips" sections)
  - Online Questions: https://docs.google.com/forms/d/e/1FAIpQLSc5VqEqJIPk22gW_hL63ZvSxcdo0UgGt_d-vbxv9xAeumVNUg/viewform?authuser=1

### Week 9 (12 Oct)

* Individual Section: *Project or No Project?"
  - in view of the apathetic response to project work, each person can elect whether or not to do a project as part of graded work
* Review Bank testing problem from midterm
* Review CI assignment
* Code Quality
* What is "good code"?  
  - What goals, problems, and forces motivate what is considered "good" in code?
  - Visible metrics or characteristics
  - Specific principles and practies for good code
* Intro to Refactoring 
  - https://cpske.github.io/ISP/refactoring
  - https://cpske.github.io/ISP/refactoring/Refactoring.pdf (slides)
  - Reading: https://refactoring.guru/refactoring

Exercise
* Pizzashop refactoring exercise <https://github.com/ISP19/pizzashop>

Assignment
* Movie Rental Refactoring <https://classroom.github.com/a/_qGEboUn>

### Week 10 (19 Oct)

* [Authentication](/authentication/)

Exercise
* Add authentication to the Todo app
  - https://cpske.github.io/ISP/assignment/week10/auth-exercise
* Agile Practices Review
  - [Agile Practice Questions](/agile/agile-practice-questions.pdf)
  - [Crossword Puzzle](/agile/crossword-puzzle.pdf) 
  - answers available online

Assignment
* Refactor one of your projects or someone else's
  - <https://cpske.github.io/ISP/assignment/week10/refactoring>
* KU Polls Iteration 3 <https://cpske.github.io/ISP/assignment/ku-polls/iteration3>

### Week 11 (26 Oct)

* Quiz on Refactoring
* Review common refactorings - <https://cpske.github.io/ISP/refactoring/Refactoring-Review.pdf>
* More Refactoring - refactorings involving structure of classes, and refactorings for creating objects
* Logging (done in KU Polls Iter 3) - <https://cpske.github.io/ISP/logging/>

Assignment
* Movie Rental 2 - <https://cpske.github.io/ISP/assignment/week11/movie-rental2>


### Week 12 (2 Nov)

* Agile - Agile values, principles, and the practices.
  - values and mindset, not a software process

* Feedback on Team Projects
  - branches are not using Github Flow
  - prepare to demo your work so far
* More Refactoring
* "Why" refactoring and benefits, both in general and for specific refactorings.

### Week 13 (9 Nov)

* Software Reviews <https://cpske.github.io/ISP/code-review/>
* Project Demos

Assignment
* Read "Reviews" chapter from textbook by Stellman and Greene.
* Readings on Code Review Best Practices (read the links, not just my summary)
  - <https://cpske.github.io/ISP/code-review/code-review-best-practices>
* Create a Review Script and Checklist. Create in project wiki and add link from your project README.md

### Week 14 (16 Nov)

* Schedule dates for final exam and project presentations.
* Review Movie Rental refactoring problems.
* Static and Dynamic typing.
* Type hints in Python, how it helps find bugs and improve refactoring.
* Logging (briefly).
* Project demos.

Exercise
* Logging practice <https://cpske.github.io/ISP/logging/logging-practice>

Assignment
* Team assignment - create installation instructions for your project
* Individual assignment - install and run another team's project according to their instructions. Post issues for any problems in the instructions.

### Week 15 (23 Nov)

* The 12-Factor App, and 7 factors that app to projects
* The Testing Pyramid and End-to-End Testing
* Selenium for testing web applications in [Web Testing](testing/WebTesting.pdf)
  - [Intro to Selenium](testing/Selenium-into)

Exercise
* Scrape search results from DuckDuckGo using Selenium. Details in Web Testing presentation slides

Assignment
* Write an app to scan and test all links on a web page [Link Scanner](assignment/week15/selenium)

### Week 16 (30 Nov)

* "Why" refactoring and benefits, both in general and for specific refactorings.
* Review
* Bug Hunting - find problems in other teams' software

Assignment
* Try to find bugs in the deployed version of other team's projects.
