---
title: Assignment - Vision and Requirements for KU Polls
---

Everyone will implement a Django application for conducting a poll or survey.  

This week, get started creating a repository, a wiki,
writing a *Vision Statement*, an initial set of *Requirements*
based on the class vision (online).

In the first two iterations, the application will look 
like the Django tutorial project.
Then we will add additional features and improve the design.
Even if you don't have experience writing web apps,
by doing this *incrementally* you'll find the work is managable
and not too hard.


## This week's assignment

1. Create a public repository named `ku-polls` in **your own** Github account.
2. Add a **README.md** that briefly describes that the project and has links to your product docs. 
   - README.md should contain links to the Wiki pages for Home, Vision Statement, and Requirements.
3. Add a `.gitignore` to the repository. 
   - During repo creation you can select Github's `.gitignore` for Python projects, then customize it to ignore IDE files and (later) virtual environments.
   - Look at the .gitignore from classroom assignments for examples.
4. Add a **Wiki** to your repository.  The wiki is for your project documents.  The Wiki should contain these 3 files:
   - `Home` - default landing page. It contains links to other wiki pages.
   - `Vision Statement` - vision of the product (be realistic). You can copy material from the class Vision Statement, but improve it.
   - `Requirements` - a specification of the initial requirements.
   - write requirements as a numbered list.
5. When you are done, schedule an online review with a TA.
   - Proof-read your own work on Github first.
   - There should **not be any Markdown formatting errors** when you review with TA.
   - Use Google sheet to schedule a time, or contact the TA by other means.


### Details

### Vision Statement

You can use the class vision statement, which we will update later.
Vision should be short and realistic, so avoid adding idealistic or
unrealistic features you won't implement.

A good Vision is **visual**.  You can add an image or mock-up of the solution.

### Requirements 

Write the requirements as a numbered list, based on what you read in the 
class Vision and discussion (if any) in class or with TA.
Try not to invent your own requirements.

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

## Use a Wiki for Project Documents

Don't put documents in with your source code -- put documents in a project wiki.

A good example is the Microsoft [VS Code Project](https://github.com/microsoft/vscode). Their wiki has iteration plans and other project docs.  The wiki is **massive**.

## How To Use a Github Wiki

1. Demo in class.  
2. [About Wikis](https://docs.github.com/en/github/building-a-strong-community/about-wikis) on Github has explanation.
3. In a wiki, to create a link to a new or existing page, you open an existing page (e.g. Home) and write the link like this: ``[[Title of Page]]``. 
   - Then save and view the page. 
   - If the link is to a **new** page, the link text will be <font color="red">red</font>. Just click on the link to create the wiki page!
   - If the link is to a wiki page that already exists, it looks like a normal hyperlink.
4. In a wiki page, create links to the world-wide web using standard Markdown syntax: `[text to display](path-or-url)`
5. Recommended way to add images to wiki pages
   - Best is to use a dedicated folder named `images/` inside the wiki for images. But it's not easy to create this.
   - if you can't do this, just use the GUI image button (in wiki editor) to upload a file and add a link to it.

### Link from your project README.md to a wiki page

To refer to a wiki page from your project's README.md,
use a link like:
```
[Wiki Home](../../wiki/Home)
```

### Why the weird path to wiki (`../../wiki/Home`)?

- When Github displays the current version of README.md to someone on the web, it has URL: ``https://github.com/username/repo-name/blob/master/README.md``.  Notice the `master/blob/` part.
- The wiki is a subfolder of your repo:
  ```
  https://github.com/username/repo-name/wiki/
  ```
  You should avoid using the absolute path to the wiki in hyperlinks -- it may not work is some contexts and will break if something is moved.
- Use a relative path to wiki.    
  README is at ``/repo-name/blob/master/README.md``    
  wiki Home is ``/repo-name/wiki/Home`    
  Hence to get from README to wiki directory you must **go up** 2 directories, i.e., ``../../wiki/`` and append the filename: ``../../wiki/Home``

- If a filename contains a space, write the space as `%20` such as ``../../wiki/Vision%20Statement``.  This is a standard for HTML hyperlinks.

## Looking Ahead

The first two iterations of this project is based on the Django Polls tutorial application.  Development work will be done in a branch (not master).

To preview the project or get started, see:

 * [Django Home](https://www.djangoproject.com/) and [Django Getting Started](https://www.djangoproject.com/start/)
 * [Django Polls App, part 1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

[Documenting your projects on Github](https://guides.github.com/features/wikis/) advise for 
  * what should be in your README file, and in what order?
  * using a Wiki


## Resources

[Relative Links in READMEs](https://help.github.com/articles/adding-images-to-wikis/)    
[Adding Images to Wikis](https://help.github.com/articles/adding-images-to-wikis/)
