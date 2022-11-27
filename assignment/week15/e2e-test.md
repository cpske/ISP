---
title: Homework: E2E Test of Your Team Project
---

Each person write an E2E test of your team project using Selenium in Python,
or Robot Framework.

1. The E2E test should be a *stand-alone test* that demonstrates a complete end-to-end use of a significant part of your application.  It does **not** need to be a thorough test of the application, and does not need use a test framework.
   - The E2E test should run *stand-alone*, not as a Django test suite. 
   - Assume the project server is already running on a cloud service or locally.  Ideally, your tests should work either way (server running locally or in the cloud).
   - You do not need to use a test framework, but the test **should** detect if something goes wrong.
   - If you want to use a test framework, pytest is more suitable than unittest. You can organize your E2E test as test functions.

2. The E2E test should demonstrate at least one end-to-end use of some significant functionality of the project, to show it is working as expected.
   - a test that only logs in and shows a page will not get any credit
   - Example for KU Polls: login, show a list of polls, choose a poll, and sshow the results

3. Externalize data values needed by your test using `python-decouple`.  You should **at least** externalize these:
   - URL the project is running at
   - Login credentials.  Create a local account for login or use OAuth.  In the case of OAuth, assume that the user is already logged in to his OAuth account (e.g. Google) and has authorize accessed to his OAuth resource.

4. Provide an usable `.env` file for the externalized values:
   - `cloud.env` for values to run the E2E test when the project server is in the cloud
   - `local.env` for values to run the E2E test when the project is running locally

5. You should at least provide `cloud.env` even if the project doesn't run on your computer.

6. Use Chrome or Firefox for tests. Not Edge or Safari.


**What to Submit**

Use this Github Classroom assignment:
<https://classroom.github.com/a/24VOGue1>

Clone it and add everything needed to run your E2E test to the repository.  Do **not** include the project code, of course.

In the repository include these files:

| File        | Description          |
|-------------|----------------------|
| README.md   | explains how to run your E2E test and what functionality tests |
| `local.env` | a python-decouple `.env` file containing values used when the project is running locally (on `localhost`). |
| `cloud.env` | a python-decouple `.env` file containing values used when the project is deployed on a cloud service |
| e2e code    | one or more files containing your E2E test(s) |


### Robot Framework

If you use Robot Framework, then use the "Resource" statement and put externalized variables in a file named `local.txt` or `cloud.txt`.

Example robot test:
```robot
*** Settings ***
Documentation      E2E Test of My Project
Resource           ${CURDIR}/local.txt

*** Variables ***
${BROWSER}         Firefox

*** Tests ***
Visit Homepage
    Open Browser         ${SITE_URL}   ${BROWSER}
    Location Should Be   ${SITE_URL}
    Title Should Be      My Project
```

Example of `local.txt`:

```robot
*** Variables ***
${HOST}         localhost
${SITE_URL}     http://localhost:8000
${USERNAME}     demouser
${PASSWORD}     hackme22
```
