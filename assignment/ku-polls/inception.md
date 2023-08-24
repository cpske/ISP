---
title: KU Polls Project Inception
---

Everyone will implement a Django application for conducting poll and surveys, called "KU Polls".  In the lab, you will perform project initialization and some project inception activities.

## 1. Setup Project Infrastructure

1. Create a public repo named `ku-polls` in **your own** Github account.

2. Repo should have (at least) these files:
   ```
   README.md
   .gitignore        # configured for a Python project
   requirements.txt  # list of Python packages that this project depends on. No excess junk.
   ```

3. **README.md** should answer these questions:
   - what does this application do?
   - how do I install and run it? (write this later)
   - links to other info. Include links to these wiki documents:
     - Vision Statement
     - Development Plan
     - Iteration 1 Plan
   An *example* repo is given in class. You **may not** copy it, but you can copy some text and may copy the Vision Statement (in wiki).

4. **`.gitignore`** should ignore pycache dirs, IDE files, MacOS junk, `.env`, "env" and "venv" (virtual environments), log files, and anything you can *recreate* from source, such as Django's 'staticfiles' directory.

4. Create a **Wiki** as part of your `ku-polls` repo. You can create and edit Wiki pages in a web browser.In the Wiki, A wiki is actually a separate repo inside your main repo.    
   The Wiki should have these pages (with links in README.md):
   `Home` (conventional name) is the default landing page and contains links to other Wiki pages. People should be able to find all project docs from Home.
   - Write a short explanation of what the Wiki is for.
   - `Vision` describes the purpose of the project, who is affected, how the product will benefit them, and the "business case" for the project.
   - `Requirements` - a list of the major requirements and features of the product. You should separate *functional requirements* from *non-functional requirements*. **Requirements must be updated over time (each week).**
   - `Development Plan` - schedule of how/when you'll implement the features, with goals

### How to Create Wiki Pages?

The idea is this: in an existing wiki page you create a link to a page that doesn't exist yet.
Then click on the link. Github will prompt you to create the page!

The wiki link is text inside double brackets like this `[[Page Title]]`.

### How to Refer to Wiki Pages in a Project README

Example README.md:

```
## Online Polls And Surveys

An application to conduct online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

This app created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Install and Run

to be added.

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)

[django-tutorial]: TODO-write-the-tutorial-URL-here
```
Avoid using the absolute path to a wiki page in hyperlinks from README. The link will break if you ever move, clone, or rename the repo.
See [Relative Links in READMEs](https://help.github.com/articles/adding-images-to-wikis/).

## 2. Project Inception

After initializing the infrastructure, create important documents that describe this project:

- Vision Statement
- Requirements
- Project Development Plan

> To be discussed in lab.

---

### Vision Statement

A Vision statement describes the purpose and indented goal of the project.
A Vision is indented to unify everyone's understanding of the purpose, who is affected, and what the intended outcome is.
Vision should be short and realistic.

A Vision includes:

- Background information
- Description of the problem and who is affected
- Vision of the solution
- How stakeholders will benefit from the solution
- Business case or value proposition of the project
- A good Vision is ***visual***.  Desirable to include images or mock-ups of what you intend to produce.

A popular template for a short Vision statement
is [this one](https://www.atlascode.com/blog/creating-a-software-product-vision-statement/).

Most projects write a more detailed Vision that is several pages long. 
[Advantis](https://www.edvantis.com/blog/project-vision-in-software-development/) has good suggestions on how to create a software project vision.


### Requirements 

Write requirements as a numbered list, based on what you read in the class Vision and discussion.
As a developer, try not to invent your our requirements.

Many projects write requirements as User Stories or Use Cases. We're not doing that here.

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

Avoid writing implementation details as requirements.

### Software Development Plan or Development Plan

*See the example project -- don't copy the text items below as header names!*

SDP *aka* "Development Plan" or "Project Plan" should include:

1. Brief description of what will be produced. Refer to Requirements & Vision instead of duplicating details.
2. Timeline or Schedule 
   - how long is project? how long are iterations? 
   - table: an initial schedule for when to implement the the major features
   - this may change, but you need an initial estimate so people can see if your plan is reasonable and feasible
   - Goal or Milestone for each iteration (these may change over time)
3. Software Process you will use
   - briefly describe process (Iterative & Incremental)
   - How to manage work products (use git and Github Flow).
   - Quality assurance plan - what testing and review will you do?
4. Technology and Tools
   - Significant technologies you will use. Include frameworks.
5. Resources you need (OK to omit for this project)
   - How many people? (for this assignment -- just you)
   - Computing resources required: cloud service? CI server? database?

### Iteration Plans

You should have an iteration plan (separate file) for *each iteration*.  You will do this as homework.

The iteration plan includes:
- goal for the iteration
- feature(s) to implement and other work to be done
- a milestone
- evaluation criteria

---

### How To Use a Github Wiki

A wiki is a good location for project documents. 
A good example is Microsoft [VS Code Project](https://github.com/microsoft/vscode).

[Documenting your projects on Github](https://guides.github.com/features/wikis/) describes what should be in your README and in what order.

> Demo in class

[About Wikis](https://docs.github.com/en/github/building-a-strong-community/about-wikis) on Github has a good intro to wiki features.

Links:
* To link to another wiki page, open an existing page (e.g. Home) and write the link as: ``[[Title of Page]]``. Save the page. 
  - Click on the link to create the wiki page!
  - If the link is to a wiki page that already exists, it looks like a normal hyperlink (not <font color="red">Red</font>).
* To link to the world-wide web use standard Markdown: `[text to display](path-or-url)`

Images: 
- Best is to use a dedicated folder named `images/` inside the wiki for images. But it's not easy to create this.
- simplest is just use the GUI image button (in wiki editor) to upload a file and add a link to it.

---



[Adding Images to Wikis](https://help.github.com/articles/adding-images-to-wikis/)
