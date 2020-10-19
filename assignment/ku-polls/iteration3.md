---
title: KU Polls Iteration 3
---

Add user authentication and restrict each user to 1 vote per poll.
For this iteration user authentication will be done using the boring old
username-password backend, which Django calls "ModelBackend".

Behavior to add or modify is:

* anyone can view the list of polls or poll results
* only an authenticated user can submit a vote
* a user can vote again on a poll, and it replaces his previous vote. He can only resubmit during a poll's voting period.
* if a user selects a poll he already voted for, it's highly desirable that the list of choices show his previous selection

## Requirements

Write your own Iteration Plan without copying text from this assignment.
Create an "Iteration 3" task board with your tasks.

Implement the features and write unit tests for them.

Your project now has many unit tests, so consider doing some refactoring
of tests as recommended in the MDN Django Tutorial.
* Create a `polls/tests` directory with an `__init__.py` file.
* Divide your tests into separate files, grouped however makes sense, such as:
  ```
  polls/tests/
             test_index.py
             test_poll_dates.py
             test_auth.py
             test_voting.py
   ```
* Delete the original `tests.py` file

## Design Hints

You need to keep track of who has voted for which poll.
This requires a change in the domain model.

(UML to be added.)

After the change, there is no "votes" attribute in Choice,
but to *hide* the impact of change you could rewrite "votes"
as a read-only property.

The votes property would sum the votes for a choice and
return the sum.  The view that show the vote counts won't see
any difference in the code.

Try to write efficent code for this.
- *Inefficient*: get all the votes and sum the ones that match this choice.
- *Effcient*: Create a query to select the votes you want and a function of queryset to count the items. Requires only one line of code.
