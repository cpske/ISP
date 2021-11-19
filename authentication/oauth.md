---
title: OAuth
---

**OAuth** is a protocol to enable a user (resource owner) to grant access to some of his "resources" to a 3rd party application.  The purpose of OAuth is **authorization** not 3rd party **authentication**. But *authentication* is implicitly proved by granting access to some private resource.


These two web pages are a good introduction to OAuth:

- [Understanding OAuth 2.0](https://medium.com/swlh/understanding-oauth-2-0-dc7ef422d915) on Medium.com. Has helpful diagrams of 2 most common use cases, called "flows".

- [Understanding OAuth2 and Building a Basic Authorization Server of Your Own: A Beginner’s Guide](https://medium.com/google-cloud/understanding-oauth2-and-building-a-basic-authorization-server-of-your-own-a-beginners-guide-cf7451a16f66) more detailed, and has links to other pages with Python code examples.  The examples uses Flask.

Detailed explanation with examples of each flow: 

- "OAuth 2.0 Simplified" at <https://www.oauth.com>. Probably the best place to learn how OAuth works.
  - [Create an Application](https://www.oauth.com/oauth2-servers/accessing-data/create-an-application/) example of using OAuth to access info about your Github repositories.


## Introduction


There are 4 components involved

- **Resource Owner** Entity (typically a person) who owns the resource. For example, a person owns his photos on Google.
- **Resource Server** the host that provides access to the protected resources, e.g. photos.google.com.
- **Client** the application that wants access to the resources, e.g. a photo viewing application.
- **User Agent** is software that the user (resource owner) uses to interact with the Client.  This may be a web browser.  For mobile apps, the Client and User Agent may be the same.

and one more:

- **Authentication Server** the server that authenticates the resource owner for the Resource Server.  You may have one server that does both authentication (Authentication Server) and holds the resources (Resource Server).

### OAuth Playgrounds

Many companies have an "OAuth Playground" where you try their OAuth services using a dummy account.

- [OAuth Playground](https://www.oauth.com/playground/) on oauth.com
- [Google OAuth Playground](https://developers.google.com/oauthplayground/) for experimenting with different Google APIs

## OAuth Flows and Grant Types

OAuth 2 has four different "flows" for different kinds of apps.
The main difference is how the application (clients) gets an access token
to access the user's resources.

| Flow           | Application Type                  |
|----------------|-----------------------------------|
| Authorization Code | Web apps where logic is on backend and private, so it can hold a secret key used to get an access token. |
| Implicit Grant | Single page web apps (logic runs in web browser) or native/mobile app. 
| Resource Owner Password Credential  | Application that cannot launch a web browser. The user gives his password to the app, which uses it to access user's Resources. Requires high trust between user and app. |
| PKCE           | Extension to implicit flow that adds a random secret to prevent CSRF and other attacks. |

## Who Can Access Your Data?

1. Who has access to your resources on Google?

   - Go to <https://accounts.google.com>
   - Choose "Data & privacy"
   - Under "Data from Apps and services you use", choose "**Third-party apps with account access**"
   - How many are there?

2. Who has acess to your resources on Facebook?

   - Go to Facebook
   - Expand the "Account" icon (weird downward triangle in upper-right corner)
   - Choose "Settings & Privacy"
   - Choose "Settings" (*why is Facebook making this info so hard to access?*)
   - Select "Apps & Websites" (?) from left side 

## Using Google OAuth

- [OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/oauth2/web-server) for apps where authentication and logic runs on server side
- [Oauth 2.0 for Client-side Web Apps](https://developers.google.com/identity/protocols/oauth2/javascript-implicit-flow) for apps where logic and resource access are done in user's browser (using Javascript)

both pages have good explanation of the steps involved.
