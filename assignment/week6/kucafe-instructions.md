---
title: Github Flow Practice
---

### Objective

Practice project initialization, Github Flow, Pull Requests, and merging with conflicts.

* Do all communication online, like a remote programming team.

Time Limit: 30 minutes

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
  - **All sections** must be formatted consistently, correct spelling, and items arranged alphabetically in each section.

* `Menu.md` contains hyperlinks to the 5 sections written as a single line, directly under the title line:
  ```
  KU Cafe Menu
  
  Breakfast | Lunch | Dinner | Night Food | Beverages  <-- links to sections
  ```

## Evaluation Criteria

1. Master branch on Github conforms to spec, is well formatted, correct English.
2. Github has 5 feature branches, all merged into master.
3. Github has project board with 5 required tasks, all done.
4. Github has 5 Pull Requests, one per feature. More than 5 PR is OK.

## Assignment

1. Team of 5 people will jointly contribute to one `ku-cafe` project on Github.
   - Teams are shown on shared Google Sheet.  Add your Github ID to sheet.

2. One person (the project lead) creates & initializes the project:
   - Use this template to create repo: <https://github.com/ISP21/ku-cafe>
   - Copy the URL of your Github repo into the Google Spreadsheet (given in class)
   - **Invite** team members to the project. Use Settings -> Collaborators to invite.
   - Create a **Kanban project board** with 5 tasks:
     - Breakfast menu
     - Lunch menu
     - Dinner menu
     - Night food
     - Beverages

3. **Each Team Member** does this:
   - Take one task on the project board, move it to "In progress", and **add your name** to the task.
   - Clone the repo from your Project Leader on Github
   - Create a local **branch** for your work, with a name such as `breakfast-menu`.
   - Do work on your feature branch, not master.
   - In `Menu.md` add your menu section and at least 4 menu items.
   - In README.md add your name, role (task), and Github id to the "About Us" table
   - In README.md, add a link to your menu section so someone can click to go directly from README to your section of Menu.md
   - **Push** your branch to Github. (`git push -u origin branch-name`)
   - **Preview** your branch on Github.  Is formatting correct? Spelling?
   - **Open a Pull Request**

4. Respond to Pull Requests (everyone).
   - When you see a Pull Request from a team member, review their branch on Github. 
   - Comment on their Pull Request. 
     - Formatting or spelling problems?  Are prices consistent? 
     - Items in alphabetical order? 
     - Do you approve the merge into master?

5. Merge & Close Pull Request (feature author).
   - Respond to comments to your Pull Request. If problems, fix them & push again.
   - After your team **approves your work**, merge into master.
   - If Github cannot do an automatic merge, it probably means that `master` has changed since you cloned it.  
   - In that case (no automatic merge), do the following:
     1. Fetch master from Github to your local repo and merge into your local `master`.
     2. Merge your feature branch into master on your machine.  Fix any conflicts (if so, you need to commit again after).
     3. Push your (merged) master to Github.  This time it should succeed.  If you made any changes to your feature branch, push those, too.


