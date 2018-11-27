## Bug Bounty Hunting:  Test 'Production' Web Apps

**Note:** By 25 November, every team should have some version of their app
deployed to the cloud and the URL shown in their README.md. (This was specified in class last week.)

Try to find defects (bugs) in other teams' web apps, using the cloud-deployed version.

1. Everyone **must** test the cloud deployment of the web app
listed on the Google sheet (same as for config testing).
2. You can also test as many apps as you like to find defects and earn bug bounty points.
3. **Report Defects** 2 places:
    - First, open an issue on team's project web.
      You must provide enough info for them to reproduce the issue.
    - Second, add a row to the Google sheet containing:
        1. app name
        2. your name
        3. issue number
        4. brief description of defect
4. No points for finding defects in your own application.  But you should report issues anyway.

## Earn Bug Bounty Points

The first person to report each confirmed "bug" or "defect" related to functionality with earn 1 point, up to a max of 20 points.

A "bug" or "defect" includes:

* page navigation errors
* authorization errors, such as being able to modify data submitted by someone else.
* anything that causes the app to crash, return an exception page, or a 5xx status code page.
* app returns incorrect or invalid data

To earn a point, the team must acknowledge the defect and you must be the first one to report it.

Please report the following, even though they don't earn bug points.

* spelling mistakes
* confusing navigation, e.g. buttons
* non-intuitive behavior (app behaves differently from other similar apps in the same situation).  

## For Teams

**Promptly** review each issue. Apply a label to the issue:

### Labels

* **bug** - if you confirm its a bug that hasn't been reported before.
* **duplicate** - the issue duplicates another issue. Add a comment like "See #18" or "Duplicates #18" to the issue, and close it.
* **question** - request for more information is needed, because the problem isn't clear or you can't reproduce it.
* **not a bug** - if you can't reproduce it, or conclude that its not a bug. You should explain *why* to the person who opened the issue.

## Example of Non-Intuitive Behavior

Phatra Asset Management has web-based account services application at https://phatraclick.phatraasset.com.  
A client can view his portfolio, buy or redeem mutual funds, or view/print a transaction report.

On the top of the page is a `logout` link.  Most users would **expect** that clicking on this link will log them out.

However, after clicking on the link it shows a page like this:

![Phatra Logout Screen](/images/PhatraLogoutScreen.png)

Is the person logged out?  The answer is **no**.
You can use the browser "Back" button to re-enter the site and perform more actions.  This is both *non-intuitive* and a potential security risk.

Its also stupid.  The "Close" button won't actually close the window on most web browsers.
