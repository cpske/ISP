---
title: Automation, Build Tools, and Continuous Integration
---

**Automation** is an ongoing goal in software development.
Don't spend time performing routine tasks that can be done automatically -- or "semi-automatically" by typing a single command.

Routine tasks you can automate are:

* configure and compile source code
* run tests
* compute code coverage of your tests
* examine code for potential problems, including semantic errors and unsafe usage ("*static analysis*")
* check for coding style errors
* automatically deploy software to a server
* Continous Integration: perform all the above, when triggered by some event such as a Github commit or adding a git tag containing special text


## Build Tools

**Build tools** automatically compile and test software.
This has long been standard practice among
C and Java programmers. Some of the most widely used tools are:

* [Make](Make.pdf) the original Unix build tool, still widely used today as Gnu Make and Microsoft nmake.
  - A "makefile" describes outputs, dependencies, and commands to execute to create the outputs when a dependency changes.
  - [Example Makefiles](https://en.wikipedia.org/wiki/Make_(software)#Example_makefiles) in [Wikipedia Make page][make]

* [Apache Ant](Ant.pdf) a standard build tool with special support for Java. I use Ant to compile and test student work in OOP, instead of doing it in an IDE.
  - an Ant build file is written in XML. Ant has lots of pre-defined "actions" or "tasks" that you can use to define a build file to do just about anything.
  - [Ivy](https://ant.apache.org/ivy/) is a companion project for dependency management. It automatically downloads (as needed) packages that your application depends on.

* [Maven][maven] and [Gradle][gradle] for both dependency management and project automation.
  - A build file defines other packages the a project depends on, as well as instructions to build, test, and generate documentation
  - Maven or Gradle automatically download any required packages (as needed) before building the application
  - Android Studio uses Gradle to build an Android application

* [Grunt](https://gruntjs.com) is a Javascript task runner used to automate tasks on Javascript and front-end web projects.
* Optional Demo:
   - build some complex software from source using make

* [List of Build Automation Software](https://en.wikipedia.org/wiki/List_of_build_automation_software) on Wikipedia. There are a lot!

## Example of Using a Build Tool

Example using Maven for Java.

1. Install [maven][maven-install] as ZIP file or from a repository.
2. Set the environment variable `M2_HOME` to the directory where you installed Maven. [How to for Windows][maven-windows]
3. Get the source code for the DBeaver Database browser (or Violet UML Editor)
   - Download source from https://github.com/dbeaver/dbeaver
   - Reduce download size by using `git clone --depth 1 url-to-clone`
4. Build the source.  Maven will download dependencies and build the source. The first time you use Maven it will download **a lot** of files. (Maybe 1GB) So avoid using a mobile data link.
   ```
   cd dbeaver
   mvn package    # configure and compile source code
   mvn site       # generate HTML "site" project report
   ```
5. After you have all the dependencies for a project installed you can work "offline" to avoid unnecessary downloads:
   ```
   mvn --offline package
   ```

## Static Analysis: check for potential errors and unsafe usage

Python is a dynamic language, so many errors are not discovered until you run the program. Even then, a defect may go unnoticed, or silently cause erroneous results. 

To find potential problems and improve your code style, use one or more of these tools.
For Python the top tools are:

* [Pylint](http://pylint.pycqa.org/en/latest/) checks coding style, variable and method use, potential semantic errors.
  - It uses the [PEP8][PEP8] style guide, but you can customize what Pylint checks and the rules to use.
  - Pylint is integrated in VS Code. Use Python -&gt; Select Linter and Python -&gt; Run Linter.
  - includes pyreverse UML diagram generator

* [Flake8][flake8] combines 3 tools: pycodestyle (uses PEP8), pyflakes, and McCabe complexity checker.  Analysis is similar to Pylint.  A "killer feature" is plugins. 
  - [How to invoke flake8](https://flake8.pycqa.org/en/latest/user/invocation.html)
  - [Configuration](https://flake8.pycqa.org/en/latest/user/configuration.html) to specify options, either global options or project-specific
  - [Django plugin](https://pypi.org/project/flake8-django/) for better analysis of Django projects

* [Mypy](http://mypy-lang.org/) static type checking using type hints
  - [Code examples](http://mypy-lang.org/examples.html) on Mypy home, side-by-side examples of using type hints

See [Code Quality Tools](../code-quality/code-quality-tools) for details of how to use them.

## Continuous Integration

Continuous Integration (CI) is a general term for platforms that automatically build, test, and even deploy applications.

CI automates a lot of repetitive work and improves quality by repeatedly checking and testing code, and generating notifications and reports for developers and others.

Continuous Integration tools 

* Travis-CI (integrates well with Github)
* Github Actions and Workflows - CI integrated into a Github repository
* Popular CI Platforms are:
  - Jenkins
  - Hudson (predecessor to Jenkins)
  - TeamCity
  - Cruise Control - one of the first CI, still great
  - CircleCI
* [20 Best CI Tools](https://www.guru99.com/top-20-continuous-integration-tools.html) on guru99 has nice summary
* [Comparison of 15 CI Tools](https://www.softwaretestinghelp.com/tools/24-best-continuous-integration-tool/) on softwaretestinghelp.com compares features

Some CI tools are hosted services, like Travis-CI and CircleCI.

Others CI are self-hosted, meaning you download the code and run it on your own server (typically a virtual server). Examples are Jenkins, Hudson, and Cruise Control. Travis-CI is reportedly a customized version of Jenkins or Hudson.

Class Exercise: [Travis CI Demo Project](travis-demo-project)

Good Example Projects on Github:
* [Checkstyle](https://github.com/checkstyle/checkstyle) has badges for many tools! (Java)
* [DBeaver](https://github.com/dbeaver/dbeaver) uses both Travis-CI and Github Actions + Codecy. (Java)

## How CI Works

Here's a basic description of how CI works.

* CI servers monitor a project's code in a Version Control System (VCS).  
* The CI server is notified by the VCS when some event occurs. Event can be a commit on a specified branch, a pull request, or a new Tag matching a particular pattern (such a "v-N.M" where N amd M are numbers).
* When an event occurs, the CI clones the repository and executes a build script contained in the repository.
* Each project monitored by CI has a build script that defines the required software, workflows, and steps you want the CI to perform.  
  - On Travis-CI, this script is named `.travis.yml`. 
  - For Github Actions, "workflows" are defined in `.github/workflows/*.yml` files.
* The CI creates either a virtual server or a Docker container, and configures it according to instructions in the CI script.  
* Next, the CI runs any "jobs" or other actions defined in the CI script and reports the results. Usually there is a long report for each job (on the CI server), and a notification sent to the team or VCS.
* You can make one "job" or action depend on other jobs completing successfully. For example, if all the tests run successfully then run a "job" to deploy the application.

## Assignment

Class exercise: [Travis-CI Demo Project](travis-demo-project)  

Demo CI projects: [Java sample][demo-ci]

## Learn More

[Travis-CI Tutorial](https://docs.travis-ci.com/user/tutorial/) simple 10-minute tutorial.

[CI with Travis CI](https://lab.github.com/githubtraining/continuous-integration-with-travis-ci) Github course - more detailed, uses Jekyll web site code (Ruby) and HTML

[Continuous Integration with Python: An Introduction](https://realpython.com/python-continuous-integration/) article with example on RealPython.com. Example uses CircleCI.

[demo-ci]: https://github.com/jbrucker/demo-ci
[demo-ci-python]: https://github.com/jbrucker/demo-pyci
[PEP8]: http://www.python.org/dev/peps/pep-0008/
[flake8]: https://flake8.pycpq.org
[gradle]: https://gradle.org
[make]: https://en.wikipedia.org/wiki/Make_(software)
[maven]: https://maven.apache.org
[maven-install]: https://maven.apache.org/install.html
[maven-windows]: https://docs.wso2.com/display/IS323/Installing+Apache+Maven+on+Windows
