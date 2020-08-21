---
title: Git Branches
---

A git repository can contain multiple branches.
The files on each branch can be checked in/out and updated separately,
without affecting other branches.

Each branch has a name, like "master".  The name is just a ***movable label** that points to the head of the branch.

### Commands for Branches

* Create a new branch named foo:
   ```
   cmd> git branch foo
   ```
* Checkout this branch so it is your current branch:
   ```
   cmd> git checkout foo
   ```
* Create branch and checkout in one command: `git checkout -b foo`.

  Now, any commits will be added to the `foo` branch.

* Switch back to the master branch:
   ```
   cmd> git checkout master
   ```
* List branches (the "*" indicates current branch):
   ```
   cmd> git branch
   * master
   foo
   ```
* List all branches including remote branches:
   ```
   cmd> git branch -a
   ```
* Display branch history as a tree: `gitk --all`.

* Display history on command line (there are many variations):
  ```
  cmd> git log --oneline --graph --all
  ```

### Example Repositories with Many Branches

ISP 2018 "Dailigram" project. "gitk --all" shows branches and tags.

ISP 2019 "Koocook" project (Mai and friends).

VS Code https://github.com/microsoft/vscode

## Understanding Branches

A git repository is a **graph**, with commits as nodes.
Each git branch is a branch on the graph.  The branch name is a **label** that points to the head of the branch.    

Try the online [Git Visualizer](http://git-school.github.io/visualizing-git) - type git commands like "git commit", "git branch", "git checkout", "git reset" and see results on the graph. 


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

## Tracking Branches

A "tracking branch" is a local branch with a corresponding remote.
It tracks changes to the remote branch (use `fetch` or `pull` to copy), 
and can push changes to the remote branch.

When you clone a remote repository, your local "master" branch is
set to track "origin/master", meaning "master" on the remote repo named "origin".  Other branches are not cloned, by default.

To create a local "tracking branch" for some branch that already
exists on a remote repository, use:
```
git checkout  -b branch_name  origin/remote_branch_name
```
If the local and remote branch have the same name, you can write:
```
git checkout --track origin/branch_name
```
and abbreviate `--track` to `-t`.

### Create a New Remote Branch for a Local Branch

You have a branch in your local repo named `dev-food`,
but no remote branch (on origin) for it.

To create a remote `dev-food` branch and track it:
```
git checkout dev-food
# "dev-food" is the name of the REMOTE branch
git push -u origin dev-food
```
The flag `-u` is short for `--set-upstream`.

Usually you want the local and remote branch names to be the same,
but you can use a different name.

### Remote Branch Examples

* To switch between branches, use `git checkout branch_name`.  It changes the current branch and changes your working copy to match the files in the branch.  

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
this creates a **detached branch**.  

2. We want to be able to make changes to the remote branch:
```
git checkout -b add_to_table origin/add_to_table
```
creates a local "tracking branch".  

3. Somehow you screw up and you have a local copy of existing branch,
but its not tracking a remote.  You can specify the remote tracking branch:
```
git checkout some_branch
git branch --set-upstream-to  origin/some_branch
```
This doesn't seem to be needed in practice.

4. Fetch a Remote Branch and Track It

You are working on a project and a teammate asks you to review his
work on the branch `dev-auth` (an important feature!).  You don't
have that branch in your local repo yet.

What is the command to fetch `dev-auth` from origin and create 
a tracking branch for it?
```
cmd>  git checkout --track origin/dev-auth
```

### Good Collection of "How To" for Git Branching

This page has some useful Git commands for working with branches and remotes:

https://www.freecodecamp.org/forum/t/push-a-new-local-branch-to-a-remote-git-repository-and-track-it-too/13222

* Rename a branch: `git branch -m old_name new_name`  (or use `--move`)
* Delete a branch: `git branch -d branch_name  (or use `--delete`)
* Force delete a branch with unmerged commits: `git branch -d --force branch-name` (`-D` is same as `-d --force`)


## Why Branches and How to Use in Your Project?

Branches let you create separate variation of a repository that can be modified without affecting other branches.  Common uses are:

1. Use a branch to develop a new feature, so new work doesn't mess up the tested and runnable "master" branch code.  Errors on the branch won't affect other branches.
2. Enable several people to work on different features or parts of program -- each uses his own branch. 
3. Use a branch to work on bug fixes.  Once the fix is tested and verified it can be "merged" into production code.
4. You can release code (from master) while work is going on (in branches).

## Resources to Learn More

Basics of Branch and Merge

* [Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) from the online [Git Book](https://git-scm.com/book/) (download available).
* [Git Branch Command Examples](ttps://www.thegeekstuff.com/2017/06/git-branch/) shows commands for 15 common tasks
* [Git Visualizer](http://git-school.github.io/visualizing-git) type git commands and see a graph of the result! *This really helps understand git*. 
* [How to Clone all Branches?](https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git) Stackover question with extensive explanation. Cloning and tracking remotes branches is a common problem.

Extra:

* [Push a new local branch to a remote](https://www.freecodecamp.org/forum/t/push-a-new-local-branch-to-a-remote-git-repository-and-track-it-too/13222) on freecodecamp.org
* [Bitbucket Interactive Branch & Merge Tutorial][bitbucket-learn-branching] uses Bitbucket cloud. You "fork" a public repo, make changes, and merge.  30-35 minutes.  

[bitbucket-learn-branching]: https://www.atlassian.com/git/tutorials/learn-branching-with-bitbucket-cloud


## Questions about Branches

You should be able to answer these.  They will be on a quiz.

1. Why uses branches? Give 3 uses.

2. What is the git command to create a local branch?

3. What is the command to list all local branches?

4. What is the command to list **all** branches, including remote branches?

5. What is the command to switch to a branch named "dev"?

6. Suppose you have 2 branches: master and dev.  What is the command to show differences between files on those branches (diffs)?

7. What are the commands to merge "dev" into "master" (need at least 2 cmds)?

8. Does a branch create a copy of the original branch's files?

9. What is a command to show a graphical view of the branches and commits? More than one answer to this.

10. If you clone a remote repository, does it clone all branches?

11. After you clone the "master" branch from Github, `git branch -a` shows all the branches, including remote ones. What happens if you try to checkout one of the branches?

12. What is the command to clone a remote branch named `dev`? (Clone it *and* track the remote so you can push your work back.)

