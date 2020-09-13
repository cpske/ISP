---
title: KU Polls Iteration 2
---

The objective of this iteration is to improve the navigation and page layout,
and add an ending date for voting on a poll.
Another objective is to externalize configuration data for security and portability.

1. In the Question class, add a `end_date` attribute that is the ending date for voting.
   * You need run migrations after this, to update the database schema.

2. In the Question class, add two methods:
   * `is_published` returns true if current date is on or after question's publication date
   * `can_vote` returns true if voting is currently allowed for this question

3. Add unit tests for `is_published` and `can_vote`.

4. If someone navigates to the polls detail page for a poll where voting is not allowed, redirect them to the polls index page and show an error message.

5. Improve navigation.
   * On polls index page, add "vote" and "results" links for each question.
   * Only show "vote" link for a poll where voting is allowed.
   * On the polls detail page, add a "Back to List of Polls" link so person can go back without voting.
   * On the voting results page, it doesn't make sense to vote again, so remove that link and instead add a "Back to List of Polls" link.

6. Improve appearance of voting results page.  Make the votes align in a column, omit the word "votes" after the count -- it's redundant.

7. Index page - show all published poll questions, not just 5 most recent.
   * Sort them by date published so newest questions are first

8. Externalize configuration. 
   * Remove the value of SECRET_KEY and DEBUG from `settings.py` and put the values in a `.env` file.
   * Don't commit `.env` to Git.
   * Use either the `python-decouple` or `django-environ` package for this. They are described on the class github.io site under "Externalize Configuration".

After making these changes, you may need to update some tests from iteration1.
