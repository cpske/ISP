---
title: Test Project Installations
---

This is an individual assignment.

The purpose of this assignment is to test how accurate, complete,
easy to understand, and well written a project's installation instructions
are.  

Your feedback will help the team improve their project,
because software that others can't use doesn't last long!

The purpose is to problems with the installation,
and bugs in basic functionality (e.g. can't view a page, can't login).
The purpose is not detailed testing of the application.

> When you apply to a tech company for an internship or job, the company
> may look at your projects on Github.  A project with a well written
> README and good documentation shows attention to detail, and that
> you care about your software.

## Instructions

[Project Testing Assignments](http://bit.ly/isp-project-testing)

1. Clone the project you are assigned to test.
2. Configure it according to the instructions given on the project's Github site.  Try not to ask the team for help.
3. Run it.  Does it show a page?  Can you navigate the app? Any error messages?
   - some features may not work, such as OAuth or a Firebase database, but the application should run and provide some basic functionality
4. Report any problems as Github issues, and paste a link to the issue on the Google spreadsheet.
   - your issue should describe the problem. If its an error, describe what command caused the error and include the error message.
   - If you don't find any problems, write "No" in the "Any issues?" column.
5. Kinds of things to report:
   - instructions that are incomplete or hard to understand
   - spelling and grammar errors
   - instructions that don't work or cause errors
   - missing steps in the instructions
   - instructions that require too much work. For example:
     - requiring you to set some variables in `settings.py` instead of using a configuration file like `.env`
     - requiring you to install MySQL
   - undocumented dependencies or requirements
   - basic functionality that doesn't work (excluding things like OAuth authentication which typically won't work on a test system)
   - anything else you think needs improvement

## For Teams

- investigate all issues.  If it's a problem, then fix it and note what you changed as a comment when you close the issue.
- if something is not a problem, explain why not in the closing comment

If your project **really** can't work with a local database, then provide the tester with test credentials (limited privelages) to access your cloud-based database and configure your cloud-based database to accept connections from the tester's location (e.g. KU's address space 158.108.\*.\*).

