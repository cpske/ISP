---
title: Github Flow Step-by-Step
---

This includes the use of a task board.

1. Choose a feature or issue to work on from your project board. 
   - Move the task from "Backlog" to "In Progress" (or similar column)
   - add your name to the task so the team knows you got it.

2. `pull` the `master` (main) branch to make sure your copy is up-to-date!

3. Create a new feature branch off of `master`. 
   - Use a **descriptive branch name**.     
   - There are two ways to create the branch:
     - 1) **create locally** and then push it:
       ```
       git checkout -b new-branch-name
       git push -u origin new-branch-name
       ```
       If you have the git setting `push.default` set to `upstream`, this "push" might not work. See ProGit or StackOverflow #2765421 for details.
     - or 2) **create on Github** and then checkout & track it 
       ```
       # after you create the new branch on Github, do:
       git checkout -t origin/new-branch-name
       ```

4. Implement and test the feature on your feature branch.
   - push to remote often

5. Open a Pull Request. 2 cases:
   - you want feedback or help, but the feature isn't done yet
   - feature is done and you want feedback & agreement to merge into `master`

6. Wait for feedback from team.  Or rather, keep working until you get feedback.

7. Apply the feedback.

8. When team agrees to merge into master, merge your branch.
   - You can merge locally and then "push" to master, or
   - Merge on Github

9. Close the Pull Request with a descriptive message.

10. Move the issue on task board to "done". (Github may do this automatically!)

![Github Flow](github-flow.png)

## Responding to a Pull Request

Everyone on the team:

1. When you see a Pull Request, check the person's work and make comments.
   - often you can do this on Github, without checking out the branch
   - pay attention to detail. Do not **assume** the work is correct.
   - add comments and suggestions to the Pull Request

2. If the PR is a request to merge, you should indicate if you approve.
