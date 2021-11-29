---
Title: Review Questions on Logging, 
---

1. Where should a 12-factor web application record log messages?
   ```

   ```

2. What should be logged at which log level?

   * User login and logout: INFO
   * Incorrect login attempt: WARNING	
   * Database or ORM queries made by our app: DEBUG
   * User activity, such as voting for a poll: INFO	
   * Expected exceptions like trying to access an optional resource: DEBUG	
   * Unexpected exceptions, like type errors: ERROR	

   Explanation:  Prioritize your log messages so that events which
   are more likely to need attention have a higher priority.
   The usual meanings of the priorities are:
   * TRACE - flow of execution of the program, such as entering or leaving methods. Even more verbose than DEBUG.
   * DEBUG - messages useful to developers for debugging or analyzing the application
   * INFO - events, activity, or actions that might help explain "what happened" while program was running. Routine activity is usually logged here.
   * WARNING - an unusual condition, or something that may need attention.
   * ERROR - software, hardware, or environment error. Something that should normally not occur.
   * CRITICAL or FATAL - an error that causes the application (or part of it) to stop working.

   Logging applications let you filter messages by severity.
   If you set the filter to "INFO", you would see all messages of level "INFO" or
   higher (WARNING, etc), but none of the "DEBUG" or "TRACE" level messages.
   Python's `logging` doesn't have a "TRACE" level, but Java loggers do.

3. A web application needs a web server.
   What approach does the 12-Factor app recommend?

   - Include the web server as part of your application.

   In the old days, developers packaged web apps in a standard format such as WAR (Java)
   or WSGI, and deployed the package to a web app server such as Tomcat, Glassfish, or Apache Httpd.
   The web server is a separate application, and usually runs as a daemon (background process).
   Many apps can run in the same server (also called a 'container'), and the 
   containers provide a lot of functionality, such as maintaining access logs,
   filtering, URL mapping, and managing database connections.

   However, configuring a server like Tomcat or Glassfish is a lot of work!
   And running multiple apps in one container means that one app can suffer 
   if another app is using all the compute resources.

   To make deployment more reliable and make web apps more portable, 
   the current approach is for web apps to be mostly self-contained.
   The web server is included as part of the application.
   For Python apps, include Gunicorn or uWSGI with your app.
   For Java, include Jetty embedded web server.

   I wrote "mostly self-contained", because apps do depend on some external services,
   such as those in the next question.

4. For "backing services" such as a database or e-mail service, how should an application handle these services?
   - Treat the service as an attached resource, with connection details stored in the "configuration".  *This makes your application more portable.*

5. What's wrong with this Django settings.py file?
```python
from dj_database_url import parse

SECRET_KEY = '#@klgknivoel#@dkr_*ablweigh9235hasdfie3hc7AC**y'
DEBUG = True
ALLOWED_HOSTS = ['*']
DATABASE_URL = 'postgres://admin:admin123@compute-1.amazonws.com:5432/d4e956bc11'
DATABASES = { parse(DATABASE_URL) }

# OAuth client credentials
SOCIAL_AUTH_FACEBOOOK_KEY = '1620005393349'
SOCIAL_AUTH_FACEBOOOK_SECRET = 'we-sell-your-data-hahaha'
```
   - Answer: Configuration data should not be stored in code.  Almost everything in the above code fragment is configuration data that should not be in code.  Some of the values need to be kept private, too.

6. In the above settings.py file, which values are "configuration" settings?
   - Everything in the code snippet, except `DATABASES = {...}`.

7. The 12-Factor App recommends storing configuration values (such as `SECRET_KEY`) where?
   - In the environment.

8. Deployment for development and production are different. How should we separate the source code for these two cases?
   - Keep development and production code as similar as possible. Vary only the config.   
   *This is related to the recommendation to have only one code base.*

9. In a web app using an MVC design, where should we put application logic, such as computing total votes in a poll?
   - The models

10. In a web app using an MVC design, where should we put page-flow logic, such as where to redirect a user after a query?
    - The controllers (Django calls them "Views")

11. What are 3 things you should test using End-to-Ending testing?
    - The flow of the application is correct, from start to finish.
    - External dependencies.
    - Application behaves as expected.

12. In the KU Polls application, suppose that a user must login before he can submit a vote. What's the best way to perform this check in code?
   - The *best* way (in my opinion) is:
       * Use method annotations, such as Django's `@Login_required`.  Its best because it separates the "concern" of verifying someone is logged in, from application logic and avoids a lot of duplicate code.
   - An *acceptable* way is:
       * Any of the above (URL router, an annotation, or a check inside the code)


