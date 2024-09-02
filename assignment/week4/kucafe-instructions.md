---
title: Github Flow Practice
---

### Purpose

1. Practice project initialization, Github Flow, creating and responding to Pull Requests, and using a task board.

2. Practice resolving merge conflicts.


### The Goal

When your are done, "master" on your `ku-cafe` repo will contain:

* `README.md` with **links** to the **5 sections** in the Menu. 
  - when someone clicks on a link it should go *exactly* to the correct section of the menu file.
* At the bottom of README are the names of your team members and their menu section. (see example)

* `Menu.md` file containing **these 5 sections** written on **one line**
  - Breakfast
  - Lunch
  - Dinner
  - Night Food
  - Beverages
  It should look like this:
  ```
  KU Cafe Menu                                         <-- format as a heading
  
  Breakfast | Lunch | Dinner | Night Food | Beverages  <-- links to sections
  ```
* All sections must be **formatted consistently** with a) correct spelling, b) items in alphabetical order in each section, c) consistent pricing.


## Evaluation Criteria

1. Master branch on Github conforms to the spec, well formatted, correct English.
2. Github has 5 feature branches, all merged into master.
3. Github has project board with 5 required tasks, all done.
4. Github has at least one Pull Request for each feature, all closed.
5. PR descriptions and comments are meaningful and helpful.

## Assignment

A team of 5 people will jointly contribute to one `ku-cafe` project on Github.
- Team assignments are shown on shared Google Sheet.

1. The **Project Lead** ("team leader") creates & initializes the project:

   - Use this template to create repo: <https://github.com/ISP21/ku-cafe>
   - Copy the URL of your Github repo into the Google Spreadsheet (given in class)
   - **Invite** team members to the project. Use: Settings -> Collaborators to invite.
   - Create a **Kanban project board** with 5 tasks:
     - Breakfast menu
     - Lunch menu
     - Dinner menu
     - Night food
     - Beverages

2. **Each Team Member** does this:
   - Take one task on the project board, move it to "In progress", and **add your name** to the task.
   - Write a meaningful description in the task. Use complete sentences. You can use Markdown, too, such as bulleted lists.
   - Clone the repo from your Project Leader on Github
   - Create a local **branch** for your work, with a name such as `breakfast-menu`.
   - Do work on your feature branch, not on master.
   - In `Menu.md` add a section for your menu and **at least** 4 menu items. More is better.
   - In README.md: add your name, role (task), and Github id to the "About Us" table.
   - In README.md: add a link to your section of Menu.md so someone can click on it to go from README to your section of Menu.md.
   - Push your branch to Github. (`git push -u origin branch-name`)
   - **Preview** your branch on Github.  Is formatting correct? Spelling?
   - **Open a Pull Request**

4. **Everyone** responds to Pull Requests!
   - When you see a PR, review the person's branch on Github
   - Comment on their Pull Request 
     - Formatting or spelling problems?  Are prices consistent? 
     - Items in alphabetical order? 
     - Do you approve the merge into master?
     - If you approve merge then write approve or write `+1` (*jargon for approve*) and a few words to confirm.

5. Feature Author: Merge & Close Pull Request.
   - Respond to comments to your Pull Request. If problems, fix them & push again.
   - **After** your team **approves your work**, merge it into master.

Github can merge automatically **if** there is nothing that will cause a conflict on master.

If Github cannot do the merge, then update your local copy of master and merge on your computer. Resolve conflicts.

Finding and intelligently fixing conflicts is the fun & puzzling part of using Git.  Doing in an IDE or mergetool helps.

After you successfully merge your work into 'master', push your changes.

It is possible that another team member pushed new changes while you were resolving conflicts,
so you *might* need to repeat the process!

## Github Projects (Task Board & Project Tracking)

Github Projects used to a simple task board, but it now quite powerful and complex.   (*Typical* Microsoft -- adding too much complexity.)

To discover what you can do with Projects, browse the docuentation:

- [Github Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects)

- [Best Practices for Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects)

Useful things you can do:

- create custom fields for tasks. Try: "Estimate" (time), "Iteration" (number), "Priority" (choose from a list), "Assignee" (who is doing it)

- convert tasks into issues! Make a task be an issue. When you close the issue the task is marked "Done" (you may need to configure this).
