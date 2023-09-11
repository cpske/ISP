---
title: KU Polls Iteration 3
---

## New Features to Add in Iteration 3

- A visitor must authenticate (login) in order to submit a vote or change his vote(s).
- An authenticated user gets only 1 vote per poll.
- A user can change his vote on a poll during the voting period and his new vote replaces his old vote. 
- If a user selects a poll he already voted on, the list of choices shows which choice he/she previously selected. For example, a radio button is selected for his previous choice.
- When a user submits a vote there is visual confirmation of his vote, such as a message on the next page he is shown.
- A visitor can login and logout.
- A link for "Login" or "Logout" is shown on most or all web pages.  In good UI design these links appear in the *same place* on every page (e.g. a common header or sidebar).

Other Behavior:

- Anyone can view the list of polls and poll results (same as before)
- (Optional) Add logging of important events, such as login, logout, failed login, and submitting a vote.

## Requirements

Project Artifacts:

- An Iteration 3 Plan in your wiki with goal, milestone(s), major work.
- Reviewed and updated Requirements document. 
- Updated the Development Plan for iteration 3.
- A **Domain Model** to your Wiki. Include a UML class diagram and some text to explain the reasoning for your domain model.
- Iteration 3 Task Board with complete tasks for work to do.
  - Convert task to "Issues" when it makes sense so they appear in your repo on Github.
- `iteration3` branch containing your work, merged into master.

Process Requirement:

- Use Github Flow.
- Commit and push work regularly.
- **No credit** (zero) for one big commit at end of work or pushing all work to Github on last day of assignment.

Software Development:

1. Do work on an `iteration3` branch and push it to Github regularly.
2. *Make small changes* to code and test each one so you can easily fix problems.  **Commit code** after each successful change.
3. Write unit tests to verify the new work is correct and satisfies requirements. A few "auth" tests are provided as starting point -- please expand on them.
4. Add at least 2 demo users to your database.  In `README.md` add the username and password for these users.  This is so we can use your application.  For **example**
   ```
   | Username  | Password        |
   |-----------|-----------------|
   |   demo1   | stupidpassword1 |
   |   demo2   | stupidpassword2 |
   ```
5. **Data Fixtures** Create new data files for questions, votes, and users.
   ```
   cmd> python manage.py dumpdata --indent=2 -o data/polls.json polls 
   cmd> python manage.py dumpdata --indent=2 -o data/users.json auth.user
   ```
   **Note the file name** is `polls.json` for polls data since the format will be different than old data.



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
- Fix the imports in test files. Instead of `import .models` use `import polls.models`. Similarly for `views`.


### (Optional) Logging

Add logging of important events:

| Event                      | Log Level |
|----------------------------|-----------|
| user login or logout       | info      |
| unsuccessful login attempt | warning   |
| user submits a vote        | info      |
| exception caught in code   | error     |

- use [Django Logging][django-logging] which uses Python's `logging` module.
- log messages automatically include (a) date and time, (b) location in code. This is done by the Formatter, so don't put it in the log message you write.
- login/logout messages should include the user's IP address 

You can configure the logger behavior, including message format, in `settings.py`.

An example of using logging is:

```python
import logging

logger = logging.getLogger("polls")
logger.info(f"{user.username} logged in from {ip_addr}")
logger.warn(f"Failed login attempt for {username} from {ip_addr}")
try:
    question = Question.objects.get(id=question_id)
except Question.DOES_NOT_EXIST as ex:
    logger.exception(f"Non-existent question {question_id} %s", ex)
```

### Getting a Visitor's IP Address - for Logging

When someone logs in you should include their IP address in the log message.

There are many posts showing how to write a `get_client_ip` 
function using the Django `request` object.
Getting the visitor's **actual** IP address is harder than it looks,
as commenters mention here:
<https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django>

One implementation (copied from the Internet)
uses HttpRequest headers sent by the client, 
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
this is OK, but request headers can be manipulated by the sender.

## Documents that may help

- MDN page on Django Authentication: <https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication>
- My tutorial on Django Authentication: <https://cpske.github.io/ISP/django/authentication>
- My page on Django Authorization: <https://cpske.github.io/ISP/django/authorization>
- Logging in Django: <https://docs.djangoproject.com/en/dev/howto/logging/>

[django-logging]: https://docs.djangoproject.com/en/dev/howto/logging/