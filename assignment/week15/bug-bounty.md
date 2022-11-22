---
title: Bug Bounty - Test 'Production' Web Apps
---

**Deadline:** 27 Nov, 6:00 PM  so that teams have time to review & fix problems.

This week, every team should have deployed their application to a cloud service.

URLs are posted in the class projects sheet: <https://bit.ly/isp2022-projects>

Report Bugs here [Bug Hunting](https://docs.google.com/spreadsheets/d/1dlIcnRwHkHJULFYWduymDe1ynh9XrFAi4XW2oYWK2CA/) and on the project's Issue Tracker.

## Assignment

Try to find defects (bugs) in other teams' apps, using the cloud-deployed version.

## What's a Defect?

- Functionality: any feature listed in their [project proposal](https://bit.ly/isp2022-projects) but cannot be done in the actual app.
- Functionality/correctness: App returns incorrect or invalid data or fails to retain data when it should
- Security errors.  
  - Disclosure of confidential settings. Can you get it to print the settings on an error page?
  - Data exfiltration, meaning to access data you should not be able to access
  - if you are more ambitious, try fuzz testing (sending random requests)
  - please try SQL Injection or Javascript Injection
- Authorization errors (a subset of "Security" errors)
  - being able to modify data submitted by someone else 
  - access a restricted page without login ("authorization bypass")
  - you don't have to use the web UI!  Discover what URLs that app uses (including looking at source code) and try submitting GET/POST/PUT/DELETE requests direct to those URLs without authorization.  This may work well with REST web service urls.
  - try to access the admin account (guess common passwords)
- Appearance: Mistakes in the UI, including spelling and formatting errors.
- Navigation errors: 
  - Links that don't work or go to the wrong page.
  - Inability to navigate, such as cannot get back to the main page without using browser Back button (remember KU Polls?).  This is a "Usability" error.
  - Any valid request that returns a 404 Not Found response.
- Anything that causes the app to become unresponsive, return an exception page, or a 5xx status code page.
- Anything that fails to work.
- Installation instructions don't work. You tried to install and run it locally using installation instructions in project's Github repository, but they don't work. This includes missing steps.
- Other perceived problems

## Testing and Reporting

1. Test as many other apps as you want to find defects and earn bug bounties.

2. **Reporting Defects**:  See instruction on the "Bug Bounty" spreadsheet.

## Earn Bug Bounty Points

The first person to report each confirmed, unique "bug" or "defect" related to functionality or installation earns 1 point. Security defects earn 2 points. Usability, Appearance, and Other defects earn 1 point if deemed significant by instructor.

The person who finds the most defects will earn an extra 5 points.

Points count as an extra homework score.


## Validation by Development Team

**Promptly** review each issue. Apply a label to the issue (Github lets you add labels to issues).

Use these labels:

* **bug** - if you confirm its a bug that hasn't been reported before.
* **duplicate** - the issue duplicates another issue. Add a comment like "Duplicates #18" to the issue, and close it.
* **question** - request for more information is needed, because the problem isn't clear or you can't reproduce it.  Add **bug**, **duplicate**, or **not a bug** label when you understand the issue.
* **cannot reproduce**
* **not a bug** - if you can't reproduce it, or conclude that its not a bug. You should explain *why* its not a bug in your comment closing the issue.

---

## Non-Intuitive Behavior in a Real, Commercial Web Site

Kiatnakin-Phatra Asset Management has web application at <https://kkpamonline.kkpfg.com/>

A client can view his portfolio, buy or sell mutual funds, and view transactions.

On the top-right of the page is a `Logout` link.  You would **expect** to be logged out by clicking this link:

![KKPAM Navigation Bar](/images/Phatra-Navbar.png)

When you click "Logout" is shows a page like this:

![KKPAM Logout Screen](/images/PhatraLogoutScreen.png)

**Is the person logged out?**  The answer is **no**.

You can use the browser "Back" button to re-enter the site and you are still logged in!  

This is *non-intuitive* and a potential security risk.

Its also stupid.  The "Close" button does not (cannot) close the browser window.


The KKPAM web app has other defects as well, including UI controls that are off-screen on some displays!
