---
title: Github Flow Step-by-Step
---

This includes the use of a task board.

1. Choose a feature or issue to work on from your project board. 
   - Move the task from "Backlog" to "In Progress" (or similar column)
   - add your name to the task
   - on Github Project board you add your name in the "Assignee" field (in table view)

2. `pull` the `master` (main) branch to make sure yours is up-to-date!

3. Create a new feature branch off of `master`.  
   - Use a **descriptive branch name**.     
   - There are two ways to create the branch:
     - **locally** and then push it, or
     - **on Github** and then checkout (clone) & track it 

4. Implement and test the feature on your feature branch.
   - push to remote often

5. Open a Pull Request. 2 cases are:
   - you want feedback or help (but the feature isn't done yet)
   - feature is done and you want feedback & agreement to merge into `master`

6. Wait for feedback from team.  Or rather, keep working until you get feedback.

7. Apply the feedback.

8. When team agrees to merge into master, merge your branch.
   - You can merge locally and then "push" to master, or
   - Merge on Github

9. Close the Pull Request with a descriptive message.

10. Move the issue on task board to "done". (Github may do this automatically!)

![Github Flow](github-flow.png)
