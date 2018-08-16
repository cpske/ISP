## Git Basics

> The answers to all these questions are in [Pro Git][ProGit] at [https://www.git-scm.com](www.git-scm.com) online book with good navigation aids, also PDF and ePub downloads. This version is *much* shorter than full book but contains all the info.
> AWS has the full [PDF of Pro Git][ProGitPdf] for download.


## Background and Basic Information

Chapter 1 of [Pro Git][ProGit] covers these questions.
In particular, you should know what's is section _1.3 Git Basics_.

1. What is Git?

2. Who invented Git?

3. What is the main difference between Git and Subversion?  Subversion is great, so why switch to Git?

4. When working with Git locally, what are these?
   * Staging area
   * Working copy
   * master

5. When you modify a file and commit it to a repository, what is stored in the repository? (_1.3 Git Basics_)
   [ ] Differences between this version and previous one.
   [ ] A snapshot of the file.  The complete file, possibly compressed.

## How To Use

1. What command(s) create a new local repository for a project named `Tetris`?

2. There are 2 ways to get a local Git repo.  What is the other way?

3. How can you see what files are in the local repository?

4. How to you add files in your working	copy *to* the git repository? (2 steps)

5. How do you compare status of your working copy to the local repo?

6. The output of `git status` is verbose (but helpful!). How to get a short view of the status?

7. What is `HEAD`?



## Undoing Changes

1. Suppose you add some files to the staging area and accidentally add a file you don't want to commit (say, B.txt).  How to remove it from staging area?
```
git ___________
# to remove everything from staging area:
git ___________
```
> Note: if you have not yet committed anything then `reset` won't work.  In that case use `git rm --cached filename` which removes the file from the "index" (list of tracked files).

2. You modify a file in your working copy, but its messed up! You to reset your working copy of this file to be the most recent copy in repo? (checkout the most up-to-date revision of this file)

3. You accidentally DELETE the (tracked) file A.txt from your working copy.  How can you recover the file from the repository?


4. Even Worse! You accidentally delete some files and commit the changes! Now the files are deleted in the current Git HEAD.   How can you get back the the most up-to-date revision from git?

```
// Find the most recent commit containing the file:
git rev-list -n 1 HEAD -- filename
e4a6b2961974958a84c94ae36cde489d201b2d45
// For last 3 commits of a file use "-n 3"
// To see more detail about the commit, use "-v"
git rev-list -v -n 2 HEAD -- filename
e4a6b2961974958a84c94ae36cde489d201b2d45
tree d20c971afa4c4a2b83c6c15e00dd9c870e70813a
parent 8d3a2862282090ee50f4a11f26b333391ebb8be6
author fatalaijon <fatalaijon@gmail.com> 1534318476 +0700

    Fix #42, also add JUnit test and better Javadoc
// Now that you found the file, how to check it out? 
____________________________________
```
> Note: Git almost never really deletes anything.  There are special commands to delete branches and squash a range of commits; these commands do delete old stuff.


## View the Commit History

1. What commands show the commit history? (many answers)
   * 
   * 
   * 

2. What command shows you the files changed for each commit?


3. The history may be long.  How can you limit how much is shown?


## Viewing Changes in Your Work

1. How can you see the differences between your working copy and most recent commit?
>```git diff```

2. How do you view what **files** are staged for commit?
>```git status```

3. How do you view differences between staged files and last commit (HEAD)? Two solutions.
  * one
  * two

4. The output of `git diff` is too hard to read. Can "git" show it graphically?
> Yes. There are 3 better ways:
> * GUI tool or Eclipse EGit.
> * `git difftool`
> * `gitk`

5. How do you use `git difftool` instead of `git diff`?
   1. Type `git difftool --tool-help``` for a list of tools git can use.
   2. Choose one you like and install it. I use meld or diffuse.
   3. `git config diff.tool meld` to specify "meld" as diff tool.
   4. Use `git difftool` instead of `git diff`


## Viewing Changes in the Repository

These commands are useful for seeing what has changed.
Its much easier to do on Github or using a GUI tool like gitk, SmartGit, or EGit (Eclipse).

1. What git command shows Difference between last 2 commits.


2. How to view Difference between 2 commits, where you specify the commit ids.
   First, view the history
   ```
   # git history, git log, git log1, or gitk
   git history
   git history
   * 8d3a286 - (22 hours ago) Add some MOOCs to References - jbrucker (HEAD -> master)
   * 051c9d4 - (4 days ago) change classroom code - jbrucker (origin/master)
   * e15706f - (5 days ago) remove bad git links - jbrucker
   * e771d36 - (5 days ago) fix typo in link reference - jbrucker
   * 76105d1 - (5 days ago) intro slides - jbrucker
   ```
   Specify 2 commits to compare, separated by "..." (3 periods).
   ```
   git diff 051c9d4...e771d36
   ```


## Great Git Questions Online

* [15 Git Questions Every Developer Should Know](https://medium.com/@gauravtaywade/15-interview-questions-about-git-that-every-developer-should-know-bcaf30409647)
* [Frequently Asked Git Questions](https://www.git-tower.com/learn/git/faq)
* [13 Essential Git Interview Questions](https://www.toptal.com/git/interview-questions)

## References

[ProGit]: https://www.git-scm.com/book/en/v2 "Pro Git online book on Git-scm.com"

[ProGitPdf]: https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf "Pro Git v.2 PDF on AWS. Longer, book format."


[Think Like a Git]: http://think-like-a-git.net/ "Understand visually how git works"

[Visualize Git]: http://git-school.github.io/visualizing-git/ "Online tools draws a graph of commits in a repo, as you type"
