---
title: KU Polls Project Inception
---

Everyone will individually implement a Django application for conducting poll and surveys, called "KU Polls".  

In this lab, you will perform project set-up and inception activities.

> "*Inception*" refers to the first phase of a software project, when you learn about the project idea, its purpose and stakeholders, agree on a vision for the project, and perform preliminary work to decide if the project is worth pursuing.

## 1. Setup Project Infrastructure

1. Create a public repo named `ku-polls` in **your own** Github account.
   - Please spell it **exactly** this way: `ku-polls`.
   - **Wrong**: `ku_polls`, `kupolls`, `KU-POLLS`, or any other name except as above.

2. Repo should have (at least) these files in the top-level of the repo, **not** in a subdirectory
   ```
   README.md
   .gitignore        # configured for a Python project
   requirements.txt  # list of Python packages this project requires (only)
   ```

3. **README.md** should answer these questions:
   - what does this application do?
   - what does the UI look like? (an image)
   - how do I install and run it? (write this later)
   - **links** to other docs and info. Include links to these wiki documents:
     - Vision Statement
     - Requirements
     - Project Plan, *aka* Project Development Plan
     - Iteration 1 Plan

4. **`.gitignore`** should ignore pycache dirs, IDE files, MacOS junk, `.env`, "env" and "venv" (virtual environments), log files, and anything you can *recreate* from source, such as Django's 'staticfiles' directory.

5. **`requirements.txt`** lists what packages your project depends on. `pip` and other tools use this file to configure a new environment for a project.  Initially your `requirements.txt` contains only:
   ```
    Django
   ```
   You can also specify required *versions* as part of requirements, for example (this means any version of Django between 5.1 and 5.2):
   ```
   Django >= 5.1, <5.2
   ```
6. Create a **Wiki** in your `ku-polls` repo, to contain project documents and software design documents. Wiki should contain these pages:

   - **Home** is the default landing page. It should explain what the Wiki is for and have **links to other wiki pages**. You should be able to find anything from the Home page.
     - A visitor should be able to find all project docs from Home.
   - **Vision** describes the purpose of the project, who is affected, how the product will benefit them, and the "business case" for the project.
   - **Requirements** lists the functional and non-functional requirements
   - **Project Plan** a schedule of how/when you will implement the features, with goals

   **Other Documents** that you will add during the project (you don't need to create this now):
   - `Iteration Plans` one file for each iteration, with major work to do, a goal, and a milestone
   - `Domain Model` UML diagram(s) of the domain model, with explanation
   - `Howto` summary of how to do things that you discover while doing the project. Very useful for team projects.
   - `Retrospectives` summary and action plan from your Retrospectives. For ease of review, put all retrospectives in one file.


### How to Refer to Wiki Pages in a Project README

In README.md use `../../wiki/xxx` to refer to a page in the Wiki of a project.    
For cxample
```markdown
## KU Polls: Online Survey Questions 

An application to conduct online polls and surveys based
on the [Django Tutorial project](TODO-write-URL-of-the-django-tutorial-here), with
additional features.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at [Kasetsart University](https://www.ku.ac.th).

## Install and Run

To be added.

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Project Plan](../../wiki/Project%20Plan)
```

Use the relative path to wiki pages in hyperlinks (as shown above) and avoid using the absolute path. 
See [Relative Links in READMEs](https://help.github.com/articles/adding-images-to-wikis/).

`%20` is the hexadecimal code for a space character.


## 2. Perform Project Inception

After creating the project infrastructure, create important documents that describe this project:

- Vision Statement
- Requirements
- Project Plan

> This will be discussed in lab.

---

### 2.1 Vision Statement

A Vision statement describes the purpose and indented goal of the project.
A Vision helps unify everyone's understanding of the goal, who is affected, and what the intended outcome is. It should be realistic.

A Vision includes:

- Background information
- Description of the problem and who is affected
- Vision of the solution
- Who are stakeholders and how they will benefit from the solution
- Business case or value proposition of the project

Most projects write a detailed Vision that is a few pages long. 
[Advantis](https://www.edvantis.com/blog/project-vision-in-software-development/) 
has good suggestions on how to create a software project vision.


### 2.2 Requirements 

This file contains a numbered list of functional requirements and a separater numbered list of non-functional requirements.
These are requirements for the *entire* KU Polls application, **not** a list of features for Iteration 1.

1. Functional Requirements are things the program should do. For this assignment you can use the "Main Features" from the Vision as functional requirements.
   - Functional Requirements are things the program should do, so avoid the owrk "can" in general.
   - Add any additional requirements discussed in class.

2.*Nonfunctional Requirements* as a separate numbered list. Examples:
  - Written in Python 
  - Uses the Django web framework
  - Portable. Can be installed and run on Windows, Linux, or MacOS.


Characteristics of good requirements are:

* Clear
* Consistent
* Complete
* Feasible
* Necessary
* Unambiguous
* Singular (one requirement is one thing)
* Testable
* Written as complete sentences with clear, correct English.

Many projects write requirements as User Stories or Use Cases. We're not doing that here.

Avoid writing implementation details as requirements.

### 2.3 Project Plan

The terms "Project Plan", "Software Development Plan", and "Project Development Plan" refer to the same thing.

It should include:

1. Brief description of what will be produced. Refer to Requirements & Vision instead of duplicating details.
2. Software Process (the process you will use)
   - briefly describe your process (you will use Iterative & Incremental)
   - how long are the iterations? (1 week)
   - How to manage work products? Use git and Github Flow.
   - Quality assurance plan - what testing and review will you do?
3. Timeline or Schedule 
   - table: a schedule of what to implement in each iteration
   - a goal or milestone for each iteration
   - the schedule may change, but you need an initial estimate so everyone can see if the plan is reasonable, feasible, and complete.
4. Technology and Tools
   - Significant technologies you will use, such as Python, your IDE, unittest test framework. 
   - Include frameworks (Django)
5. Resources you need -- you can **omit this** for this project.
   - How many people? For this assignment: just you 
   - What skills? For this assignment: Knowledge of Python and Django
   - Computing resources required: cloud service? CI server? database?

### Iteration Plans

You will make an iteration plan (in a separate file) for *each iteration* at the start of the iteration.

The iteration plan includes:
- goal for the iteration
- feature(s) to implement and other major work to be done.  Omit task-level work because that will be in the Task Board and we don't want duplication.
- a milestone
- evaluation criteria

---

### How to Create Wiki Pages?

The idea is: in an existing wiki page (e.g. Home) create a link to a page that doesn't exist yet.  A wiki link is text inside double brackets like this `[[Page Title]]`.

Save the page, view it, and click on the <font color="red">red</font> link to create the new page!


### How To Use a Github Wiki

A wiki is an excellent location for project documents. 
A good example is Microsoft [VS Code Project](https://github.com/microsoft/vscode).

[Documenting your projects on Github](https://guides.github.com/features/wikis/) describes what should be in your README and in what order.

[About Wikis](https://docs.github.com/en/github/building-a-strong-community/about-wikis) on Github has a good intro to wiki features.

Links:

- To link to another wiki page, open an existing page (e.g. Home) and write the link as: ``[[Title of Page]]``.  There is also a setting to use Markdown-style links to Wiki pages. 
- To link to the world-wide web use standard Markdown:   
  `[text to display](url-or-path)` such as `[Wikipedia](https://wikipedia.org)`

Images: 
- See [Adding Images to Wikis](https://help.github.com/articles/adding-images-to-wikis/) on Github.
