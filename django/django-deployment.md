## General Issues for Deploying a Web Application

There are 3 styles of deployment to the "cloud".

1. Deploy to a server or virtual server you configure yourself.
    * This involves configuring a static web server (like nginx or Apache HTTPD), possibly a database, and other software you need
    * Known as "infrastructure as a service" (IaaS) or "platform as a service" (PaaS) depending on how much you have to do yourself
2. Deploy your app in a Docker container
    * You package your application as a Docker image file. The could service manages Docker (often using Kubernetes).
    * The database is usually provided by a separate service.
3. Deploy application directly to the cloud.
    * The cloud service provides everything (except possibly a database server).
    * You provide a configuration file that tells the cloud service what software you need and how to configure and launch your app.
    * Heroku is example of this.
    * This model is known as "serverless computing".

## Common Errors or Concerns when Using a Cloud Service

1. Protecting confidential configuration values such as database password, application secret key, private files.
2. Software dependencies.  The installed software won't be same as on your computer -- you must make dependencies explicit.
3. Database initialization.
4. Handling of static files, such as images, CSS, Javascript.

## Additional Work in Deploying a "Production" Cloud Application

For a production application you also need to understand and plan for the following.

1. Logging and viewing logs of events.
2. Backing up the database and other dynamic data (e.g. user uploads).
3. Security, including monitoring and responding to attacks.


## Deploy Django App on Google Cloud using App Engine Standard

