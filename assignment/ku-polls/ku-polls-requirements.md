---
title: Assignment - Vision and Requirements for KU Polls
---

Everyone will implement a Django application for conduction a poll or survey.  
You'll apply an *iterative and incremental* development process.

This week, get started setting up a repository,
writing a *Vision Statement*, an initial set of *Requirements*
based on the class vision (online),
and have them reviewed by someone.

In the first iteration or two, the application will look 
like the Django tutorial project,
but we will add some additional features and improve the design.
Even if you don't have experience writing web apps,
by doing it *incrementally* you'll find the work is managable
and not too hard.

## This week's assignment

1. Create a public repository named `ku-polls` in **your own** Github account.
2. Add a README.md that briefly describes that the repository is for and contains links to your product docs. 
3. Add a `.gitignore`. During repo creation you can select Github's `.gitignore` for Python projects, then customize it such as ignoring IDE files and (later) virtual environments.
4. Add a Wiki to your repository.  The Wiki should contain these 3 files:
   * Home - default landing page. It contains a description and links to other pages.
   * Vision Statement - vision of the product (be realistic). You can borrow material from the class Vision Statement. A rare instance where copying is allowed.
   * Requirements - a specification of the initial requirements.
5. When you are done, schedule an online review with a TA or instructor.
   * TA is not your personal editor. You should check your files for correctness first.
   * Use Google sheet to schedule a time, or contact the TA by other means.

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

### Why Use a Wiki for Documents?

Advantages of using a Wiki instead of the repository itself are:

* If documents are in the repo, then every time you change a document it creates a new commit that clutters your repo history.
  - you can mitigate this by putting docs in a separate branch, but the branch ref would still be changing frequently
* Editing files and adding hyperlinks in a wiki is easier than using Markdown docs in the repository
  - Github wikis support both Markdown and reStructured Text (rst) as mark-up language. You can use either.

The Microsoft [VS Code Project](https://github.com/microsoft/vscode) uses a wiki for project plans and other project docs.  The wiki is **massive**.

## How To Use a Github Wiki

Demo in class.  [About Wikis](https://docs.github.com/en/github/building-a-strong-community/about-wikis) on Github.

In a wiki, you can create hyperlinks to the world wide web using the same syntax as in README: ```[text to display](path-or-url)```

To create a link **to another wiki page**:
1. Use MediaWiki style links like this: ```[[Title of Page]]```.
2. When you view the wiki page the link text will be <font color="red">red</font> if the page doesn't exist yet.
3. Just click on the link to create a new wiki page!

* Recommended way to add images to wiki pages
   - Suggest that you use a dedicated folder named `/images/` inside the wiki for images (not easy to create this)
   - advise from Github isn't very good
   - if you can't do this, just use the GUI image button (in wiki editor) to upload a file and add a link to it.

### Link from your project README.md to a wiki page

To understand this, it helps to know a few things about URLs and Github repo:

1. You can use *relative URLs* in Markdown.  So if you want to refer to a file in the **parent directory** of the current file you can use:
   ```
   Link to [Another File](../another-file)
   ```
2. The current version of README.md on the master branch has URL: ``https://github.com/username/repo_name/blob/master/README.md``.  `/blob/master/path/somefile` can be used to refer to the current version of any file in your repo.
3. If a filename contains a space, write the space as `%20` (as in html hyperlinks).
4. Github creates a (invisible and undocumented) a `/wiki/` sub-URL of your repo URL for the wiki:
   ```
   https://github.com/fatalaijon/ku-polls/wiki
   ```
5. Combining the above, in README.md we can refer to a Wiki page named "Vision Statement" using the relative URL:
   ```
   [My Vision Statement](../../wiki/Vision%20Statement)
   ```
  notice that there is no `.md` in the filename. A wiki filename is the page title.
   

## Resources

[Documenting your projects on Github](https://guides.github.com/features/wikis/) advise for 
  * what should be in your README file, and in what order?
  * using a Wiki
  * the guides **do not** tell you how to create links from README to a wiki page, or from a wiki doc to a project file in the repo.
[Relative Links in READMEs](https://help.github.com/articles/adding-images-to-wikis/)    
[Adding Images to Wikis](https://help.github.com/articles/adding-images-to-wikis/)
