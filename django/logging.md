
## How to Create a Log Message

In your Python code, use:

```python
import logging

# in this case we use module name as logger name.
# You can use whatever makes sense.
logger = logging.getLogger(__name__)
logger.critical("A critical problem, such as database error.")
logger.error("Log when an error")
logger.warning("Log a warning about something unusual")
logger.info("Information about some interesting event, e.g. user login")
logger.debug("Something useful for developers")
```

For logging exceptions with a stack trace, Logger also has:
```
logger.excpetion(e)
```
which emits an ERROR level log message.

An example from the polls tutorial application.
```python
def vote(request, question_id):
    """Vote for one of the polls identified by question_id."""
    ### informational (a usual event)
    logger.info("Vote submitted for poll #{0}".format(question_id))
    try:
        q = Question.objects.get(id=question_id)
        choice_id = request.POST['choice_id']
        logger.info("Question {0} vote for choice {1}".format(q, choice_id))
        choice = q.choice_set.get(pk=choice_id)
    except:
        logger.warning("Invalid question id {0} or choice id {1}"
                       .format(question_id,choice_id))
        context = {'question':q, 'error_message':"Missing or invalid answer choice"}
        return render(request, 'polls/detail.html', context)
```


## Django Standard Logging Names

Django uses some predefined loggers.  You can configure loggers for these names to 
control how much logging is done and where the log messages go.

| Logger     |  Description |
|:-----------|:-------------|
| django     | Catch-all logger for django log messages. |
| django.request | Log HTTP requests. HTTP 4xx responses create `warning` log message, 5xx responses create `error` log messages. |
| django.server | When using "runserver" will log all requests with `info` log messages |
| django.template | Log errors in templates. Missing context variables logged at `debug` level. |
| django.db.backends | Log interactions with database. All SQL statements are logged at the `debug` level, which can be quite verbose. |
| django.security.xxx  | Log security-related problems, including messages from a *SuspiciousOperation* error. These messages are **not** sent to the django.request logger. |
| django.security.csrf | Log cross-site request forgery attacks. |


## How to Configure Logging

Configure logging in your project's `settings.py`. You can specify:

- define one or more "loggers". For example a "console logger", a "file logger", or a network logger.
- which log messages (debug, info, etc.) to log to each output stream
- the format of log messages

See [Django Logging Howto][django-logging-howto] for details.

## Example Logging Configuration

This is not guaranteed to work.

```python
# settings.py

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'details': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'polls.log',
            'formatter': 'details',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'polls': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

## Reference

[Django Logging Howto][django-logging-howto]

[Django Logging](https://docs.djangoproject.com/en/stable/topics/logging/) full documentation

[Django Logging Extensions](https://docs.djangoproject.com/en/stable/topics/logging/#django-s-logging-extensions) describes the various loggers that Django uses for its own messages, such as `django.request` and `django.security`.

[django-logging-howto]: https://docs.djangoproject.com/en/stable/howto/logging/ 
