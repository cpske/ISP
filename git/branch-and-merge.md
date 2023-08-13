---
title: Git Branches
---

A git repository can contain many branches.
The files on each branch can be edited & updated, without affecting anything on other branches.

Here's a git repo with 3 branches. The circles are commits (git commit):
![git branches](./git-branches.png)

## Understanding Branches

A git repository is a **graph**, with commits as nodes on the graph.
Each git branch is a branch on the graph.  The branch name is a **label** that always points to the **head** of the branch (usually the most recent commit).    

Try the online [Git Visualizer](http://git-school.github.io/visualizing-git) - type git commands like "git commit", "git branch", "git checkout", "git reset" and see results on the graph. 

*Common Mistake*: a branch name is a movable label that points to the "head" of a branch. It does not refer to the entire branch.

## Why & How to Use Branches in Your Project?

In a project use branches to...

- **work on a new feature**, so new work does not mess up the tested and runnable "master" code.  Code on one branch won't affect other branches (until you merge).
- **several people can work on features at the same time**, without conflicts. Each person works on his own "feature branch".
- **fix bugs**.  When a bug is reported, create a new `bugfix` branch to work on a fix.  Once the fix is thoroughly tested you *merge* it into the main or release branch. An extra benefit is the "bugfix" branch will contain a history of what you changed to fix the bug.
- **experiment**. Try new "proof of concept" code that may or may not be added to your project using a separate branch.

Use branches even if you are the only person working on the project!

### Commands for Branches

* Create a new branch named foo:
  ```
  cmd> git branch foo
  ```
* Checkout this branch so it is your current branch:
  ```
  cmd> git checkout foo
  ```
* Create branch and checkout in one command:
  ```
  cmd> git checkout -b foo
  ```
  Now, any commits will be added to the `foo` branch.

* Switch back to the master branch:
  ```
  cmd> git checkout master
  ```
* Show your branches (the \* shows your current branch):
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

* Display history in a terminal window (there are many options for this):
  ```
  cmd> git log --oneline --graph --all
  ```
* Usually `git log1` is an *alias* for the above command.

### Some Projects with Many Branches

ISP 2022 [WongNung][] project by your TAs (Pawitchaya & Napasakorn). "gitk --all" shows branches and tags.

ISP 2019 [Koocook][] project (Mai, Thanathorn, Chayathon) separate branch for major features.  A professional, shippable product.

VS Code <https://github.com/microsoft/vscode>. How many branches? How many commits?

[Koocook]: https://github.com/KooCook/koocook-dj/tree/dev
[Dailigram]: https://github.com/LilBank/dailigram
[WongNung]: https://github.com/WongNung/WongNung

## Merging

Merging means combining files from different branches.  

- Merging may also involve the same branch from different repositories.
- `git pull` first fetches changes from a remote (`git fetch`) and then merges them (`git merge`).

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

A **tracking branch** is a local branch with a corresponding remote branch.
Use use `fetch` or `pull` to update your local copy, and `push` to update the remote branch, to keep them in sync.

When you clone a remote repository, your local "master" branch is set to track "origin/master", meaning "master" on the remote repo named "origin".  Other branches are **not cloned** by default.

* Create a local "tracking branch" for some branch that already exists on a remote repository:
   ```
   git checkout  -b branch_name  origin/remote_branch_name
   ```

* If the local and remote branch have the same name, you can write:
   ```
   git checkout --track origin/branch_name
   ```
   you can abbreviate `--track` to `-t`.

### Create a New Remote Branch for a Local Branch

You have a branch in your local repo named `dev-food`,
but no remote branch (on origin) for it.

To create a **remote** `dev-food` branch and track it:
```
git checkout dev-food
# in the "push" commend, "dev-food" is the name for the REMOTE branch
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

1. We just want to **look** at the branch code but not make changes:
   ```
   git checkout origin/add_to_table
   ```
   this creates a **detached branch**.  

2. We want to **make changes** and push to the remote branch:
   ```
   git checkout -b add_to_table origin/add_to_table
   ```
   creates a local "tracking branch".  

3. Somehow you screw up and you have a local copy of existing branch,
but its not tracking a remote.  You can add the remote tracking branch:
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

### Good Collection of Branching "How To"

This page has some useful Git commands for working with branches and remotes:

<https://www.freecodecamp.org/forum/t/push-a-new-local-branch-to-a-remote-git-repository-and-track-it-too/13222>

* Rename a branch: `git branch -m old_name new_name`  (or use `--move`)
* Delete a branch: `git branch -d branch_name  (or use `--delete`)
* Force delete a branch with unmerged commits: `git branch -d --force branch-name` (`-D` is same as `-d --force`)

## Resources to Learn More

Basics of Branch and Merge

* [Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) from the online [Git Book](https://git-scm.com/book/).
* [Git Branch Command Examples](ttps://www.thegeekstuff.com/2017/06/git-branch/) shows commands for 15 common tasks
* [Git Visualizer](http://git-school.github.io/visualizing-git) type git commands and see a graph of the result! *This really helps understand git*. 
* [How to Clone all Branches?](https://stackoverflow.com/questions/67699/how-to-clone-all-remote-branches-in-git) Stackover question with extensive explanation.

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

