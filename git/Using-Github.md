---
title: Why Use Github?
---

Presentation: [Using Github](Using-Github.pdf)

Using Git on your local computer is good, but...

* what if your hard disk fails?
* how do you **share a project** with someone else?
* how do you work on a project from 2 computers (home computer and laptop at KU)?

Github let's you keep an up-to-date copy of your local repository that you and others can access from anywhere.  It also provides many services to help your project.

---

Git supports **remote** repositories that can be synchronized and cloned.   
Popular git hosting sites are:

* [Github](https://github.com) owned by Microsoft
* [Gitlab](https://gitlab.com)
* [Bitbucket](https://bitbucket.org) owned by Atlassian

A **remote** Git hosting site let's you:

* synchronize your local repository with the remote. It's efficient and fast.
* create a new local copy (clone) from the remote
* view project activity, updates, and compare changes between versions
* share access (read-only or read-write) with other people 
* create a professional looking web site for your project (*Github pages* on github.io)
* automatically run tests using Github Actions

### How to Start a Project on Github

There are two ways to start a project with Github.
The choice depends on these cases: 

**Case 1**: You already have code on your computer; you want to copy it to Github.    
**Case 2**: A project already exists on Github; you want to copy it to your computer.    
**Case 3**: You don't have anything yet.

The only difference is how you create your local project repository and connect it with Github.  After that, the normal workflow is the same in all cases.

### Case 1: You already have code on your computer. Copy it to Github.

In this case, there are 3 steps

1. Create a local repository for your project.  Then commit your code to it.
    ```shell
    cmd> cd workspace/myproject
    cmd> git init
    cmd> git add README.md .gitignore  (create these files yourself)
    cmd> git add src                   (add your source code)
    cmd> git commit -m "initial code checkin"
    ```
   A `.gitignore` file prevents you from accidentally committing the wrong files to git.  Once you have a good `.gitignore` file, you can copy it from one project to another. 

2. On [Github](https://github.com) create an **empty** repository for the project.
    a. on Github click on the "+" icon at upper-right of your home page and choose "create new repository".
    b. give the repository a name. It does **not** need to be the same as your local project name.
    c. don't put any files in the Github repo -- the repo must be **EMPTY**
    d. copy the URL that Github shows you, for example `https://github.com/billgates/assignment1.git`. 
3. On your local computer, add Github as "remote" repository.  Suppose the repo you created in Step 2 has URL "https://github.com/billgates/assignment1.git". Then enter:
   ```shell
   cmd> git remote add origin https://github.com/billgates/assignment1.git
   cmd> git push -u origin master
   ```
   This adds the Github repo as a remote repository named "origin".  "origin" is the standard name for the default remote, but there is nothing special about the name "origin".  `git push` means to copy your local repository to the remote (github), `-u origin master` means to make "origin" be the default target and "master" the default branch for a "push" command.

You only need to type `git push -u origin master` the **first time** you connect to Github.  After that, when you want to update Github you just type:
```shell
    cmd> git push
```

### Case 2: A project already exists on Github, but not on your computer

This is easy.

1. Using a web browser, go to the project page on Github so you can copy the URL
2. Click the "Code" button. This will show the URL to use for cloning. 
    * Click the button next to the URL to copy it to your clipboard 
3. On your computer, in the **parent directory** of where you want to clone the project, enter the command:
    ```shell
    cmd> git clone https://github.com/billgates/someproject.git
    ```
    This creates a **new local directory** having the same name as remote repository (`someproject`) and clones the Github repo into it.

4. If you want to use a **different name** for your copy of the repository, then type:
    ```shell
    cmd> git clone https://github.com/billgates/someproject.git  myproject
    ```
    in this case, git will create a directory named `myproject` and copy the project there.

When you clone a project, git remembers the "upstream" location. So you can push (copy) your
local changes using `git push`.

> **Common Mistake**    
> Some students create a directory for the repo and do "git clone" inside 
> that directory. This creates an extra layer of directories.
> ```
> cmd> cd workspace
> cmd> mkdir project1     (WRONG)
> cmd> cd project1        (WRONG)
> cmd> git clone https://github.com/clueless/project1.git
> copied 8 files in 0.2sec
> ```
> Now the clueless person has this:
> ```
> workspace/
>      project1/
>          project1/      (created by "git clone")
>              .git/
>              README.md
>              more files
> ```
> The project is in `workspace/project1/project1/`.

### Pro Tip

Instead of the command line, clone the Github repo and start a project in your IDE.

### Case 3: You don't have ANYTHING yet

In this case you can start from either local project or Github.  
But Case 2 (clone from Github) requires less typing. 
Just create a new repo on Github, let Github add a README.md and .gitignore file for you, and then clone it. (Customize README.md and .gitignore later.)

### Pushing Local Changes to a Remote (Github)

Once you have connected a local repository with a Github repository using either Case 1 or Case 2, the information
is saved in the local git configuration.  You can "push" (send) your changes to Github using:
```
cmd> git push
```

### Where Is My Remote?

To view the "remote" for a local git repository, open a terminal window and change directory to the repository. Then type:
```
cmd>  git remote -v
```
it will print something like this:
```
origin https://github.com/hacker/assignment1 (fetch)
origin https://github.com/hacker/assignment1 (pull)
```

### More Detail About My Remote

To see more information, including remote branches, use:
```
cmd>  git remote show origin
* remote origin
  Fetch URL: git@github.com:billgates/project1.git
  Push  URL: git@github.com:billgates/project1.git
  HEAD branch: master
  Remote branches:
    master tracked
    dev    tracked
  Local branches configured for 'git pull':
    master merges with remote master
    dev    merges with remote dev
  Local refs configured for 'git push':
    master pushes to master (up to date)
    dev    pushes to dev    (up to date)
```

### Is My Local Copy Up to Date with Remote?

Use the above command (`git remote show origin`) or
```
git branch -vv
```

### Typical Workflow Using Git and Github

When using git with Github, after you have created both a local repository and Github remote repository, you need to follow a pattern to ensure that everything is kept up-to-date.

If you work alone (single person project) it's pretty easy. If you work on a team, then you need to be more careful.

Here are the usual steps for an **individual project** (you are the only one committing to Github):

1. Check status of your working copy: 
   ```
   cmd>  git status
   ```
   - If `git status` shows that you need to commit some work, then do it.
   - If you want to see the differences between your working copy of a file, and the same file that is in your git repo, use this command:
   ```
   cmd>  git diff filename      (enter the actual name of a file)
   ```
2. Do some work on your working copy.
3. Test and review your work.  Fix any errors.
4. Check status (again): `git status`
5. Add and commit any changed or added files:
   ```shell
   cmd> git add file1.py data/mydata.txt ...
   # commit everything
   cmd> git commit -m  "describe what you did"
   ```
   - Use a *descriptive commit message*. Don't be lazy.
   - **Shortcut:** after checking status, if you want to commit **all** changed files then you skip "git add" and use the "-a" (all) flag:
   ```shell
   cmd> git commit -am "describe what you did"
   ```
6. Push your work to Github:
   ```
   cmd> git push
   ```

### Using Github Flow on a Team Project

For a team project, you should follow [Github Flow][understanding-github-flow].

*Github Flow* is also useful on an individual project.

Please also read [How We Use Github][how-we-use-github-flow] by Scott Chacon.

![Github Flow Diagram](github-flow.png)

[understanding-github-flow]: https://guides.github.com/introduction/flow/
[how-we-use-github-flow]: http://scottchacon.com/2011/08/31/github-flow.html

### Learn Github

* [Using Git on Github](https://guides.github.com/activities/hello-world/), a tutorial on using git with gitub, including use of branches.  The example is a text file with variation in branches.

### Authentication

There are 2 protocols you can use to authenticate to Github (or other git service):

1. HTTPS - Github URL looks like `https://github.com/your_github_id/reponame.git`
   - You enter your username and password to authenticate
   - Git "remembers" the authentication for duration of current shell window

2. SSH - Github URL looks like `git@github.com:your_github_id/reponame.git`
   - You create a public/private ssh key pair and save the public key on Github.
   - Uses challenge-response to authenticate, so you never send your password over the net.
   - Generally more secure than HTTPS

Which ever protocol you use, you can instruct Git to save your password during a session so you don't need to type it each time you push or fetch:
```
cmd> git config --global credential.helper cache
```

### Use SSH Keys For Github Authentication

The steps are described in [Connecting to Github with ssh](https://help.github.com/articles/connecting-to-github-with-ssh/).


