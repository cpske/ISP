---
title: Bug Bounty - Test 'Production' Web Apps
---

**Deadline:** Nov 29, 12:00 noon (so teams have time to fix problems)

By now, every team should have deployed their application to a cloud service.
The URLs are posted in the class projects sheet: <https://bit.ly/ISP2021-projects>

## Assignment

Try to find defects (bugs) in other teams' apps, using the cloud-deployed version.

## What's a Defect?

- Anything in their [project proposal](https://bit.ly/ISP2021-projects) but cannot be done in the actual app.
- App returns incorrect or invalid data
- Security problems.  Please try SQL Injection and Javascript Injection.
  - if you are more ambitious, try fuzz testing (sending random data).
- Authorization errors, such as being able to modify data submitted by someone else or access a restricted page without login. These are security errors.
- Mistakes in the UI, including spelling and formatting errors.
- Navigation errors: Links that don't work or go to the wrong page.  Inability to navigate, such as cannot get back to main page without using browser Back button). Any valid request that returns a 404 Not Found response.
- Anything that causes the app to become unresponsive, return an exception page, or a 5xx status code page.
- Anything that fails to work.
- Other perceived problems

## Testing and Reporting

1. Test as many other apps as you want to find defects and earn bug bounties.
   - The first report of a confirmed, unique defect earns 1 point.
2. **Report Defects** in 2 places:
   - First, open an issue on team's project repository.
     1. describe the problem
     2. include information on **how to reproduce the problem**
     3. helpful: include screenshot(s) showing the problem
   - Second, add a row to the Google spreadsheet at <http://bit.ly/isp-project-testing> on the "Bug Reports" page.  Include:
     1. your name
     2. project name
     3. defect category (categories are in the bug reporting sheet)
     4. link to issue on Github
     5. brief description of defect
4. Wait for team to **confirm the bug**.  If they do not confirm within 2 days, email the instructor.
5. No points for finding defects in your own application. But you should report issues anyway.

## Earn Bug Bounty Points

The first person to report each confirmed, unique "bug" or "defect" related to functionality will earn 1 point. Points count as extra homework score.

The person who finds the most defects will earn an extra 5 points.


## Other Defects (No Bounty But Please Report)

Please report the following, even though they don't earn bug points.

- spelling mistakes
- confusing navigation
- non-intuitive behavior (app behaves differently from what users would normally experience in a web app). 

## Validation by Development Team

**Promptly** review each issue. Apply a label to the issue (Github lets you add labels to issues).

Use these labels:

* **bug** - if you confirm its a bug that hasn't been reported before.
* **duplicate** - the issue duplicates another issue. Add a comment like "Duplicates #18" to the issue, and close it.
* **question** - request for more information is needed, because the problem isn't clear or you can't reproduce it.  Add **bug**, **duplicate**, or **not a bug** label when you understand the issue.
* **not a bug** - if you can't reproduce it, or conclude that its not a bug. You should explain *why* its not a bug in your comment closing the issue.


## Example of Non-Intuitive Behavior in a Commercial Web Site

Kiatnakin-Phatra Asset Management has web-based application at <https://kkpamonline.kkpfg.com/>
A client can view his portfolio, buy or redeem mutual funds, and view a transaction report.

On the top-right of the page is a `Logout` link.  Most users would **expect** that clicking on this link will log them out.

![Phatra Navigation Bar](/images/Phatra-Navbar.png)

When you click "Logout" is shows a page like this:

![Phatra Logout Screen](/images/PhatraLogoutScreen.png)

**Is the person logged out?**  The answer is **no**.

You can use the browser "Back" button to re-enter the site and you are still logged in!  This is *non-intuitive* and a potential security risk.

Its also stupid.  The "Close" button won't close the browser window.

## Multiple Defects at KKPAM

The web app actually has **multiple defects**.

1. You must click through 4 pages to get to the page showing your portfolio.
2. On a standard 1368x1024 display (typical notebook display) the "Logout" button is pushed off the right edge of screen.
3. Click on a fund name shows uninteresting info about the fund instead of details of your holdings of that fund, which is the **expected & desired behavior** for most people.
4. Pages have a "Main Menu" button that shows the portfolio pages. This **is not** a main menu. Example of **inconsistent naming**.
5. The logout page has a `Close` button, but it doesn't work in any modern browser!  
   - This makes me think the developers don't understand the way browsers work.
