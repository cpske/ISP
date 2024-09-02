---
title: KU Polls Iteration 3
---

## New Features to Add in Iteration 3

- A visitor must authenticate (login) in order to submit a vote or change his vote(s).
- An authenticated user gets only 1 vote per poll.
- A user can change his vote on a poll during the voting period and his new vote replaces his old vote. 
- If a user selects a poll he already voted on, the list of choices shows which choice he/she previously selected. For example, a radio button is selected for his previous choice.
- When a user submits a vote there is visual confirmation of his vote, such as a message on the results page "*Your vote for xxxx has been saved*".
- A visitor can login and logout.
- A link for "Login" or "Logout" is shown on most or all web pages.  In good UI design these links appear in the *same place* on every page (e.g. a common header or sidebar).

Other Behavior:

- Anyone can view the list of polls and poll results (same as before)
- Logging of important events: login, logout, failed login, and submitting a vote.

## Requirements

### New and Updated Project Artifacts

- An Iteration 3 Plan in your wiki with goal, milestone(s), and list of major work.
- Reviewed and updated Requirements document. 
- Updated the Development Plan for iteration 3.
- Updated **Domain Model** page in your Wiki. Add a new UML class diagram and some text to explain the reasoning for your domain model.
- Iteration 3 Task Board with complete tasks for work to do.
  - Convert task to "Issues" when it makes sense so they appear in your repo on Github.
- `iteration3` branch containing your work, merged into master.

### Process Requirement

- Use Github Flow. Work on `iteration3` branch.
- Commit and push work **regularly**.
- **No credit** (zero) for one big commit & push of work at end of the iteration.

### Features

1. Add new model classes to implement the new Domain Model.

2. Use Django's built-in authentication "app" for user management (username and password).

3. Use the Django [Messages Middleware](../../django/messages-framework) to display messages on pages.
   - This will make your code and templates *much* cleaner and simpler.

4. In the Django tutorial they use an `error_message` field in the poll detail template (`detail.html`).  Replace this cludgy code with the messages middleware.

5. Add at least 3 demo users to your database.  To make it easier for TAs to evaluate your code, please use these names:
   | username   | password   |
   |------------|------------|
   | demo1      | hackme11   |
   | demo2      | hackme22   |
   | demo3      | hackme33   |
   - You can add more users if you want.

6. **Data Fixtures** Create 2 data files. One file for polls questions, one file for user data. 
   ```
   cmd> python manage.py dumpdata --indent=2 -o data/polls-v3.json polls 
   cmd> python manage.py dumpdata --indent=2 -o data/users.json auth.user
   ```

### Coding Suggestion

1. *Make small changes* to code and test each change so you can easily fix problems.  **Commit code** after each successful change.

2. Write unit tests to verify the new work is correct and satisfies requirements. A few "auth" tests are provided as starting point -- please expand on them.

### (Optional) Divide Tests into Separate Files

Your code now has many unit tests. Consider separating tests
into separate files, as recommended in the MDN Django Tutorial.

- Create a `polls/tests` directory containing an `__init__.py` file.
- Divide your tests into separate files, with related tests in one file, such as:
  ```
  polls/tests/
             __init__.py
             test_index.py
             test_poll_dates.py
             test_auth.py
             test_voting.py
   ```
- Delete the original `tests.py` file
- Fix the imports in test files. Change `import .models` to `import polls.models`.
- Similarly, change `import .views` to `import polls.views`.

### Logging

Add logging of important events:

| Event                      | Log Level |
|----------------------------|-----------|
| user login or logout       | info      |
| unsuccessful login attempt | warning   |
| user submits a vote        | info      |
| exception caught in code   | error     |

- use [Django Logging][django-logging] which is Python's `logging` module.
- logging methods automatically include (a) date and time, (b) location in code. This is done by the Formatter, so don't add it in the log message you write.
- login/logout messages should include the user's IP address 

You can configure the logger behavior, including message format, in `settings.py`.

An example of using logging is:

```python
import logging

logger = logging.getLogger("polls")
# log an information message
logger.info(f"{user.username} logged in from {ip_addr}")
# log a warning message
logger.warn(f"Failed login for {username} from {ip_addr}")

# Logging an exception.
# log.exception will include a stack trace
# log.error can be used instead if you don't want the stack trace
try:
    question = Question.objects.get(id=question_id)
except Question.DoesNotExist as ex:
    logger.exception(f"Non-existent question {question_id} %s", ex)
```

### Getting a Visitor's IP Address for Logging

When someone logs in you should include their IP address in the log message.

There are many posts showing how to write a `get_client_ip` 
function using the Django `request` object.
Getting the visitor's **actual** IP address is harder than it looks,
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

## Resources that may help

- MDN page on Django Authentication: <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication>
- My tutorial on Django Authentication: <https://cpske.github.io/ISP/django/authentication>
- My page on Django Authorization: <https://cpske.github.io/ISP/django/authorization>
- Logging in Django: <https://docs.djangoproject.com/en/dev/howto/logging/>

[django-logging]: https://docs.djangoproject.com/en/dev/howto/logging/
