---
title: Github Flow Practice
---

In a team create a menu for KU Cafe.  Follow the steps below!

The purpose is to practice project initialization, Github Flow, and merging with conflicts.

### The Goal

When your are done, "master" on  your github repo will contain:

* a `README.md` with link to the menu and your team names.
* a menu with **4 sections**: Breakfast Menu, Lunch Menu, Dinner Menu, and Beverages
    - there is only one Beverages section
* instead of "Dinner Menu" you may use "Night Food Menu"

### Requirements

* **Everyone** must have at least one commit (with work) on Github
* **Everyone** must have at least one constructive comment on Pull Requests
* Feature branches must be on Github (proof of work)
* I will check these on Github

## Project Initialization

1. **One** team member create a repo named `kucafeN` (`N`=your row number) in the **ISP19** organzation (not personal repo).
   - Only one repo per TEAM.
   - Public
   - URL: `https://github.com/ISP19/kucafeN` (N = a number assigned in class)

2. Clone it to your machine.

3. Create 2 files:

File:  **README.md**
```
# KU Cafe

[Menu](menu.md)

## About Us

| Name   | Role  | Github   |
|--------|-------|----------|
| Your name | Team Lead, breakfast menu | your_github_id |
| ...       | (team members will add themselvs here) | other_github_id |
```

File:  **menu.md**
```
## Menu

| Item                                   | Price |
|:---------------------------------------|------:|
| nothing yet                            |  0.0  |

## Beverages

| Item                                   | Price |
|:---------------------------------------|------:|
| nothing yet                            |  0.0  |

---

We accept PromptPay, KUPay, Alipay, and cash. No credit cards.
```

4. Add the files and push to Github.

5. Invite team members:  Settings -> Collaborators.

6. Create a task board using "Projects".
   * Task board should have 4 columns:
       - "To Do" or "Backlog"
       - "In Progress" or "Started"
       - "Review"
       - "Done"
   * Use any template (or none).  Automated Kanban is OK.

7. 3 Tasks
   * **Note**: it may work better to first create Issues in Github issue tracker.  You can create "Feature" issues.  Then create Tasks in Project board from Issues.
      - *Why?* Github Issues have more structure and can be referenced in commits.

   * Create breakfast menu
   * Create lunch menu
   * Create dinner menu
   * Each sub-team (2 people) will implement one task.

8. Implement "Breakfast menu" using Github Flow.
   - pair updates their copy of master
   - pair creates a branch named breakfast-menu and switches to it
   - pair adds their names to README.md
   - Modify `menu.md`
       * change the title line from "## Menu" to "## Breakfast Menu"
       * add menu items (your choice) to the menu table
       * add beverage items (your choice) to the "## Beverage" section
   - **WRONG**, **WRONG** do **not** rename "menu.md" or create a new file name "breakfast-menu.md".
   - **CORRECT** put your work directly in `menu.md`. **DO NOT RENAME THIS FILE**.
   - Check your work.  Is markdown correct? Spelling? Consistent formatting?
   - Commit and push your changes
   - Open a Pull Request
   - EVERYONE on team pulls the branch and comments on Pull Request
   - Look for SPELLING ERRORS, wrong words, formatting errors, inconsistencies

9. Merge your menu into master!
   - When TEAM approves your changes, pull an update of master branch.
   - Merge your branch **into** master. **NOT** merge master into your branch.
   - Check the result for correctness.
   - Push the changes.

---

## Alternate Starter Menu

To help structure your work, you can use an initial `menu.md` like this.
It may reduce merge conflicts a little.

```
## Breakfast Menu

| Item                                   | Price |
|:---------------------------------------|------:|
| nothing yet                            |  0.0  |

## Lunch Menu

Coming soon.

## Dinner Menu

Coming soon.

## Beverages

| Item                                   | Price |
|:---------------------------------------|------:|
| nothing yet                            |  0.0  |

---

We accept PromptPay, KUPay, Alipay, and cash. No credit cards.
```
