---
title: Project Configuration and README
---

1. **Separate configuration data from code**.  Use a configuration file and/or the environment.
   * Consider using the `python-decouple` package
   * Provide a sample configuration file, with comments

2. Your application should have at least 3 methods of deployment:
   * Local installation ("dev" deployment)
   * Cloud deployment ("production")
   * Test deployment (Django provides this)
   * **Extra Credit** a "preview" cloud deployment that is entirely separate from "production"

3. The local installation **must not** use the production (cloud) database!  Use a separate database, and make it user-selectable.

4. Provide initial data for local installation.  Installation instructions must include an **easy** way to initialize the database and add data, so app can be used.
   * Example: for recipes app, provide data for some categories and recipies.
   * Look at Django `manage.py loaddata ...` for this.
   * Include data for a local user with known username and password.

5. Improve your installation instructions:
   * Installation steps must be numbered 1, 2, 3 ....
   * Separate "Installation" instructions from "Running the app"
   * Also see the next item

6. Dependencies should be accurate and realistic!
   * Wrong: "Requires Python 3.6.6."
       - *Really?* Python 3.6.5 or 3.6.7 won't work? Python 3.5 won't work?

7. Use a standard order of sections in README.md - see below.

8. **Deploy To Cloud by Saturday, 24 Nov, 12 midnight**.

9. **Add Logging** to your application. 
    * Log all unexpected exceptions.
    * Log user events.  At least login and logout.

### Order of Info in README.md

**Project Name**

(optional badges)

Project description as paragraph(s).    
Screenshot of application.

URL of deployed application

**Team Members**

listed as a table.  Don't include student ID (its not relevant)

**Development Documents**

* Link to iteration plans
* Link to task board
* Link to issues

**Installation Instructions**

* Required Software
1. first install step
2. second install step

**Wrong**:

1. `pip install django`
2. `pip install djangorestframework`
3. `pip install python-decouple`
4. Run: `python manage.py runserver 8000`
5. Browse to http://localhost:8000

1-3 should all be in a `requirements.txt` file. Steps 4-5 are "How to Run" not "installation".  Instructions should note differences in operating system.

**How to Run**

Instructions how to run the app that was just installed.
