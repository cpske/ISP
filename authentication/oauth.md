---
title: OAuth
---

**OAuth** is a protocol to enable a user (resource owner) to grant access to some of his "resources" to a 3rd party application.  The purpose of OAuth is **authorization** not 3rd party **authentication**. But *authentication* is implicitly proved by granting access to some private resource.


These are good sites for learning OAuth:


- [Understanding OAuth2 and Building a Basic Authorization Server of Your Own: A Beginner’s Guide](https://medium.com/google-cloud/understanding-oauth2-and-building-a-basic-authorization-server-of-your-own-a-beginners-guide-cf7451a16f66) more detailed, and has links to other pages with Python code examples. 

- [OAuth 2.0 Simplified](https://oauth.com) at <http://oauth.com>. This site also has a hands-on [OAuth Playground](https://www.oauth.com/playground/).

- [Create an Application](https://www.oauth.com/oauth2-servers/accessing-data/create-an-application/) example on oauth.com; use OAuth to access info about your Github repositories.


## Introduction


There are 4 components involved

- **Resource Owner** Entity (typically a person) who owns the resource. For example, a person owns his photos on Google.
- **Resource Server** the host that provides access to the protected resources, e.g. photos.google.com.
- **Client** the application that wants access to the resources, e.g. a photo viewing application.
- **User Agent** is software that the user (resource owner) uses to interact with the Client.  This may be a web browser.  For mobile apps, the Client and User Agent may be the same.

and one more:

- **Authentication Server** the server that authenticates the resource owner for the Resource Server.  You may have one server that does both authentication (Authentication Server) and holds the resources (Resource Server).

### OAuth Playgrounds

Several companies have an "OAuth Playground" where you try their OAuth services using a dummy account.

- [OAuth Playground](https://www.oauth.com/playground/) on oauth.com. This is the best one for experiencing the OAuth Flows.

- [Google OAuth Playground](https://developers.google.com/oauthplayground/) for experimenting with different Google APIs

- [WSO Identity Server Playground](https://is.docs.wso2.com/en/latest/guides/access-delegation/auth-code-playground/) create apps in Java using WSO's identity server code.

## OAuth Flows and Grant Types

OAuth 2 has four different "flows" for different kinds of apps.
The main difference is how the application (clients) gets an access token
to access the user's resources.

| Flow           | Application Type                  |
|----------------|-----------------------------------|
| Authorization Code | Web apps where logic is on backend and private, so it can hold a secret key used to get an access token. |
| Implicit Grant | Single page web apps (logic runs in web browser) or native/mobile app. 
| Resource Owner Password Credential  | Application that cannot launch a web browser. The user gives his password to the app, which uses it to access user's Resources. Requires high trust between user and app. |
| PKCE           | Proof Key for Code Exchange is an extension to the Authorization Code Flow (and maybe for Implicit Flow) that adds a random secret to prevent CSRF and other attacks. |


## Who Can Access Your Data?

1. What Apps Use Google to Authenticate You?

   - Go to <https://accounts.google.com>
   - Choose "Security" (used to be under "Data & Privacy")
   - Choose "Signing in to other sites"
   - How many are there?

2. What Apps can access your Google data?
   - Go to your account ("Manage my account")
   - Choose "Data & Privacy"
   - Choose **Third Party Apps with Account Access**

3. Who has acess to your resources on Facebook?

   - Go to Facebook
   - Expand the "Account" icon (weird downward triangle in upper-right corner)
   - Choose "Settings & Privacy"
   - Choose "Settings" (*why is Facebook making this info so hard to access?*)
   - Select "Apps & Websites" (?) from left side 


## Using Google OAuth

- [OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/oauth2/web-server) for apps where authentication and logic runs on server side
- [Oauth 2.0 for Client-side Web Apps](https://developers.google.com/identity/protocols/oauth2/javascript-implicit-flow) for apps where logic and resource access are done in user's browser (using Javascript)

both pages have good explanation of the steps involved.

## Adding OAuth to Django Project

In 2022, [django-allauth][django-allauth] appears to be the best package
for using OAuth and OpenID in Django.  It also handles local accounts and
replaces the `django.contrib.auth` app for local accounts.

The [django-allauth][] docs are easy to read, but this tutorial may
also help:

- [How To Authenticate Django Apps using django-allauth][digitalocean-allauth] tutorial by DigitalOcean.

To understand what allauth can do, read the section [Supported Flows][supported-flows].

The Allauth login template is pretty ugly.
This tutorial shows how to write your own login template for django-allauth:
<https://codeburst.io/master-the-user-authentication-in-django-allauth-f1a4368bb460>

[django-allauth]: https://django-allauth.readthedocs.io/en/latest/
[supported-flows]: https://django-allauth.readthedocs.io/en/latest/overview.html#supported-flows
[digitalocean-allauth]: https://www.digitalocean.com/community/tutorials/how-to-authenticate-django-apps-using-django-allauth

Allauth constructs:
- `SocialApp` - a model that contains credentials for a single OAuth/OpenID provider.  It stores the "Client ID", "Client Secret", and (optional) Key used to access the provider.
  - You add `SocialApp` records using the Django admin interface.
  - The `name` field is the Client app name that you gave the OAuth provider when you registers for OAuth credentials. Be sure the name matches exactly.
  - `client_id`, `secret`, and `key` are credentials given by the OAuth provider
- `SocialAccount` - a model for a user's social account. When a user authenticates using OAuth, a SocialAccount object is created for him.  `SocialAccount` contains:
   - `user` - foreign key to a `User` for this account
   - `provider` - provider's name
   - `uid` - user id
   - `last_login`
   - `date_joined`
   - `extra_daa` a JSONField to store all data returned by the OAuth provider after authentication. The data returned depends on the "scope" you request from the OAuth provider.
- `SocialToken` - stores the OAuth *access token* and foriegn keys linking it to a *SocialAccount* (user) and *SocialApp* (provider)

### Reverse URLs

Instead of the django.contrib.auth url names `login`, `logout`, `password_change`, etc. you can use the Allauth url names:

- `allauth:account_login`
- `allauth:account_logout`
- `allauth:account_set_password`
- etc. (send an invalid GET request with DEBUG=True to see all)

### Specify the `LOGIN_URL`

The `@login_required` decorator will redirect users to `settings.LOGIN_URL`


### Update a User's profile after social login

When a user authenticates via a social auth provider, Django associates this
with a User instance and sets the `username` and `email` attributes, 
but not other attributes like `first_name` or `full_name`.
But you can add this to your application.

Django has "signals" that are triggered (fired) by specific events.

You can add a "post save" signal for `SocialAccount` objects:
```python
# Add to a models file
from django.db.models.signals import post_save

post_save.connect(update_profile, sender=SocialAccount)
```

and:

```python
def update_profile(sender, instance: SocialAccount, **kwargs):
    """Update User data. instance.user is a reference to the Django User."""
    user = instance.user
    user.full_name = instance.extra_data['name'] # depends on provider
    # get other attributes
    user.save()
```

[Example code by Rishabh Agrahari](https://github.com/pyaf/allauthproject) on Github.
