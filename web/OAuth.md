## OAuth 2 Web App Flow

There are 3 parties involved:

* web app (OAuth client)
* OAuth Provider which authenticates users, such as Google
* user - the owner of the credentials

1. User navigates to web app's login page. He clicks on "Authenticate with Google" link.
2. Web app redirects user to a Google URL to authenticate.  It includes some parameters that tell the OAuth provider you want an "authorization code" to access the user's info, and a redirect URL:
```
https://oauthprovider.com/auth/?
   response_type=code&
   redirect_uri=YOUR_CALLBACK_URI&
   client_id=YOUR_CLIENT_ID&
   scope=profile&
   scope=email
```
3. OAuth Provider (Google) asks user if he wants to grant access to your site for the access permissions (scope) you requested.  You may also need to specify these when you register your app.
   * If user isn't currently logged in, he is prompted to login first.
4. If user approves, the OAuth Provider (Google) does two things:
   a. Create a short-lived **authorization code** for your site
   b. Redirect user to your callback URL, with the authorization code included.
```
   https://YOUR_CALLBACK_URI/...?code=auth_code
```
5. The `auth_code` is a short-lived token.  Your app must exchange it for an access token.  So, your app send an HTTPS request (as API call, not using web browser) to OAuth provider.  This time, you must prove your app's identity using the client secret obtained during registration.
```
https://oauthprovider.com/auth/?
   grant_type=authorization_code&
   code=auth_code&                 <-- auth_code sent to your callback URL.
   redirect_uri=YOUR_CALLBACK_URI&
   client_id=YOUR_CLIENT_ID&
   client_secret=YOUR_CLIENT_SECRET
```
6. OAuth Provider verifies the parameters.  If everything is OK, it sends back an **access token**.  It may also send a **refresh token** that can be used to refresh the access token, since access tokens expire.

## Front-end Authentication

This is a different OAuth Flow for apps that have rich front-ends that mostly communicate with backend using a RESTful API.  The front-end obtains a "token" from the OAuth server, and gives the token to the backend.  Since the front-end is running on user's machine, so secret is used in the request.

This flow is described in the TopTal article on Social auth.

## Python Social Auth Library

[Python Social Auth][psa] library on Github provides methods making it easier to create an OAuth client for different providers, including Google, Github, Facebook.

PSA has several subprojects, including a Django component to integrate social-auth-core in a Django project.

### Python components to include in your project

In `requirements.txt` and your actual environment, include:
```
social-auth-core
social-auth-app-django
```
Execute:
```
# On my machine, run these as root (sudo) to install globally
pip install social-auth-core
pip install social-auth-app-django
```

### Django Project: configure authentication backends

In project settings file, add:
```
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
for key in ['GOOGLE_OAUTH2_KEY',
            'GOOGLE_OAUTH2_SECRET',
            'FACEBOOK_KEY',
            'FACEBOOK_SECRET']:
    # Use exec instead of eval here because we're not just trying 
    # to evaluate a dynamic value here
    # we're setting a module attribute whose name varies.
    exec("SOCIAL_AUTH_{key} = os.environ.get('{key}')".format(key=key))
```
The Social Auth Pipeline depends on which OAuth flow you use.
This example is from [Social Auth Docs][psadocs].  An example with optional parts enabed is in the Toptal article
```
SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. On some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social_core.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social_core.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    'social_core.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
    'social_core.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'social_core.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social_core.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    # 'social_core.pipeline.social_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
    'social_core.pipeline.user.create_user',

    # Create the record that associates the social account with the user.
    'social_core.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social_core.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social_core.pipeline.user.user_details',
)
```
The pipeline is explained in the [Social Auth Docs][psadocs],
in the section [/en/latest/pipeline.html](https://python-social-auth.readthedocs.io/en/latest/pipeline.html).

### How to Test?

The Toptal article suggests using the Django Responses library.  Article has a link to the author's test code.


## Registering Your App with OAuth Provider

During registration you must provide:
* callback URL

You will receive:
* client key
* client secret

## Resources

[How to Integrate OAuth 2 Into Your Django/DRF Back-end](https://www.toptal.com/django/integrate-oauth-2-into-django-drf-back-end) explains how to implement OAuth client that authenticates via Google or Facebook, uses SocialAuth. (toptal.com)

[Python Social Auth][psa] library on Github and [documentation][psadocs]. Library for auth via Social sites.o

[Simple Todo API with Django and OAuth2](https://www.madewithtea.com/simple-todo-api-with-django-and-oauth2.html) - looks a bit out-of-date, not much about OAuth.

[psa]: https://github.com/python-social-auth "Python Social Auth library on Github"

[psadocs]: http://python-social-auth.readthedocs.org/ "PSA Documentation"
