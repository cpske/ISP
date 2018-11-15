## Selenium WebDriver in Python

### Installation

You need the selenium package and at least one browser driver.

Install instructions: https://pypi.org/project/selenium/

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

### 3.Function to Test all Links

Write a `invalid_urls( urllist )` function
to test a list of urls (as Strings).
If the URL is OK, don't do anything.
Return a new list containing all the invalid or unreachable URLs.

You can use Selenium WebDriver or Python httplib or urllib2 for this.
Try sending just a HEAD request instead of GET request. 
The HEAD request only returns the response header without the page content, which will be a lot faster.

 For urllib2, just open the URL.

### 4. Print all Invalid Links on the Course Homepage

In the main method, also print all the bad (unreachable) URLs.

### 5. (Optional) Efficiency Improvement

When you create a browser object using
```python
# Firefox
browser = webdriver.Firefox(options)
# Chrome
browser = webdriver.Chrome(options)
```
you can pass configuration parameters and command line options to the
browser.

Can you find a way to tell the browser **not** load images on the page?  It will make loading faster.




