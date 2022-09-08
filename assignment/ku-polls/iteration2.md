---
title: KU Polls Iteration 2
---

The objective of this iteration is to improve the navigation and page layout,
add an end date for a poll, and add some useful methods so that views can query a poll using methods instead of testing attributes directly.

Another objective is to externalize configuration data for security and portability.

This iteration does not require much new code. It's a good chance to review what you learned about Django. Reread the tutorial or view a different one -- it really improves learning.

## Tasks

1. Create an "Iteration 2 Plan" in your ku-polls wiki and write a plan as you did for Iteration 1.
2. Create an "Iteration 2" task board and define tasks.
3. Create an `iteration2` branch for your work.  
   - First, be sure you have merged *all work* from `iteration1` into `master` and pushed both to Github.
   - Create `iteration2` as a branch from `master` (not iteration1).

## New Features and Enhancements

1. In the Question class, add an `end_date` attribute that is the ending date for voting.
   - `end_date` can be null. In that case, voting is allowed anytime after `pub_date`.
   - This changes the database schema, so you need to create a migration (`makemigrations polls`) and run migrations (`migrate`) after this.

2. In the Question class, add two methods:
   - `is_published` returns True if current date is on or after question's publication date. Use local date/time, not UTC!
   - `can_vote` returns True if voting is allowed for this question
   - modify your views code to use these methods instead of directly testing `question.pub_date >= something`.

3. Create **unit tests** for `is_published` and `can_vote`.
   - for `can_vote` you need to test several cases, including but not limited to: 
     i. `pub_date` is in the future, 
     ii. current date/time is exactly the `pub_date` or exactly the `end_date` (voting allowed),
     iii. current date/time is after `end_date`,
     iv. a poll with no `end_date` (null).

4. If someone navigates to a poll detail page when voting is not allowed, redirect them to the polls index page and show an error message on the page.
   - Use the "Django Messages Framework" to pass and show the error message. It's simpler than passing an `error_message` via the context. (That's cludgy and I wonder why the tutorial used that at all.)
   - [Messages Framework](/ISP/django/messages-framework/) is shown in [topics list](https://cpske.github.io/ISP/) on class github.io site.

5. If someone goes to the base URL of the web site, such as `http://localhost:port/`, redirect them to the polls index page.
   - After the redirect, the actual URL (`http://localhost:port/polls/`) the visitor's browser should show the actual polls URL in the browser address bar, i.e. /polls/ not /.

6. Allow visitor to view results without voting.
   - On polls index page, add a "results" links for each question, so someone can view results without voting.
   - You may add a "vote" link, too.
   - The links to vote (clicking on the question text or clicking on "vote") should only be hyperlinks if voting is allowed (`can_vote`).
   
7. Improve navigation between pages.
   - On the polls detail page, add a "Back to List of Polls" link so person can go back without voting.
   - On the voting results page, also add a "Back to List of Polls" link (use same text message as above). Remove the "Vote again" link -- a visitor should get only one vote per question!
   - You can use any *intuitive* text or icon instead of "Back to List of Polls".  Just be consistent.

8. Improve the appearance of voting results page.  
   - Make the votes align in a column and omit the word "votes" after the count (redundant). 
   - Remove the bullets.

9. Externalize configuration data.

   - Remove the **values** of `SECRET_KEY`, `DEBUG`, and `TIME_ZONE` from `settings.py` and put their values in a `.env` file.
   - See [Externalize Configuration](/ISP/django/external-configuration/) for how to do this.  I suggest you use `python-decouple`. It is the most general purpose and has better docs than the `django-environ` package. 
   - In `settings.py`, **do** provide safe **default** values for the externalized parameters, so someone can run your app even if they don't have a `.env` file.  Don't use your actual secret key as a default value!  Any string will do, such as "missing-secret-key".
   - Do not commit `.env` to Git.  Add it to `.gitignore` (if its not already in .gitignore).
   - **Do** create a `sample.env` file and commit it to Git. The file should include comments telling the installer what to do:
     ```
     # Create a secret key using ...
     SECRET_KEY = secret-key-value-without-quotes
     # set DEBUG to True for testing, False for actual use
     DEBUG = False
     ```

10. Add correctly-formatted docstring comments to the models and views.
    - *Do I really need to make this an assignment?*
    - Using the coding standard and writing documentation should be something you **always** do. Amazingly, though, many students did not write docstrings in their iteration 1 code!

11. Rerun your unit tests from Iteration 1.  If any fail, then either fix the bug or update the tests.
    - When TA tests your code, tests should all pass.

