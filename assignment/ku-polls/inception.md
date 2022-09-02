---
title: KU Polls Project Inception
---

Everyone will implement a Django application for conducting poll and surveys, called "KU Polls".  In this assignment you will perform project inception and some project initialization activities.

In Project Inception you will create:

- a *Vision Statement* for the product
- initial set of *Requirements*
- a *Development Plan*

For project initialization, set up some "infrastructure":

- Github repository with standard files
- Wiki for project documents
- Github Project for recording Backlog and tasks


## Project Inception

You'll write the Vision and other project docs in a Wiki, so create a Github
repo first, with a README.  (You can clone it later.)

1. Create a public repository named `ku-polls` in **your own** Github account.

2. Initialize the repo with a `README.md` and `.gitignore` (for Python).

3. `README.md` is the first page a visitor sees.  It should answer these questions:
   - what does this application do?
   - how do I install and run it?
   - where to look for more info?
   Start on the 1st and 3rd items now.  
   - *See below for example README*. 

4. In the Wiki, name the first page `Home` (a conventional name); this is the default landing page and contains links to other Wiki pages. People should be able to find all project docs from Home.
   - Write a short explanation of what the Wiki is for.
   Add links to these pages (even though the pages don't exist yet):
   - Vision
   - Requirements
   - Development Plan
   The Github Wiki syntax for a link to another wiki page is `[[Page Title]]`.
   - After you create links in Home, you create a wiki page by clicking on its link.

5. Create a `Vision Statement` 
   - Create a Vision that describes the purpose of the project, who is affected, how the product will benefit them, and the major features of the product
   - this is a rare instance where it is OK to copy text from the example. You can customize it, but it must be accurate. (*See class example for KU Polls.*)
   
5. `Requirements` - list of the major requirements and features of the product 
   - OK to copy text from the class example and customize it, but it must be accurate.

6. `Development Plan` - same instructions as Requirements.


Example README.md:

```
## Online Polls And Surveys

An application for conducting online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

App created as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Install and Run

to be added.

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)

[django-tutorial]: TODO-write-the-tutorial-URL-here
```

### Project Infrastructure

Start the "infrastructure" you will use:

1. `.gitignore`
   - start with Github's .gitignore for Python projects, or create your own. 
   - should ignore pycache dirs, IDE files, MacOS junk, `.env`, virtual env directories "env" and "venv", log files, and anything you can *recreate* from source, such as Django's 'staticfiles' directory.
   - For ideas, look at the .gitignore from assignments in this course.
   - Normally you would ignore the database (db.sqlite3) but for easy of grading your work, please include the database in Iteration 1.  
   - You'll delete it from git after you create a *fixture* for initialization data. (Iteration 2 or 3.)

2. **Wiki** for project documents.
   - you created this above

3. **Project and Task Board(s)**. 
   - Define columns and fields you want.
   - *Suggestion*: Add a field for `Iteration` in Project "Settings".
     > If you have an `Iteration` field and assign tasks/backlog to an iteration (1, 2, ...), then when you create a Task Board for an iteration you can apply a *filter* so that the Task Board includes only items that match a particular value of `Iteration` (field). 
   - Add Product Backlog of features to implement
   - *At the start of each iteration:* refine the Backlog and add additional tasks you discover

---

## Description of Documents

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
Other projects write a detailed Vision that is several pages long. [Advantis](https://www.edvantis.com/blog/project-vision-in-software-development/) has good suggestions on how to create a software project vision.

### Requirements 

Write requirements as a numbered list, based on what you read in the class Vision and discussion.
As a developer, try not to invent your our requirements.

Projects often write requirements as User Stories or Use Cases. We're not doing that here.

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

### Software Development Plan

*See the example project -- don't copy text of items 1-4 as header names!*

SDP *aka* "Development Plan" or "Project Plan" should include:

1. Brief description of what will be produced. Refer to Requirements & Vision instead of duplicating details.
2. Timeline or Schedule 
   - how long is project? how long are iterations? 
   - table: your initial plan for when to implement the major features
   - this can change over time, but you need to make an estimate so people can see if your plan is at all reasonable
   - goal or milestone for each iteration (can change over time).
3. Software Process you will use
   - briefly describe process (Iteration & Incremental)
   - How to manage work products (use Github Flow). Important!
   - Quality assurance plan - what testing and review will you do?
4. Technology and Tools
   - Significant technologies you will use. Include frameworks.
5. Resources needed (OK to omit for this project)
   - How many people? (for this assignment -- just you)
   - Computing resources required: cloud service? CI server? database?


### How To Use a Github Wiki

A wiki is a good location for project documents. 
A good example of an extensive, long-running project wiki is the Microsoft [VS Code Project](https://github.com/microsoft/vscode). 

[Documenting your projects on Github](https://guides.github.com/features/wikis/) describes what should be in your README and in what order. How to use a Wiki.

1. Demo in class.  
2. [About Wikis](https://docs.github.com/en/github/building-a-strong-community/about-wikis) on Github has a good intro.
3. To create a link to another wiki page, open an existing page (e.g. Home) and write the link as: ``[[Title of Page]]``. Save the page. 
   - If the link is to a **new** page, the link text will be <font color="red">red</font>. Click on the link to create the wiki page!
   - If the link is to a wiki page that already exists, it looks like a normal hyperlink.
4. Links to the world-wide web use standard Markdown: `[text to display](path-or-url)`
5. To add images to wiki pages:
   - Best is to use a dedicated folder named `images/` inside the wiki for images. But it's not easy to create this.
   - if you can't do this, just use the GUI image button (in wiki editor) to upload a file and add a link to it.

### Link from README.md to a wiki page

To refer to a wiki page from your project README.md, use a link like:
```
[Wiki Home](../../wiki/Home)
```

Why the weird path `../../wiki/`?

- `./wiki/` is a subfolder of your repository that is a *separate* Git repo for the wiki.

- When Github displays the repo's README.md on the web, it has a URL like: 
   ```
   https://github.com/username/repo-name/blob/master/README.md
   ```
- Notice the `blob/master/` part.  To get back to the base folder of your repo (where `wiki` is) you need to go up the directory tree 2 levels: `../../`
- `../../wiki/` means "go up 2 levels, then into the directory `wiki`".

Avoid using the absolute path to the wiki in hyperlinks from README -- it may not work is some contexts and will break if you move, clone, or rename the repo.

If a wiki page name (the filename) contains a space, in links write the space as `%20` (same as used in web URLs) such as 
```
[Vision Statement](../../wiki/Vision%20Statement)
```

---

[Relative Links in READMEs](https://help.github.com/articles/adding-images-to-wikis/) 

[Adding Images to Wikis](https://help.github.com/articles/adding-images-to-wikis/)
