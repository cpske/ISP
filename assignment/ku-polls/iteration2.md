---
title: KU Polls Iteration 2
---

The objective of this iteration is to add an end date to polls,
improve the navigation and page layout,
and add some useful methods so that views can query a poll using methods instead of testing attributes directly.

Another objective is to externalize data for security and portability.

You will also automate running of tests.

## Tasks

1. Create an **Iteration 2 Plan** in your ku-polls wiki and write a plan as you did for Iteration 1.
2. Add links to "Iteration 2 Plan" in
   - Home page in Wiki
   - README.md
3. Review and update these wiki documents:
   - **Project Plan** - in particular, add details of Iteration 2 major work & goal or milestone
   - **Requirements** - add any new requirements that are significant
4. Create an `Iteration 2` task board and define tasks.
5. Create an `iteration2` branch for your work.
   - First, be sure you have merged *all work* from `iteration1` into `master` and pushed both branches to Github.
   - Create `iteration2` as a branch from `master` (not iteration1).

6. After you update the model (add `end_date`) and revise your polls questions, create a new data file named **data/polls-v2.json**.
   ```
   # in your "ku-polls" repository, enter:
   python manage.py dumpdata --indent=2 -o data/polls-v2.json polls
   ```
   Include `data/` and `data/polls-v2.json` in your git repository.


## New Features

1. In the `Question` class, add an `end_date` attribute that is the ending date for voting.
   - `end_date` can be `null`. If it is null, then voting is allowed anytime after `pub_date`.

2. Add a default for the `pub_date`.  The default is the current date and time.
   - This **doesn't work**:  `pub_date = DateTimeField( ..., default=timezone.now())`
     - The expression is evaluated when the code is first loaded, not when a new Question is created.
   - Use a function name **without parens** instead of the function value so that it is evaluated when the object is created. 
   - Don't use `auto_now`. It doesn't do what you might expect.

3. Items 1 & 2 change the database schema, so you need to make a migration and apply it ("migrate").

4. In the Question class, add two methods:
   - `is_published` returns True if the current date-time is on or after question's publication date. Use local date/time, not UTC!
   - `can_vote` returns True if voting is allowed for this question. That means, the current date/time is between the `pub_date` and `end_date`. If `end_date` is null then can vote *anytime* after `pub_date`.

5. Modify your views code to use these two methods. The view code should *not* directly test `question.pub_date >= something` (poor encapsulation).

6. Write **unit tests** for `is_published`. Test these cases:
   - question with future pub date (should not be shown in the UI)
   - question with the default pub date (now)
   - question with pub date in the past

7. Write at least **3 unit tests** for `can_vote`.    
   - Design 3 tests for different cases.  The tests should not be redundant.
   - Use a descriptive name for each test and write a one sentence docstring to describe what you are testing, e.g.
   ```python
   def test_cannot_vote_after_end_date(self):
      """Cannot vote if the end_date is in the past."""
      ...
   ```

7. If someone navigates directly to a poll detail page when voting is not allowed, redirect them to the polls index and show an error message on the index page.   
  A visitor can do this by entering the poll URL in his browser, such as  `http://localhost:8000/polls/k/` (k = poll number)
   - Use the "Django Messages Framework" to set and show the error message. It's much simpler than passing an `error_message` via the context. (That's cludgy and I wonder why the tutorial did that.)
   - [Messages Framework](/ISP/django/messages-framework/) document describes how.

## Navigation Improvements

Navigating the app's pages is clumsy. Sometimes a visitor has to use the browser Back button, too! Let's improve navigation.

1. If someone goes to the base URL of the web site, such as `http://localhost:8000/`, redirect them to the polls index page.
   - After the redirect, the visitor's web browser should show the actual URL (`http://localhost:8000/polls/`) not the base URL `/`.
   - Many ways to do this. Have a look at Django's `RedirectView` class and `RedirectView.as_view()` method.
  
