## OAuth and OpenID

OAuth is a standard for 3rd party-based authentication and access control.
This is the protocol used by the many "Login with Google" or "Login with Facebook" links on sites all over the Internet.

The original use of OAuth was to enable a 3rd party app to access a protected resource (e.g. some of your data) on a server. 
You would use OAuth to grant authorization to the 3rd party app.

A natural application of this is simple to assert your identity.  By granting the 3rd party app access to anything, you are proving your identity on the OAuth server (e.g. Google).  Often, the 3rd party app requests access to your real name and login on the OAuth server.

[OpenID](https://openid.net/) and OpenID Connect provide assertion of identity. After authenticating to an OpenID service, you can use your identity to connect to other services or sites that are allowed to use that OpenID service.  A form of "single sign-on".


## WSO2 Identity Server

Server side for providing OAuth, SAML, and single sign-on services.

https://is.docs.wso2.com/en/5.9.0/

## Secure QR Login (SQRL)

A new authentication protocol and software that eliminates need for any secret data on the server side.

It uses Elliptic Curve public-private keys that are dynamically generated from a single "master key" and a site's identity based on the site's URL.  The result is that the client does not need to remember private keys for each site, making it easy to store your "identity" on multiple devices.
