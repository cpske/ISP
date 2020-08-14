---
title: Git, Version Control, and Github
---

Software Version Control means managing the versions and history of software work products.

A **Version Control System** (VCS) performs:

* authenticate users
* control who can view, copy, or change files (access control)
* history of all changes with attribution (who changed it) and reason (commit message)
* ability to "check out" or "check in" several files or other changes at once as a single transaction (git *commit*)
* let's you checkout any previous version of the files -- so you never lose work
* maintains integrity of files -- does not allow corruption of files or loss of work 
  - VCS does not allow people to accidentally overwrite each other's work
  - git requires a new commit always be based on the current version of what is in the repository
* manage multiple variations (branches) of the same project, so that teams can work on different features without affecting other's work

Git is the dominant VCS in the world today, so we will focus on how to use Git. 
Other VCS are Mercurial and Subversion (a centralized VCS).

## Learning Git

Presentation: [Git Basics](Git-Basics.pdf)

Each of these covers the basics (one is enough):

[Git Basics](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository) from the excellent, free [Pro Git Book](https://git-scm.com/book/en/v2). 

[Learn Git Interactive](https://learngitbranching.js.org) interactive graphical tutorial, includes branch, merge, rebase, and more.

My [Intro to Git](intro-git) - but *Pro Git* is better.

## Understanding Git

A git repository is structured as a **graph**. The **nodes** are commits.  

Each commit includes
* time stamp
* author name and email
* message
* link to previous commit
* link to files in this commit, and other transactions (rename, delete)

Branches and HEAD are just **movable labels** referring to commits.

[Git Visualizer][GitVisualizer] type git commands and see a graph of the result! *This really helps understand git*. 

[Learn Git Interactive](https://learngitbranching.js.org) interactive graphical tutorial, includes branch, merge, rebase, and more.

## Git Branches

* [Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) from the online [Pro Git Book][Git Book]
* My [branch and merge](branch-and-merge) notes
* [Merge Practice](Merge-Practice.pdf) in class exercise


### Learn More About Branch and Merge

* [How to use local branches with remotes](https://www.freecodecamp.org/forum/t/push-a-new-local-branch-to-a-remote-git-repository-and-track-it-too/13222) article has good exmaple of working with branches, such as:
   - Push your local branch to remote (creates remote branch): `git push -u origin branch_name`
   - Create a local branch to track a remote: `git checkout -b branch_name origin/branch_name` (and then maybe `git pull` to be sure your branch is up-to-date)
   - Rename (move) a branch: `git branch -m old_name new_name`
* [Git Branch Command Examples](ttps://www.thegeekstuff.com/2017/06/git-branch/) shows commands for 15 common tasks
* [Understanding Git Branches](https://www.sbf5.com/~cduan/technical/git/git-2.shtml) short article with pictures of what branch commands do.
* [How to Clone all Branches?](https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git)  
  - This Stackover question explains the problem and soluations. 
  - Cloning and tracking remotes branches is a common issue and it's **not done** automatically when you clone a repo.

## Remotes and Github

[Remotes and Github](Using-Github.pdf) presentation and [notes](Using-Github.md)

## Navigating a Repository

[Advanced Git Tips for Python Developers][git-tips-python] has good examples of navigating a git repository and using `git stash` to save uncommited changes in your working copy.

Some useful tips:

* `HEAD~` (HEAD tilde) means "the predecessor of HEAD". Instead of HEAD, you can put any commit label, e.g. `git checkout bugfix~` for the predecessor of commit "bugfix".
* `HEAD~3` means 3 commits before current HEAD.
* `HEAD^` means a parent of HEAD, by default the first parent.
* `foo^1` and `foo^2` are parents of a commit `foo` created by a merge (commit with 2 parents).

Example use: what files did the most recent commit change?
```
 git diff HEAD^ HEAD
 # to see just the names of changed files:
 git diff HEAD^ HEAD --name-only
```

Github has nice visual tools for showing changes between any commits, 
but (of course) they are only available for the remote on Github not your local repo.

## Tags

A **tag** is a name assigned to a commit, like a bookmark, to make it easy to refer to it later.  On Github, tags are used to mark *releases* of a product.

[Git Tags](git-tag) - my notes on how to use tags.

## Git Common Use Cases

[Git-tips](https://github.com/git-tips/tips) how to perform common tasks in Git. 


* common use scenarios
  - view history of commits
  - recover deleted or mangled file
  - "undo" staging
  - "undo" a commit
  - see what has changed (diffs)
  - checkout a particular commit or a particular file
  - work with remotes - push, fetch, pull. How to add, change, and view remotes.
  
* Using Git
    - understand git as a graph of commits. This really helps.
    - use `git diff` (many forms) to see differences between last commit, stagin
    - undo a change in file in working copy
    - revise a commit, such as adding something you forget (w/o creating a new commit)
    - "undo" a commit by rolling back HEAD to previous commit
* How to view the history of a repository, and see what changed.
  - `git log`, `git log2`, `git history`, `gitk`, other visual tools
  - What is the meaning of commit ids? (`734a00b`)?  
  - Why not use `1`, `2`, `,3` for commit numbers (like Subversion)?
  - Git in Eclipse
* How to create and use branches. When to delete a branch?
  - Read Branch and Merge from ProGit: 
  - How `git push` handles branches depends on your configuration:
  ```
  git config --global push.default simple
  ```
  This is the default behavior in Git 2.0.  There are several choice with these meaning:
     * `simple` - push the current branch to upstream, but only if the upstream branch name is exactly the same
    * `upstream` - push the current branch to its upstream branch.
    * `tracking` - old, deprecated alias for `upstream`
    * `matching` - push all matching branches (branches on local that also exist on the remote)
* Use of tags
* Merging
* How to examine and fix conflicts
* Tracking work on Github
* Forking




## Github Flow - Managing Work on a Project

A git "workflow" for solo or team projects. 

* [Github Flow Illustrated Guide](https://guides.github.com/introduction/flow/) and
* [Description on Githubflow.io](https://githubflow.github.io/). Step #5 -merge only after pull request review is important! 
* [Pull Request Tutorial](https://yangsu.github.io/pull-request-tutorial/) why and how to use pull requests.
[Github Branching Convention](https://gist.github.com/digitaljhelms/4287848) has nice graph of using branches as in Github flow.
* [Commenting on Pull Requests](https://help.github.com/en/articles/commenting-on-a-pull-request) - examples of providing feedback to a Pull Request.
* Slides on Pull Requests [PDF](Pull-Requests.pdf) [PPT](Pull-Requests.ppt)


[Github Flow](https://guides.github.com/introduction/flow/)

[Github Branching Convention](https://gist.github.com/digitaljhelms/4287848) has nice graph of using branches as in Github flow.

## Specialized Git Uses

* [Git Aliases](aliases) how to create an alias for a git command, such as "git co" alias for "git checkout".

* Using Git [Submodules](submodule) to include another repository *inside* an existing Git repository tree.  Very useful for managing work, such as a separate repo for tests.




## Git Command Summary (cheatsheet)

[Git Cheatsheet](https://gist.github.com/raineorshine/5128563) Git commands in a bash shell file    
[Github Cheatsheet](/git/git-cheat-sheet.pdf) PDF file

## Resources

* [Pro Git Book][ProGit] and downloadable book [PDF][ProGitPdf]
  - online version has good navigation aids, but is *much shorter* than the book
* [Think Like a Git][ThinkLikeaGit] visually understand how Git works.
* [Visualizing Git][VizualizeGit] interactive tool is view graph of a repository.
* [Anatomy of a Git Commit](https://blog.thoughtram.io/git/2014/11/18/the-anatomy-of-a-git-commit.html) explains *what* is in a Git "commit". 

[ProGit]: https://www.git-scm.com/book/en/v2 "Pro Git online book on Git-scm.com"
[ProGitPdf]: https://github.com/progit/progit2/releases/download/2.1.245/progit.pdf
[ProGitAws]: https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf "Pro Git book v.2 PDF on AWS."
[ThinkLikeaGit]: http://think-like-a-git.net/ "Understand visually how git works"
[GitVisualizer]: http://git-school.github.io/visualizing-git/ "Interative tool draws a graph of commits in a repo"
[git-tips-python]: https://realpython.com/advanced-git-for-pythonistas/

## Good Git Questions Online

* [15 Git Questions Every Developer Should Know](https://medium.com/@gauravtaywade/15-interview-questions-about-git-that-every-developer-should-know-bcaf30409647)
* [Frequently Asked Git Questions](https://www.git-tower.com/learn/git/faq)
* [13 Essential Git Interview Questions](https://www.toptal.com/git/interview-questions)
