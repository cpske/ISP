---
title: KU Polls Iteration 2
---

The objective of this iteration is to improve the navigation and page layout,
and add an ending date for voting on a poll.
Another objective is to externalize configuration data for security and portability.

1. Create an "Iteration 2 Plan" in your ku-polls wiki and write a plan, using the same format as iteration1.

2. Create an "Iteration 2" project board and define tasks.

3. Create an `iteration2` branch for your work.  
   - Before that, be sure you have merged `iteration1` into `master` and pushed both to Github.
   - Create `iteration2` as a branch from `master` (not iteration1).

Features and enhancements for Iteration 2:

1. In the Question class, add a `end_date` attribute that is the ending date for voting.
   * You need run migrations after this, to update the database schema.

2. In the Question class, add two methods:
   * `is_published` returns true if current date is on or after question's publication date
   * `can_vote` returns true if voting is currently allowed for this question

3. Create unit tests for `is_published` and `can_vote`.

4. If someone navigates to the polls detail page for a poll where voting is not allowed, redirect them to the polls index page and show an error message.
   - Suggest you use the "Django Messages Framework" for this. It's simpler than passing an error_message via the context.
   - [Messages Framework](/ISP/django/messages-framework/) is shown in [topics list](https://cpske.github.io/ISP/) on class github.io site.

5. Improve navigation.
   * On polls index page, add "vote" and "results" links for each question.
   * Only show "vote" link for a poll where voting is allowed.
   * On the polls detail page, add a "Back to List of Polls" link so person can go back without voting.  You can use your choice of text instead of "Back to List of Polls".
   * On the voting results page, also add a "Back to List of Polls" link.

6. Improve appearance of voting results page.  Make the votes align in a column, omit the word "votes" after the count -- it's redundant, remove the bullets.

7. Index page - show all published poll questions, not just 5 most recent.
   * Sort them so that the newest questions are first

8. Externalize configuration data. 
   * Remove the value of SECRET_KEY and DEBUG from `settings.py` and put their values in a `.env` file.
   * Don't commit `.env` to Git.
   * See [Externalize Configuration](/ISP/django/external-configuration/) for how to do this.
   * Use either the `python-decouple` or `django-environ` package. They are described on the class github.io site under "Externalize Configuration".

After making these changes, you may need to update some unit tests that you wrote in iteration1.
