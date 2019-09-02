## Why Branches and How to Use in Your Project

1. Use a branch to develop new features, so code on the master branch is always tested and runnable.  Errors on the branch don't affect code on "master".
2. Enable several people to work on different features or parts of program -- each uses his own branch.  Your changes won't conflict with someone else's changes.
3. You can release code (from master) while work is going on (in branches).

## Merging

* Merging is combining files from different branches.  
* Merging may also involve same branch from different repositories.
    - `git pull` first fetches changes from a remote (`git fetch`) and then merges them.

What can happen?

* Best case: no conflicts or overlaps.
* Conflicting changes to a file.
* Non-conflicting changes in a file (successful merge) but result is incorrect!
    - example: two people add the **same** method to a class.
    - one person adds method at **top** of file, the other adds in at **bottom**.
    - first person "pushes" his changes to Github.  No problem since he's ahead of the branch on Github.
    - second person must "pull" or "fetch" and "merge" from Github to update his version.
    - `git merge` sees that person 1 added something at top, but line range doesn't conflict with person 2's changes, so it copies in the lines.   Merge succeeds.
    - Now the file has 2 copies of the same method!

## Branches and Tracking Branches

A "tracking branch" is a local branch with a corresponding remote.
When you clone a remote repository, your local "master" branch is
set to track "origin/master" (master branch at URL nicknamed origin).

To create a local "tracking branch" for some branch that already
exists on a remote, use:
```
git checkout --track origin/branch_name
# another command that does the same thing:
git checkout -b branch_name origin/branch_name
```

To add a remote for a local branch (no remote copy yet) do:
```
git remote add 



## Bitbucket Interactive Branch & Merge Tutorial

https://www.atlassian.com/git/tutorials/learn-branching-with-bitbucket-cloud

* 30-35 minutes
* requires a (free) Bitbucket account
* you "fork" a public repo for the tutorial

## Reading: Basics of Branch and Merge

* [Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) from the online [Git Book](https://git-scm.com/book/) (download available).
* [Git Branch Command Examples](ttps://www.thegeekstuff.com/2017/06/git-branch/) shows commands for 15 common tasks
* [Git Visualizer](http://git-school.github.io/visualizing-git) type git commands and see a graph of the result! *This really helps understand git*. 

Optional:

* [Understanding Git Branches](https://www.sbf5.com/~cduan/technical/git/git-2.shtml) short article with pictures of what branch commands do.
* [Git-tips](https://github.com/git-tips/tips) how to perform common tasks in Git. 
* [How to Clone all Branches?](https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git) Stackover question with extensive explanation. Cloning and tracking remotes branches is a common problem.

## How To Use Branches in a Project?

In project work, your team should agree to and use a convention for branches and merging. For this course, use Github Flow.

* [Github Flow](https://guides.github.com/introduction/flow/)
* [Github Branching Convention](https://gist.github.com/digitaljhelms/4287848) has nice graph of using branches as in Github flow.

Please be consistent about...
* names you use for release tags.  
* names for bugfix branches.



## Questions on Branches

You should be able to answer these.  They will be on a quiz.

1. Why uses branches? (There are several uses.)

2. What is the git command to create a local branch?

3. What is the command to list the local branches?

4. What is the command to list **all** branches, including remote branches?


## Questions about Using Branches

1. What is the command to switch to a branch named "dev"?

2. Suppose you have 2 branches: master and dev.  How can you see what are the differences (diffs)?

3. What are the commands to merge "dev" into "master"?

4. Does a branch create a copy of the original branch's files?

5. What is a command to show a graphical view of the branches and commits? More than one answer to this.


## Branches and Remotes

1. If you clone a remote repository, does it clone all branches?

2. After you clone a remote, `git branch -a` shows all the branches. What happens if you try to checkout one of the branches?

3. What is the command to clone a remote branch? (Clone it *and* track the remote so you can push your work back.)


### Remote Branch Examples

* To switch between branches, use `git checkout branch_name`.  It changes the current branch and also changes your working copy to match the HEAD of the new branch.  

* "CallMeBus" from Programming 2: https://github.com/thanakritfluk/callmebus

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
Only shows "master".  Add "--all" or "-a".
```
cmd> git branch -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/add-correct
  remotes/origin/add_to_table
  remotes/origin/master
```
This means we have references ("refs") to remote branches on "origin", but no local branch that tracks them.

Suppose we want to look at the branch code.  There are 2 cases:

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

3. Somehow you screw up and you have a local copy of existing branch,
but its not tracking a remote.  You can specify the remote tracking branch:
```
git checkout some_branch
git branch --set-upstream-to  origin/some_branch
```
This doesn't seem to be needed in practice.

## References

* [Push a new local branch to a remote](https://www.freecodecamp.org/forum/t/push-a-new-local-branch-to-a-remote-git-repository-and-track-it-too/13222) on freecodecamp.org

