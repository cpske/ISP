---
title: Topics
navigation_order: 3
---

A collection of historical material from ISP. 
For current ISP course may cover different topics.

Please see [Google Classroom][google-classroom] for current topics & material.

[google-classroom]: https://classroom.google.com/w/NjE0ODE4Mzg4ODEz/t/all

<table border="0">
<tr valign="top"> <th width="25%">Lab Topic</th> <th width="75%">Description</th> </tr>
<tr valign="top">
<td markdown="span">
[ISP2022 Introduction](introduction/index) 
</td>
<td markdown="span">
[Introduction to course and goals](introduction/index), 
prerequisites, required work, project, and grading.    
[Advice from an SKE scholar & entrepeneur](introduction/Jomzap-Recommendations.pdf).    
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
[Git](git)
</td>
<td markdown="span">
Git commands and common tasks, structure of a git repo, branches, merging, and remote repos.    
[Visualize][GitVisualizer] a repo as a graph.    
[Use SSH Keys](https://help.github.com/articles/connecting-to-github-with-ssh/) for authentication instead of your Github password.
</td>
</tr>

<tr valign="top">
<td markdown="span">
Git and Development
</td>
<td markdown="span">
[Using Github](git/Using-Github) and [slides](git/Using-Github.pdf).    
[Github Flow](git/index#github-flow), branches, issues, &amp;
[pull requests](git/Pull-Requests.pdf).    
Github Flow is a workflow for a team to effectively work together using git.    
Importance of descriptive commit messages and Pull Requests.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Unit Testing](testing)
</td>
<td markdown="span">
Testing "units" of code.  Testing behavior - not just methods.      
[JUnit for Java](/testing/Intro-to-Unit-Testing.pdf) and 
[Unit test in Python](testing/PythonUnitTesting.pdf)    
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
Mai's [Type Hint Practice](type-hints/type-hints-practice.pdf).     
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Code Quality](code-quality)
</td>
<td markdown="span">
Principles, guides, tips, and [tools](code-quality/code-quality-tools) for writing good quality "clean" code.    
Coding standard, [docstring comments](code-quality/docstrings) and [code checkers](code-quality/code-quality-tools).
Essential for all developers!
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Refactoring](refactoring)
</td>
<td markdown="span">
Improve code by restructuring it without changing the external functionality.    
[Common refactoring situations](refactoring/Refactoring-Patterns.pdf) and how to do them using an IDE.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Assertions](code-quality/assertion)
</td>
<td markdown="span">
"Asserts" are tests of what should be true at some point in code.  Assertions reduce errors and document code-level assumptions.
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
[Code Review](code-review)
</td>
<td markdown="span">
[Software Review](code-review/Reviews.pdf) slides and [Overview](code-review)      
[Code Review Best Practices](code-review/code-review-best-practices) from experts    
[Reviews chapter from Stellman &amp; Greene](code-review/Reviews-Stellman-and-Greene.pdf)    
[Review Checklists](code-review#checklists) examples and guidance    
Assignment: Code Review Checklist and Procedure (script)
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
Web App Testing    
End-to-End Testing    
</td>
<td markdown="span">
[Web App Testing](testing/WebTesting.pdf) how to test web apps, includes E2E with Selenium.    
[Intro to Selenium](testing/Selenium-intro) and [Page Scraping](testing/Selenium-scraping).
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
[Authentication](authentication)  
</td>
<td markdown="span">
Techniques for authenticating users and software clients (apps), including OAuth.    
Django's [authentication](django/authentication) and [authorization](django/authorization) modules.
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
[UML](uml)
</td>
<td markdown="span">
The standard for visual software modeling and design.    
You should be able to understand common UML diagrams.
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
[HTTP](web/index)
</td>
<td markdown="span">
HTTP is the communication protocol used by web apps and web services.    
[Introduction to HTTP](web/HTTP.pdf)    
[HTTP in Action](web/HTTP-in-Action.pdf) class exercises using HTTP, requires ncat or netcat.    
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Web Servers and Frameworks](web/index#web-frameworks)
</td>
<td markdown="span">
[Introduction](web/Web-Apps-and-Web-Servers.pdf) to how a web server and web app typically handle requests and responses.  This helps make sense of the various components of a web framework.    
[WSGI](web/wsgi-servers) standard for connecting Python web apps to web app servers.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Django](django/django)
</td>
<td markdown="span">
[Introduction to Django](django/Intro-to-Django.pdf) and MVC design pattern.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[KU Polls Project](assignment/ku-polls/)
</td>
<td markdown="span">
A polls application based on the Django Polls tutorial, implemented as an iterative and incremental project.  Each iteration involves planning, design, implementation, testing, and review.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Database Basics](database/Database-Basics.pdf)
</td>
<td markdown="span">
Intro to database concepts and how to use a database in code.
Tables, field types, identity fields, relating tables, basic CRUD operations.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Object-Relational Mapping](database/orm)
</td>
<td markdown="span">
ORM concepts and frameworks. Different domain models and their database table schema.
All web frameworks use ORM.
Understanding ORM concepts makes it easier to understand and work
with Django models.
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
[Separate Configuration from Code](refactoring/separate-configuration)
</td>
<td markdown="span"> 
[Separate configuration from code](refactoring/Separate-config-from-code.pdf) is a good practice for all software, not just web apps.    
How to [Externalize Configuration](django/external-configuration) in Django.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Import and Export Data](django/data-import-export) 
</td>
<td markdown="span">
How to create "starter" data so that others can easily set-up and use your Django application.
</td>
</tr> 

