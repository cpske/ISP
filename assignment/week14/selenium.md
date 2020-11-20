---
title:  Selenium Web Testing Assignment
---

## 1. Function to Find and Return all `<a href=...>` Tags

Write a Python function named `get_links(url: str)`.
The parameter is a String containing a URL.
Use Selenium to find all the "a" tags on the page.

Return: a list of strings containing all the URLs
for all hyperlinks on the page.  Each URL should
appear only once in the list (no duplicates).

Ignore page fragments -- the end of a URL starting with `#` sign,
such as `#breakfast` in https://kucafe.com/menu#breakfast.

```python
def get_links(url):
    """Find all links on page at the given url.
       Return:
          a list of all unique hyperlinks on the page,
          without "page fragments".
    """
    # TODO your solution
    return links
```

To get an attribute of a page element use `element.get_attribute('name')`
such as `link.get_attribute('href')`.


### 2. Function to Test a Single URL 

Write a function named `is_valid_url(url: str)` to test if
a url is reachable (valid) or now.
Return True if the URL is OK, False otherwise.

There are several ways to do this. Top choices are:

1. Selenium WebDriver 
2. Python httplib or urllib

If you use Python httplib or urllib, you don't need to actually
fetch the page -- that is slow and uses a lot of bandwidth.
For `urllib`, simply open the the URL.  If the URL is bad it 
will raise an HTTPError. Check the error code in the HTTPError.
For any error code except 403, it's a bad link.
Be sure to *close* the URL connection before returning.

For `httplib`, send a HEAD request instead of GET request. 
The HEAD request only returns the response header without the page content, 
which is a lot *faster* and smaller.

### 3. Function to test a list of URLs

Write a function named `invalid_urls(urllist: List)`
to test a list of urls (as Strings).
It returns a new list containing the invalid URLs.
If no invalid URLs, return an empty list.

Obviously, you should use your `is_valid_url` for this.

### 4. Main Function: Print bad links on the course homepage

Use your code to print all the bad links on https://cpske.github.io/ISP/


### Challenge Problem

For each link on the course home page, **if** the link refers
to another page in the same domain as the origin,
then scan that page for bad links, too.

Don't scan pages in other domains.


## What to Submit

In the code you submit, use Chrome or Firefox as the browser.
Don't use Safari or Microsoft Edge, because they don't work on Linux.

## More Info

[My Intro to Selenium](/ISP/testing/Selenium-intro)

[My Intro to Page Scraping](/ISP/testing/Selenium-scraping)

[Selenium API Docs](https://selenium.dev/selenium/docs/api/py/), best for API reference

[ReadTheDocs for Selenium](https://selenium-python.readthedocs.io/api.html) unofficial docs, has API and also info about installing and using Selenium.

[Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html) in the Selenium docs.
in [Selenium Docs](https://selenium-python.readthedocs.io/locating-elements.html) (unofficial docs).
