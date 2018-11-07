## OAuth 2 Authorization Flows and Grant Types

**Authorization Code** is a 3-party flow used by web applications.
This is also the flow in the original OAuth 1.0 (but details differ in OAuth 2).

Authorization Code flow is used in web apps.  It can also be used in mobile
apps using the *Proof Key for Code Exchange" (PKCE) technique.

**Implicit** a 2-party flow, used in Javascript apps, e.g. single-page web apps.

**Resource Owner Password Credentials** is a flow where the user (resource owner)
gives the application his userid/password for relay to the auth server.
Obviously this is reasonable only for trusted apps.
It is used in mobile apps, even though "trusted" is maybe a bad idea.

**Client Credentials** for machine-to-machine (or app-to-app) communication,
such as an application accessing a protected API.



## OAuth Roles

**Client** - an applicatoin that wants to access some data or "resrource" owned by someone on another site/application (the resource server).  Or, the client application may merely want to identify a person via another site/application.

**Resource Owner** - person or principal that "owns" the resource that the client wants to access.

**Resource Server** the application/site that stores (provides access to) the user's(Resource Owner) information.

**Authorization Server** the server that grants access to a user's information.  This is often the same as the Resource Server.

| Role                 | Google           | Twitter               |
|----------------------|------------------|-----------------------|
| client               |

## OAuth Tokens

* Grant Token
* Bearer Token

A token is an opaque string or object used to identify or authorize a request.
In OAuth a token can either be a String or JSON Web Token (JWT).
As a String, it would look like:


### Managing Tokens in an App

Tokens need to be used multiple times, so they need to be stored
while the app is running.  They *might* need to be stored between
user sessions.  How to store them?

Client-side such as single-page apps.
Tokens are stored either in session storage, local storage, or cookies.
Delete them when no longer needed (even though they are opaque strings
that expire anyway).

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


## References


* [OAuth 2.0: The Complete Guide](https://auth0.com/blog/oauth2-the-complete-guide/) basic explanation of OAuth concepts and operation.  Not a "complete guide" but worth reading.

* [OAuth 2 Overview](https://auth0.com/docs/protocols/oauth2) on [oauth0.com](https://ouath0.com). oauth0 is a commercial provider of OAuth products (not the OAuth official site oauth.com). Their articles on OAuth and OpenID Connect are well-written.

* [10 Things You Should Know About Tokens](https://auth0.com/blog/ten-things-you-should-know-about-tokens-and-cookies/) explains how to use and store tokens in client-side apps, i.e. Javascript. Useful general information.

* [JWT for OAuth Client Authhorization Grants](https://www.ibm.com/support/knowledgecenter/en/SSEQTP_liberty/com.ibm.websphere.wlp.doc/ae/cwlp_jwttoken.html) by IBM, describes JWT tokens and gives example how to create one in Java (requires several libaries to compile Java code).