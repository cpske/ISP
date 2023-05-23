---
title: Schedule
navigation_order: 1
---

> This schedule may be wrong!    
> See **[Google Classroom][google-classroom]** for weekly material and assignments.
>
> Do the assignments as posted on [Google Classroom][google-classroom].

[google-classroom]: https://classroom.google.com/c/NDk2ODk1MDE0NTgy?cjc=r3466kb

---

### Schedule

#### Preparation

Please do this before the course starts. Otherwise, do it in Week 1.

- [Sign-up and Install Required Software](assignment/week1/signup-and-software)
- Read [About the course](about) for essential class resources & how to contact TAs.


### Week 1

- [Introduction to the course](introduction/)
- [Introduction to software process](software-process/)
- Exercise: Software Process Basics (Google Form)
- Exercise: [Write a Process Description for an Everyday Project](assignment/week1/general-process-exercise) 
- [Code Quality, Coding Style, and Coding Standards](code-quality)
- Python Coding Style: [How to Write Beautful Python Code with PEP8](https://realpython.com/python-pep8/) on [Real Python](https://realpython.com/)
- Exercise: apply the Python style guidelines
- Programming 2 Review, basic Python and O-O concepts.


#### Week 1 Lab

- [Git](git/) concepts, Git commits as a graph, managing files and using Git history. 
- Exercise: Git practice (submit on Github)
- Exercise: use the [Git Visualizer](http://git-school.github.io/visualizing-git/) to see a git graph
- Exercise: use `gitk` tool that is included with git
- Exercise: complete parts 1-2 of [Learn Git Interactive](https://learngitbranching.js.org/). Section on *Moving Work Around* is recommended.
- [Using Github](git/Using-Github) & Github Classroom.
- Exercise: practice using Github Classroom (not done in 2022)
- Quiz: Programming Skill Assessment

#### Week 1 Assignment

- [Software Process Homework](assignment/week1/software-process-homework) reading assignment
- [Software Process Questions](https://forms.gle/M5RcqiDUh4NkFviW9) based on the reading
- Git commands "cheat sheet" on Github


### Week 2

- [Scrum](agile/scrum)
  - Watch [Scrum in Under 10 Minutes](https://www.youtube.com/watch?v=XU0llRltyFM) on Youtube
  - [Introduction to Scrum](agile/scrum) with links you should **read**
  - Read [Scrum Guide](https://www.scrumguides.org/scrum-guide.html). Anything in the Scrum Guide may be on a quiz.
- [Git branch and merge](git/branch-and-merge)
- Exercise: practice merge and conflict resolution
- [Git remotes](https://cpske.github.io/ISP/git/Git-Remotes.pdf)

#### Week 2 Lab

- Feedback on Week 1 assignments
- Github Flow and Pull Requests - [Github's Intro](https://guides.github.com/introduction/flow/)
- Exercise: Github Flow questions (Google form)
- Exercise: KU Cafe

#### Week 2 Assignment

- Reading Assignment:
  - [Scrum Guide](https://scrumguides.org/scrum-guide.html)
  - [Github Flow](https://guides.github.com/introduction/flow/)
  - [Pull Request Tutorial](https://yangsu.github.io/pull-request-tutorial/)
  - [Commenting on Pull Requests](https://help.github.com/en/articles/commenting-on-a-pull-request)
- Complete at least parts 1 & 2 of this tutorial: <https://learngitbranching.js.org/>
- Add Remote Commands to your Git "cheat sheet" from Week 1, using remotes.md in starter code.

### Week 3

- [Introduction to Testing](testing/)
- [Python Unit Testing](testing/PythonUnitTesting.pdf) my slides
  - [unittest](https://docs.python.org/3/library/unittest.html) in the official Python docs
- Exercise: unit testing practice (simple exercise)

#### Week 3 Lab

- Quiz on week 1 and 2 material
- Review Github Flow
- [Coding Standard and Code Quality](/code-quality/)
- [Docstring Comments](code-quality/docstrings). Three conventions and the one we recommend.
  - for parameters and return values use [type hints](type-hints/) instead of writing the data type in comments
- Exercise: add docstring comments to code
- Exercise: improve a code using Pylint
- Unit Tests for a Bank Account code
- Homework: Read "*Documenting Python Code*" <https://realpython.com/documenting-python-code/>. Really *read it*.
- Homework: Finish Unit Tests for Bank Account

#### Week 3 Assignment

- Create a Burn-down chart for a Sprint. 
Not assigned this year:
- [Command Line Basics](assignment/week3/Command-Line-Basics.odt) you should know (nothing to submit) 
  - <https://drive.google.com/open?id=1igAYSBGdshgz1ESZOjcFwP0x-vCT-02CatdWEcVV7aQ>

### Week 4

- **Preparation:** install ncat on your computer and TEST IT: <https://nmap.org/ncat/>.
- [Intro to TCP/IP and HTTP Protocol](web/index), [presentation](web/HTTP.pdf)
- Exercise: [HTTP in Action](web/HTTP-in-Action.pdf). Manually enter HTTP requests and responses using ncat.


#### Week 4 Lab

- [Intro to Django](django/Intro-to-Django.pdf)
- [KU Polls Project Inception](assignment/ku-polls/inception) 
  - Create a Vision, Requirements, and a Roadmap for the project (Project Plan)
  - Initialize a Github repository, add essential docs to a Wiki, and start a Project
- Description of KU Polls first iteration (Django Polls tutorial)
  - Domain Model for Polls app - `Question` and `Choice` classes
  - You will be implementing features according to the tutorial, so goods tasks are "Implement Tutorial part 1", "Implement Tutorial part 2", etc.
  - As you do each part of the tutorial **add a long description** to each task, using Markdown.
  - Development work on a git branch named `iteration1`. Push this branch to Github. Merge to master/main when done.

#### Week 4 Assignment

- [KU Polls Iteration 1](assignment/ku-polls/iteration1) (Django Tutorial)
  - submit work in your own `ku-polls` repo on Github.
  - use correct repo structure! No extra layer of directories.


### Week 5

- Review progress on KU Polls iteration 1.
- [Web app and web framework overview](web/index#web-frameworks) and [presentation](web/Web-Apps-and-Web-Servers.pdf)
  - was week 4 in prior years
- [How Django handles requests (with graphic)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction#what_does_django_code_look_like) on MDN
  - *Did anyone read this?* 
- [Django Review](django/Django-review-1.pdf)
- Improvements to KU Polls for Iteration 2
  - add an `end_date` to polls, 
  - add methods `is_published`, `can_vote`
  - improve navigation by adding links to home page - should never need to use "Back" button
  - add default landing page (redirect)
  - externalize configuration data and secrets
- Quiz: Unit Testing

#### Week 5 Lab

- [Separate configuration from code](refactoring/separate-configuration) & how to externalize configuration
  - [Presentation](refactoring/Separate-config-from-code.pdf)
  - a [12-Factor App](https://12factor.net/config) recommended practice, also called "externalize configuration" 
- Exercise: Externalize Configuration <https://github.com/ISP21/decouple-example>

#### Week 5 Assignment

- Start background work and proposal for course team project
- [KU Polls Iteration 2](assignment/ku-polls/iteration2.md)


### Week 6

- Introduce the Team Projects.
- [Brief Introduction to Databases](database/Database-Basics.pdf)
- Database Exercise: <https://cpske.github.io/ISP/assignment/week6/database-exercise> 
  - Use a database browser to view & describe the KU Polls database schema
- Converting a software model to database model
- [Basics of Object-Relational Mapping](database/Persistence-and-ORM.pdf) 
- Persistence in Django: how Django provides the CRUD operatons
- Overview of KU Polls Iteration 3
- Homework (due before Thursday lab): Revise KU Polls domain model
- [Authentication](authentication)
- Lab: Intro to Authentication in Django
- Lab: Refactor KU Polls for Iteration 3 (1-user-1-vote)

#### Assignment

- Django Review Questions (answer online): <https://forms.gle/zPuPzzt76QWboFZXA>
- (Not assigned in 2021, but a good thing to do) [Test another student's KU Polls](assignment/week6/ku-polls-peer-testing)


### Team Project

Submit a project proposal using the Project Spreadsheet

- Project Guidelines: <http://bit.ly/ISP-project-description>
- Proposal Template: <http://bit.ly/ISP-project-template>
- Project Proposals: 
  * <http://bit.ly/ISP2021-projects> to submit your team and proposal
  * <http://bit.ly/ISP2020-projects> last year's proposals


### Week 7

- Review some previous material and assignments
- Why spend so much time on KU Polls?
- UML Class & Sequence Diagrams (added in 2022)
- Class Diagram exercise
- Sequence Diagram exercise
- Lab: Smoke Testing of another student's KU Polls (post issues)
- Virtual Environments for Python

#### Assignment

- [KU Polls Iteration 4](assignments/ku-polls/iteration4)

Not covered in 2022:
- [Code Coverage tools](testing/code-coverage) for Python 
- Exercise: apply code coverage
- [Testing in Django](testing/WebTesting.pdf) - how to test models, views, url dispatcher, and templates
- ORM modeling practice (optional) write Django models for a sales application 
  - Github Classroom Assignment: <https://classroom.github.com/a/UOcT0BOr>
  - Instructions: <https://cpske.github.io/ISP/assignment/orm/Modeling-Practice.pdf>


### Midterm 

- Exam is 27 September. Time and Location TBA.
- Covers everything so far.
- Recommended OBS Video Settings: <https://drive.google.com/open?id=1xiDH6NImH0PAAZp5AUNWtJeLzlRSYoqiAOFE8wFS1vM&authuser=1>
  - We may not need this is 2021 if we can use KU's Exam application.

- Coding Part at a Later Date
- Coding emphasize **unit testing** and **code quality**.
- Coding will also cover **refactoring** and maybe **design patterns**.


### Week 8

- [Logging](logging/)
- [Logging practice](logging/logging-practice)
- User Stories
- [Milestones](software-process/Milestones.pdf) to show progress toward completion of a project
- [Domain Modeling](modeling/Domain-Models.pdf) and [Category List](modeling/Conceptual-Category-List.pdf) to help discover domain classes
- Lab: User Stories.  Construct User Stories, then use them to discover Domain Classes.


#### Assignment

- [Add Logging to KU Polls](assignment/ku-polls/logging)
- Write User Stories for your project.  Add them to the project wiki.
- Add a *domain class diagram* to your project docs
- Use the User Stories to identify domain classes and help you create a domain model


### Week 9

- [Automation and Continuous Integration](automation/)
- Exercise using CI - add Travis-CI and Codecov to demo-pyci project
  - Instructions <https://cpske.github.io/ISP/automation/travis-demo-project>
  - Starter code (to be added) 
- Code Coverage & Coverage Tool for Python
- Exercise: add code coverage to demo-pyci project, use Codecov.io to display the report, and add badges to the project README
- Lab: Adding *badges* to your Github repo, to indicate status. Badges provide a quick visual indicator of project health.


#### Assignment

- [Add CI to KU Polls](assignment/week8/ku-polls-ci-assignment)
  - Use CI to run unit tests and run code coverage
  - Add "badges" to your KU Polls README.md for Travis and CodeCov status
- Reading on terminology & concepts for refactoring and design patterns
  - Next week you will be asked to explain these terms and concepts, and identify them in code.
- Read <https://refactoring.guru/refactoring> 
- [Movie Rental Refactoring, Part 1](assignment/movierental/movierental-part1)
  - Starter Code on Github: <https://classroom.github.com/a/_qGEboUn>


### Week 10

- What is "good code"?  How can we improve the quality of code?
  - Goals, problems, and forces on software that motivate the defination of "good code" and why it's important.
  - Visible metrics and characteristics of good and poor code
  - Principles and practices for writing good code
- [Introduction to Refactoring](refactoring/) and [slides](refactoring/Refactoring.pdf)
- [Refactoring Signs](https://refactoring.guru/refactoring/smells) (*aka* "Code Smells") on refactoring.guru
- [When to Refactor](https://refactoring.guru/refactoring/when) and [Refactoring Process](https://refactoring.guru/refactoring/how-to)
- [Catalog of Refactorings](https://refactoring.guru/refactoring/techniques)
- Refactoring Exercise: Pizzashop refactoring <https://github.com/ISP2022/pizzashop>
- Anything on <https://refactoring.guru/refactoring> may be on a quiz!

- [Static Typing](https://cpske.github.io/ISP/code-quality/Type-Checking.pdf), Static Analysis, and [Type Hints](type-hints/introduction)
- Static Type Checking Exercise: [scorecard.py](type-hints/scorecard.py)
- [Type Hints](type-hints) and [Introduction](type-hints/introduction) by Mai Noripong
- Another [Type Hints Introduction](https://fastapi.tiangolo.com/python-types/) on FastAPI; really good, simple examples.
- [Type Hints Practice](https://docs.google.com/document/d/1S-5o_NHJXQosnQIT3pvI20wxxzonOKm_ryG0lYKu_Ws/) on Google Docs

> IDEs have refactoring actions that perform refactoring faster and reduce errors. 
> But, in Python the refactoring tools *work poorly* unless the code has accurate *type hints*. *Type Hints* also improve static analysis so that tools can find more problems and potential errors.
> Please pay special attention to the type hints for Collections, return types, and optional values.

#### Assignment

- Homework: Learn the Refactorings on [Refactoring.Guru](https://refactoring.guru/refactoring). Details on Google Classroom.
- Homework: Movie Rental refactoring, Part 1.


### Week 11

- [Review common refactorings](refactoring/Refactoring-Review.pdf) - submit your answers on Google Classroom (Google Form)
- More Refactoring - refactor structure of classes, creating objects (*Not done in 2022*)
- [Refactoring Patterns](refactoring/Refactoring-Patterns.pdf)
- Intro to Design Patterns
- Singleton & Factory Method Patterns - other patterns are covered in Prog2 and SS&D
- Type Hints Practice (*see link in Week 10*)
- Lab: Organizing Django code. Replace "models.py", "tests.py", and "views.py" with directories (packages) containing multiple files. 
- Lab: [CookieCutter Django](https://github.com/cookiecutter/cookiecutter-django) and [documentation](https://cookiecutter-django.readthedocs.io/en/latest/) have examples and good advice for structuring Django projects. Discover and describe some of them.

#### Assignment

- [Movie Rental Refactoring, Part 2](assignment/week12/movie-rental2)
- Team Projects: prepare to demo your work soon

## Week 12

- [Agile](agile/agile) - Agile values, principles, and practices.
- Exercise: [Agile Practice Review Questions](agile/agile-practice-questions.pdf)
- Introduction to OAuth
- Exercise: OAuth Playground and questions on Google Classroom (form)
- [Code Reviews][code-review]

- Lab: perform a short code review and **then** start on your team's code refview script and checklist.

[code-review]: https://cpske.github.io/ISP/code-review/
[code-review-assignment]: https://cpske.github.io/ISP/assignment/week12/code-review

#### Assignment

- Read [Reviews](code-review/Reviews-Stellman-and-Greene.pdf) chapter from book by Stellman and Greene.
- Read 3 [Code Review Best Practices](code-review/code-review-best-practices) articles in [Code Review Assignment][code-review-assignment]
- [Create a Code Review Script and Checklist](assignment/week12/code-review) and then do a walk-through of project code

- (*not in 2022*) Homework: Read the [Learn More](agile/agile#learn-more) articles in [Agile](agile/agile). They are fundamental.
- Optional: [Agile Crossword Puzzle](agile/crossword-puzzle.pdf) 
  - answers available online
- (*not in 2022*) Read the articles in [Agile Practices](assignment/week9/agile-practices) (there will be quiz on this) 
- Read tips from *Practices of an Agile Developer* ("Tips" sections in assignment)

### Week 13

- Refactoring Review (again)
- Review Movie Rental refactoring
- Testing Pyramid and End-to-End Testing in [Web Testing](testing/WebTesting.pdf)
- [Selenium](testing/Selenium-intro) for testing web applications. Some slides in [Web Testing](testing/WebTesting.pdf)
- [Selenium Exercise](testing/SeleniumExercise.pdf) scrape search results from DuckDuckGo
- Lab: Project Demos


#### Assignment

- Reading on Agile Practices (tba)
- [Link Scanner](assignment/week15/selenium) write an app to scan and test all links on a web page using Selenium, and reports bad links.


### Week 14

- Remaining project demos.
- Review Agile Practices (week 10 assignment), including comments in code.
- The [12-Factor App](web/12FactorApp.pdf) - 7 factors that apply to your projects
- Robot Framework - a great tool for automation and E2E testing.

#### Assignment

- Team assignment: 
  1. create installation instructions for your project
  2. use a virtualenv for local installation
- Team Assignment: deploy your application to a cloud service


### Week 15

- Review
- Bug Hunting - find problems in other teams' software

#### Assignment

- Individual assignment: [install and run another team's project](assignment/week15/installation-testing)
  - Post issues for any problems in their installation instructions.
  - Goal is to find problems with installation and setup, not in the application itself (that is next week's Bug Bounty assignment).

- [Bug Bounty](assignment/week15/bug-bounty) - try to find bugs in deployed projects of other teams 
  - URLs of deployed projects are shown in Google Sheet for Project Testing
  - Top bug hunters will earn extra assignment points

<a></a>
<a href="#week-1"></a>
<a href="#week-8"></a>
<a href="#schedule"></a>
