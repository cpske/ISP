---
title: ISP Topics
---
[Old 2019 index](index2019)

<table border="0">
<tr valign="top"> <th width="25%">Topic</th> <th width="75%">Description</th> </tr>
<tr valign="top">
<td markdown="span">
[Introduction](introduction/index)
</td>
<td markdown="span">
[Introduction to course and goals](introduction/index), 
prerequisites, required work, project, and grading.    
[Advice from an SKE scholar & entrepeneur](introduction/Jomzap-Recommendations.pdf).    
[Assignment](assignment/week1/signup-and-software) to do by first week.    
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Software Processes](software-process) <br/>
</td>
<td markdown="span">
An introduction to software process concepts and practices. The Waterfall process compared to iterative and incremental development; the Unified Software Develop Process (UP) as a model.    
[Github features that support SDLC](https://github.com/features)
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Agile](agile/agile)
</td>
<td markdown="span">
[Agile values, principles, and practices](agile/agile) for software development.
Agile values and practices can be incorporated into any development process.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Scrum](agile/scrum)
</td>
<td markdown="span">
Scrum for managing development work and iterations.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Git](git) and Version Control
</td>
<td markdown="span">
Git commands and common tasks, structure of a git repo, [branches][git-branching], [aliases](git/aliases), and using remote repositories.   
[Visualizing](git/index#git-visualizer) a git repo.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[More Git](git)
</td>
<td markdown="span">
[Branching and Merging][git-book-branching-and-merging]    
[Using SSH Keys](https://help.github.com/articles/connecting-to-github-with-ssh/) so you never need to enter your Github password
</td>
</tr>
<tr valign="top">
<td markdown="span">
Git and Development
</td>
<td markdown="span">
[Github Flow](git/index#github-flow), issues, branches, &amp;
[pull request](git/Pull-Requests.pdf).    
Importance of descriptive commit messages and Pull Requests.     
Using tags; Tags and Releases on Github.   
[Pull Request Tutorial](https://yangsu.github.io/pull-request-tutorial/) why and how to use pull requests.    
[Git submodules](git/submodule) to divide a project among multiple repositories.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Unit Testing](testing)
</td>
<td markdown="span">
Testing of "units" of code.  Testing Behavior - not just methods.      
[JUnit for Java](/testing/Intro-to-Unit-Testing.pdf) and 
[unit test in Python](testing/PythonUnitTesting.pdf)    
[Code Coverage](testing/code-coverage) 
</td>
</tr>

<tr valign="top">
<td markdown="span">
Mock Objects
</td>
<td markdown="span">
Mock Objects for testing.
</td>
</tr>

<!-- Types and Type Checking -->
<tr valign="top">
<td markdown="span"> 
Static Typing
</td>
<td markdown="span">
[Intro to Types and Type Checking](code-quality/Type-Checking.pdf) (slides)
and [Python Type Hinting](type-hints/introduction) by Mai.       
Python docs [Typing support][python-typing] and
[Collections base classes][python-abc-collections] are excellent.    
Add type hints to detect errors: [scorecard.py](type-hints/scorecard.py)      
Mai's [Type Hint Practice](type-hints/type-hint-practice.pdf).     
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Code Quality](code-quality/index)
</td>
<td markdown="span">
Principles, guides, tips, and tools for writing good quality "clean" code.    
Coding standard, comments as documentation, and code checkers.
Essential for all developers!
</td>
</tr>

<tr valign="top">
<td markdown="span">
Assertions
</td>
<td markdown="span">
Assertions are executable statements of what should be true at some point in code, often used to "*assert*" conditions for parameters.  Assertions reduce errors and document code-level assumptions.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Refactoring](refactoring)
</td>
<td markdown="span">
Improve existing code by restructiring it without changing external functionality.
Common refactoring situations and how to do them using an IDE.
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
Code Review
</td>
<td markdown="span">
[Software Review](code-review/Reviews.pdf) slides and [Summary](code-review/code-review)       
[Code Review Best Practices](code-review/code-review-best-practices) from various sources    
[Reviews chapter from Stellman &amp; Greene](code-review/Reviews-Stellman-and-Greene.pdf)    
[Assignment: Code Review Checklist and Script](assignment/code-review)    
Example Review Checklists: [Java](code-review/Java-Code-Review-Checklist.pdf), 
[PSP](code-review/PSP-Review-Script-Checklist.pdf)
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
End-to-End Testing    
</td>
<td markdown="span">
[Web App E2E Testing](testing/WebTesting.pdf) with Selenium.    
[Intro to Selenium](testing/Selenium-intro)    
1. Refactor your Django tests into separate files, based on what is being tested.    
2. Perform code coverage on your Django tutorial code and your project code.    
3. [Find Bad Links](assignment/selenium) using Selenium. 
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
[Automation and CI](automation)  
</td>
<td markdown="span">
[Continuous Integration](https://docs.travis-ci.com/user/for-beginners)    
[Ant](automation/Ant.pdf), [Make](automation/Make.pdf), and other build tools  
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
[12-Factor App](web/12FactorApp.pdf)   
</td>
<td markdown="span">
Recommendations for maintainable cloud-based applications, by Heroku. 
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
UML 
</td>
<td markdown="span">
Visual software design, function, and deployment using UML.
</td>
</tr>
</table>

[git-branching]: https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell
[git-book-branching-and-merging]: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
[isp-qa]: https://isp2018.github.io/isp-qa/ 	
[type-hints]: type-hints/introduction.md
[python-abc-collections]: https://docs.python.org/3/library/collections.abc.html
[python-typing]: https://docs.python.org/3/library/typing.html
---

## Web Applications and Django

<table border="0">
<tr valign="top"> <th width="25%">Topic</th> <th width="75%">Description</th> </tr>

<tr valign="top">
<td markdown="span">
[HTTP](web/index#http)
</td>
<td markdown="span">
HTTP is the communication protocol used by web apps and web services.    
[Introduction to HTTP](web/HTTP.pdf)    
[HTTP in Action](web/HTTP-in-Action.pdf) class exercises using HTTP, requires ncat or netcat.    
Useful [Http Tools](web/http#tools) for manually testing and debugging web interactions.
</td>
</tr>

<tr valign="top">
<td markdown="span">
Web Apps and Frameworks
</td>
<td markdown="span">
Intro to how a web server and web app typically handle requests and responses.  This helps make sense of the various components of a [web framework](web/web-frameworks).    
[WSGI](web/wsgi-servers) standard for connecting Python web apps to web app servers.
</td>
</tr>

<tr valign="top">
<td markdown="span">
Django
</td>
<td markdown="span">
[Introduction to Django](django/Intro-to-Django.pdf)
</td>
</tr>

<tr valign="top">
<td markdown="span">
Django Polls Project
</td>
<td markdown="span">
Everyone will implement the Django Polls tutorial project.  We'll structure it as an iterative software project. In each iteration you'll implement new features and learn new material.
</td>
</tr>

<tr valign="top">
<td markdown="span">
Database Basics
</td>
<td markdown="span">
Intro to database concepts and how to use a database in code.
Tables, field types, identity fields, relating tables, basic CRUD operations.
</td>
</tr>

<tr valign="top">
<td markdown="span">
Object-Relational Mapping
</td>
<td markdown="span">
ORM concepts and frameworks.  All web frameworks use ORM.
Two common design patterns for ORM. 
Table schema for different domain models.    
Understanding ORM concepts makes it easier to understand and work
with Django models.
</td>
</tr>

<tr valign="top">
<td markdown="span">
Data Import
</td>
<td markdown="span">
[Import and Export Data](django/data-import-export) how to create 
"starter" data for others to easily install and use your polls application
</td>
</tr> 

<tr valign="top">
<td markdown="span">
Virtual Environment
</td>
<td markdown="span"> 
[Virtualenv Quickstart](django/virtualenv-quickstart) and [Using Virtualenv](django/virtualenv) - how to run apps in a virtual environment
for portability, reliability, and security.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Messages Framework](django/messages-framework) 
</td>
<td markdown="span">
Easily pass messages from a view to a template
</td>
</tr>
   
<tr valign="top">
<td markdown="span">
[Externalize Configuration](django/decouple-configuration)  
</td>
<td markdown="span"> 
[Separate configuration from code](refactoring/Separate-config-from-code.pdf) is a practice that applies to all software, not just web apps.
For Django, use [decouple](django/decouple-configuration)  
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
Organize Tests & Models
</td>
<td markdown="span">
[Separate your tests](django/django-test-organization) and [models](django/separate-model-classes) into individual files. Improves team work
by avoiding conflicts.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Logging](logging/Logging.pdf)
</td>
<td markdown="span">
[Logging](logging/Logging.pdf)    
[Logging Practice](logging/logging-practice)
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
Deployment
</td>
<td markdown="span">
How to package and deploy a web application.
Manage dependencies and isolate apps in containers.
</td>
</tr>
</table>

---

## Other Topics

Some of these may be *implicitly* covered as part of other topics.

<table border="0">
<tr valign="top"> <th width="25%">Topic</th> <th width="75%">Description</th> </tr>
<tr valign="top">
<td markdown="span">
Project Planning
</td>
<td markdown="span">
1. Writing a good Vision statement    
2. Defining Goals and Milestones    
3. Key planning concepts from the RUP framework    
4. Prioritizing development (RUP: value to customer, high risk, importance to architecture)    
5. Prototyping to reduce risk and uncertainly
</td>
</tr>
<tr valign="top">
<td markdown="span">
Essential Project Documents
</td>
<td markdown="span">
*Vision Statement* - describes goal and "vision" of the product    
*Requirements* - features, use cases or user stories ("Software Requirements Specification" in some projects)    
*Project Plan* - overall plan of what to build at each iteration, and the process to use   
*Iteration Plan* - goal, milestones, and tasks for one iteration    
*Software design* - document at least high level design    
*Project notebook*, e.g. wiki, to record:
	- decisions related to architecture 
	- important design decisions and *why* you made them (rationale)    
	- solutions and knowledge      
*Build & installation instructions* - including dependencies
</td>
</tr>
<tr valign="top">
<td markdown="span">
Project Tools
</td>
<td markdown="span">
Project board - whole project and each iteration   
Issue tracker - bugs, change requests, and more    
Burn-down or Burn-up chart (optional)    
Project wiki - good location for iteration plans, software design notebook, recording knowledge and solutions    
**Information Radiators**:  project tools should quickly convey useful info & easily visible as part of your normal workflow
</td>
</tr>
<tr valign="top">
<td markdown="span">
Process Improvement
</td>
<td markdown="span">
How discover and *implement* improvements to your development process
</td>
</tr>
<tr valign="top">
<td markdown="span">
Measuring Progress and Quality
</td>
<td markdown="span">
Velocity - the team's rate of task completion <br/>
Common software metrics, like LOC, functions, code "units". <br/>
Count and classify defects.  Design defects, coding defects, test defects, regression defects.
</td>
</tr>
<tr valign="top">
<td markdown="span">
Estimation
</td>
<td markdown="span">
Frequent question from managers and customers is "*how long will it take?*" or "*when will be ready?*"  Planning requires good estimates, but most developers are very poor at estimation.
<br/>
- How to estimate development time and code size <br/>
- Jittat's Slides <br/>
- Track your effort in order to improve ability to estimate <br/>
- [Agile Estimation](http://www.construx.com/Resources/Presentation/Agile_Estimation__Key_Principlies_and_Practices_for_Successful_Agile_Practices/) talk by Construx (Steve McConnell's company)
</td>
</tr>
<tr valign="top">
<td markdown="span">
Self-improvement
</td>
<td markdown="span">
- Importance of continual learning and reading<br/>
- Advice from SKE @ TaskWorld in [introduction](introduction) folder<br/>
- _Pragmatic Programmer_ Item 5: Your Knowledge Portfolio (p. 37) <br/>
- Goal-directed learning instead of comprehensive learning or random videos<br/>
- Track your own performance<br/>
- Create and improve your own Personal Software Process
</td>
</tr>
<tr valign="top">
<td markdown="span">
Communication
</td>
<td markdown="span">
One of the main causes of unsuccessful projects is poor communication.
</td>
</tr>
<tr valign="top">
<td markdown="span">
Anti-Patterns for Developers
</td>
<td markdown="span">
[10 practices of highly ineffective software developers](https://www.infoworld.com/article/2615765/application-development/10-practices-of-highly-ineffective-software-developers.html) on InfoWorld
</td>
</tr>

</table>

---
Project & Task Boards

- [Trello](https://trello.com)
- [Asana](https://asana.com) 
- Github "Project Boards" (cards are a bit limited as to what you can record)
- [7 Scrum Software Tools สำหรับใช้บริหารจัดการโปรเจค](https://www.borntodev.com/2020/02/20/scrum-software-tools/) (Thai)
- Note: task board must to viewable by TAs and instructor!

Good places for final project documentation:
* Github pages - can be created from files in a specified directory or branch of your project repository.
* readthedocs.io
* swagger.io - mainly for API and programmer docs

Everyone should know how to use Markdown. It's the *lingua franca* of online project docs.

----

### Software Engineering and Skills that Startups Need

In the [IEEE Spectrum](https://spectrum.ieee.org/the-institute/ieee-member-news/software-engineering-grads-lack-the-skills-startups-need), 
software engineer Nitish Devadiga says that 
startups need graduates who can build scalable systems for distributed, data-intensive apps using cloud computing.
But, software engineering programs emphasize traditional skills like software processes, analysis, and project management. 

At startups, engineers participate in a broad variety of work including market research, new product ideas, designing system architecture, and cost-effective development.
Iterative development and rapid time to market are important to a startup's survival.  Startups also depend on cloud resources.

"*When you join a startup, there's a lot of emphasis on design of the application, reusability and clean code, and the ability ot conduct and undergo code reviews, as well as the ability to think of and build systems that can scale...*", Devadiga says.
A "*practical understanding of infrastructure architecture design patterns, DevOps, and cloud platform services like compute instances, object storage, and queueing services*" also helps, he says

His view is biased since he is principle engineer at a startup specializing in data analytics.

IEEE lists [free online resources](https://spectrum.ieee.org/the-institute/ieee-member-news/educational-resources-that-get-students-up-to-speed-on-advanced-manufacturing-and-programming-languages) students can use to supplement their education.