See:    
[Getting Started with Django](https://cloud.google.com/python/django/) describes 4 ways to deploy Django to Google Cloud.
  * Google App Engine Standard Environment
  * Google App Engine Flexible Environment - more configuration choices, including use of Docker
  * Google Kubernetes - deploy Django in a Docker container
  * Google Compute Engine - deploy in a VM

[Running Django on App Engine Standard Env](https://cloud.google.com/python/django/appengine) - how to deploy on GAE Standard, using the Django tutorial application.

### General Setup

Install the [Google Cloud SDK][google-cloud-sdk].  The `gcloud` command is used
for some operations.

[Google Cloud Console](https://console.cloud.google.com/) (GCP) at
[https://console.cloud.google.com/](https://console.cloud.google.com/) is a
common endpoint for creating, editing, and monitoring GCP applications.
Become familiar with it.

### Steps to Deploy on GAE

1. Download the Cloud SQL Proxy, which lets you access a Google cloud database from your local machine.
```bash
wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O bin/cloud_sql_proxy
chmod +x bin/cloud_sql_proxy
```
2. Create a Cloud SQL Instance.
   * Goto https://console.cloud.google.com/sql/instances?pli=1
   * Use a 2nd generation instance.
   * Select MySQL as database.
   * Give it a non-sensitive name. Name is publicly visible.
     - Project: Django Polls
     - Database instance ID: polls
     - Root password: [Ku_city][Iku]
     - "MySQL Development" database: 1 vCPU, 0.6GB memory, 
     - storage: 10GB is minimum
     - disable binary logging
     - **Region**: `asia-southeast1`
     - Add database flags: none added
   * Select **region**. Choose same region as your app runs in.
   

2. Use `gcloud` command from Google Cloud SDK to check the connection:
```bash
# the last argument is name of the sql database instance
gcloud sql instances describe --project django-polls-218907 polls
```
* Info returned by this command includes the Cloud SQL **connection name** needed to configure connection to the database.
  - The instance connection name is [PROJECT_NAME]:[REGION_NAME]:[INSTANCE_NAME]
  - My Connection Name: `django-polls-218907:asia-southeast1:polls`
  - IP Address: 35.240.220.4

3. Edit Django `mysite/settings.py` and set:
   - database setting for running on google cloud
   - separate database setting for when running locally, and connecting via cloud_sql_proxy.

4. Start the SQL Cloud Proxy using a TCP port:
```bash
  bin/cloud_sql_proxy -instances="instance_connection_name"=tcp:3306
  # for sample project
  bin/cloud_sql_proxy -instances="django-polls-218907:asia-southeast1:polls"=tcp:3306
```
5. Create a database and database user in the Cloud SQL database, by connecting to the proxy with an sql client of your choice.
   * Using `mysql` client connecting to cloud_sql_proxy:
```bash
   # Confusing. "polls" is name of the MySQL database
   # and also name of the schema (in the database) used for this app.
   # Better to give the MySQL database a different name.
   mysql -u root -p -h localhost [--port=3306] polls
```
   > This didn't work for me.
   * Using GCP Console (console.cloud.google.com/sql/instances).
     1. to create a new database schema named **polls** inside the "polls" database
     2. create an admin user **polls_admin** (jjj) who has full control over database:
     3. Give full control:  GRANT ALL ON polls.* TO 'polls_admin';

6. Start the database on GCP, then initialize it:
```bash
./manage.py makemigrations
./manage.py makemigrations polls
./manage.py migrate
./manage.py createsuperuser
# Now run it
./manage.py runserver
```
and navigate to http://localhost:4000/admin/


### Connect to Cloud SQL Proxy using Sockets or FUSE

Other ways to connect to the Cloud Proxy are described in 
[About the Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy#gcloud).
Many of them involve creating a *socket* the a `/gcloud` directory,
and connecting to that socket. One proxy intance can server many sockets.

There are many ways to start the proxy using sockets:
```bash
# 1. Automatic instance discovery
./cloud_sql_proxy -dir=/cloudsql &
# 2. Project discovery
./cloud_sql_proxy -dir=/cloudsql -projects=myProject &
# 3. Compute Engine with explicit instance specification
./cloud_sql_proxy -dir=/cloudsql -instances=myProject:asia-southeast1:myInstance &
```
For all 3 of these cases, to connect using `mysql` client use the socket name:
```shell
mysql -u username =S /cloudsql/myProject:asia-southeast1:myInstance
```

### Deploy the Application to App Engine

```
# Collect all static content to top-level STATIC_ROOT (in settings.py) dir
./manage.py collectstatic
gcloud --project django-polls-218907 app deploy
```

### Using a Service Account

The [About the Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy#gcloud) docs describe how to create a service account.

### Security and Credentials

In the GCP tutorial for deploying a Django app to the Google App Engine,
the database credentials are stored in `mysite/settings.py`.
For example:
```python
if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/<your-cloudsql-connection string>
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/django-polls-218907:asia-southeast1:polls',
            'USER': 'polls_admin',
            'PASSWORD': 'fat-chance!',
        }
    }
else:
    # Running locally
    DATABASES = {
        local database settings
    }
```

The `settings.py` file is needed to both configure and run the application,
so its probably part of your Github repository files.  But it contains
your GCP database credentials.

You can make this more secure in two ways.

1. **Don't use the database root user**. As shown above, create a separate database user who only has access to your app database, not the entire Cloud SQL Database.  You can create this user using GCP console (in browser) or MySQL client, with cloud_sql_proxy running.
```
Todo: add the commands
```

2. **Move credentials from settings.py to app.yaml, and don't commit app.yaml to Github**.  Here's an example.  In `app.yaml` define some environment variables:
```yaml
runtime: python37

env_variables:
  SECRET_KEY: 'django app secret key'
  DEBUG: 'False'
  DB_HOST: '/cloud/sql/django-polls-123456:southeast-asia1:pollsdb'
  DB_NAME: 'pollsdb'
  DB_USER: 'polls_admin'
  DB_PASSWORD: 'fat-chance!'
```
and in `mysite/settings.py` refer to the environment variables:
```python
import os

DEBUG = os.environ['DEBUG'] == 'True'
SECRET_KEY = os.environ['SECRET_KEY']
  .
  .
  .
DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.mysql',
         'HOST': os.getenv('DB_HOST','127.0.0.1'),
         'USER': os.getenv('DB_USER','none'),
         'PASSWORD': os.getenv('DB_PASSWORD',''),
    }
}
```
`os.getenv('DB_HOST','127.0.0.1')` means to get the value of `DB_HOST` from the environment, and if no envvar exists with that name then use the value '127.0.0.1' instead.

When the application is run on GAE, the environment variables from app.yaml will be used.  When run locally it will either use default values or values you have set in your own local environment.


---
[google-cloud-sdk]: https://cloud.google.com/sdk/docs/
   
