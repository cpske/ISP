---
title: KU Polls Iteration 3
---

## New Features to Add in Iteration 3

1. A visitor must authenticate (login) in order to submit a vote or change his vote(s).
2. An authenticated user gets only 1 vote per poll.
3. A user can change his vote on a poll during the voting period and his new vote replaces his old vote. 
4. If a user selects a poll he already voted on, the list of choices shows which choice he/she previously selected. For example, a radio button is selected for his previous choice.
5. When a user submits a vote there is visual confirmation of his vote, such as a message on the results page "*Your vote for xxxx has been recorded*".
6. A visitor can login and logout.
7. A link for "Login" or "Logout" is shown on all web pages.  
   > It is good UI design these links appear in the ***same place*** on every page.
   > Suggest you create a common "base" template for your polls pages. Put common header, footer, and CSS in the base template instead of duplicating it on every page!

Other Behavior:

8. Anyone can view the list of polls and poll results (same as before)
9. [Log](#logging) important events: login, logout, failed login, and submitting a vote.

## Requirements

### 1. Project Artifacts

- **Iteration 3 Plan** in your wiki with goal, milestone(s), and list of major work.
- Reviewed and updated **Requirements**. 
- In **Development Plan**, updated major work and goal for iteration 3.
- Revised **Domain Model** in your Wiki has a new domain class diagram for Iteration 3, along with some text to explain the reason for the new model and sample Python code of how the model is used.
- **Task Board** for Iteration 3 with tasks for the work to do (now done).
  - Convert task to "Issues" (when it makes sense) so they appear in your Issue Tracker on Github.
- `iteration3` branch containing your work, merged into master.

### 2. Process Requirement

- Use Github Flow. Work on `iteration3` branch.
- Commit and push to Github **regularly**.
- **No credit** (zero) for one big commit & push of work at end of the iteration.

### 3. Features

1. New model classes to implement the new Domain Model.

2. Use Django's built-in authentication "app" for user management and authentication.

3. Use the Django [Messages Middleware](../../django/messages-framework) to display messages on pages.
   - This will make your code and templates *much simpler* and cleaner.
   - Use messages for Feature #5 above (confirmation message after vote submitted).

4. In the Django tutorial they use an `error_message` field in the poll detail template (`detail.html`).  Replace this cludgy code with Messages.

5. [Log](#logging) these events using Python logging: 
   - login, logout, failed login, submit a vote
   - for login, failed login, and logout, include the user's IP address in the log message.
   - for submit a vote, include the username, question id, and choice id in the message.

6. Add these 3 demo users to your database.  To help the TAs run your code, please use these names:
   ```
   username   password
   --------   --------
   demo1      hackme11
   demo2      hackme22
   demo3      hackme33
   ```
   - You can add other users if you want.

7. **Data Fixtures** Create 2 data files. One file for polls questions, one file for user data. 
   ```
   cmd> python manage.py dumpdata --indent=2 -o data/polls-v3.json polls 
   cmd> python manage.py dumpdata --indent=2 -o data/users.json auth.user
   ```

---

### Coding Suggestion

1. **Make small changes** to code and test each change so you can easily fix problems.  *Commit code* after each successful change.

2. Write unit tests to verify your new work is correct and satisfies requirements (like 1 user 1 vote). 
   - Some [sample auth tests](./test_auth_user.py) to get started. Please expand on these.


### Logging

Log important events such as login, logout, and voting.  Your code should record a log message when these events occur:

| Event                      | Log Level |
|----------------------------|-----------|
| user login or logout       | info      |
| unsuccessful login attempt | warning   |
| user submits a vote        | info      |
| exception caught in code   | error     |

- use [Django Logging][django-logging] which uses Python's `logging` module.
- logging methods use a Formatter to include (a) date and time, (b) name of module that emitted the message, (c) severity. The Formatter adds these, so don't include this info in your log message.
- see my logging notes for now specify a format, but the Django default is probably OK.
- login/logout messages should include the user's IP address 

You configure the logger behavior, including message format, in `settings.py`.

An example of using logging:

```python
import logging

# Get a logger for this module.
logger = logging.getLogger("polls")
# log an information message
logger.info(f"{user.username} logged in from {ip_addr}")
# a warning message
logger.warning(f"Failed login for {username} from {ip_addr}")

# Logging an exception.
# log.exception will include a stack trace
# log.error can be used instead if you don't want the stack trace
try:
    question = Question.objects.get(id=question_id)
except Question.DoesNotExist as ex:
    logger.exception(f"Non-existent question {question_id} %s", ex)
```

By default, Django prints log messages of severity `warning`, `error`, and `fatal` on console,
but does not print messages of lower severity, like `info`.  
To print `info` messages, add a setting to your `settings.py` file as described in the [Logging Howto Page][django-logging].


### Get a Visitor's IP Address for Logging

When someone logs in you should include their IP address in the log message.

There are many posts showing how to write a `get_client_ip` 
function using the Django `request` object.
Finding the visitor's **actual** IP address is harder than it looks,
as commenters mention here:
<https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django>

One implementation uses HttpRequest headers sent by the client, 
`HTTP_X_FORWARDED_FOR` and `REMOTE_ADDR`

```python
def get_client_ip(request):
    """Get the visitor’s IP address using request headers."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
```
This is OK, but request headers can be manipulated by the sender.

### (Optional) Divide Tests into Separate Files

Your code now has many unit tests. Consider separating tests
into separate files, as recommended in the MDN Django Tutorial.

1. Create a `polls/tests` directory containing an `__init__.py` file.
2. Divide your tests into separate files, with related tests in one file, such as:
   ```
   polls/tests/
             __init__.py
             test_index.py
             test_poll_dates.py
             test_auth.py
             test_voting.py
    ```
3. Delete the original `tests.py` file
4. Fix the imports in test files.    
   - Change `import .models` to `import polls.models`.
   - Change `import .views` to `import polls.views`.

---

## Useful Resources

- MDN page on Django Authentication: <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication>
- My tutorial on Django Authentication: <https://cpske.github.io/ISP/django/authentication>
- My notes on Django Authorization: <https://cpske.github.io/ISP/django/authorization>
- Logging in Django: <https://docs.djangoproject.com/en/stable/howto/logging/>
- My notes on Django logging: <https://cpske.github.io/ISP/django/logging>

[django-logging]: https://docs.djangoproject.com/en/stable/howto/logging/
