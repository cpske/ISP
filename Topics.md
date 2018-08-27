## Introduction to Software Process

* What is a software process, and what are its components.
* All devs have a software process, whether they realize it or not.
* The problems of software development that drive the need for a good software process:
  - complexity
  - change
  - (high) defects and errors
  - lack of predictability or consistency
  - (un)maintainability

## Later: Overview of Common Software Processes

* Waterfall: the most misrepresented process.
* "Agile" is *not* a software process. 
  - Agile describes values, goals, and some practices incorporated into many software processes (see slide).
  - Created as reaction to perceived inefficiency of existing processes.
* Practices of Scrum, XP, and maybe Crystal as examples of Agile.
* "Planned Based" or "Plan Driven" compared to Agile.
  - Unified Process (UP) is main example.
  - Plan-based vs Agile process is a continuum of choices, not either-or.

Videos:
* [Agile at Microsoft](https://www.youtube.com/watch?v=-LvCJpnNljU) about the Visual Studio Team Services transition to agile. Interesting, but some fuzzy use of buzzwords like "team owns X", "team is empowered to ...". 41 minutes.
 

## Focus of this Course

* Focus on software process related skills, knowledge, habits, and personal characteristics that will help you as professional dev.
* Learn how software companies in Thailand develop software, and what skills, knowledge, characteristics their managers find important.
* Jittat's slide: 3 dimensions of "Build the Right Product", "Build the Product Right", "Build it Fast".  This course focuses on skills and habits to help you "Build it Right".
  - A side-effect (maybe) is you can build *faster* and be more adaptive to change (so you build the right product).


## Habits and Practices of a Professional Developer

* Get help from working pros.


## Useful Skills and Habits for Software Developer

### 1. Git and Github - beyond the basics. 

* Prerequisite: you should already know:
  - 2 ways to create a local git repo.
  - Concepts: local repo, remote, working copy, staging area (or "index"), commit.
  - How to check status of local repo.
  - How to add files to repo or update them.
  - Synchronize local repo with a remote repo.
* Review, if necessary:
  - Git covered in Programming 2: [Intro to Git](https://skeoop.github.io/git/intro-git) and [Github](https://skeoop.github.io/git/intro-github), [dumb slides](https://skeoop.github.io/git/)
  - [Git Basics](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) from the excellent [ProGit Book](https://git-scm.com/book/en/v2). Free PDF and ePub of *ProGit* also on [git-scm.com](https://git-scm.com/book/en/v2).
* How to view the history of a repository, and see what changed.
  - `git log`, `git log2`, `git history`, `gitk`, other visual tools
  - What is the meaning of commit ids? (`734a00b`)?  
  - Why not use `1`, `2`, `,3` for commit numbers (like Subversion)?
  - Git in Eclipse
* How to create and use branches. When to delete a branch?
  - Read Branch and Merge from ProGit: 
  - How `git push` handles branches depends on your configuration:
  ```
  git config --global push.default simple
  ```
  This is the default behavior in Git 2.0.  There are several choice with these meaning:
     * `simple` - push the current branch to upstream, but only if the upstream branch name is exactly the same
    * `upstream` - push the current branch to its upstream branch.
    * `tracking` - old, deprecated alias for `upstream`
    * `matching` - push all matching branches (branches on local that also exist on the remote)
* Use of tags
* Merging
* How to examine and fix conflicts
* Tracking work on Github
* Forking
* Github flow

### 2. Testing

* Different kinds of testing:
  - unit testing
  - function testing
  - integration test
  - system and acceptance tests

* Unit Testing
  - Using JUnit for Java
  - Why use unit testing?  How to design test cases.
  - Data-driven test cases
  - New design of JUnit 5
 
* PyUnit or UnitTest for Python.

### 3. Mock Objects for Testing

* Why use Mock objects?
* Some mock frameworks.
* Mocks and design.  As example, mock a database or external data source (a common use of mocks).

### 4. Build Tools, Build Management, and Automatic Build-and-Test

* Basic build tools: using Ant or Maven for Java.
  - maybe cover "make" and GNU make for perspective

* Build and Dependency Management Tools:
  - ant and ivy (for dependency mgmt)
  - maven
  - gradle

* Using automatic build and test with CircleCI or Travis on Github.

### 5. Reviews

* Reviews find more defects than testing, according to many studies.
* Different kinds of reviews.
* For ISP, desk check and pair reviews probably most relevant.

### 6. Clean Code, Literate Code

* Important lessons from *Clean Code* and *Code Complete*.

* Maybe look at *Practices of an Agile Developer*.  Each chapter is short and covers one lesson.  Some parts are online.

* Importance of consistent coding style.

* How to use Checkstyle. How to configure and safe a code style Eclipse or IntelliJ.

* Look at coding guidelines from some real projects. Apache is good source.

### 7. Refactoring (?)

Important topic, but not sure if I'll include it in this course.

### ?. Assertions and Design by Contract

* Reduce defects, spot defects sooner.
* In Java you can leave assertions in the final code.  They can be enabled or disabled using the run-time `-ea` flag.  You can even selectively enable assertions for some classes but not others!  
  - If assertions are not enabled, the "assert" statements are skipped so there is no performance penalty.



### 11. Measuring Progress and Quality

* How to measure your output?
* Common software metrics, like LOC, functions, code "units".
* Classify and count defects.  Design defects, coding defects, test defects.

### 12. Estimation

* How to estimate: dev time, code size.
* Jittat's Slides: [intro]( ), Jittat

* [Agile Estimation](http://www.construx.com/Resources/Presentation/Agile_Estimation__Key_Principlies_and_Practices_for_Successful_Agile_Practices/) talk by Construx (Steve McConnell's company)

### Planning and Tracking

* [Waffle](https://waffle.io) or [Trello](https://trello.com) for tasks. Wallfe integrates with Github issues.  
* Github "Project Boards" has similar features. But cards are limited to Github issues, pull requests, and notes.  May not always match project "tasks".

### 12. Tracking Your Own Performance

* How do you know you are getting better?
* You can't improve that which you can't measure.
* Task Lists and Checklists.

### 13. Self-improvement

* Importance of continual learning and reading
* See _Pragmatic Programmer_ Item 5: Your Knowledge Portfolio (p. 37).
* Goal-directed learning for new technology.  Instead of comprehensive learning or random videos.
  - "*Begin with the end in mind*" (Stephen Covey) 

### 14. Communication

### 15. Business Model  

Helps to understand the components of a software business, and forces involved.

* [Business Model Canvas Explained](https://www.youtube.com/watch?v=QoAOzMTLP5s) Youtube into to a tool for business modeling.

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

## Suggestions from SKE Graduates at TaskWorld

I put the ones I think are most important first.

### Resourcefulness

When working, they will face issues that they have never been taught.
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

Example, some people write this (JS):
    const finishedTasks = _.filter(tasks, task => task.finished)
    const unnishedTasks = _.reject(tasks, task => task.finished)

But having read through the docs, I know that we can do this instead:
    const [finishedTasks, unfinishedTasks] = _.partition(tasks, task => task.finished)

This is because I’ve read through docs of the utility library (_) proactively.

*More generally, if you are working at the edge of your knowledge you will make more mistakes
and be less productive because you didn't use some capabilities beyond the edge of your knowledge.*

## Understanding/appreciation of design principles]

I heard that students don’t get much from learning design patterns in OOP.
It feels like they had to remember class diagrams for whatever reason.
I would focus more on getting students to feel the experience of a working but unmaintainable code.
Then when design principles and patterns come to the rescue, students may have a better appreciation of them.
Refactoring katas may help.

## Understanding/appreciation of project management tools

One engineer told me that when working in a group project,
they don’t see why they have to use tools like Trello.
So the tool gets unused and problems arise.
I would focus on common communication problems that occurs when doing group projects before introducing tools, so students can associate a tool with a problem it’s intended to solve from the beginning.

## Using Git and GitHub and a Git workflow

I recommend GitHub Flow (https://guides.github.com/introduction/flow/, not the same as Git Flow), and it works in solo projects as well as team projects.
The code in master branch is live in production (automatically deployed by CI).
To not break production, a developer pushes work in progress and changes in a topic branch, opens a pull request early, reviews it, and once tested, merge it into production.
This allows for keeping the master branch stable, which is important later for working in teams.

## Others

- Good error handling practices makes debugging easier.
- Most likely, the students will have to work on assignments in other subjects, so time management is essential.
- Automated testing skills — how to write good tests. Tests should make software easier to change safely, not harder. Bad tests prevents the code from being refactored.