<tr valign="top">
<td markdown="span">
[Virtual Environment](django/virtualenv)
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
Easily pass messages from a view to a template.
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
[Organize Tests & Models](django/test-organization)
</td>
<td markdown="span">
[Separate your tests](django/test-organization) and [models](django/organize-django-code) into individual files, to reduce conflicts on team projects.
</td>
</tr>

<tr valign="top">
<td markdown="span">
[Logging](logging/)
</td>
<td markdown="span">
[Logging](logging/Logging.pdf) is an essential part of a web application.   
[Logging Practice](logging/logging-practice) and [demo_log.py](logging/demo_log.py) code
</td>
</tr>

<tr valign="top">
<td markdown="span"> 
Deployment
</td>
<td markdown="span">
How to package and deploy a web application.
Manage dependencies and isolate applications in containers.
</td>
</tr>
</table>

---

## Other Topics

These may be *implicitly* covered as part of other topics.

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
[License](https://choosealicense.com)
</td>
<td markdown="span">
Understand the different open source licenses like GNU, BSD, MIT,  and Creative Commons
so you can choose one that matches what you want.    
Don't just *blindly* write "GNU" which is incomplete (should be "GNU GPL v3" or similar) and inappropriate for many projects.  The GPL can be quite restrictive!
</td>
</tr>
<tr valign="top">
<td markdown="span">
Project Tools
</td>
<td markdown="span">
Project board - a board for whole project and task board for each iteration   
Issue tracker - bugs, change requests, and more    
Burn-down or Burn-up chart (optional) - track your rate of progress    
Project wiki - good location for iteration plans, software design notebook, recording knowledge and solutions    
</td>
</tr>
<tr valign="top">
<td markdown="span">
Information Radiator
</td>
<td markdown="span">
Create **one place** that quickly conveys all useful info about your project.    
When project info (tasks, communication, docs, tools) are spread across many different places, people don't use them!    
The information radiator is **one place** that links to everything you need.
Some teams use Slack, Discord, or the Project Board as info radiator.   
*Web hooks*, *integrations*, and *badges* can be used to connect tools and notifications.     
</td>
</tr>
<tr valign="top">
<td markdown="span">
Task Boards
</td>
<td markdown="span">
Task board should be part of your workflow -- part of an *information radiator*.  Good choices are:     
[Trello](https://trello.com)    
[Asana](https://asana.com)     
[Github Project Boards](https://docs.github.com/en/github/managing-your-work-on-github/about-project-boards)        
[7 Scrum Software Tools สำหรับใช้บริหารจัดการโปรเจค](https://www.borntodev.com/2020/02/20/scrum-software-tools/) (Thai)    
Note: task board must to viewable by TAs and instructor!
</td>
</tr>
<tr valign="top">
<td markdown="span">
[Markdown](documentation/markdown)
</td>
<td markdown="span">
Everyone should know how to use Markdown. It's the *lingua franca* of online project docs. Much easier and cleaner to write than HTML.
</td>
</tr>
<tr valign="top">
<td markdown="span">
Process Improvement
</td>
<td markdown="span">
How to discover and *implement* improvements to your development process
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
[Estimation slides](estimation/Estimation.pdf) and [Prof. Jittat's Slides](estimation/06a-estimation.pdf)<br/>
Frequent question of managers and customers is "*how long will it take?*" or "*when will be ready?*"  Planning requires good estimates, but most developers are very poor at estimation.
<br/>
- How to estimate development time and code size <br/>
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
- Advise from [SKE grad @ TaskWorld](introduction/taskworld-advise)<br/>
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

[Old 2019 ISP index](2019/)

---
## Project Documentation 

Good places for project documentation:

* [Github Wiki][github-wiki] - good for all kinds of project docs, plans, designs, reference material, and retrospective summaries
* [Github pages](https://pages.github.com/) - create a static site from a specified directory or branch of your project repository
* [readthedocs.io](https://readthedocs.io)
* [swagger.io](https://swagger.io) - mainly for API and programmer docs

[github-wiki]: https://guides.github.com/features/wikis/

[GitVisualizer]: http://git-school.github.io/visualizing-git/ "Interative tool draws a graph of commits in a repo"

---

Links to test your link scanner:

- <a> "a" tag without "href"</a>
- <a href="#project-documentation">project documentation</a> "href" with page fragment only (valid reference)
- <a href="#project-and-foo-boards">project and task boards</a> "href" with page fragment only (invalid ref)
- <a href="https://www.does.not.exist">www.does.not.exist</a> href with unresolvable hostname
- <a>another linkless "a" tag</a>
