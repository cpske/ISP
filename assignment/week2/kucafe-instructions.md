---
title: Github Flow Practice
---

### Purpose

Practice project initialization, Github Flow, Pull Requests, merging conflicts, and using a task board.

Practice online communication, like a remote programming team.

> For this exercise, students who took ISP last year cannot be team leader:


### The Goal

When your are done, "master" on your `ku-cafe` repo will contain:

* `README.md` with **links** to the **5 sections** in the Menu. At the bottom of README are the names of your team members and their menu section. (see example)
  - when someone clicks on a link it should go *exactly* to the correct section of the menu file.

* `Menu.md` file containing **these 5 sections**
  - Breakfast
  - Lunch
  - Dinner
  - Night Food
  - Beverages
  - All sections must be **formatted consistently** with a) correct spelling, b) items in alphabetical order in each section, c) consistent pricing.

* `Menu.md` contains hyperlinks to the 5 sections written as a single line, directly under the title line:
  ```
  KU Cafe Menu
  
  Breakfast | Lunch | Dinner | Night Food | Beverages  <-- links to sections
  ```

## Evaluation Criteria

1. Master branch on Github conforms to the spec, well formatted, correct English.
2. Github has 5 feature branches, all merged into master.
3. Github has project board with 5 required tasks, all done.
4. Github has at least one Pull Request for each feature. 
5. PR descriptions and comments are meaningful and helpful.

## Assignment

1. Team of 5 people will jointly contribute to one `ku-cafe` project on Github.
   - Teams are shown on shared Google Sheet.  Add your Github ID to sheet.

2. The **Project Lead** ("team leader") creates & initializes the project:

   - Use this template to create repo: <https://github.com/ISP21/ku-cafe>
   - Copy the URL of your Github repo into the Google Spreadsheet (given in class)
   - **Invite** team members to the project. Use: Settings -> Collaborators to invite.
   - Create a **Kanban project board** with 5 tasks:
     - Breakfast menu
     - Lunch menu
     - Dinner menu
     - Night food
     - Beverages

3. **Each Team Member** does this:

   - Take one task on the project board, move it to "In progress", and **add your name** to the task.
   - Add a meaningful description to the task. One sentence is enough.
   - Clone the repo from your Project Leader on Github
   - Create a local **branch** for your work, with a name such as `breakfast-menu`.
   - Do work on your feature branch, not master.
   - In `Menu.md` add a section for your menu and **at least** 4 menu items. More is better.
   - In README.md: add your name, role (task), and Github id to the "About Us" table.
   - In README.md: add a link to your section of Menu.md so someone can click on it to go from README to your section of Menu.md.
   - Push your branch to Github. (`git push -u origin branch-name`)
   - **Preview** your branch on Github.  Is formatting correct? Spelling?
   - **Open a Pull Request**

4. **Everyone** Respond to Pull Requests!
   - When you see a Pull Request from a team member, review their branch on Github. 
   - Comment on their Pull Request. 
     - Formatting or spelling problems?  Are prices consistent? 
     - Items in alphabetical order? 
     - Do you approve the merge into master?
     - If you approve merge then write approve or write `+1` (*jargon for approve*).

5. Feature Author: Merge & Close Pull Request.
   - Respond to comments to your Pull Request. If problems, fix them & push again.
   - After your team **approves your work**, merge into master.


If Github cannot do an automatic merge, it may mean that `master` has changed 
since you cloned it.  

In that case, you should merge on your own machine.  Follow the steps we did in class to merge.

Finding and intelligently fixing conflicts is the fun & puzzling part of using Git.

After you successfully merge your work into 'master', push your changes.

It is possible that another team member pushed new changes while you were resolving conflicts,
so you *might* need to repeat the process!

