---
title: Automation, Build Tools, and Continuous Integration
---

**Automation** is a recurring goal in software development.
Don't spend time performing routine tasks that can be done automatically, or "semi-automatically" by typing a single command.

Routine, repeatable tasks you can automate are:

* configure and compile source code
* run unit tests and other tests
* check code for coding style errors
* examine code for potential problems, including semantic errors and unsafe usage; called *static analysis*
* automatically deploy software to a server
* Continous Integration: automatically perform all the above, usually triggered by some event such as a Github commit or a tag containing special text


## Build Tools

Programmers use **build tools** to automatically build software.  This has long been standard practice among
C and Java programmers. Some build tools are:

* [Make](Make.pdf) the original Unix build tool, still widely used today as Gnu Make and Microsoft nmake.
  - A "makefile" describes outputs, dependencies, and commands to execute to create the outputs when a dependency changes.
  - [Example Makefiles](https://en.wikipedia.org/wiki/Make_(software)#Example_makefiles) in [Wikipedia Make page][make]
* [Apache Ant](Ant.pdf) a standard build tool with special support for Java. I use Ant to compile and test student work in OOP, instead of doing it in an IDE.
  - an Ant build file is written in XML. Ant has lots of pre-defined "actions" or "tasks" that you can use to define a build file to do just about anything.
  - [Ivy](https://ant.apache.org/ivy/) is a companion project for dependency management. It automatically downloads (as needed) packages that your application depends on.
* [Maven][maven] and [Gradle][gradle] for both dependency management and project automation.
  - A build file defines other packages the a project depends on, as well as build & test instructions. 
  - Maven or Gradle will automatically download any required packages (as needed) before building the application. 
  - Gradle is used in Android Studio to control the build of an Android application
* [Grunt](https://gruntjs.com) is a Javascript task runner used to automate tasks on Javascript and front-end web projects.
* Optional Demo:
   - build some complex software from source using make
* [List of Build Automation Software](https://en.wikipedia.org/wiki/List_of_build_automation_software) on Wikipedia. There are a lot!

[make]: https://en.wikipedia.org/wiki/Make_(software)
[maven]: https://maven.apache.org
[gradle]: https://gradle.org


## Continuous Integration and Project Automation

Continuous Integration tools 

* Using automatic build and test with Travis-CI on Github.
* Github's C.I. features
* Other Popular CI Platforms are:
  - Jenkins
  - Hudson (predecessor to Jenkins)
  - TeamCity
  - Cruise Control - one of the first, and still great, CI
  - Buddy
  - CircleCI
* [20 Best CI Tools](https://www.guru99.com/top-20-continuous-integration-tools.html) on guru99 has nice summary
* [Comparison of 15 CI Tools](https://www.softwaretestinghelp.com/tools/24-best-continuous-integration-tool/) on softwaretestinghelp.com compares features

Some CI tools are hosted services, like Travis-CI and CircleCI.

Others CI are self-hosted, meaning you download the code and run it on your own server (typically a virtual server), such as Jenkins and Cruise Control. Travis-CI is reportedly a customized version of Jenkins or Hudson.

[Travis CI Demo Project](travis-demo-project)

## Assignment

[Travis-CI Assignment](assignment/week7/ci-travis)  

Demo CI projects: [Java sample][demo-ci], [Python sample][demo-ci-python], [Explained](automation/travis-demo-project.md)

[demo-ci]: https://github.com/jbrucker/demo-ci
[demo-ci-python]: https://github.com/jbrucker/demo-pyci
