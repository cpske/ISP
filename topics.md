## Introduction to Software Process

* What is a software process, and what are its components.
* All devs have a software process, whether they realize it or not.
* (Maybe later) Overview of some common software processes.
* "Agile" is *not* a software process. "Agile" describes values, goals, and some practices incorporated into many software processes.
* The problems of software development that drive the need for a good software process:
  - complexity
  - change
  - (high) defects and errors
  - lack of predictability or consistency
  - (un)maintainability
* Jittat's slide: 3 dimensions of "Build the Right Product", "Build the Product Right", "Build it Fast".  This course focuses on skills and habits to help you "Build it Right".
  - A side-effect (maybe) is you can build *faster* and be more adaptive to change (so you build the right product). 

## Focus of this Course

* Focus on software process related skills, knowledge, habits, and personal characteristics that will help you as professional dev.
* Learn how software companies in Thailand develop software, and what skills, knowledge, characteristics their managers find important.


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

### 8. Logging

Professional, production code usually has some form of logging.
You can't just print to the console -- there may not even be a "console".

### 9. Basics of Security

Like logging, this is an important part of real code that student
programmers tend not to think about.

### 10. Deployment

* How to deploy applications?
* Creating a portable deployment.
  - Docker for containers, or VM images.
* Documenting build, dependences, and deployment.
* Deploying to the "cloud".

### 11. Measuring Progress and Quality

* How to measure your output?
* Common software metrics, like LOC, functions, code "units".
* Classify and count defects.  Design defects, coding defects, test defects.

### Estimation

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


## Application

To apply all of this, design and develop an application.

For learning value, writing a web app using a framework may be most valuable.

But, some of what we learned is hard to apply when you are working with a new framework, language, or problem domain. Estimates and defects will be worse when working with something unfamiliar.


