---
title: Schedule
---

> This schedule may be wrong!    
> See **[Google Classroom][google-classroom]** for weekly material and assignments.

[google-classroom]: https://classroom.google.com/w/NjkxNTc2NDc5NzM4/t/all

---

### Schedule

#### Preparation

- [Sign-up and Install Required Software](assignment/week1/signup-and-software)
- Read [About the course](about) for essential class resources & how to contact TAs.


### Week 1

- [Introduction to the course](introduction/)
- Schedule: Google Doc <https://docs.google.com/document/d/1uxclHXjCULDpY8p97YRq13tThdltA84MJyuUo_8o1Kk/>
- [Introduction to software process](software-process/)
  - Google Slides: <https://drive.google.com/file/d/1y62gRCjgbpHcxbD6G86YKpHUszzPZ2j7/view>

### Week 1 Lab
- Review of "Your Software Process" Assignment
- Writing a Vision and Scope Document
  - Google Doc <https://docs.google.com/document/d/1iVuHzEUcEYQ5SUfIY6bKUe0nfM3WQbk5V9XO6yxFrlk/>
  - Excerpt from Stellman & Greene on [Software Project Planning](https://cpske.github.io/ISP/vision/Project-Planning-Stellman-and-Greene.pdf) and the Vision.
  - Exercise. Analyze a Vision & Scope

#### Week 1 Assignment

- 1.1 Preparation https://cpske.github.io/ISP/assignment/week1/signup-and-software
- 1.2 Your Software Process
      - Submit a Google Doc using template
- 1.3 Software Process Reading and Questions
      - [Software Process Homework](assignment/week1/software-process-homework) reading assignment
      - [Software Process Questions](https://forms.gle/tkqnsAf4DvPEpj6Q9)

### Week 2

- [Scrum](agile/scrum)
  - Watch [Scrum in Under 10 Minutes](https://www.youtube.com/watch?v=XU0llRltyFM) on Youtube
  - [Introduction to Scrum](agile/scrum) contains links that you should **read**
  - Read [Scrum Guide](https://www.scrumguides.org/scrum-guide.html). Anything in the Scrum Guide may be on a quiz.
- Exercise: Scrum Questions (Google Form)
- Scrum Review Questions done in class

### Week 2 Assignment

- Read [Scrum Guide](https://www.scrumguides.org/scrum-guide.html).
- Read at least one of these to get another perspective on Scrum:
  - [Scrum Primer](https://cpske.github.io/ISP/resources/Scrum-Primer.pdf) - practical guide to using Scrum in a project. Mostly text. The authors are software process experts.
  - [Comprehensive Scrum Guide](https://www.visual-paradigm.com/scrum/what-is-scrum/) by Visual Paradigm.  Very good with lots of illustrations & links.
    A couple of minor misstatements, I think.
- Not required: my Scrum notes https://cpske.github.io/ISP/agile/scrum
- Preview the Week 3 material on HTTP.


### Week 3

- Preparation: install ncat on your computer and TEST IT: <https://nmap.org/ncat/>.
- [Intro to TCP/IP and HTTP Protocols](web/index), [presentation](web/HTTP.pdf)
- Practice using HTTP [HTTP in Action](web/HTTP-in-Action.pdf).
- Introduce KU Polls and this week's assignment.

### Week 3 Lab

- Introduction to Web Frameworks - what they do
- [KU Polls Project Inception](assignment/ku-polls/inception)
  - create a repository, wiki, and Github project
  - write a Vision & Scope, Project Plan with timeline 
- Brief [Intro to Django](django/Intro-to-Django.pdf)

#### Week 3 Assignment

- [KU Polls Iteration 1](assignment/ku-polls/iteration1) (Django Tutorial)

### Team Project

Submit a project proposal using the Project Spreadsheet

### Week 4

- [Git Branch & Merge](git/branch-and-merge)
- [Github Flow](https://guides.github.com/introduction/flow/)
- Exercise: Branch & Merge Practice
- Github Flow Questions (Google Form)

#### Week 4 Lab

- [Django Review](django/Django-review-1.pdf)
- Exercise: Django Review Questions (Google Form)
- Exercise: KU Polls Peer Review (test another student's KU Polls)
- Assignment: KU Polls Domain Class Diagram
- How to [Separate Configuration from Code](django/external-configuration) a best practice for software

#### Week 4 Assignment

- [KU Polls Iteration 2](assignment/ku-polls/iteration2.md)
- Read Sections 3.1 - 3.5 of *ProGit* (free online book) about branch, merge, and remote branches.


### Week 5

- Quiz on material from weeks 1 - 4.
- Exercise: Practice Github Flow as a team, *KU International Cafe*

#### Week 5 Lab

- Description of KU Polls Iteration 3
- [Authentication](authentication) and Authentication in Django
- In-class group coding of revised Domain Model for KU Polls
  1. Update your Domain Model (a document in your project wiki) & submit a link
  2. Implement User login/logout feature and require login to vote (but no change to votes model)
  3. Refactor to use Vote object for each user's vote

#### Week 5 Assignment

- [KU Polls Iteration 3](assignment/ku-polls/iteration3.md)
- Use the Django [Messages Framework](django/messages-framework) in KU Polls

### Week 6

- Review [Python Unit Testing](testing/PythonUnitTesting.pdf) my slides
  - [unittest](https://docs.python.org/3/library/unittest.html) in the official Python docs
- Exercise [Test Automation on Github](https://docs.google.com/document/d/1Plh3Uh1E02BOBQxnwdiYlEbKh8fBTm1kMqL43rbA4ZQ/) submitted to Github Classroom

#### Week 6 Lab

- [Logging](logging/)
- [Logging practice](logging/logging-practice) submitted to Github Classroom


#### Week 6 Assignment

- [KU Polls Iteration 4](assignment/ku-polls/iteration4.md)
- Test another student's KU Polls, including instalation instructions

### Week 7

1. [Code Coverage](testing/code-coverage) in Python
2. Exercise: How good were the tests in last week's CI assignment?  Was any code missed? 
3. Type Hints and Static Typing
4. Sequence Diagrams
5. Testing and Mock Objects
6. Draw a burn-down chart
7. Write Sphinx-style docstring and type hints from Google style docstring.
   - complete missing parts of docstring by studying the code.
8. Type hints exercise


#### Week 7 Assignment




### Midterm 

- Exam is 25 September. Room 202.
- Covers everything so far.

---

## Topics Not Covered (Yet)

### Database and ORM

- [Brief Introduction to Databases](database/Database-Basics.pdf)
- Database Exercise: <https://cpske.github.io/ISP/assignment/week6/database-exercise> 
  - Use a database browser to view & describe the KU Polls database schema
- Converting a software model to database model
- [Basics of Object-Relational Mapping](database/Persistence-and-ORM.pdf) 

- ORM modeling practice (optional) write Django models for a sales application 
  - Github Classroom Assignment: <https://classroom.github.com/a/UOcT0BOr>
  - Instructions: <https://cpske.github.io/ISP/assignment/orm/Modeling-Practice.pdf>




### Git

- [Git](git/) concepts, Git commits as a graph, managing files and using Git history. 
- Exercise: Git practice (submit on Github)
- Exercise: use the [Git Visualizer](http://git-school.github.io/visualizing-git/) to see a git graph
- Exercise: use `gitk` tool that is included with git
- Exercise: complete parts 1-2 of [Learn Git Interactive](https://learngitbranching.js.org/). Section on *Moving Work Around* is recommended.
- [Using Github](git/Using-Github) & Github Classroom.
- [Git branch and merge](git/branch-and-merge)
- Exercise: practice merge and conflict resolution
- [Git remotes](https://cpske.github.io/ISP/git/Git-Remotes.pdf)


### Coding Style and Coding Standards

- [Code Quality, Coding Style, and Coding Standards](code-quality)
- Python Coding Style: [How to Write Beautiful Python Code with PEP8](https://realpython.com/python-pep8/) on [Real Python](https://realpython.com/)
- [PEP257 Docstrings](https://peps.python.org/pep-0257/) - only one page
- [Sphinx style docstrings](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html) good for documenting parameters, returns, and exceptions
- Exercise: apply the Python style guidelines
- [Coding Standard and Code Quality](/code-quality/)
- [Docstring Comments](code-quality/docstrings). Three conventions and the one we recommend.
  - for parameters and return values use [type hints](type-hints/) instead of writing the data type in comments
- Exercise: add docstring comments to code
- Exercise: improve a code using Pylint



### Miscellaneous

- Create a Burn-down chart for a Sprint. 
Not assigned this year:
- [Command Line Basics](assignment/week3/Command-Line-Basics.odt) you should know (nothing to submit) 
  - <https://drive.google.com/open?id=1igAYSBGdshgz1ESZOjcFwP0x-vCT-02CatdWEcVV7aQ>





<a></a>
<a href="#week-1"></a>
<a href="#week-8"></a>
<a href="#schedule"></a>
