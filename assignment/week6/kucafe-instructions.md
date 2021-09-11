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
  All 5 sections must be formatted consistently, with items arranged alphabetically.

# `Menu.md` contains a single line of hyperlinks to the 5 sections, directly under the title line:
  ```
  KU Cafe Menu
  Breakfast | Lunch | Dinner | Night Food | Beverages  <-- links to sections
  ```

## Assignment

1. Teams of 5 people will jointly contribute to a `ku-cafe` project on Github.
   * Only **one repository per team**.

2. One person (the project lead) initializes the project:
   - creates the `ku-cafe` repository in his/er own account
   - invite team members to the project. Use Settings -> Collaborators to invite.
   - create a Kanban project board with 5 tasks:
     - Breakfast menu
     - Lunch menu
     - Dinner menu
     - Night food
     - Beverages

3. **Each Team Member** does this:
   - Take one task on the project board, move it to "In progress", and **add your name** to the task.
   - Clone the repo from the Project Lead on Github
   - Create a local **branch** for your work, with a name such as `breakfast-menu`.
   - In `Menu.md` add your menu section and at least 4 menu items.
   - In README.md add your name, role (task), and Github id to the "About Us" table
   - In README.md, add a link to your menu section so someone can click to go directly from README to your section of Menu.md
   - **Push** your branch to Github
   - **Preview** your branch on Github.  Is formatting correct? Spelling?
   - **Open a Pull Request**

4. Respond to Pull Requests (everyone).
   - When you see a Pull Request from a team member, review their branch on Github. (Easier to review on Github than cloning to your local machine.)
   - Comment on their Pull Request. Formatting or spelling problems?  Are prices consistent? Items in alphabetical order?

5. Merge & Close Pull Request (feature author).
   - Respond to comments to your Pull Request. If problems, fix them & push again.
   - After your team **approves your work**, merge into master.
   - If Github cannot do an automatic merge, it probably means that `master` has changed since you cloned it.  In that case, do the following:
     1. Fetch master from Github to your local repo and merge into your local `master`.
     2. Merge your feature branch into master.  Fix any conflicts (if so, you need to commit after).
     3. Push your master to Github.  This time it should succeed.  If you made any changes to your feature branch, push those, too.



## Starter Code

`ku-cafe.zip` contains starter code for these files:
```
README.md
Menu.md
```
The person who creates your team's ku-cafe repo should add this starter code.
Everyone else should clone the repo.
