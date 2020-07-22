---
layout: page
title: ISP Topics
---

**Schedule** 01219245 ISP Mon 10-12, 13-16 starting 10 Aug 2020.   
**Location** class will be online with some meetings and live lectures in room E204.  Location of online meeting will be announced before class starts.

<table border="0">
<tr valign="top">
<th width="25%">Topic</th>
<th width="75%">Description</th>
</tr>

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
[Software Processes](software-process)
</td>
<td align="left" markdown="span">
An introduction to software process concepts, goals, and practices. The Waterfall process as a simple linear (and still widely used) process, the Unified Software Develop Process (UP) as a good model for iterative and incremental processes, and Scrum for small team projects.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
[Agile Principles and Practices](agile)
</td>
<td align="left" markdown="span">
Agile describes a set of values, principles, and practices for software development,
that emphasize frequent delivery of running software, customer collaboration, 
and self-managing teams.  The values and principles can be incorporated into any
development process.
</td>
</tr>

<tr valign="top">
<td align="left" markdown="span">
## Scrum
[Scrum](agile/index#scrum)
</td>
<td align="left" markdown="span">
Scrum is a set of Agile practices for iterative development. Scrum focuses on
develop activities and can be incorporated in many software (or non-software) projects.
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
We study unit testing concepts and testing in Java (JUnit) and Python (unittest and doctest).
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

</table>

--------------------------------------------------------------------

### Developer Skills
 - review of OOP fundamentals in Python (assessment exercise)
 - coding convention
 - unit testing
 - using UML




## Writing

   - How to write a project proposal
   - Writing goals, objectives, and milestones

* Velocity - computed from Story Points and actual time spent, or just time.

* The RUP framework and a few key concepts.

## Database Basics and ORM

* ORM mapping concepts.  After doing the Django tutorial, explain how
  relationships are mapped to database tables.
   - identity field as key.  Synthetic id, sequence, natural id, or compound key
   - many-to-1, 1-to-1 (not that common), 1-to-many
   - Foreign Keys 
   - cascading (cascading save, cascading delete) for foreign-key objects
   - lazy instantiation
   - object uniqueness for entities
   - 2 design patterns: DAO and Active Object
   - anti-pattern: anemic models (and fat controllers)

* Prioritizing development
   - Larman and RUP: value to customer, high risk, importance to architecture
   - Prototype to reduce risk or uncertainly about suitability


### Mock Objects for Testing

* Why use Mock objects?
* Some mock frameworks.
* Mocks and design.  As example, mock a database or external data source (a common use of mocks).

### Build Tools, Build Management, and Automatic Build-and-Test

* Basic build tools: using Ant or Maven for Java.
  - maybe cover "make" and GNU make for perspective

* Build and Dependency Management Tools:
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

### Planning and Tracking

Your project needs *at least*:

* vision statement, describing goal and "vision" of the project
* project plan - what to build and plan for what to build in each iteration
* task board for each iteration, containing tasks for that iteration and their status
* issue tracker for bugs, change requests, and more
* (desirable) burn-down or burn-up chart.  "Burn up" is similar to an "earned value" chart.

Task Boards that can also be used for iteration plans:
* Github "Project Boards" has similar features. Cards are limited to Github issues, pull requests, and notes.  These may not always match project "tasks".
* [Trello](https://trello.com)
* [Asana](https://asana.com) 


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

---

## Suggestions from SKE Graduates at TaskWorld

I put the ones I think are most important first.

### Resourcefulness

When working, developers face issues that they have never been taught.
An important skill is how to find answers.
- Understanding stack traces and logs
- Reading API docs
- Using Google to find a solution
- Asking good questions on StackOverflow

### End-to-end software life cycle

One engineer told me, when they were studying and working in a group project,
there is always the same person who will work on operations (e.g. deployment).
Ideally, a developer should be able to bring their ideas to life on their own.
Including:
- Design a solution
- Implement a solution
- Testing
- Manual deployment
- Automated testing
- Continuous integration
- Continuous deployment

### Proactiveness in understanding the fundamentals

Most software nowadays is made by glueing ready-made parts together.
When they parts don’t work as expected, if they don’t know how each part works, 
then fixing the problem is hard.
To be more effective, I sometimes go and read through the docs of fundamental things.

Many developers learn reactively and just-in-time when they need to solve a problem.
This means they only know few methods that they had to use.
When they encounter a new problem, they try to use what they know little about, and come up with a convoluted code, when there is a method that solves it more effectively.

Example, some people write this (Javascript):
    const finishedTasks = _.filter(tasks, task => task.finished)
    const unnishedTasks = _.reject(tasks, task => task.finished)

But having proactively read through the docs of the utility library (`_`), I know that we can do this instead:

    const [finishedTasks, unfinishedTasks] = _.partition(tasks, task => task.finished)

More generally, *if you are working at the edge of your knowledge you will make more mistakes
and be less productive because you don't use some capabilities beyond the edge of your knowledge.*

## Understand and appreciate design principles

I heard that students don’t get much from learning design patterns in OOP.

It feels like they had to remember class diagrams for whatever reason.

I would focus more on getting students to feel the experience of a working but unmaintainable code.
Then, when design principles and patterns come to the rescue, they may have a better appreciation of them.
Refactoring katas may help.

## Understanding and appreciation of project management tools

One engineer told me that when working in a group project,
they don’t see why they have to use tools like Trello.
So the tool is unused and problems arise.
I would focus on common communication problems that occurs when doing group projects before introducing tools, so students can associate a tool with a problem it’s intended to solve from the beginning.

## Using Git and GitHub and a Git workflow

I recommend GitHub Flow (https://guides.github.com/introduction/flow/, not the same as Git Flow), and it works in solo projects as well as team projects.
The code in master branch is live in production (automatically deployed by CI).
To not break production, a developer pushes work in progress and changes in a topic branch, opens a pull request early, reviews it, and once tested, merge it into production.
This allows for keeping the master branch stable, which is important later for working in teams.

## Other Suggestions

- Good error handling practices makes debugging easier.
- Most likely, the students will have to work on assignments in other subjects, so time management is essential.
- Automated testing skills — how to write good tests. Tests should make software easier to change safely, not harder. Bad tests prevents the code from being refactored.

