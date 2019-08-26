## Git Basics

> The answers to all these questions are in [Pro Git][ProGit] at [https://www.git-scm.com](www.git-scm.com) online book with good navigation aids, also PDF and ePub downloads. This version is *much* shorter than full book but contains all the info.
> AWS has the full [PDF of Pro Git][ProGitPdf] for download.


## Setting Up Git

There are few things you should do when setting up Git for use on a machine.  One of them is to set some configuration variables:

```
// your name and email address, which are added to commits you "push"
git config --global user.name "Bill Gates"
git config --global user.email "bill@msft.com"
// editor git should open when you need to edit something.  Or set envvar EDITOR
git config --global core.editor "mate -w"
```

## Repository as a Graph of Commits

Branches, Tags, and HEAD are just labels pointing to commits.

Try the [Git Viusalizer][GitVisualizer].

[Think Like a Git][ThinkLikeaGit] also has visual explanation of git.

## Background and Basic Information

Chapter 1 of [Pro Git][ProGit] covers these questions.
In particular, you should know what's is section _1.3 Git Basics_.


## Good Git Questions Online

* [15 Git Questions Every Developer Should Know](https://medium.com/@gauravtaywade/15-interview-questions-about-git-that-every-developer-should-know-bcaf30409647)
* [Frequently Asked Git Questions](https://www.git-tower.com/learn/git/faq)
* [13 Essential Git Interview Questions](https://www.toptal.com/git/interview-questions)

## References

* [Pro Git Book][ProGit] and downloadable [PDF][ProGitPdf]
* [Think Like a Git][ThinkLikeaGit] visually understand how Git works.
* [Visualizing Git][VizualizeGit] interactive tool is view graph of a repository.
* [references](references) for more useful documents


[ProGit]: https://www.git-scm.com/book/en/v2 "Pro Git online book on Git-scm.com"
[ProGitPdf]: https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf "Pro Git v.2 PDF on AWS. Longer, book format."

[ThinkLikeaGit]: http://think-like-a-git.net/ "Understand visually how git works"
[VisualizeGit]: http://git-school.github.io/visualizing-git/ "Online tools draws a graph of commits in a repo, as you type"

