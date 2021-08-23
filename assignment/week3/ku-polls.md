---
title: Assignment - Vision and Requirements for KU Polls
---

Everyone will implement a Django application for conducting a poll or survey.  

This week, get started creating a repository, a wiki,
writing a *Vision Statement*, an initial set of *Requirements*
based on the class vision (online),
and have them reviewed by someone.

In the first iteration or two, the application will look 
like the Django tutorial project,
but we will add additional features and improve the design.
Even if you don't have experience writing web apps,
by doing this *incrementally* you'll find the work is managable
and not too hard.

## This week's assignment

1. Create a public repository named `ku-polls` in **your own** Github account.
2. Add a **README.md** that briefly describes that the project and has links to your product docs. 
   - README.md should contain links to the Wiki pages for Home, Vision Statement, and Requirements.
3. Add a `.gitignore`. During repo creation you can select Github's `.gitignore` for Python projects, then customize it such as ignoring IDE files and (later) virtual environments.
4. Add a **Wiki** to your repository.  The wiki is for your project documents.  The Wiki should contain these 3 files:
   - `Home` - default landing page. It contains links to other wiki pages.
   - `Vision Statement` - vision of the product (be realistic). You can borrow material from the class Vision Statement, but try to improve it.
   - `Requirements` - a specification of the initial requirements.
5. When you are done, schedule an online review with a TA or instructor.
   - Use Google sheet to schedule a time, or contact the TA by other means.

**TA is not your personal editor**. You should check your files for correctness first.

### Details

### Vision Statement

You can use the class vision statement, which we will update later.
Vision should be short and realistic, so avoid adding idealistic features
you can't implement.

A Vision should be **visual**.  You can add an image of the solution.

### Requirements 

Many Agile projects write requirements as "user stories", 
but for now we will use the old fashion list of functional and non-functional requirements.

Write the requirements as a list, based on what you can infer from the class Vision and
discussion in class.  
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
* written as complete sentences with good English!

We will discuss some guidelines for a good requirement in class.

Avoid writing implementation details as requirements.

### Use a Wiki for Documents

Advantages of using a Wiki instead of the repository itself are:

* If documents are in the repo, then every time you change a document it creates a new commit that clutters your repo history.
* When you clone or "pull" the repo, you have to download all the project docs, too.
* Editing files and adding hyperlinks in a wiki is easier than using Markdown docs in the repository.
  - Github wikis support Markdown, reStructured Text (rst), and many other mark-up languages; you can do complex formatting of docs.

The Microsoft [VS Code Project](https://github.com/microsoft/vscode) uses a wiki for project plans and other project docs.  The wiki is **massive**.

## How To Use a Github Wiki

1. Demo in class.  
2. [About Wikis](https://docs.github.com/en/github/building-a-strong-community/about-wikis) on Github.
3. In a wiki, you create hyperlinks to the world wide web using the same syntax as in README: `[text to display](path-or-url)`
4. To create a link **to another wiki page**:
   - In an existing wiki page (Home) Use MediaWiki-style links like this: `[[Title of Page]]`.
   - Then view the wiki page (Home). The link text will be <font color="red">red</font> if the page doesn't exist yet.
   - Just click on the link to create a new wiki page!

5. Recommended way to add images to wiki pages
   - Best way is to use a dedicated folder named `/images/` inside the wiki for images (not easy to create this).
   - advise from Github isn't very good
   - if you can't do this, just use the GUI image button (in wiki editor) to upload a file and add a link to it.

### Link from your project README.md to a wiki page

To refer to a wiki page from your project's README.md,
use a link like:
```
[Wiki Home](../../wiki/Home)
```

Why this weird path?

- The current version of README.md on the master branch has URL: ``https://github.com/username/repo-name/blob/master/README.md``. 
- The wiki is a (undocumented) subfolder of your repo:
  ```
  https://github.com/username/repo-name/wiki/
  ```
  But, you should avoid using the absolute path to the wiki in hyperlinks -- it may not work is some contexts and will break if something is moved.
- Use a relative path to wiki. README is at ``/repo-name/blob/master/`` hence to get to the wiki directory you must **go up** 2 directories.  The relative path is therefore ``../../wiki/`` and append the filename, e.g. ``../../wiki/Home``.
- If a filename contains a space, write the space as `%20` (as in html hyperlinks), such as ``../../wiki/Vision%20Statement``.
   https://github.com/fatalaijon/ku-polls/wiki
   ```

## Looking Ahead

The first iteration or two of this project is based on the Django Polls tutorial application.  Development work will be done in a branch (not master).

To preview the project or get started, see:

 * [Django Home](https://www.djangoproject.com/) and [Django Getting Started](https://www.djangoproject.com/start/)
 * [Django Polls App, part 1](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)

[Documenting your projects on Github](https://guides.github.com/features/wikis/) advise for 
  * what should be in your README file, and in what order?
  * using a Wiki
  * glaring omission: the guides **does not** tell you how to create links from README to a wiki doc, or from a wiki doc to a project file in the repo.


## Resources

[Relative Links in READMEs](https://help.github.com/articles/adding-images-to-wikis/)    
[Adding Images to Wikis](https://help.github.com/articles/adding-images-to-wikis/)
