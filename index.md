---
title: Schedule
navigation_order: 1
---

> This schedule may change!    
> See **[Google Classroom][google-classroom]** for weekly material and assignments.
> You should do the assignments posted on Google Classroom.

[google-classroom]: https://classroom.google.com/c/MzczOTE1MjA0NDE4?cjc=ka25cph

#### Links

* [About the course](about) has links to Google Classroom & Github Classroom

---

### Schedule

### Preparation

Please do this before the course starts. Otherwise, do it in Week 1.

* [Sign-up, Survey, and Required Software](assignment/week1/signup-and-software)

### Week 1

* [Introduction to course](introduction/)
* [Introduction to software process](software-process/)
* Exercise: [Write a Process Description for an Everyday Project](assignment/week1/general-process-exercise) 
* [Using Github](git/Using-Github) & Github Classroom.
* Exercise: practice using Github Classroom
* Python Coding Style: [How to Write Beautful Python Code with PEP8](https://realpython.com/python-pep8/) on [Real Python](https://realpython.com/)
  - [How to Write Docstring Comments](code-quality/docstrings)
  - Example given in class
* Exercise: apply the Python coding standard
* Programming 2 Review, basic Python and O-O concepts.
* Exercise: Programming Skill Assessment


#### Assignment

- [Software Process Homework](assignment/week1/software-process-homework) assigned reading
- [Software Process Questions](https://forms.gle/M5RcqiDUh4NkFviW9) based on the reading


### Week 2

* [Scrum](agile/scrum)
  - Watch [Scrum in Under 10 Minutes](https://www.youtube.com/watch?v=XU0llRltyFM) on Youtube
  - [Introduction to Scrum](agile/scrum introduction) with links you should **read**
  - Read [Scrum Guide](https://www.scrumguides.org/scrum-guide.html). Anything in the Scrum Guide may be on a quiz.
* [Version Control & Git](git/) - understanding git repos
  - Common git use scenarios
  - [Git branches](git/branch-and-merge)
  - Exercise: use the [Git Visualizer](http://git-school.github.io/visualizing-git/) and complete parts 1-2 of [Learn Git Interactive](https://learngitbranching.js.org/). Section on *Moving Work Around* is recommended, too.

#### Assignment

* Answer [Scrum Questions](https://docs.google.com/forms/d/e/1FAIpQLSccesC0cZCxaAmpOzgQ2EaOzYOZ9egDvrw54kUOwyFmqDJZeg/closedform) a Google Form
* Complete at least parts 1 & 2 of this tutorial: <https://learngitbranching.js.org/>
* Create a Github Repo of Git common usage with "how to" examples 
  - Assignment with starter docs on Github Classroom: <https://classroom.github.com/a/q7wONzhR>

### Week 3

* **Preparation:** install ncat on your computer and TEST IT
  - ncat: <https://nmap.org/ncat/> a newer version of "netcat"
  - if you computer already has netcat then you can use that. In a command line shell try `netcat` or `nc` to see if its installed.
* Feedback on Week 1 assignments
* [Intro to HTTP Protocol](web/HTTP.pdf)
* [HTTP in Action](web/HTTP-in-Action.pdf): manually enter HTTP requests using netcat or ncat
* [Git Remotes](git/Git-Remotes.pdf)
* [Branch and Merge](git/branch-and-merge)
* [Git Merging and Conflict Resolution](git/Merge-and-Conflict-Practice.pdf)

#### Assignment

* [Command Line Basics](assignment/week3/Command-Line-Basics.odt) you should know (nothing to submit) 
  - <https://drive.google.com/open?id=1igAYSBGdshgz1ESZOjcFwP0x-vCT-02CatdWEcVV7aQ>
* Add Git remote commands to your Git commands repo
  - [git-remote-commands](assignment/week3/git-remote-commands)
* KU Polls project inception
  - [Assignment](assignment/week3/ku-polls) write a vision statement and requirements
  - Background for Vision Statement: <https://cpske.github.io/ISP/assignment/ku-polls/vision>

### Week 4

* Quiz 1 (paper) and Quiz 2 (coding)
* [Web app and web framework overview](web/index#web-frameworks) and [presentation](web/Web-Apps-and-Web-Servers.pdf)
* [Intro to Django](django/Intro-to-Django.pdf)
* How to do KU Polls first iteration (Django Polls tutorial)
  - Create a wiki and how to refer to it in project README
  - Create a Project board (task board) and how to add issues as tasks
  - Using a task board on Github
  - Design the UI pages
  - Domain Model for Polls app - `Question` and `Choice` classes
  - Development work on a git branch (iteration1)
* [Github Flow](git/index#github-flow) for managing work in git
  - if not enough time to cover in class then this is self-learning assignment

#### Assignment

* Github Flow 
  - Read: <https://cpske.github.io/ISP/git/index#github-flow> (read the files refered to in this page)
  - Answer questions online: <https://forms.gle/HWLQ5retVNoquSJ38>
  - Copy of questions: <https://cpske.github.io/ISP/assignment/week4/github-flow-questions>
* [KU Polls Iteration 1](assignment/week4/ku-polls-iter1) (Django Tutorial)
  - submit work in your own `ku-polls` repo on Github.
  - use correct repo structure! No extra layer of directories.

### Week 5

* No class meeting due to Songkran
* Review progress on KU Polls iteration 1 (online)
* Start background work and proposal for course team project.

#### Assignment

* Work on [KU Polls Iteration 1](https://cpske.github.io/ISP/assignment/week4/ku-polls-iter1). 
  - Don't wait until the due date to push code! That's a **poor development process**.
* (Not assigned in 2020) Questions about Agile coding based on PAD - agile-and-coding.md

### Week 6

* [Django Review](django/Django-review-1.pdf)
* [Unit Testing](testing/)
  - [Intro to testing](testing/Intro-to-Testing.pdf)
  - [Python Unit Testing](testing/PythonUnitTesting.pdf) my slides
  - [unittest](https://docs.python.org/3/library/unittest.html) in the official Python docs
* [Brief Introduction to Database](database/Database-Basics.pdf)
* [Separate configuration from code](refactoring/separate-configuration) - why and how
  - [slide presentation](refactoring/Separate-config-from-code.pdf)
  - also called "externalize configuration" 
  - a [12-Factor App](https://12factor.net/config) recommended practice
* Describe the Improvements to KU Polls for Iteration 2
* Exercise
  - Database practice in class: <https://cpske.github.io/ISP/assignment/week6/database-exercise>
  - View & describe database schema and tables using [sqlitebrowser][] or [dBeaver][]

[sqlitebrowser]: https://sqlitebrowser.org/
[dBeaver]: https://dbeaver.io/

#### Assignment

* Django Review Questions (answer online): <https://forms.gle/zPuPzzt76QWboFZXA>
* [Unit testing assignment](assignment/week6/unit-testing-assignment) to submit on Github Classroom 
  - Github Classroom assignment: <https://classroom.github.com/a/Tls2V5I9> contains starter code
  - Description of the [Auction class](assignment/week6/AuctionTest.pdf)
* [KU Polls Iteration 2](assignment/ku-polls/iteration2.md)
  - add an `end_date` to polls, 
  - add methods `is_published`, `can_vote`
  - improve navigation by adding links to home page
  - add default landing page (redirect)
  - show all poll questions (not just 5)
  - externalize configuration data and secrets
* (Not assigned in 2020) [Test another student's KU Polls](assignment/week6/ku-polls-peer-testing)

### Team Project

Submit a project proposal

* Project Guidelines: <http://bit.ly/isp2020project-description>
* Proposal Template: <http://bit.ly/ISP-project-template>
* Project Spreadsheet: <http://bit.ly/ISP2020-projects> to submit your team and proposal link

### Week 7

* [Testing in Django](testing/WebTesting.pdf) - how to test models, views, url dispatcher, and templates
* [Code Coverage tools](testing/code-coverage) for Python 
* [Introduction to Object-Relational Mapping](database/Persistence-and-ORM.pdf)
(ORM)
* Review some previous material and assignments
* Exercise: In class team exercise using Github Flow 
  - <https://cpske.github.io/ISP/assignment/week7/kucafe-github-flow>
  - Team assignments in Google Docs spreadsheet (shown in class)
  - Starter code (ku-cafe.zip) <https://cpske.github.io/ISP/assignment/week7/ku-cafe.zip>
* ORM Practice - interactively use Django's ORM commands to hack the U.S. presidential election
  - <https://drive.google.com/open?id=10c6lLZwzyZU6UOKtw0zFUpIHLiWKPad2nOZpwarqHEE&authuser=1>

#### Assignment

* Add Code Coverage to KU Polls
* ORM modeling practice (optional) write Django models for a sales application 
  - Github Classroom Assignment: <https://classroom.github.com/a/UOcT0BOr>
  - Instructions: <https://cpske.github.io/ISP/assignment/orm/Modeling-Practice.pdf>

### Midterm 

* Exam is XX Septemer rooms 202 and 203. Times: TBA
* Covers everything so far.
* Coding part will emphasize **unit testing** and **code quality**.
* Recommended OBS Video Settings: <https://drive.google.com/open?id=1xiDH6NImH0PAAZp5AUNWtJeLzlRSYoqiAOFE8wFS1vM&authuser=1>

### Week 8

* [Code Quality, Coding Style, and Coding Standards](code-quality)
  - coding style for Python (you learned this in Programming 1, I think)
* [Comment style in Python](code-quality/comments)
  - there are 3 common standards for how to document parameters and returns
  - you can use either the Python standard or Google's standard (more concise)
  - use type hints to document data types of parameters and return values, instead of writing the data types in docstring comments
  - Read this: <https://realpython.com/documenting-python-code/>
* Style checking tools, esp. pylint and flake8
  - <https://cpske.github.io/ISP/code-quality/code-quality-tools>
  - How to configure flake8 -- but it is *better* to fix your code rather than add exceptions to flake8!
  - Pylint and Flake8 can be used inside an IDE, including Eclipse, Pycharm, and VS Code
  - The style-checking tool for Java is [Checkstyle][].  CPSKE has its own checkstyle rules.
* [Automation and Continuous Integration](automation/)
* Guidelines for Team Projects
* Exercise
  - Use pylint and modify coding style in BankAccount code (`bank_account` and `money`) until pylint gives you a score 10.0. 
  - Also run flake8.
  - Push code to **your own github account** (change the upstream URL first)
    1. create an empty `banking` repo on Github
    2. in your local repo: `git remote set-url origin https://github.com/your_account/banking.git`
* Exercise using CI - add Travis-CI and Codecov to demo-pyci
  - Instructions <https://cpske.github.io/ISP/automation/travis-demo-project>
  - Starter code <https://cpske.github.io/ISP/automation/demo-pyci.zip> 

[Checkstyle]: https://checkstyle.org/index.html

#### Assignment

* Apply flake8 to your KU Polls code and fix all problems
   - use flake8 config file to exclude code that is not yours (migrations, django packages, virtual envs)
* [Agile Practices](assignment/week8/agile) (there will be quiz on this) 
  - Read tips from *Practices of an Agile Developer* ("Tips" sections in assignment)
  - Online Questions: <https://docs.google.com/forms/d/e/1FAIpQLSc5VqEqJIPk22gW_hL63ZvSxcdo0UgGt_d-vbxv9xAeumVNUg/viewform?authuser=1>
* [Add CI to KU Polls](assignment/week8/ku-polls-ci-assignment)
  - Use CI to run unit tests and run code coverage
  - Add "badges" to your KU Polls README.md for Travis and CodeCov status
  - Sites with *insane* number of badges: [Checkstyle](https://github.com/checkstyle/checkstyle)

### Week 9

* Individual Selection: *Project or No Project?*
  - in view of the apathetic response to project work, each person can elect whether or not to do a project as part of graded work
* Review Bank testing problem from midterm
* Review CI assignment
* Code Quality
* What is "good code"?  
  - What goals, problems, and forces motivate what is considered "good" in code?
  - Visible metrics or characteristics
  - Specific principles and practies for good code
* [Intro to Refactoring](refactoring/)
  - [slides](refactoring/Refactoring.pdf)
  - Reading: <https://refactoring.guru/refactoring> 
* Anything on <https://refactoring.guru/refactoring> may be on a quiz!
* Exercise
  - Pizzashop refactoring exercise <https://github.com/ISP19/pizzashop>

#### Assignment

* Movie Rental Refactoring <https://classroom.github.com/a/_qGEboUn>, Part 1

### Week 10

* [Authentication](/authentication/)
* Authentication Exercise: [Add authentication to the Todo app](assignment/week10/auth-exercise)
* Agile Practices Review
  - [Agile Practice Questions](agile/agile-practice-questions.pdf)
  - [Crossword Puzzle](agile/crossword-puzzle.pdf) 
  - answers available online

#### Assignment

* *Refactor* one of your projects or someone else's
  - <https://cpske.github.io/ISP/assignment/week10/refactoring>
* [KU Polls Iteration 3](assignment/ku-polls/iteration3)

### Week 11

* Quiz on Refactoring
* [Review common refactorings](refactoring/Refactoring-Review.pdf)
* More Refactoring - refactorings involving structure of classes, and refactorings for creating objects
* [Logging](logging/) - you already did in KU Polls Iter 3
* [Logging practice](logging/logging-practice)

#### Assignment

* [Movie Rental Refactoring, Part 2](assignment/week11/movie-rental2)


### Week 12

* Agile - Agile values, principles, and the practices.
  - values and mindset, not a software process

* Feedback on Team Projects
  - branches are not using Github Flow
  - prepare to demo your work so far
* More Refactoring
* "Why" refactoring and benefits, both in general and for specific refactorings.

### Week 13

* [Software Reviews](code-review/)
* Project Demos

#### Assignment

* Read "Reviews" chapter from textbook by Stellman and Greene.
* Read Code Review Best Practices (read the links, not just my summary)
  - <https://cpske.github.io/ISP/code-review/code-review-best-practices>
* [Create a Code Review Script and Checklist](assignment/week13/code-review). 
  - Write them in your project wiki and add links from your project README.md

### Week 14

* Schedule dates for final exam and project presentations.
* Review Movie Rental refactoring problems.
* Static and Dynamic typing.
* [Type hints](type-hints/) in Python to find bugs and improve refactoring.
* [Logging](logging/) (briefly).
* Project demos.

#### Assignment

* Team assignment: create installation instructions for your project
* Individual assignment: [install and run another team's project](assignment/week15/installation-testing)
  - Post issues for any problems in their installation instructions.
  - Goal is to find problems with installation and setup, not in the application itself (that is next week's Bug Bounty assignment).

### Week 15

* The [12-Factor App](web/12FactorApp.pdf) - 7 factors that apply to your projects
* The Testing Pyramid and End-to-End Testing in [Web Testing](testing/WebTesting.pdf)
* [Selenium](testing/Selenium-intro) for testing web applications in [Web Testing](testing/WebTesting.pdf)
* [Selenium Exercise](testing/SeleniumExercise.pdf) scrape search results from DuckDuckGo

#### Assignment

* [Link Scanner](assignment/week15/selenium) write an app to scan and test all links on a web page 
* Team Assignment: deploy your application to a cloud service


### Week 16

* "Why" refactoring and refactoring benefits, both in general and for specific refactorings.
* Review
* Bug Hunting - find problems in other teams' software

#### Assignment

* [Bug Bounty](assignment/week15/bug-bounty) - try to find bugs in deployed projects of other teams 
  - URLs of deployed projects are shown in Google Sheet for Project Testing
  - Top bug hunters will earn extra assignment points
