---
title: KU Polls Project Inception
---

Everyone will individually implement a Django application for conducting poll and surveys, called "KU Polls".  

In this lab, you will perform project set-up and inception activities.

> "*Inception*" refers to the first phase of a software project, when you learn about the project idea, its purpose and stakeholders, and decide if the project is worth pursuing.

## 1. Setup Project Infrastructure

1. Create a public repo named `ku-polls` in **your own** Github account.
   - Please spell it **exactly** this way: `ku-polls`.

2. Repo should have (at least) these files:
   ```
   README.md
   .gitignore        # configured for a Python project
   requirements.txt  # list of Python packages this project requires (only)
   ```

3. **README.md** should answer these questions:
   - what does this application do?
   - how do I install and run it? (write this later)
   - links to other docs and info. Include links to these wiki documents:
     - Vision Statement
     - Development Plan
     - Iteration 1 Plan
   An *example* repo is given in class. You **may not** copy it, but you can copy some text and may copy the Vision Statement (in wiki).

4. **`.gitignore`** should ignore pycache dirs, IDE files, MacOS junk, `.env`, "env" and "venv" (virtual environments), log files, and anything you can *recreate* from source, such as Django's 'staticfiles' directory.

5. **`requirements.txt`** lists what packages your project depends on. `pip` and other tools use this file to configure a new environment for a project.  Initially your `requirements.txt` contains only:
   ```
    Django
   ```
   There are several ways to specify required *versions* as part of requirements, for example:
   ```
   Django >= 4.1, <5.0
   ```
6. Create a **Wiki** in your `ku-polls` repo, to contain project documents and software design documents. Wiki should contain these pages:

   - **Home** is the default landing page. It should explain what the Wiki is for and have links to other wiki pages.
     - A visitor should be able to find all project docs from Home.
   - **Vision** describes the purpose of the project, who is affected, how the product will benefit them, and the "business case" for the project.
   - **Requirements** 
     1. A numbered list of the requirements and features of the product.
     2. Requirements should be written as things the program must or should do.
     3. *Functional* and *non-functional* requirements should be separate numbered lists.  I don't require any *non-functional* requirements for KU Polls, but an example would be "Written in Python using the Django web framework".
   - **Development Plan** - schedule of how/when you'll implement the features, with goals
     - Edit and personalize the Development Plan according to what you think you will actually do.

### How to Refer to Wiki Pages in a Project README

Example README.md:

```
## KU Polls: Online Survey Questions 

An application to conduct online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

This app was created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Install and Run

to be added.

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)

[django-tutorial]: TODO-write-the-django-tutorial-URL-here
```

Avoid using the absolute path to a wiki page in hyperlinks. The link will break if you ever move, clone, or rename the repo.
See [Relative Links in READMEs](https://help.github.com/articles/adding-images-to-wikis/).


## 2. Project Inception

After creating the project infrastructure, create important documents that describe this project:

- Vision Statement
- Requirements
- Project Development Plan

> This will be discussed in lab.

---

### Vision Statement

A Vision statement describes the purpose and indented goal of the project.
A Vision helps unify everyone's understanding of the goal, who is affected, and what the intended outcome is. It should be realistic.

A Vision includes:

- Background information
- Description of the problem and who is affected
- Vision of the solution
- Who are stakeholders and how they will benefit from the solution
- Business case or value proposition of the project
- A good Vision is ***visual***.  Include images or mock-ups of what you intend to produce.

A popular template for a short Vision statement
is [this one](https://www.atlascode.com/blog/creating-a-software-product-vision-statement/).
But the short form is vague and missing a lot of important details.

Most projects write a more detailed Vision that is a few pages long. 
[Advantis](https://www.edvantis.com/blog/project-vision-in-software-development/) has good suggestions on how to create a software project vision.


### Requirements 

Write a numbered list of the requirements for the KU Polls application, based on what you read in the class Vision statement and class discussion.

Requirements are things the program should do.

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

### Development Plan or Software Development Plan

*See the example project -- please don't copy the text !*

Also called "Project Plan" or "Software Development Plan". It should include:

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
   - Significant technologies you will use. Include frameworks.
5. Resources you need -- you can **omit this** for this project.
   - How many people? (for this assignment: just you) What skills?
   - Computing resources required: cloud service? CI server? database?

### Iteration Plans

You will make an iteration plan (in separate file) for *each iteration*.  You will do this as homework.

The iteration plan includes:
- goal for the iteration
- feature(s) to implement and other major work to be done.  Omit task-level work because that will be in the Task Board and we don't want duplication.
- a milestone
- evaluation criteria

---

### How to Create Wiki Pages?

The idea is: in an existing wiki page (e.g. Home) create a link to a page that doesn't exist yet.  A wiki link is text inside double brackets like this `[[Page Title]]`.

Save the page, view it, and click on the (<font color="red">red</font>) link.

Github will prompt you to create the new page!


### How To Use a Github Wiki

A wiki is a good location for project documents. 
A good example is Microsoft [VS Code Project](https://github.com/microsoft/vscode).

[Documenting your projects on Github](https://guides.github.com/features/wikis/) describes what should be in your README and in what order.

[About Wikis](https://docs.github.com/en/github/building-a-strong-community/about-wikis) on Github has a good intro to wiki features.

Links:

- To link to another wiki page, open an existing page (e.g. Home) and write the link as: ``[[Title of Page]]``.  There is also a setting to use Markdown-style links to Wiki pages. 
- To link to the world-wide web use standard Markdown: `[text to display](path-or-url)`

Images: 
- [Adding Images to Wikis](https://help.github.com/articles/adding-images-to-wikis/)


