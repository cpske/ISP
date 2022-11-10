---
title: Homework: E2E Test of KU Polls
---

Write functional (E2E) tests of your KU Polls app using Selenium.

**What to Submit**

Put all tests in file `polls/tests/functional_test.py` and commit it to
your django-polls repository on Github, in the master branch.

**Assignment**

Use Selenium Webdriver and either unittest or pytest to implement the tests below.  Use either Chrome or Firefox as the web browser (not Edge or Safari).


Write 4 unit tests:

1. Go to `/polls/`.  Find an `H1` tag and verify that it contains the page title that you used in your app.
2. Got to `/polls/` and find a poll question on the page. The test passes if it is found.
   - Do **not** assume that the question has id 1 or any other specific id.
   - You may also test the question text. That's even better.
3. Click on a polls hyperlink.  Verify that it goes to a page with list of choices to vote on.
4. Click on the first choice.  Verify that it goes to a page of voting results.
   - Do **not** assume that the choices have any specific id. That may vary.

You need to create *at least* one Question with some Choices (one Choice is not enough!).  Use a `setUp` method for that.

Since you create the Question and Choices in setUp, your test code knows what text to expect, so you can write selenium E2E tests that go beyond what is required and test the actual text of the polls voting page.
That's it!  E2E testing (functional testing) tests that your app behaves correctly, but doesn't try to throughly test every detail.  Use unittests for details.

**Suggestions**

You will need to have some polls data in the test database for these
tests to use.  You a `setUp` method or `setUpClass` (done only once).

* Setup for `unittest`: https://docs.python.org/3/library/unittest.html
    ```python
    @classmethod
    def setUpClass(cls):
        """This method is run only once, before any tests are run."""
        pass

    def setUp(self):
        """This method is called before every test."""
        pass
    ```

* Setup for `pytest`: https://docs.pytest.org/en/latest/xunit_setup.html

* Starting Selenium and opening a browser window takes time, so do it in setUpClass instead of in setUp.

* When all the tests finish you should close the browser window.  unittest has a `tearDownClass` method for clean-up tasks like that.


## More Info

[My Intro to Selenium](/ISP/testing/Selenium-intro)

[My Intro to Page Scraping](/ISP/testing/Selenium-scraping)

[Selenium API Docs](https://selenium.dev/selenium/docs/api/py/), best for API reference

[ReadTheDocs for Selenium](https://selenium-python.readthedocs.io/api.html) unofficial docs, has API and also info about installing and using Selenium.

[Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html) in the Selenium docs.
in [Selenium Docs](https://selenium-python.readthedocs.io/locating-elements.html) (unofficial docs).
