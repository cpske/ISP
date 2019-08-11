## OAuth Exercise

1. Go to the [Google OAuth Playground][oauth-playground].
2. Choose an API you want to authorize to access your data.
   * I chose Google Calendar Events scope (url is shown in playground)
3. Click "Authorize API".  Playground directs you to the provider's OAuth authorization page.  Here's the URL it uses:
```
https://accounts.google.com/o/oauth2/v2/auth?
   redirect_uri=https://developers.google.com/oauthplayground&
   prompt=consent&
   response_type=code&
   client_id=407408718192.apps.googleusercontent.com&
   scope=https://www.googleapis.com/auth/calendar.events
   &access_type=offline
```
4. Grant access to "Google OAuth 2.0 Playground" to access your data.
5. You should be redirected back to OAuth Playground, with an **authorization code**.
6. Exchange the authorization code for **access token**.
7. Make a request to the provider.
   * For Google Calendar events scope, I chose "list events".
   * The `calendarid` is "primary" for your default calendar. 
   * The request is:
```
GET /calendar/v3/calendars/primary/events/ HTTP/1.1
Host: www.googleapis.com
Content-length: 0
Authorization: Bearer 
ya29.GltHBtwX42km37qAGnxkNeWMU2qw2pBPJnifdgDmSpNGWG9ZuomjwDwkwJ-J7qgC6SqmwNcLPmU2MT28FJELhdUAFlkkoVcGFZKKH6mFYy34scQdszn53dbDDqWD
```



[oauth-playground]: https://developers.google.com/oauthplayground/
