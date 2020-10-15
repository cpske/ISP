---
title: Authentication
---

Presentation Slides: 
[Intro to Authentication & Authorization](Authentication-and-Authorization.pdf)

[Authentication in Django](/ISP/django/authentication)    
[Authorization in Django](/ISP/django/authorization)

## Authorization Methods

1. Username and password 
   - passwords must be remembered and kept secret
   - servers should *never* store password as plain text or encrypted w/o salt
   - **weak** since passwords can be stolen or guessed

2. Biometrics
   - authenticate using a fingerprint, facial recognition, or iris scan
   - device stores "metrics" based on your fingerprint, face, or iris and then matches them to later requests to authenticate
   - only iris scan is reasonably secure. Fingerprint and face scans are hackable.  
   - Researchers have used 3D printing to copy a fingerprint from a photograph and used it to unlock phones.

3. TLS-based authentication (public-private keys)
   - you create a public-private key pair and give the public key to the server.
   - private key is kept encrypted and confidential on your device.
   - each time you "login", the server sends a challenge that you respond to using your private key.

4. Third-party Authentication - authenticate yourself using a trusted third party
   - OAuth
   - OpenId
   - Many implementations to "Covert Redirect" bug (2014) using XSS attack. Mostly fixed since then. 

5. Single Sign-on - used on comporate networks (like KU) so a user authenticates once (to auth server) and can access many servers.  Uses time-based token stored on user's device.
   - Kerberos
   - Microsoft Active Directory


### Has Your Password Been Stolen?

* [Have I Been Pwned?](https://haveibeenpwned.com/) - check email address
* [Stolen (pwned) Passwords](https://haveibeenpwned.com/Passwords) - check a password.  This page does **not** send your password over the Internet. Only a *partial hash* is sent; everything else is done in the browser.
* [Firefox Monitor](https://monitor.firefox.com/) similar to "Have I Been Pwned?".
* [Firefox Breach Monitoring](https://monitor.firefox.com/breaches) when you visit a site using Firefox, it warns you if this site has been compromised in the last 3 years -- so you can protect yourself.
  - Available in Firefox: Menu -> "Protections Dashboard"

Example of a Firefox breach alert when user visits a compromised site:    
![firefox breach alert](firefox-breach-alert.png)


## OAuth

OAuth is a standard for 3rd party-based authentication and access control.
This is the protocol used by the "Login with Google" or "Login with Facebook" links on sites all over the Internet.

The original use of OAuth was to enable a 3rd party app to access a protected resource (e.g. some of your data) on a server. 
You would use OAuth to grant authorization to a 3rd party app.

A natural application of this is to assert your identity.  By granting the 3rd party app access to *anything*, you are proving your identity on the OAuth server (e.g. Google).  
Often, the 3rd party app requests access to your real name and login or e-mail on the OAuth server.

OAuth2 (the current version) has different **flows** based 
on use cases, also called **grant types**.
As a programmer, when you apply for access to
an OAuth server (like Google) it's important that you choose 
the correct flow.

1. Server-Side Web Applications (like Django): 
   - type: Web Server Flow or "Authorization Code" grant
   - when you register your web app with the OAuth service, the OAuth service gives you a "client id" and "client secret"
   - your web app uses the "client id" and "client secret" whenever it requests access to a user's data
   - your web app must protect the "client secret"!
   - good sequence diagram: [Auth Code Grant](https://op-developer.fi/p/authcodegrant)

2. OAuth for Mobile Apps:
   - since a mobile app cannot keep secret information, there is not "client secret" and some restrictions on use
   - description and diagram: [Mobile App Dev with OAuth 2](https://www.ateam-oracle.com/oauth-2-0-authorization-code-flow-for-mobile-apps) some parts are specific to Oracle

3. Browser-based Apps - Javascript or Web Assembly apps running in the browser
   - browser-based apps cannot keep secrets, so there is not "client secret". Instead, a dynamically generated secret is sent with each request to prevent replay attacks.
   - 


### OAuth Resources

* [เรียนรู้เทคโนโลยี OAuth2](https://sysadmin.psu.ac.th/2019/03/03/what-is-oauth2/) from Songkhla University.


Not Recommended:

* [OAuth 2.0](https://oauth.net/2/) from oauth.net. An obfuscated, overly complex description of OAuth by people working on the RFC. This is why people think OAuth is hard (it isn't).

* [OAuth 2 Simplified](https://aaronparecki.com/oauth-2-simplified/#web-server-apps) good one page description but deceptively trying to collect e-mail addresses. His e-book is *not* free.

Details of how to use OAuth on Google. 

A downside of Google's OAuth is that they require you to install Google-specific packages.  (Since OAuth is a standard, this should *not* be necessary.)

* [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/oauth2/web-server) for web apps where the OAuth request is made from the server-side (back-end). 
* [Using OAuth 2.0 to Access Google APIs](https://developers.google.com/identity/protocols/oauth2)


## OpenID

[OpenID](https://openid.net/) and OpenID Connect provide assertion of identity. After authenticating to an OpenID service, you can use your identity to connect to other services or sites that are allowed to use that OpenID service.  A form of "single sign-on".



## Secure Quick Reliable Login (SQRL)

A new authentication protocol and software that eliminates need for any secret data on the server side.

SQRL generates all public-private keys from the user's single "master key" plus the site's URL, using Elliptic Curve public-private keys.

The result is that 
* the client does not need to save the private keys for each site; it only needs to save the master key (in encrypted form)
* as a result, it is easy to store your master key on multiple devices -- no need to sync saved credentials across devices
* the web sites you visit only store your public key, so there are no "secrets" to be leaked by a data breach. As Gibson writes: "*SQRL gives the server no secrets to keep*".

When a user visits a site, the site displays a QR code containing the site URL and a challenge (a nonce). The SQRL client captures the QR code, regenerates the private key for that site, and uses it to send an encrypted response to the challenge.  The response can be sent via the web page (same channel) or from a mobile phone using a separate channel (out of band).

* [SQRL on grc.com](https://www.grc.com/sqrl/sqrl.htm) Gibson's description of SQRL, details of the protocol, and links to both client and server-side implementations.
* SQRL mobile clients for Android and iOS are available.


## WSO2 Identity Server

This authentication server looks interesting,
so I note it here.
It provides server-side for OAuth, SAML, and single sign-on services.

https://is.docs.wso2.com/en/5.9.0/
