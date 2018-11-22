## Team Assignment for 22 Nov

1. Your application should have at least 3 methods of deployment:
   * Local install ("dev" deployment)
   * Cloud install ("production")
   * Testing (Django provides this)
2. The "local (dev) install" **must not** use the production (cloud) database!  Use a separate database.
3. Provide initial data for local installation.  Installation instructions must include an **easy** way to initialize the database and add data, so app can be used.
   * Example: for recipes app, provide data for some categories and recipies.
   * Look at Django `manage.py loaddata ...` for this.
   * Include data for a local user with known username and password.
4. Separate "config" data from code.  Use a config file and/or the environment.
   * Consider `python-decouple` package
5. There must be a way to specify a **different** config file from the default one, so you can have separate config data for "dev" and "production".
6. Install Instructions:
   * Installation steps must be numbered 1, 2, 3 ....
   * Separate "installation" instructions from "running the app"
7. Dependencies should be accurate and realistic!
   * Wrong: "Requires Python 3.6.6."
       - *Really?* Python 3.6.5 or 3.6.7 won't work? Python 3.5 won't work?
   * Wrong: in `requirements.txt`:
   ```
   pytz==2018.4
   ```
       - `pytz` contains Timezone info. Use the latest version: `pytz>=2018.4`.
8. Use a standard order of sections in README.md - see below.
9. **Deploy To Cloud by Saturday, 24 Nov, 12 midnight**.
10. Add Logging to your application.
11. Create a thorough End-to-Ending test using Selenium.
    * Must test many features of your app using Selenium to control browser.
    * Use the most important features, including input and search.
    * Must detect and report problems.

### Heads Up - Bug Hunting

Other students will be testing your cloud deployment.

Watch for bug issues.

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
1. step 1
2. next step
3. next step

**Wrong**:

1. `pip install django`
2. `pip install djangorestframework`
3. `pip install python-decouple`
4. Run: `python manage.py runserver 8000`
5. Browse to http://localhost:8000

1-3 should all be in a `requirements.txt` file. Steps 4-5 are "How to Run" not "installation".

**How to Run**

Instructions how to run the app that was just installed.
