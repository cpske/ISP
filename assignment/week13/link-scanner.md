---
title: Link Finder using Selenium
---

Write the following class and functions using Selenium.
Starter code is provided on Github Classroom.

`main.py` contains an example usage.  When I ran it, it printed 93 hyperlinks.

#### What to Submit

Push your code to Github Classroom.

#### Plagiarism

If copying is detected on this assignment, everyone involved will receive F for the course.

### 1. Singleton Class to Create a Headless Browser

Complete the `Browser` class.  Write a `get_browser` class method that returns a singleton instance of a *headless* Firefox or Chrome web browser (your choice).

```python
browser = Browser.get_browser()
browser.get("http://some.place") # nothing is shown on screen
browser2 = Browser.get_browser()
browser2 is browser              # browser is a singleton
True
```
- "Headless" means there is no GUI interface for the browser. This makes it much faster.
- Use Chrome or Firefox (no other browser).
- Your code should be portable, so do not specify a path to your browser driver in code.
- A technique that works for both Chrome and Firefox is to use the `--headless` argument:
  ```python
  options = webdriver.FirefoxOptions()
  options.add_argument("--headless")
  browser = webdriver.Firefox(options=options)
  ```
- Your code should work if someone omits the options, so it opens **one** browser window. That is, with a small modification the code runs in either GUI and headless modes.


### 2. Link Finder

Use Selenium to implement this:
```python
def find_link(url: str, link_text: str) -> str:
    """Search a web page for a hyperlink with link text that exactly matches link_text.  
    
    Return the matching hyperlink URL. If more than one match, return the first one.

    :param url: URL of the web page to scan
    :param link_text: the text of a hyperlink to search for
    :return: string form of the first matching hyperlink URL, or None if no match
    :raises ValueError: if the url is invalid
    """
```

### 3. Find All Hyperlinks on a Page

Write a method that returns a collection of all the link URLs that appear in `<a>` tags on a page (so it doesn't include URLs of Javascript or CSS files, which don't use the `<a>` tag).

```python
def find_links(url: str) -> Collection[str]:
    """Return the URLs of all hyperlinks found inside of <a> tags. 
    
    This excludes links to Javascript and CSS files.
    The returned collection of hyperlinks should be unique.

    :param url: URL of the web page to scan
    :return: collection of unique urls of hyperlinks on the page
    :raises ValueError: if the url is not valid
    """
```
- Some `<a>` tags may not contain an `href` attribute. Your code should handle that case. Don't crash or return empty elements in the collection.
