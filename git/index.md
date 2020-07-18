## Learning Git

* Git Basics [class notes](git-basics) guidelines given in class, including .gitignore [PDF](Git-Basics.pdf), [PPT]([Git-Basics.ppt)
* [Learn Git Interactive](https://learngitbranching.js.org) interactive graphical tutorial on git, includes branch, merge, rebase, and more.

### Branch and Merge

* [Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) from the online [Git Book][Git Book].
* My [branch and merge](branch-and-merge) notes.
* Merge Practice (in class): [PDF](Merge-Practice.pdf), [PPT](Merge-Practice.ppt)
* [How to use local branches with remotes](https://www.freecodecamp.org/forum/t/push-a-new-local-branch-to-a-remote-git-repository-and-track-it-too/13222) article has good exmaple of working with branches, such as:
    - Push your local branch to remote (creates remote branch): `git push -u origin branch_name`
    - Create a local branch to track a remote: `git checkout -b branch_name origin/branch_name` (and maybe do a `git pull` to be sure your branch is up-to-date)
    - Rename (move) a branch: `git branch -m old_name new_name`

* [Git Branch Command Examples](ttps://www.thegeekstuff.com/2017/06/git-branch/) shows commands for 15 common tasks

* [Understanding Git Branches](https://www.sbf5.com/~cduan/technical/git/git-2.shtml) short article with pictures of what branch commands do.
* [How to Clone all Branches?](https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git)  This Stackover question explains the problem and soluations. Cloning and tracking remotes branches is a common issue (its not done automatically when you clone a repo)..

## Using Github

* Github guidelines for this course [PDF](Using-Github.pdf), [PPT](Using-Github.ppt)

## Github Flow - Managing Work on a Project

A git "workflow" for solo or team projects.  We will use this:

* [Github Flow Illustrated Guide](https://guides.github.com/introduction/flow/) and
* [Description on Githubflow.io](https://githubflow.github.io/). Step #5 -merge only after pull request review is important! 
* [Pull Request Tutorial](https://yangsu.github.io/pull-request-tutorial/) why and how to use pull requests.
[Github Branching Convention](https://gist.github.com/digitaljhelms/4287848) has nice graph of using branches as in Github flow.
* [Commenting on Pull Requests](https://help.github.com/en/articles/commenting-on-a-pull-request) - examples of providing feedback to a Pull Request.
* Slides on Pull Requests [PDF](Pull-Requests.pdf) [PPT](Pull-Requests.ppt)

### Specific Git Uses

* [Git Aliases](aliases) how to create an alias for a git command, such as "git co" alias for "git checkout".

* Using Git [Submodules](submodule) to include another repository *inside* an existing Git repository tree.  Very useful for managing work, such as a separate repo for tests.

### Github and Continuous Integration

Github integrates with other cloud services, including CI servers and Heroku.
When you commit something to Github, it will notify the service that there is new code and the service (typically) will "pull" the new code.

You configure the services for want for each repository.

* [C.I. Integration with Github](ci-integration) my notes, incomplete

## References

### Interactive Git Visualizer

[Git Visualizer](http://git-school.github.io/visualizing-git) type git commands and see a graph of the result! *This really helps understand git*. 

[Learn Git Interactive](https://learngitbranching.js.org) interactive graphical tutorial on git, includes branch, merge, rebase, and more.


### Git Books

[ProGit Online Book](https://www.git-scm.com/book/en/v2) at [https://www.git-scm.com] read online or download PDF.  Online version has good nagivation aids, and is *much* shorter than full book but still has all the content you need.

[ProGit Book PDF](https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf) on AWS (free PDF).  This version is longer, with book-like formattingand pagination.

[Think Like a Git](http://think-like-a-git.net/) online book helps understand visually how git works.  Helps understand how to use Git.

Each Git commit is a node on a graph.  But what is in that node?  This article explains, with diagrams:

[Anatomy of a Git Commit](https://blog.thoughtram.io/git/2014/11/18/the-anatomy-of-a-git-commit.html) explains *what* is in a Git "commit".  

### Git Command Summary (cheatsheet)

[Git Cheatsheet](https://gist.github.com/raineorshine/5128563) Gist as a bash shell file.

[Hub.github.com](https://hub.github.com/) command line wrapper for git.

[Git-tips](https://github.com/git-tips/tips) how to perform common tasks in Git. 
[Git Book]: https://git-scm.com/book/

### Good Git Questions Online

* [15 Git Questions Every Developer Should Know](https://medium.com/@gauravtaywade/15-interview-questions-about-git-that-every-developer-should-know-bcaf30409647)
* [Frequently Asked Git Questions](https://www.git-tower.com/learn/git/faq)
* [13 Essential Git Interview Questions](https://www.toptal.com/git/interview-questions)
