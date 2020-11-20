# Settings from
# https://python-social-auth.readthedocs.io/en/latest/configuration/settings.html

INSTALLED_APPS = [
    ...
    'social_django',
    ...
]

AUTHENTICATION_BACKENDS = [
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.yahoo.YahooOpenId',
    ...
    'django.contrib.auth.backends.ModelBackend',
]

# Require HTTPS in redirect after authentication by 3rd party
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False

# where to redirect to in case of error
SOCIAL_AUTH_LOGIN_URL = '/login/'

# redirect after successful login
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/logged-in/'

# User model must have username and email fields
SOCIAL_AUTH_USER_MODEL = 'django.contrib.auth.models.User'


