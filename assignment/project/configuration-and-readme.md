---
title: Project Configuration and README
---

1. **Separate configuration data from code**.  Use a configuration file and/or the environment.
   - Consider using the `python-decouple` package
   - Provide a sample configuration file, with comments describing what the settings are for.

2. Your application should have at least 3 methods of deployment:
   - "Dev" installation - run locally or on a server
   - Production deployment - in the cloud or a virtual server
   - Test deployment - Django provides this
   - **Extra Credit** a "preview" cloud deployment that is entirely separate from "production"

3. The local installation **must not** use the production (cloud) database!  
   - Use a separate database, and make it user-selectable.

4. Provide initial data for dev (local) deployment .  
   - Installation instructions must include an **easy** way to initialize the database and add data, so app can be used by others.
   - Example: for recipes app, provide data for some categories and recipies.
   - Look at Django `manage.py loaddata ...` for this.
   - Better way: run database in its own Docker container
   - Include some user with known username and password in initial data

5. Provide good installation instructions:
   - Describe this in a separate document
   - Installation steps must be numbered 1, 2, 3 ....
   - Document the requirements, including OS and Python requirements.
   - Must be **actually what is required** not what you happen to be using!
   - Example: don't write "Python 3.11.4" if the app works fine on Python 3.9

6. Dependencies should be accurate and realistic!
   - Wrong: "Requires Python 3.11.4"
   - *Really?* Python 3.11.2 won't work?  Python 3.9 or 3.10 won't work?

7. Use a standard orderinf of sections in README.md - see below.

8. **Deploy To Cloud by ___________(TBA)__________________**.

9. **Add Logging** to your application. 
   - Log all unexpected exceptions.
   - Log user events.  Include login, logout, failed login attempt with IP addr.


### Order of Info in README.md

**Project Name**

[badges]

Project description as paragraph(s).    

Screenshot of application.

URL of deployed application

**Team Members**

listed as a table.  Don't include student ID (its not relevant)

**Development Documents**

- Link to project wiki - someplace with an index of all project docs.
- Links to iteration plans and retrospectives.
- Link to project tracker (Github Project, Trello, Assana, etc). Must be readable by TAs and instructors.

**Installation Instructions**

- Refer to a separate file. 
- OK to have separate instructions for development and production deployments

**How to Run**

Instructions how to run the app that was just installed.  If these are long, put in a separate document. OK to combine with "Installation Instructions".
