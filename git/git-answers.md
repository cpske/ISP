
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

# Branch and Merge Questions

1. What is the command to create a new branch named `dev-food`?

    git branch dev-food

2. What is command to find out what your current branch is?

    git branch

3. Command to show **all** branches including remote ones?

    git branch -a

4. What is command to switch working copy to `dev-food`?

    git checkout dev-food


5. You commit some files to `dev-food` and try to "push" them to Github, but it fails:

    ```
    cmd>  git add pizza.py
    cmd>  git commit -m "add a new food"
    cmd>  git push
    fatal:  The current branch dev-food has no upstream branch. 
    ```

    Explain why the error and how to fix the problem.

    > Fixing is easy -- git tells you what to do.

     (its the same command as adding a remote to "master")

6. Add "origin" as remote and push dev-food all in one command

    ```
    #    git push -u  upstream_name upstream_branch
    cmd> git push --set-upstream origin dev-food
    ```4. Even Worse! You accidentally delete some files and commit the changes! Now the files are deleted in the current Git HEAD.   How can you get back the the most up-to-date revision from git without "undoing" the commit?

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

    // Now you found the file! how to check it out? 
    ____________________________________
    ```
