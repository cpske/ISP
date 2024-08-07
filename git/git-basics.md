---
title: Git Basics
---

## About Git

Some things you can do with Git are:

* easily make a copy of a project's source code on another machine
* view a history of all changes to project files, and compare revisions
* checkout any past revision to a project, even files that have been deleted!
* control who can read and write to the repository
* quickly switch your "working copy" between different versions of repository files

This file describes how to create and use a local git repository, using the `git` command line program.  
How to use Github is introduced in a separate document.

See [Why Use Git?](#why-use-git) (below) for how Git can save you from disaster.

## Git Software

Tools for using git incliude:

1. **Git command line tool** - the basic "git" we will use. This is the best way to learn git. 
2. **Git GUI client** such as [Github Desktop](https://desktop.github.com/) for Windows and OSX, [SourceTree](https://www.sourcetreeapp.com/), or
[SmartGit](https://www.syntevo.com/smartgit/).
3. **IDE built-in Git feature** Eclipse, Netbeans, IntelliJ, PyCharm, VS Code, and even BlueJ all include git tools. After you understand git, these tools are a fast and easy way to use git while programming.
   - but if you *don't* know git first it is easy to make mistakes or be confused.

For this introduction, we will use the Git command line.

### Installing Git

**Windows**:  Download from [http://git-scm.com/downloads](http://git-scm.com/downloads).    
**Mac OSX**:  Includes "git".  Open a Terminal window and type `git`.  The OS might prompt you to install Git from XCode.  If `git` is already installed, it will print a help message.    
**Old Mac OSX**:  If your OSX is old and does not have "git", then download Git from [http://git-scm.com/downloads](http://git-scm.com/downloads).    
**Ubuntu or Debian**:  in a terminal window, enter `sudo apt-get install git`.    
**Other OS**: see [install commands for Linux](https://git-scm.com/download/linux)

## Personalize Your Git Configuration

Before you can use Git to "push" commits to a remote repository
you must set configuration values containing **your name** and **email**.
Use a command or terminal window to enter these:

```
# your name and email address, which are added to commits
git config --global user.name "Bill Gates"
git config --global user.email "bill@msft.com"

# The editor git should open to edit a commit message or conflict.
# Instead of this, you can set a shell environment variable named EDITOR
# Suppose you want to use 'nano' as the editor for git commits. Enter:
git config --global core.editor nano
# for Mate on Mac OSx (needs -W option):
git config --global core.editor "mate -w"
```

### Creating a Local Git Repository

A git **repository** stores the files for **one project**.  To create a git repository for a project:

1. Open a **command line window** where you can type commands:
    * MS Windows: open a "command prompt" (cmd) or "**bash shell**".
    * Mac OSX: open a "terminal". Just type "term" in the search box.
    * Linux: open a "terminal" window.
2. Change to the directory containing your project, or create a new directory.  Linux/MacOS: `cd directory`, Windows: `chdir directory`.
```shell
cmd> cd workspace/myproject
```
3. Run `git init` to create an empty repository. You must do this **inside the project directory**.
```shell
cmd> git init
```
This creates a subdirectory named `.git` for the repository. Don't edit files in that directory! Let git manage it.  Now your project will look something like:
```shell
myproject/
    .git/   (git local repository - don't modify this)
     
```
4. The new git repository is empty. You must add files, as described below.

### Add files to the Repository and Check Status

You tell git which files it should save in the repository using the `git add` command.  Use a text editor to create a file file named `README.md` containing some text:
<blockquote>
<pre>
    # My Project  
    by Bill Gates  (use your own name)  
    
    This README.md that describes the project. 
    In contains formatting using Markdown syntax, which you should learn.
</pre>
</blockquote>

Tell Git that you want to add this file to the repository:
```shell
cmd> git add README.md
```
Note: you can add many files on one line by writing their names separated by space. You can use wildcard chars, too.

`git add` marks the files for adding to the repository, but does not actually copy them in the repository.  You can check the status using:
```shell
cmd> git status
  Changes to be commited:
     new file:  README.md
```
The `git status` command shows that there is 1 new files waiting to be added to the repository.

To save the file(s) to the repository use `git commit`.  You must write a log message (-m) with a short explanation:
```shell
cmd> git commit -m "Initial code checkin"
  1 file changed, 1 insertions, 0 deletions
cmd> git status
  nothing to commit, working directory clean
```
Now your repository contains 1 file (called **tracked files**).

## Adding a Directory to the Repository

You can use `git add` to add a directory and all its contents.  Git will add **everything** in the directory and its subdirectories -- so be careful!

Create a directory named `demo` and a source file `person.py`:
```shell
cmd> mkdir demo
cmd> cd demo
cmd> edit person.py  (use your favorite editor to edit the file)
# change back to project directory
cmd> cd ..
```

To add **everything** in the project `demo` (sub)directory to git, use:
```shell
cmd> git add demo
```

Check the git status:
```shell
cmd> git status
```

Save the directory and its contents to the repository:
```shell
cmd> git commit -m "add source code"
```

**After** you add the `demo` dir to git, if you later create a new file in the "demo" directory then you must add that file to git yourself. It is **not** automatic.

### View History

View the history of all commits (revisions) to a repository by typing `git history` or `git log1` or `git log --oneline` 
For the example above:
```shell
cmd> git log --oneline
git history
* 992a0c5 - (2 minutes ago) add source code - fatalaijon (HEAD -> master)
* 5d1ab24 - (5 minutes ago) initial code checkin - fatalaijon 
```
This shows there were 2 commits. The most recent commit has revision code 992a0c5 and message "add source code". It is also the HEAD revision on the master branch.

### Updating Files in the Repository

When you make changes to a previously commited file (called a **tracked file**), you should update the file in the repository. That is, "commit" the changes.   After finishing some work (editing files, adding files), check the status of your working copy:
```shell
cmd>  git status
On branch master
Changes not staged for commit:
   modified:   demo/Problem1.py
   modified:   README.md
```
This shows that `demo/Problem1.py` and `README.md` have been modified since the last commit. 

### Important Git Concepts

Git uses 4 storage areas:

1. **Working Copy** is the files in your project directory (and its subdirectories). These are the files you edit during your work; it includes **tracked** files (files you have added to repo using *git add*) and **untracked** files.  
2. **Staging Area** of files waiting to be committed to the repository. `git add` adds files to the staging area.
3. **Local Repository** contains all revisions of all files "added" and "committed" to the repository, along with dates and log messages.  When a file is updated, only the changes are stored, so a repository does not require much space.
4. **Remote Repository** (optional) is a git repository on another host, like Github.  You can synchronize your local repository with the remote repository.

A **Revision** is one snapshot of a project, created using "git commit".  Each revision is identified by a code like 58eb09c. This code (the revision id) is based on a hashcode of the committed files.

**HEAD** refers the most recent revision of files on your current branch.

**master branch** (or **master**) is the main branch of revisions in a repository. 

**Tracked files** refers to files that you have committed to the repository. Git constantly checks for changes to these files, every time you run `git status` or other commands.

### What to Save (and NOT Save) in Git

For a programming project, save the files needed to build and run your project, plus documentation.  This includes Java source code (`*.java`), configuration files, and icons.  

You **do not** need to save files that can be recreated, such as compiler output (`*.class` files) or executable builds. In general, don't include large images, videos, or archives (zip) downloaded from the Internet.

Here is a common list of files and directories to save (commit) in a Git repository, and some files not to commit:

<table align="center">
<tr valign="top">
<th width="50%" markdown="span"> Files to Save in Git </th>
<th wdith="50%" markdown="span"> Files <u>Not</u> to Save </th>
</tr>
<tr valign="top">
<td markdown="span"> 
<em>Files needed to build the project</em>
<br>
<em>Documentation</em>
</td>
<td markdown="span">
<em>Anything that can be recreated from other files</em>
</td>
</tr>
<tr valign="top">
<td markdown="span"> 
Source code      
`*.java` or `*.py`    
icons and config files    
`README.md` and other documentation
</td>
<td markdown="span"> 
Compiler output (`bin` or `build` dir)    
`*.class`    
`__pycache__`
</td>
</tr>
<tr valign="top">
<td markdown="span">
`requirements.txt` (Python)
</td>
<td markdown="span">
IDE Project files (see below)
</td>
</tr>
</table>

### What are IDE Project Files?

When you create a "project" using an IDE, it creates files that describe the project configuration.  Programmers usually don't save these files in the repository because a) they can be easily recreated by the IDE, and b) for a *team* project, your IDE settings can conflict with another team member's settings!

Project files created by common IDEs are:

* Eclipse
    ```
    .classpath
    .project
    .settings/ (directory)
    ```
* Netbeans
    ```
    nbproject/
    nbdist/
    nb-configuration.xml
    ```
* IntelliJ and PyCharm
    ```
    .idea/
    out/
    *.iml
    *.iws
    *.ipr
    ```
* Visual Studio Code (vscode)
    ```
    .vscode/
    ```

### The README.md File

README.md is a text file with Markdown formatting.  Github and Bitbucket show a web page from this file (after formatting it) when someone visits your repository. Use README.md to describe the project and anything the viewer needs to know, like how to build and run it.  Most projects on Github have a README.md.

The [Atom Editor](https://github.com/atom/atom) on Github also has a good README.md.

Here is a simple example of README.md:

### Example README.md
```markdown
# Bus Ticket Counter
by Bill Gates

Counts the number of tickets sold for a fleet of buses.
Written in Java and requires Java version 8 or newer.
Based on my [elab](https://elab.cpe.ku.ac.th) program.
```

Markdown is widely used to create online documentation, and the syntax is simple.  Learn Markdown here:

* [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) on Github explains Markdown in one page
* [Markdown Tutorial](https://www.markdowntutorial.com/lesson/2/) interactive tutorial.

### How to Create README.md?

You can use any text editor to create it, *or* use your IDE.  In Eclipse, choose New -> File and enter the name (README.md). Be sure to put it in the top directory of your project, _not_ inside the src/ dir.


Some good, free text editors are:

* [Atom](https://atom.io) editor that understands syntax of many languages. Has Markdown preview. A bit slow to start.
* [Sublime](https://www.sublimetext.com) similar features to Atom
* [Notepad++](https://notepad-plus-plus.org) for Windows only. A great replacement for the crummy "Notepad" editor.
* [Vim](https://vim.sourceforge.io) the standard Linux editor, also part of Apple OSX.  Vim is a keystroke-efficient editor that runs in a terminal window, but a bit cryptic to learn. The GUI version is easier to use. 

### Use .gitignore to "Ignore" Unwanted Files

Every time you type `git status` it will display all the untracked files, including files you **don't** want to commit to git.  You can tell git that it should never commit certain files by creating a file named `.gitignore` in your project top-level directory.  `git status` won't show these files and you won't accidentally commit them.

The `.gitignore` file is optional, but very useful.  You only need to write it once, then copy it from one project to another.

Here is an example `.gitignore` file for both Java and Python projects:
```shell
# compiler output and build directories
*.class
*.temp
bin/
build/
out/
dist/
# Python compiled files
__pycache__
*.py[cod]

# Eclipse project files
.classpath
.project
.settings/

# Netbeans project files
nbproject/
nbdist/
nb-configuration.xml

# IntelliJ project files
.idea/
out/
*.iml
*.iws
*.ipr

# MacOS junk
.DS_Store
```

**Note:** You must tell git to add `.gitignore` to the repository:
```shell
cmd> git add .gitignore
cmd> git commit -m "Add .gitignore"
```

**Note:** Github has examples of `.gitignore` for different programming languages.  A good way to discover things for your own `.gitignore`.

## Why Use Git

You **work all week** on the final project for your Programming 1 course. 
You write source code (in /src) and a report (Report.docx), so you project looks like this:
```shell
myproject/
    .gitignore
    README.md
    Report.docx
    bin/   (compiler output)
    dist/  (runnable application)
    src/   (many source code files)
```
You commit everything except "bin" to git, and go to lunch.

While you are at lunch, your **cat deletes Report.docx** by walking on the keyboard!  Your project report is gone!

![](cat-on-keyboard.jpg?raw=true)

What to do?

Since you saved the report using git, you can **recover** the most recent version of the report from the repository:
```shell
cmd> git checkout -- Report.docx
```

If your cat deletes (or edits) lots of files, you can revert *everything* in  working copy to the most recent revision in git. This will discard all changes to your working copy since the last "git commit".
```shell
# Be careful. This will overwrite your working copy 
# with the most recent revision commited to git.
cmd> git reset --hard
```

## Repository as a Graph of Commits

A git repository has a graph structure. Each commit is a node in the graph.

Branches, Tags, and HEAD are just labels pointing to commits (nodes).

Try the [Git Visualizer][GitVisualizer] at http://git-school.github.io/visualizing-git/ to see a graph of a Git repo.


[Think Like a Git][ThinkLikeaGit] also has visual explanation of git.

[ThinkLikeaGit]: http://think-like-a-git.net/ "Understand visually how git works"
[GitVisualizer]: http://git-school.github.io/visualizing-git/ "Online tools draws a graph of commits in a repo, as you type"

## Git Resources to Learn More

See the Git [index page](index#resources).