2. Improve navigation between pages.
   - On the polls detail page, add a "Back to List of Polls" link so visitor can go back to the index.
   - On the voting results page, also add a "Back to List of Polls" link (same text message as above).
   - You can use any *intuitive* text or icon you like instead of "Back to List of Polls"; but be consistent.
   - Remove the "Vote again" link. A visitor should get only one vote per poll!

3. Add links so that a visitor to view polls results without voting.
   - On polls index page, add a "Results" link for each question.
   - On the poll "detail" page, also add a link to "Results".

## Other Enhancements

1. Improve appearance of the voting results page.
   - Make the choice text and votes line up in columns (use a table or CSS) 
   - Remove the ugly bullets!
   - Remove the word "votes" after the count (it's just clutter)

2. Externalize configuration data in `settings.py`.
   - Add `python-decouple` to your project. Use it to externalize values of these variables in `settings.py`:
     ```
     SECRET_KEY
     DEBUG
     ALLOWED_HOSTS
     TIME_ZONE
     ```
   - Put the **values** of those variable in a `.env` file in your project root directory.
   - Include **safe defaults** in `settings.py` for every externalized setting, in case a variable is not set in `.env`.
     ```
     # what is a safe default for DEBUG?
     DEBUG = config("DEBUG", cast=bool, default=???)
     ```
   - See [Externalize Configuration](/ISP/django/external-configuration) for more info.

3. Do **not** commit `.env` to Git, but *do* create and commit a `sample.env` file so that someone knows what they need to set.
   - include helpful comments in `sample.env`
   ```
   # Copy this file to .env and edit the values
   # Create a secret key using (todo: how to create a secret key?)
   SECRET_KEY = secret-key-value-without-quotes
   # Set DEBUG to True for development, False for actual use
   DEBUG = False
   # ALLOWED_HOSTS is a comma-separated list of hosts that can access the app.
   # You can use wildcard chars (*) and IP addresses. Use * for any host.
   ALLOWED_HOSTS = localhost, 127.0.0.1, ::1, testserver
   # Your timezone
   TIME_ZONE = Asia/Bangkok
   ```

4. Add correctly-formatted docstring comments to the models and views.
   - Write class docstring and method/function docstring.
   - First line should be a complete sentence.
   - Use `flake8` to verify docstrings.

## Testing (This isn't required in 2024 -- we'll add it later)

1. Create a Github Action to automatically run your unit tests.
   - You only need to run using one version of Python (the Github template uses many versions)
   - You may need to include `testserver` in ALLOWED\_HOSTS for the tests to run.

2. Add a github "badge" to README.md that shows the status of tests.

3. All tests should pass.  They should pass both on Github and when TA runs your code in a virtual env.

## Evaluaton

Project Artifacts

- "Iteration 2 Plan" is accurate and complete: GOAL, MILESTONE, FEATURES/WORK
- Iteration 2 Task Board has tasks covering the work. Most or all are "Done".
- Requirements doc is project requirements, not iteration requirements.
- README has link to Iteration 2 Plan
- README has Badge showing tests pass on Github

Configuration

- `sample.env` works (either copy to `.env` or source into the environment)
- `mysite/settings.py` externalize and has defaults for:
  - `SECRET_KEY`
  - `DEBUG`
  - `ALLOWED_HOSTS`
  - `TIME_ZONE`
- `python-decouple` is in "requirements.txt"
- migrations run without error
- loaddata works 

Code

- `is_published` is correct
- `can_vote` is correct
- both methods have docstring describing what they do and what they return
- views do not directly test value of `question.pub_date`

Tests

- all unit tests pass
- at least 3 tests for `is_published`
- at least 4 tests for `can_vote`

Run the App - Functionality

- "/" redirected to "/polls/"
- "/polls/" page shows poll status: open or closed
- poll detail page has "Back to Index" or similar
- can vote
- polls results page has "Back to Index" or similar
- link to view poll results without voting
- cannot vote on closed poll, even using URL bar or HTTP client app

