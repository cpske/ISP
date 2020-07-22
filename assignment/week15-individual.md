---
title: Bug Bounty:  Test 'Production' Web Apps
---

**Deadline:** Dec 3, midnight (so teams can fix the bugs)

By now, every team should have a  version of their app
deployed to the cloud and the URL shown in their README.md.

## Assignment

Try to find defects (bugs) in other teams' apps, using the cloud-deployed version.

1. Everyone **must** test the cloud deployment of the project
listed on the Google sheet for installation testing (the project you installed locally).
    - Spreadsheet is at http://bit.ly/isp-project-testing
2. Test as many other apps as you want to find defects and earn bug bounties.
    - The first report of a confirmed, unique defect earns 1 point.
3. **Report Defects** in 2 places:
    - First, open an issue on team's project repository.
      Provide enough information for them to reproduce the issue.
    - Second, add a row to the Google spreadsheet at http://bit.ly/isp-project-testing on the "Bug Reports" page.  Include:
        1. project name
        2. your name
        3. issue number
        4. brief description of defect
4. Wait for team to **confirm the bug**.  (See below)
5. No points for finding defects in your own application. But you should report issues anyway.

## Earn Bug Bounty Points

The first person to report each confirmed, unique "bug" or "defect" related to functionality will earn 1 point, up to a max of 15 points.

The person who finds the most defects will earn an extra 5 points.

A "bug" or "defect" includes:

* app returns incorrect or invalid data
* page navigation errors
* authorization errors, such as being able to modify data submitted by someone else or access a restricted page without login
* anything that causes the app to crash, return an exception page, or a 5xx status code page.
* other kinds of errors may earn a point

## Other Defects (No Bounty But Please Report)

Please report the following, even though they don't earn bug points.

* spelling mistakes
* confusing navigation
* non-intuitive behavior (app behaves differently from what users would normally experience in a web app).  

## Validation by Development Team

**Promptly** review each issue. Apply a label to the issue (Github lets you add labels to issues).

Use these labels:

* **bug** - if you confirm its a bug that hasn't been reported before.
* **duplicate** - the issue duplicates another issue. Add a comment like "Duplicates #18" to the issue, and close it.
* **question** - request for more information is needed, because the problem isn't clear or you can't reproduce it.  Add **bug**, **duplicate**, or **not a bug** label when you understand the issue.
* **not a bug** - if you can't reproduce it, or conclude that its not a bug. You should explain *why* its not a bug in your comment closing the issue.


## Example of Non-Intuitive Behavior in a Commercial Web Site

Phatra Asset Management has web-based account services application at https://phatraclick.phatraasset.com.  
A client can view his portfolio, buy or redeem mutual funds, and view/print a transaction report.

On the top-right of the page is a `Logout` link.  Most users would **expect** that clicking on this link will log them out.

![Phatra Navigation Bar](/images/Phatra-Navbar.png)

When you click "Logout" is shows a page like this:

![Phatra Logout Screen](/images/PhatraLogoutScreen.png)

**Is the person logged out?**  The answer is **no**.

You can use the browser "Back" button to re-enter the site and you are still logged in!  This is *non-intuitive* and a potential security risk.

Its also stupid.  The "Close" button won't close the browser window.
