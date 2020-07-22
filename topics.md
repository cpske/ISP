---
layout: page
title: ISP Topics
---

**Schedule** 01219245 ISP Mon 10-12, 13-16 starting 10 Aug 2020.   
**Location** class will be online with some meetings and live lectures in room E204.  Location of online meeting will be announced before class starts.

<table border="0">
<tr valign="top"> <th width="25%">Topic</th> <th width="75%">Description</th> </tr>

<tr valign="top">
<td align="left" markdown="span">
[Introduction to Course](introduction/index)
</td>
<td align="left" markdown="span">
[Introduction to course goals and topics](introduction/index), 
prerequisites, required work and grading, and how to access material.    
Assignment to do by first week.    
[Advice from an SKE scholar & entrepeneur](introduction/Jomzap-Recommendations.pdf).    
Why do a team project in a course on "*Individual* Software Process"?
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
[Software Processes](software-process) <br/>
Iterative &amp; Incremental Development
</td>
<td align="left" markdown="span">
An introduction to software process concepts and practices. The Waterfall process compared to iterative and incremental development; the Unified Software Develop Process (UP) as a model, and Scrum for managing iterations.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
[Agile](agile)
</td>
<td align="left" markdown="span">
Agile is a set of values, principles, and practices for software development,
that emphasize frequent delivery of running software, customer collaboration, 
and self-managing teams.  The values and principles can be incorporated into any
development process.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
[Scrum](agile/index#scrum)
</td>
<td align="left" markdown="span">
Scrum is a set of practices for iterative development. Scrum focuses on
development activities and can be incorporated in many software (or non-software) projects.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
[Git](git) and Version Control
</td>
<td align="left" markdown="span">
Basics of using a git to manage work products, compare or recover previous versions, and how to work with remote repositories.

Git *branches* are used to manage work on features or fixes, and *tags* are used to mark specific points in a repository, such as a release.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
Git and Development
</td>
<td align="left" markdown="span">
Using Github Flow, issues, commit messages, 
pull request reviews, and referencing code in issues.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
[Unit Testing](testing)
</td>
<td align="left" markdown="span">
Unit testing is testing of individual "units" of code, such as classes and methods.
Testing Behavior - don't only test code (TBA)   
[Code Coverage](testing/code-coverage)      
Unit testing in Java (JUnit) and Python (unittest). Python doctest.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
Mock Objects
</td>
<td align="left" markdown="span">
Mock Objects for testing.
</td>
</tr>

<!-- Types and Type Checking -->
<tr valign="top">
<td align="left" markdown="span"> 
Types and    
Type Checking
</td>
<td markdown="span">
[Intro to Types and Type Checking](code-quality/Type-Checking.pdf) (slides)    
[Type Hints][type-hints] in Python

Read Mai's [Type Hints][type-hints] write-up     
and these Python docs: [Typing][python-typing], 
[Collections base classes][python-abc-collections] (shows what methods each type provides)
Add type hints to detect errors: [scorecard.py][scorecard.py]      
Do the exercises in Mai's [Type Hints][type-hints] write-up    
[Type Hint Practice](code-quality/type-hint-practice.pdf) exercise     
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
[Refactoring](refactoring)
</td>
<td align="left" markdown="span">
Refactoring means to improve existing code without changing its external functionality.
We cover common refactoring situations and how to do them using an IDE.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span"> 
Code Review
</td>
<td markdown="span">
[Software Review](code-review/Reviews.pdf) slides and [Summary](code-review/code-review)       
[Code Review Best Practices](code-review/code-review-best-practices) from various sources    
[Reviews chapter from Stellman &amp; Greene](code-review/Reviews-Stellman-and-Greene.pdf)    
Example Checklists: [Java](code-review/Java-Code-Review-Checklist.pdf), 
[PSP](code-review/PSP-Review-Script-Checklist.pdf)    
[Assignment: Code Review Checklist and Script](assignment/code-review)
</td>
</tr>

<tr valign="top">
<td align="center" markdown="span"> 
End-to-End Testing    
</td>
<td markdown="span">    
[Web App E2E Testing with Selenium](testing/WebTesting.pdf)    
   
[Intro to Selenium](testing/Selenium-intro)    
1. Refactor your Django tests into separate files, based on what is being tested.    
2. Perform code coverage on your Django tutorial code and your project code.    
3. Selenium: [Find Bad Links](assignment/selenium). 
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span"> 
[12-Factor App](web/12FactorApp.pdf)   
</td>
<td markdown="span">
The [12-Factor App](web/12FactorApp.pdf) is a set of recommendations for maintainable
cloud-based applications, developed by Heroku. 
</td>
</tr>

</table>

---
## Web Applications

<table border="0">
<tr valign="top"> <th width="25%">Topic</th> <th width="75%">Description</th> </tr>

<tr valign="top">
<td align="left" markdown="span">
[HTTP](web/index#http)
</td>
<td align="left" markdown="span">
HTTP is the communicatoin protocol used by web apps and web services.    
[Introduction to HTTP](web/HTTP.pdf)    
[HTTP in Action](web/HTTP-in-Action.pdf) class exercises using HTTP, requires ncat or netcat.    
Useful [Http Tools](web/http#tools) for manually testing and debugging web apps.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
Web Apps and Frameworks
</td>
<td align="left" markdown="span">
Short intro to how a web server and web app typically handle requests and responses.  This helps make sense of the various components of a [web framework](web/web-frameworks).    
[WSGI](web/wsgi-servers) standard for connecting Python web apps to web app servers.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
Django
</td>
<td align="left" markdown="span">
[Introduction to Django](django/Intro-to-Django.pdf).    
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
Django Polls Project
</td>
<td align="left" markdown="span">
Everyone will implement the Django Polls tutorial project.  We'll structure it as an iterative software project. At each iteration you'll learn new material that will help with your course project.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
Database Basics
</td>
<td align="left" markdown="span">
Intro to database concepts and how to use a database in code.
Essentials to know are:
- table schema and field types
- identity field as key
- how to relate tables using foreign keys
- how to view and edit schema
- 4 basic CRUD operations
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
Object-Relaltional Mapping
</td>
<td align="left" markdown="span">
ORM concepts and frameworks.  All web frameworks either include an ORM
or rely on one for persisting data.  Two common design patterns for
ORM.    
Django models provide ORM services, but they are obscured.   
Understanding ORM concepts will make it easier to understand and work
with Django models.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
[Logging](logging/Logging.pdf)
</td>
<td markdown="span">
[Logging](logging/Logging.pdf)    
[Logging Practice](logging/logging-practice)
</td>
</tr>
</table>

---

## Developer Skills
 - review of OOP fundamentals in Python (assessment exercise)
 - coding convention
 - unit testing
 - using UML

## Project Planning

* Writing Goals and Milestones.

* Velocity - computed from Story Points and actual time spent, or just time.

* The RUP framework and a few key concepts.

* Prioritize Development
   - Larman and RUP: value to customer, high risk, importance to architecture
   - Use a Prototype to reduce risk or uncertainly about suitability

Your project needs *at least*:

* vision statement, describing goal and "vision" of the project
* project plan - what to build and plan for what to build in each iteration
* task board for each iteration, containing tasks for that iteration and their status
* issue tracker for bugs, change requests, and more
* (desirable) burn-down or burn-up chart.

Task Boards 

* [Trello](https://trello.com)
* [Asana](https://asana.com) 
* Github "Project Boards" has similar features. Cards are limited to Github issues, pull requests, and notes.  These may not always match project "tasks".

Some projects use Trello or Asana for iteration plans.  In the course project, use
the Github Wiki for visibility.




### Build Tools, Build Management, and Automatic Build-and-Test

* Basic build tools: using Ant or Maven for Java.
  - maybe cover "make" and GNU make for perspective

* Build and Dependency Management Tools
  - ant and ivy (for dependency mgmt)
  - maven
  - gradle

* Using automatic build and test with CircleCI or Travis on Github.

### Reviews

* Reviews find more defects than testing, according to many studies.
* Different kinds of reviews.
* For ISP, desk check and pair reviews probably most relevant.

### Clean Code, Literate Code

[Clean Code](http://www.jeremybytes.com/Downloads/CleanCode.pdf) PDF by JeremyBytes. His web page on [clean code](ww.jeremybytes.com/Demos.aspx#CC) has other useful material.

* Important lessons from *Clean Code* and *Code Complete*.

* Maybe look at *Practices of an Agile Developer*.  Each chapter is short and covers one lesson.  Some parts are online.

* Use a coding convention, and consistent coding style.

* How to use Checkstyle. How to configure and safe a code style Eclipse or IntelliJ.

* Look at coding guidelines from some real projects. Apache is good source.

### Documenting Your Code

* Python Docstrings, Javadoc, or Scaladoc to create documentation for everyone to use.  
* Syntax of Python Docstrings.
    - 3 variations: Python official docstrings, Google style, Numpy style
* Tools for formatting them:
    - pydoc
    - python interactive: help(something)
    - Sphinx and the Napolean addon
* Code comments to explain *why* and details not obvious from code

### Project Documentation

What to document?

- installation instructions
- requirements and features
- software design
- rationale for decisions and design. Record important design decisions and *why* you made them.  This helps other developers, including you in the future.
- user guide

Good places for documentation
* Github pages or readthedocs.io for user and programmer documentation
* Github wiki for design notes and rationale

A Github pages (github.io) site can be generated from your main project repository, using (a) a docs directory, (b) a specific branch (usually `gh_pages`), or use a separate repo.

Everyone should know how to use Markdown. Its much more readable than HTML, so you'll make fewer errors.

### Measuring Progress and Quality

* How to measure your output?
* Common software metrics, like LOC, functions, code "units".
* Classify and count defects.  Design defects, coding defects, test defects.



## Estimation

* How to estimate: development time and code size.
* Jittat's Slides: [intro]( ), Jittat

* [Agile Estimation](http://www.construx.com/Resources/Presentation/Agile_Estimation__Key_Principlies_and_Practices_for_Successful_Agile_Practices/) talk by Construx (Steve McConnell's company)



## Assertions and Design by Contract (?)

* Reduce defects, spot defects sooner.
* In Java you can leave assertions in the final code.  They can be enabled or disabled using the run-time `-ea` flag.  You can even selectively enable assertions for some classes but not others!  
  - If assertions are not enabled, the "assert" statements are skipped so there is no performance penalty.

### Tracking Your Own Performance

* How do you know you are getting better?
* You can't improve that which you can't measure.
* Task Lists and Checklists.

### Self-improvement

* Importance of continual learning and reading
* See _Pragmatic Programmer_ Item 5: Your Knowledge Portfolio (p. 37).
* Goal-directed learning for new technology.  Instead of comprehensive learning or random videos.
  - "*Begin with the end in mind*" (Stephen Covey) 

### Communication



----

## Anti-Patterns

[10 practices of highly ineffective software developers](https://www.infoworld.com/article/2615765/application-development/10-practices-of-highly-ineffective-software-developers.html) on InfoWorld

----

## Development Skills You Didn't Learn in OOP

1. Logging
  - Professional, production code usually has some form of logging.
  - You *cannot* print to the console: there may not be a "console".
  - Example: info on 100K accounts stolen from KTB, 3K stolen from KBANK (Bangkok Post).  **How did they know what was stolen?** 

2. Basics of Security
  - Like logging, this is an important part of real code. You need to think about during design and development. Don't "add it later".

3. Deployment
  - How to package and deploy applications?
  - Creating a portable deployment.
  - Managing dependencies.
  - Docker for containers, or VM images.
  - Documenting build, dependences, and deployment.
  - Deploying to the "cloud".

## Application

To apply all of this, design and develop an application.

For learning value, writing a web app using a framework may be most valuable.

But, some of what we learned is hard to apply when you are working with a new framework, language, or problem domain. Estimates and defects will be worse when working with something unfamiliar.

