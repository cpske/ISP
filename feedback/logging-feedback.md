---
title: Feedback on Logging Practice
---

## "DEBUG" Message != "Found a bug"

Many people wrote examples like this:
```
   logger.debug(f"Bug found")
```
2 problems with this.

First Problem (most important):

* DEBUG level is the *least* severe logging level -- it is less important than INFO level.  So "DEBUG" messages are often not output at all.
* Use DEBUG to help debug an application or trace the flow of control.
* If detect a "bug", you should log it at *at least* the WARNING level.
* If you use DEBUG level to "log" bug, the message might not be output!

Second Problem: 
* "Found a bug" or "Bug found" is a uselessly **vague** message.
* Log messages should help you locate a problem. They should be specific and contain relevant information, such as exactly what was detected.

## Examples of Poor Log Message Examples

Deducted 1 point for multiple poor example messages.

Here are some poor ones:
```
logger.debug("BUG FOUND!")
logger.info("Some info show up!")
logger.warning("UNEXPECTED Watch out!")
logger.error("ERROR!")
logger.critical("CRITICAL ERROR!")

logger.debug("Found DEBUG")
logger.info("Connecting")
logger.warning("Your computer is infected")
logger.error("An error occurred while displaying")
logger.critical("Your start menu isn't working")

logger.debug("A bug has been detected")
logger.info("information has been found")
logger.warning("Some defect has been found")
logger.error("Some error has been occur")
logger.critical("Some risky critical error has been occur")
```

## Log Messages Are For Developers & Product Support, Not End Users 

**End users** do not read log files.

So these are not appropriate log messages:

```
logger.info("You have 7 new notifications.")
logger.warning("You have 10 minutes left to use demo.")
logger.error("This product is out of stock.")

logger.warning("This is the warning. Please check and fix the code.")
logger.error("There is an error in your code, please fix it.")
logger.critical("You should fix your code immediately!")

logger.warning("Your computer is infected")
logger.critical("Your start menu isn't working")
```

### Guidance

* Log messages are for developers, admins, and (for a commercial product) customer support. Log messages are  **not for end users**.
* Log messages should be **specific** and include detail to help a developer/admin locate the problem.
  - "An error occurred" is uselessly vague.


## Good Examples

```
logger.debug("loaded configuration from config.ini")
logger.info("Application started")
logger.warning("DEBUG=True but settings.ALLOWED_HOSTS includes 0.0.0.0")
logger.error("Unsupported database provider, defaulting to SQLite")
logger.critical("Error parsing config.ini, line 21: 'DEBUG==True'")

logger.info("Request from 128.4.2.8: GET /polls/3/")
logger.warning("Invalid email *@yahoo.com. Ignored.")
logger.error("Can't divide by 0")  # also specify where it occurred
# This might occur in a low-level network driver or instrument controller.
logger.critical("Low signal")  # should be more specific
```
