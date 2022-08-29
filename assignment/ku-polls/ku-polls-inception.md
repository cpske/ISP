---
title: KU Polls Project Inception
---

Everyone will implement a Django application for conducting a poll or survey.  You will apply an *iterative and incremental development* process. 

The first iteration implements the Django tutorial project, so you can do Iteration 1 as you study the tutorial. 

In this assignment (Project Inception), you will create:
- a *Vision Statement* for the product
- initial set of *Requirements*
- a *Development Plan*
- "infrastructure" you will use for development

Even if you have no experience writing web apps,
by doing this *incrementally* you'll find it's easy to learn and the work is managable.


## Project Inception

1. Create a public repository named `ku-polls` in **your own** Github account.

2. Initialize the repo with a `README.md` and `.gitignore` (for Python).

3. `README.md` is the first page a visitor sees.  It should answer these questions:
   - what does this application do?
   - how do I install and run it?
   - where to look for more info?
   Start on the 1st and 3rd items now.

4. In with Wiki, create a `Home` page (a conventional name) that is the default landing page and contains links to other Wiki pages.  This is how people find things in your Wiki.  
   - Write a short explanation of what the Wiki is for.
   Add links to these pages (even though the pages don't exist yet):
   - Vision
   - Requirements
   - Development Plan
   The Github Wiki syntax for a link to another wiki page is `[[Page Title]]`.
   - After you create links in Home, you create a wiki page by clicking on its link.

5. Create a `Vision Statement` 
   - Create a Vision that describes the purpose of the project, who is affected, how the product will benefit them, and the major features of the product
   - this is a rare instance where it is OK to copy text from the example KU Polls Vision. You can customize it, but it must be accurate. (*See class example for ku polls.*)
   
5. `Requirements` - list of the major requirements and features of the product 
   - OK to copy text from the class example and customize it, but it must be accurate.

6. `Development Plan` - same instructions as Requirements.


Example README.md:

```
## Online Polls And Surveys

An application for conducting online polls and surveys based
on the [Django Tutorial project][django-tutorial], with
additional features.

Written as part of the [Individual Software Process](
https://cpske.github.io/ISP) course at Kasetsart University.

## Install and Run

to be added.

## Project Documents

All project documents are in the [Project Wiki](../../wiki/Home).

- [Vision Statement](../../wiki/Vision%20Statement)
```

### Project Infrastructure

Start the "infrastructure" you will use:

1. `.gitignore`
   - you can start with Github's .gitignore for Python projects, or create your own. 
   - should ignore pycache dirs, IDE files, MacOS junk, the default database (db.sqlite3), `.env`, virtual env directories "env" and "venv", log files, and anything you can *recreate* from source, such as Django's 'staticfiles' directory.
   - For ideas, look at the .gitignore from assignments in this course.

2. **Wiki** for project documents.
   - you created this above

3. **Project and Task Board(s)**. Include:
   - Product Backlog of features to implement
   - Iteration Backlog of features for an iteration (do this at the start of each iteration)
   - Define useful fields and tags for your project board
   - In the new Github Projects, you can create an "Iteration" field to your project.  If you do that, you can create a Project Board for each iteration by *filtering* the project tasks for a specified iteration value.

---

## Description of Documents

### Vision Statement

Vision should be short and realistic; avoid adding idealistic, wishful, or unrealistic features you won't implement.

A Vision includes:
- Background information
- Description of the problem and who is affected
- Vision of the solution
- How stakeholders will benefit from the solution
- Business case or value proposition of the project

A good Vision is ***visual***.  It's good to include images or mock-up of what you intend to produce.

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
* Written as complete sentences with good English!

Avoid writing implementation details as requirements.

### How To Use a Github Wiki

Don't put documents in your source repo -- put documents in a project wiki. A good example is the Microsoft [VS Code Project](https://github.com/microsoft/vscode). Their wiki is *massive*.

1. Demo in class.  
2. [About Wikis](https://docs.github.com/en/github/building-a-strong-community/about-wikis) on Github has a good intro.
3. To create a link to a new or existing wiki page, you open an existing page (e.g. Home) and write the link like this: ``[[Title of Page]]``. Save the page. 
   - If the link is to a **new** page, the link text will be <font color="red">red</font>. Click on the link to create the wiki page!
   - If the link is to a wiki page that already exists, it looks like a normal hyperlink.

4. In a wiki page, create links to the world-wide web using standard Markdown: `[text to display](path-or-url)`
5. Recommended way to add images to wiki pages
   - Best is to use a dedicated folder named `images/` inside the wiki for images. But it's not easy to create this.
   - if you can't do this, just use the GUI image button (in wiki editor) to upload a file and add a link to it.

### Link from README.md to a wiki page

To refer to a wiki page from your project README.md, use a link like:
```
[Wiki Home](../../wiki/Home)
```

Why the weird path `../../wiki/Home`?

- `./wiki/` is a subfolder of your repository that is a *separate* Git repo for the wiki.

- When Github displays the repo's README.md on the web, it has a URL like: 
   ```
   https://github.com/username/repo-name/blob/master/README.md
   ```
- Notice the `master/blob/` part.  To get back to the base folder of your repo (where `wiki` is) you need to go up the directory tree 2 levels: `../../`
- `../../wiki/` means "go up 2 levels, then into directory `wiki`".

Avoid using the absolute path to the wiki in hyperlinks -- it may not work is some contexts and will break if you move, clone, or rename the repo.


If a wiki page name (the filename) contains a space, in links write the space as `%20` (same as used in web URLs) such as 
```
[Vision Statement](../../wiki/Vision%20Statement)
```

---

## Resources

[Documenting your projects on Github](https://guides.github.com/features/wikis/). What should be in your README and in what order. How to use a Wiki.

[Relative Links in READMEs](https://help.github.com/articles/adding-images-to-wikis/)    
[Adding Images to Wikis](https://help.github.com/articles/adding-images-to-wikis/)
