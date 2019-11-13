## Project Testing Assignment

This is an individual assignment.
Install another team's project on your computer and try to run it.
Use the instructions on the project's homepage (README.md) for how
to install and run.

This will help the team uncover problems in their project,
and you may learn something that helps your own project.

Since you are running the project locally, OAuth authentication probably won't
work.  So, if login is required then find some other way to login (such as
a locally stored test login).

### Instructions for Tester

1. Find the project that you are assigned to test here: [Project Testing](http://bit.ly/isp-project-testing)

2. Copy the test report template: [http://bit.ly/isp-project-test](http://bit.ly/isp-project-test) and customize it according to instructions in the template.

3. Share your test report doc with everyone at ku.th (or everyone on the web) and add a link in [Project Testing](http://bit.ly/isp-project-testing) spreadsheet.

4. Go to the project's Github site and read the instructions for installing and running the project.  Two projects (Manatee Chat and Travel Planner) require you to install 2 Github projects.

5. Follow their instructions, and: 
   a) create a report of what you encountered (using the template from step 2)
   b) post issues on the team's Github repo

6. Things to report:
   - instructions that are incomplete or hard to understand
   - things the don't work or cause errors
   - undocumented dependencies. For Python projects, there may be dependencies on packages not listed in `requirements.txt`.
   - A good way to find undocumented dependencies is run the project in a virtualenv, using only the project `requirements.txt` to add packages to virtualenv.
   - instructions that require too much work
       * Example: requiring many modifications to `settings.py` instead of using the [python-decouple][decouple] package and providing an example `.env` file, e.g. `test.env`.

7. Run the application and perform whatever functionality has been implemented so far.
   - Report anything that doesn't work as it should.
   - Report deficiencies that keep you from using the application, such as can't search because their is no data in database.


### Instructions for Team

1. Provide clear and simple installation instructions. 
   - Optionally provide an install script.
   - Avoid requiring tester to install a lot of heavy-weight apps, like PostgreSQL or MySQL.

2. Provide configuration for a light-weight database like SQLite and an easy way of changing the project config to use this database. 
   - Consider providing a separate configuration file for local installation versus cloud-based installation. This is easy to do using a Python file or the [decouple][decouple] package.
   - provide a way to import initial data into the project, or write code for application to do this itself (if app detects an empty database it downloads and imports initial data)
   - Django has "dumpdata" (export database model data to JSON) and "loaddata" (import model data from JSON) commands for this. 

3. Fix problems as soon as possible so tester can finish his assignment.

4. If your project **really** can't work with a local database, then provide the tester with test credentials (limited privelages) to access your cloud-based database and configure the cloud-based database to accept connections from anywhere.  


## Ref

[Python-decouple][decouple] module and [how to use it][decouple-howto].

If you don't like depending on *yet another package*, you could do the same thing using environment variables (envvariables) or a Python script that sets configuring variables and is invoked by settings.py.

For Java or Scala, the standard approach is to use a Properties file for configuration values.  You used properties in one of the Coin Purse labs.


[decouple]: https://pypi.org/project/python-decouple/ "Python-decouple module"
[decouple-howto]: https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html
