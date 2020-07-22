---
title: Selenium WebDriver in Python
---

### Installation

You need the selenium package and at least one browser driver.

Installation instructions: https://pypi.org/project/selenium/

This only installs Selenium, not the browser drivers:
```shell
pip install -U selenium
```

### 1. Function to Find all `<a href=...>` Tags

Write a Python function named `get_links(url)`.
The parameter is a String containing a URL.
Use Selenium to find all the "a" tags on the page,
and return a list of all the 'href' values on the page.

```python
from selenium import webdriver

def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    browser = webdriver.Firefox()
    browser.get(url)
    #TODO get all 'a' tags on page
    #TODO for each 'a' tag, get the href attribute value
    browser.close()
    return links
```

Ref: See [Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html)
in [Selenium Docs](https://selenium-python.readthedocs.io/locating-elements.html) (unofficial docs).

To get an attribute of a page element use `element.get_attribute('name')`
such as `link.get_attribute('href')`.

### 2. Print all Links on the Course Homepage

Write a `main` method to print all the links (href values)
on the course homepage, one per line.

Homepage:  https://cpske.github.io/ISP/

### 3. Function to Test all Links

Write a `invalid_urls( urllist )` function
to test a list of urls (as Strings).
If the URL is OK, don't do anything.
Return a new list containing all the invalid or unreachable URLs.

You can use Selenium WebDriver or Python httplib or urllib for this.
Try sending just a HEAD request instead of GET request. 
The HEAD request only returns the response header without the page content, 
which is a lot *faster* and smaller.

For urllib2, just open() the URL.  If the URL doesn't exist,
opening it will raise an exception.

### 4. Print all Invalid Links on the Course Homepage

In the main method, also print all the bad (unreachable) URLs.


### 5. E2E Test of Your Django Polls

Write functional (E2E) tests of your Django Polls app using Selenium.

**What to Submit**

Put all tests in file `polls/tests/functional_test.py` and commit it to
your django-polls repository on Github, in the master branch.

**What to Test**

1. Go to `/polls/`.  Find an `H1` tag and verify that it contains "Current Polls" (or whatever text your heading is).
2. Got to `/polls/` and find a poll question on the page.  The test passes if it is found.
3. Click on a polls hyperlink.  Verify that it goes to a page with list of choices to vote on.
4. Click on the first choice.  Verify that it goes to a page of voting results.

That's it!  E2E testing (functional testing) tests that your app behaves correctly, but doesn't try to throughly test every detail.  Use unittests for details.

You can use either `unittest` or `pytest` for these tests.

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

Write tests to do this.  You may want to modify your templates to make page elements easier to find.

For example, in your `index.html` template, add an `id` or `class` attribute to your elements for polls questions.

## More Info

[My Intro to Selenium](/ISP/testing/Selenium-intro)

[My Intro to Page Scraping](/ISP/testing/Selenium-scraping)

[Selenium API Docs](https://selenium.dev/selenium/docs/api/py/), best for API reference

[ReadTheDocs for Selenium](https://selenium-python.readthedocs.io/api.html) unofficial docs, has API and also info about installing and using Selenium.

