---
title: KU Polls Iteration 2
---

The objective of this iteration is to improve the navigation and page layout,
add an end date for a poll, and add some useful methods.

Another objective is to externalize configuration data for security and portability.

This iteration does not require much new code, so it's a good chance to review what you learned about Django. Reread the tutorial or view a different one; it really helps.

## Tasks

1. Create an "Iteration 2 Plan" in your ku-polls wiki and write a plan as you did for Iteration 1.
2. Create an "Iteration 2" task board and define tasks.
3. Create an `iteration2` branch for your work.  
   - First, be sure you have merged `iteration1` into `master` and pushed both to Github.
   - Create `iteration2` as a branch from `master` (not from iteration1).

## New Features and Enhancements

1. In the Question class, add an `end_date` attribute that is the ending date for voting.
   - This changes the database schema, so you need to create a migration (`makemigrations polls`) and run migrations (`migrate`) after this.

2. In the Question class, add two methods:
   - `is_published` returns True if current date is on or after question's publication date
   - `can_vote` returns True if voting is currently allowed for this question
   - modify your views code to use these methods instead of directly testing `question.pub_date >= something`.

3. Create **unit tests** for `is_published` and `can_vote`.

4. If someone navigates to a poll detail page when voting is not allowed, redirect them to the polls index page and show an error message on the page.
   - Use the "Django Messages Framework" to pass and show the error message. It's simpler than passing an `error_message` via the context. (That's cludgy and I wonder why the tutorial used that at all.)
   - [Messages Framework](/ISP/django/messages-framework/) is shown in [topics list](https://cpske.github.io/ISP/) on class github.io site.

5. Redirect "/" to the polls index.
   - If someone goes to the base URL of the web site, such as `http://localhost:8000/`, redirect them to the polls index page.
   - After the redirect, the actual URL (`http://localhost:8000/polls/`) should show in visitor's web browser URL bar.

6. Improve navigation.
   - On polls index page, add "vote" and "results" links for each question, so someone can view results without voting.
   - Enable the "vote" link for a poll only if voting is allowed. OK to hide the link if voting not allowed.
   - On the polls detail page, add a "Back to List of Polls" link so person can go back without voting.  You can use other text instead of "Back to List of Polls". What is most intuitive?
   - On the voting results page, also add a "Back to List of Polls" link (use same text message as above).

7. Improve the appearance of voting results page.  
   - Make the votes align in a column and omit the word "votes" after the count -- it's redundant. 
   - Remove the bullets.

8. Externalize configuration data.
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

9. Update your unit tests from Iteration 1 so that they still pass.

