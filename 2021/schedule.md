---
title: Schedule
navigation_order: 1
---

> This schedule may change!    
> See **[Google Classroom][google-classroom]** for weekly material and assignments.    
> You should do the assignments posted on [Google Classroom][google-classroom].

[google-classroom]: https://classroom.google.com/c/NDk2ODk1MDE0NTgy?cjc=r3466kb

---

### Schedule

#### Preparation

Please do this before the course starts. Otherwise, do it in Week 1.

* [Sign-up and Install Required Software](assignment/week1/signup-and-software)
* Read [About the course](about) for essential class resources & how to contact TAs.


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
  - [Introduction to Scrum](agile/scrum) with links you should **read**
  - Read [Scrum Guide](https://www.scrumguides.org/scrum-guide.html). Anything in the Scrum Guide may be on a quiz.
* [Version Control & Git](git/) - understanding git repos
  - Common git use scenarios
  - [Git branches](git/branch-and-merge)
  - Exercise: use the [Git Visualizer](http://git-school.github.io/visualizing-git/) and complete parts 1-2 of [Learn Git Interactive](https://learngitbranching.js.org/). Section on *Moving Work Around* is recommended, too.

#### Assignment

* Answer [Scrum Questions](https://docs.google.com/forms/d/e/1FAIpQLSccesC0cZCxaAmpOzgQ2EaOzYOZ9egDvrw54kUOwyFmqDJZeg/closedform) a Google Form
* Complete at least parts 1 & 2 of this tutorial: <https://learngitbranching.js.org/>
* Create a Github Repo of Git "how to" answers.  Assignment on Github Classroom: <https://classroom.github.com/a/q7wONzhR>
* Create a Burn-down chart for a Sprint. Details on Google Classroom.


### Week 3

* **Preparation:** install ncat on your computer and TEST IT: <https://nmap.org/ncat/>.
* Feedback on Week 1 assignments
* [Git Remotes](git/Git-Remotes.pdf)
* [Branch and Merge](git/branch-and-merge)
* [Git Merging and Conflict Resolution](git/Merge-and-Conflict-Practice.pdf)
* [Intro to TCP/IP and HTTP Protocol](web/index), [presentation](web/HTTP.pdf)
* Exercise: [HTTP in Action](web/HTTP-in-Action.pdf). Manually enter HTTP requests and responses using ncat.

#### Assignment

* [Command Line Basics](assignment/week3/Command-Line-Basics.odt) you should know (nothing to submit) 
  - <https://drive.google.com/open?id=1igAYSBGdshgz1ESZOjcFwP0x-vCT-02CatdWEcVV7aQ>
* Add Git remote commands to your Git commands repo
  - [git-remote-commands](assignment/week3/git-remote-commands)
* [KU Polls Project Inception](assignment/week3/ku-polls), initialize `ku-polls` repo, write a vision statement and requirements
  - Background for Vision Statement: [vision](assignment/ku-polls/vision)


### Week 4

* [Web app and web framework overview](web/index#web-frameworks) and [presentation](web/Web-Apps-and-Web-Servers.pdf)
* [Intro to Django](django/Intro-to-Django.pdf)
* How to do KU Polls first iteration (Django Polls tutorial)
  - Domain Model for Polls app - `Question` and `Choice` classes
  - Create a Project board (task board) and how to add issues as tasks
  - Creating tasks from issues
  - Design the UI pages
  - Development work on a git branch named `iteration1`
* [Github Flow](git/index#github-flow) for managing work in git
  - if not enough time to cover in class then this is self-learning assignment

#### Assignment

* [KU Polls Iteration 1](assignment/ku-polls/iteration1) (Django Tutorial)
  - submit work in your own `ku-polls` repo on Github.
  - use correct repo structure! No extra layer of directories.


### Week 5

* Review progress on KU Polls iteration 1.
* [Intro to Testing](testing/)
  - [Python Unit Testing](testing/PythonUnitTesting.pdf) my slides
  - [unittest](https://docs.python.org/3/library/unittest.html) in the official Python docs
* Exercise: unit testing (unittest-start)
* Intro to Team Projects. 
* [Django Review](django/Django-review-1.pdf)
* Describe the Improvements to KU Polls for Iteration 2
  - add an `end_date` to polls, 
  - add methods `is_published`, `can_vote`
  - improve navigation by adding links to home page
  - add default landing page (redirect)
  - externalize configuration data and secrets

#### Assignment

* (Not assigned in 2020) Questions about Agile coding based on PAD - agile-and-coding.md
* Start background work and proposal for course team project.
* Read about Github Flow 
  - [Github Flow Illustrated Guide](https://guides.github.com/introduction/flow/)
  - [Detailed Description of Github Flow](http://scottchacon.com/2011/08/31/github-flow.html) Step #5: merge only after pull request review is important. I don't agree with Step #6: deploy immediately.
* Read about Pull Requests
  - [Pull Request Tutorial](https://yangsu.github.io/pull-request-tutorial/) and why to use pull requests on Github.  The section "Squash, Rebase, and Cherry Pick" is optional.
  - [Commenting on Pull Requests](https://help.github.com/en/articles/commenting-on-a-pull-request) how to provide useful feedback to a Pull Request. Shows how to add comments that refer to code.
* Answer Questions about Github Flow and Pull Requests
  - Google Form: <https://forms.gle/HWLQ5retVNoquSJ38> (old version)
  - Copy of questions: <https://cpske.github.io/ISP/assignment/week4/github-flow-questions> (not all questions included)
* [KU Polls Iteration 2](assignment/ku-polls/iteration2.md)


### Week 6

* Some Django review. Using the Django interactive console.
* [Separate configuration from code](refactoring/separate-configuration) - why and how
  - [Presentation](refactoring/Separate-config-from-code.pdf)
  - a [12-Factor App](https://12factor.net/config) recommended practice, also called "externalize configuration" 
  - Simple example: <https://github.com/ISP21/decouple-example>
* Review Github Flow
* Exercise: team practice using Github Flow 
  - <https://cpske.github.io/ISP/assignment/week6/kucafe-instructions>
  - Team assignments: **URL will be given in class**
* Testing Assignmemt: [Auction Test Assignment](assignment/week6/unit-testing-assignment) on Github Classroom (**URL given in class**)
  - Requirements for the [Auction class](assignment/week6/AuctionTest.pdf)
  - Should be completed during lab this afternoon.

* Introduction to Database - *this may be moved to week 7 if not enough time*
  - [Brief Introduction to Database](database/Database-Basics.pdf)
* Database Exercise
  - Database practice in class: <https://cpske.github.io/ISP/assignment/week6/database-exercise> <!-- should be week7 -->
  - View & describe the KU Polls database schema using a database browser.

#### Assignment

* Django Review Questions (answer online): <https://forms.gle/zPuPzzt76QWboFZXA>
* (Not assigned in 2021, but a good thing to do) [Test another student's KU Polls](assignment/week6/ku-polls-peer-testing)


### Team Project

Submit a project proposal using the Project Spreadsheet

* Project Guidelines: <http://bit.ly/ISP-project-description>
* Proposal Template: <http://bit.ly/ISP-project-template>
* Project Proposals: 
  * <http://bit.ly/ISP2021-projects> to submit your team and proposal
  * <http://bit.ly/ISP2020-projects> last year's proposals


### Week 7

* [Testing in Django](testing/WebTesting.pdf) - how to test models, views, url dispatcher, and templates
* [Code Coverage tools](testing/code-coverage) for Python 
* Exercise: apply code coverage
* [Introduction to Object-Relational Mapping](database/Persistence-and-ORM.pdf) - how Django provides the CRUD operatons
* ORM Practice - interactively use Django's ORM commands to hack the U.S. presidential election
  - <https://drive.google.com/open?id=10c6lLZwzyZU6UOKtw0zFUpIHLiWKPad2nOZpwarqHEE&authuser=1>
* Review some previous material and assignments

#### Assignment

* Add Code Coverage to KU Polls
* ORM modeling practice (optional) write Django models for a sales application 
  - Github Classroom Assignment: <https://classroom.github.com/a/UOcT0BOr>
  - Instructions: <https://cpske.github.io/ISP/assignment/orm/Modeling-Practice.pdf>

### Midterm 

* Exam is 27 September. Time and Location TBA.
* Covers everything so far.
* Coding part will emphasize **unit testing** and **code quality**.
* Recommended OBS Video Settings: <https://drive.google.com/open?id=1xiDH6NImH0PAAZp5AUNWtJeLzlRSYoqiAOFE8wFS1vM&authuser=1>
  - We may not need this is 2021 if we can use KU's Exam application.


### Week 8

* [Code Quality, Coding Style, and Coding Standards](code-quality)
  - coding style for Python. Already covered in week 1.
* [Comment style in Python](code-quality/index)
  - there are 3 common standards for how to document parameters and returns
  - for graded work, please use the Python standard style or Google's standard, which is more concise
  - for data type of parameters and return values: use [type hints](type-hints/) instead of writing the data type in comments!
* Read: "Documenting Python Code" <https://realpython.com/documenting-python-code/>
* Style checking tools. We will use pylint and flake8.
  - <https://cpske.github.io/ISP/code-quality/code-quality-tools>
  - How to configure flake8 -- but it is *better* to fix your code rather than add exceptions to flake8!
  - For graded assignments you cannot customize flake8, unless the explicitly allowed.
* Style Checking Exercise:
  1. How do you view or change the style rules in your IDE?
  2. Use pylint to correct some code (may use banking app or person). Modify code until you get a score of 10.
  3. Use flake8 to correct some code. Modify code until no messages from flake8.
* For Java, the standard tool is [Checkstyle][Checkstyle].  CPSKE has its own checkstyle rules.
* Guidelines for Team Projects
* [Automation and Continuous Integration](automation/)
* Exercise using CI - add Travis-CI and Codecov to demo-pyci project
  - Instructions <https://cpske.github.io/ISP/automation/travis-demo-project>
  - Starter code (to be added) 
[CI starter code]: <https://cpske.github.io/ISP/automation/demo-pyci.zip> 

[Checkstyle]: https://checkstyle.org/index.html

#### Assignment

* Apply flake8 to your KU Polls code and fix all problems
   - use flake8 config file to exclude code that is not yours (migrations, django packages, virtual envs)
* [Add CI to KU Polls](assignment/week8/ku-polls-ci-assignment)
  - Use CI to run unit tests and run code coverage
  - Add "badges" to your KU Polls README.md for Travis and CodeCov status
  - Site has **lots** of badges: [Checkstyle](https://github.com/checkstyle/checkstyle)


### Week 9

* Review CI assignment
* What is "good code"?  
  - The goal of refactoring is "good code". So, what is good code?
  - Goals, problems, and forces motivate characteristics of "good" code
  - Visible metrics or characteristics
  - Principles and practies for good code
* [Introduction to Refactoring](refactoring/) and [slides](refactoring/Refactoring.pdf)
  - "Why" refactoring and the benefits, both in general and for specific refactorings
* Refactoring Exercise: Pizzashop refactoring <https://github.com/ISP19/pizzashop>
* Anything on <https://refactoring.guru/refactoring> may be on a quiz!
* User Stories - write stories for team projects

#### Assignment

* Read <https://refactoring.guru/refactoring> 
* Movie Rental Refactoring <https://classroom.github.com/a/_qGEboUn>, Part 1
* Read the articles in [Agile Practices](assignment/week9/agile-practices) (there will be quiz on this) 
* Read tips from *Practices of an Agile Developer* ("Tips" sections in assignment)


### Week 10

* Discussion on Team Projects 
  - how to get started, prioritizing work, meetings with TAs
* Refactoring Practice - refactor some code on Github (link on Google Classroom)
* [Agile](agile/agile) - Agile values, principles, and the practices.
  - conists of values and mindset, not a software process
* Exercise: [Agile Practice Review Questions](agile/agile-practice-questions.pdf)
* Optional: [Agile Crossword Puzzle](agile/crossword-puzzle.pdf) 
  - answers available online
* Homework: essential reading on Agile
  - read "Learn More" articles in [Agile](agile/agile#learn-more)

#### Assignment

* (Not in 2021) *Refactor* one of your projects or someone else's
  - <https://cpske.github.io/ISP/assignment/week10/refactoring>


### Week 11

* [Authentication](authentication)
* Authentication Exercise: 
  - 2021: Add authentication to KU Polls
    1. Discuss and plan the feature
    2. Create a new branch for your work
    3. Add authentication. See [Django Authentication](django/authentication)
    4. Create one or two users
    5. Write tests
    6. Add authorization to KU Polls. See [Django Authorization](django/authorization)
    7. Test it
    8. Revise the KU Polls domain model
    9. Implement the changes to the domain model
  - 2020: [Add authentication to the Todo app](assignment/week11/auth-exercise-todo)

#### Assignment

* [KU Polls Iteration 3](assignment/ku-polls/iteration3)


### Week 12

* [Review common refactorings](refactoring/Refactoring-Review.pdf)
* More Refactoring - involving structure of classes, or for creating objects
  - [Refactoring Patterns](refactoring/Refactoring-Patterns.pdf)
* [Type Checking](code-quality/Type-Checking.pdf)
* Type Checking Exercise: [scorecard.py](type-hints/scorecard.py)
* [Type Hints](type-hints)
  - Another [Type Hints Intro](https://fastapi.tiangolo.com/python-types/) on FastAPI; really good, simple examples.
* [Type Hints Practice](type-hints/type-hints-practice.doc)
* [Logging](logging/) - you already did in KU Polls Iteration 3
* [Logging practice](logging/logging-practice)


Assignment:

- [Movie Rental Refactoring, Part 2](assignment/week12/movie-rental2)
- Team Projects: prepare to demo your work next week


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

* Final exam date. Schedule date(s) for project presentations.
* The [12-Factor App](web/12FactorApp.pdf) - 7 factors that apply to your projects
* Review some Agile Practices (week 10 assignment), including comments in code.
* Review Movie Rental refactoring problems.
* Remaining project demos.
* Testing Pyramid and End-to-End Testing in [Web Testing](testing/WebTesting.pdf)
* [Selenium](testing/Selenium-intro) for testing web applications. Some slides in [Web Testing](testing/WebTesting.pdf)
* [Selenium Exercise](testing/SeleniumExercise.pdf) scrape search results from DuckDuckGo

#### Assignment

* [Link Scanner](assignment/week15/selenium) write an app to scan and test all links on a web page 
* Team assignment: 
  1. create installation instructions for your project
  2. use a virtualenv for local installation
* Team Assignment: deploy your application to a cloud service


### Week 15

* Review
* Bug Hunting - find problems in other teams' software

#### Assignment

* Individual assignment: [install and run another team's project](assignment/week15/installation-testing)
  - Post issues for any problems in their installation instructions.
  - Goal is to find problems with installation and setup, not in the application itself (that is next week's Bug Bounty assignment).

* [Bug Bounty](assignment/week15/bug-bounty) - try to find bugs in deployed projects of other teams 
  - URLs of deployed projects are shown in Google Sheet for Project Testing
  - Top bug hunters will earn extra assignment points

<a></a>
<a href="#week-1"></a>
<a href="#week-8"></a>
<a href="#schedule"></a>