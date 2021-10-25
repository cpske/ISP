---
title: KU Polls Iteration 3
---

Add user authentication and allow each user only 1 vote per poll.

User authentication will be done using boring old username-password 
authorization, which Django calls "ModelBackend".

Behavior to add or modify is:

* Only an authenticated user can submit a vote
* Anyone can view the list of polls or poll results (same as before)
* A user can change his vote on a poll, and his new vote replaces his old vote. He can only change his vote during a poll's voting period.
* If a user selects a poll he already voted for, the of choices shows his previous vote 
* Add logging of the following events:
  - user login or logout. An "info" level log message, including username and IP address.
  - unsuccessful login attempt (username or password incorrect). a "warning" log message, including username entered and IP address.
  - user submits a vote for a poll. "info" log message including username and poll id voted on (but not choice id).
  - all log messages should include the date and time (that's done by the formatter, don't put it in your log message).
  - log to the console, like Django does.
  - use `loggers`, not print statements!

## Requirements

Write your own Iteration Plan without copying text from this assignment.
Create an "Iteration 3" task board with your tasks.

Implement the features and write unit tests for them.

Your project now has many unit tests, so consider refactoring the 
tests as recommended in the MDN Django Tutorial.
- Create a `polls/tests` directory with an `__init__.py` file.
- Divide your tests into separate files, grouped however makes sense, such as:
  ```
  polls/tests/
             __init__.py
             test_index.py
             test_poll_dates.py
             test_auth.py
             test_voting.py
   ```
- Delete the original `tests.py` file


## Design Hints

You need to keep track of who has voted for which poll.
This requires a change in the domain model.

![user-vote-choice](user-vote-choice.png)

After this change, there is no "votes" attribute in Choice.
To **hide the impact of change** you could redefine `votes`
as a read-only property that computes and returns the votes for a choice.

The votes property would sum the votes for a choice and
return the sum.  The view that show the vote counts won't see
any difference in the code.

### Use the Database Capabilities instead of Fetching All Votes!

Try to write efficent code for this.

- *Inefficient*: get all the votes and sum the ones that match a choice.

- *Effcient*: Create a query to select the votes you want and a function of queryset to count the items. Requires only one line of code.
   ```python
   votes = Vote.objects.all().filter(some-criteria).count()
   ```

## Getting a Visitor's IP Address

When someone logs in you should record their IP address as part of the log message.

There are many posts showing how to write a `get_client_ip` function using 
info in the Django `request` object.
Getting the visitor's **actual** IP address can be harder than it looks,
as some commenters mention here:
https://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django

Try to choose a good implementation, but it doesn't have to be perfect.

