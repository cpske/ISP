## Why Branches and How to Use in Your Project

Agile practices include

1. Maintain runnable, potentially releasable code.
2. Release early and often.  
3. Development team works in parallel.

Branches can help you do these things.

Two examples of how to:

* [Github Flow](https://guides.github.com/introduction/flow/)
* [Github Branching Convention](https://gist.github.com/digitaljhelms/4287848) gist by J. Helms has nice graph of using branches as in Github flow.


## Basics of Branch and Merge

* [Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) from the online [Git Book](https://git-scm.com/book/) (download available).
* [Git Branch Command Examples](ttps://www.thegeekstuff.com/2017/06/git-branch/) at Geek Stuff
* [Understanding Git Branches](https://www.sbf5.com/~cduan/technical/git/git-2.shtml) 
* [Git-tips](https://github.com/git-tips/tips) how to perform common tasks in Git.
* [How to Clone all Branches?](https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git) Stackover question with extensive explanation.k


## Create or Get a Branch 

* Why uses branches? (There are several uses of branches.)

* What is the git command to create a local branch?

* What is the command to list the local branches?

* What is the command to list all the branches in a repo, including remote branches?

* What is the command to clone a remote branch?

## Using Branches

* What is the command to switch to a branch named "dev"?

* What is the command to che

* Suppose you have 2 branches: master and dev.  What are the commands to merge "dev" into "master"?

* Does a branch create a copy of the original branch's files?


* To switch between branches, use `git checkout branch_name`.  It changes the current branch and also changes your working copy to match the HEAD of the new branch.  But what happens if you have unsaved changes in your working copy when you type `git checkout ...`.

* What is a command to show a graphical view of the branches and commits? More than one answer to this.


## Branches and Remotes

* If you clone a remote repository, does it clone all branches?

* But, after you clone a remote, `git branch -a` shows all the branches. What happens

### Remote Branch Example

"CallMeBus" from Programming 2: https://github.com/thanakritfluk/callmebus

The repository has 3 branches on Github.

If we clone it:
```
git clone https://github.com/thanakritfluk/callmebus.git
```
and type:
```
cmd> git branch
* master
```
Only shows master.  Add "--all" or "-a".
```
cmd> git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/add-correct
  remotes/origin/add_to_table
  remotes/origin/master
```
But we don't have a clone of the other branches, just a reference ("ref").
There are 2 cases:

1. We just want to look at the branch code:
```
git checkout origin/add_to_table
```
this creates a detached branch.  

2. We want to commit changes to the branch:
```
git checkout -b add_to_table origin/add_to_table
```
creates a local "tracking branch".  It tracks changes to the remote branch, and can push changes to the remote branch.
