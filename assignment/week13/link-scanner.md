---
title: Link Scanner and Tester using Selenium
---

Write a Python application that finds all hyperlinks and image links on a web page and tests them.  
It then prints on the console:

1. All valid, unique URLs of hyperlinks on the page.  
   - Include URLs in `<a>` and `<img>` tags.
   - Do not include urls found inside other tags.
   - Remove parameters, query parameters, and page fragments from the URLs.
   - Sort urls by reverse domain names if you can, but this is not required.   
     This means:
     - `*.biz` urls before `*.com` before `*.org` 
     - `mail.google.com` before `help.microsoft.com` because `google.com` is before `microsoft.com`
     - "eng.ku.ac.th", "cpe.eng.ku.ac.th", and "www.iup.ku.ac.th" appear together.

2. Next print all URLs that require authentication, authorization, or payment to access.
   - you can determine this using the HTTP response code
   - if there are no such URLs, then omit this part of the output

3. Next print all bad or invalid URLs.
   - This includes URLs with invalid syntax, non-existing URLs, and server errors.
   - if there are no such URLs then omit this.

If a URL is longer than 120 characters, then print only the first 120 characters followed by "..."
```
https://www.infoworld.com/article/2615765/application-development/10-practices-of-highly-ineffective-software-developers...
```

Name your file `linkscanner.py`. It should be runnable and accept a URL to scan as command line parameter. For example:

```
cmd>  python linkscanner.py https://www.cpe.ku.ac.th
```
if someone forgets the url then print a usage message:
```
cmd>  python linkscanner.py
Usage:  python linkscanner.py url
```

### Programming Requirements

- The application must *not* open a browser window. Run in headless mode.
- Include a `requirements.txt` listing the packages your app uses, including selenium.
- Use a current version of Chrome or Firefox (not Safari since its not portable).  You can assume that the Chrome and Firefox webdrivers are installed and on the user's PATH, or use webdriver-manager.
- To facilitate changing the browser settings or browser type, in `linkscanner.py` include a `Browser` class with `get_browser` class method as described below.

You must complete 2 functions in the starter code, but you can (and should) add other functions
to help your code.

The two required functions are:

- `find_links(url: str)` Find all the hyperlinks on a page and return them as a collection
- `verify_url(url: str)` Verify a single URL.

You must also implement the `Browser.get_browser()` class method.

## What to Submit

Push your code to Github Classroom.


### Requirement for Individual Work

This is an individual assignment. Please discover how to implement it yourself. Do not ask other students for help, or share code. You may ask TAs for clarification, help, and technology questions.

There are many ways to implement this assignment, hence highly similar codes will be questioned. If copying is determined, everyone involved will receive F for the course. 


### 1. Browser Class to Create a Headless Browser

Write a `Browser.get_browser()` class method in `linkscanner.py` a *headless* Firefox or Chrome `WebDriver` (your choice).

Usage:

```python
# create a headless Selenium WebDriver
browser = Browser.get_browser()
isinstance(browser, selenium.webdriver.remote.webdriver.WebDriver)
True
browser.get("https://www.ku.ac.th")  # headless - nothing is shown on screen
browser.get_full_page_screenshot_as_file("/tmp/ku.png") # save image of web page
```

- Your code must be portable, so do not specify a path to the Chrome or Firefox webdriver.
- "Headless" means there is no browser GUI window.
- A technique that works for both Chrome and Firefox is to use the `--headless` argument:
  ```python
  options = webdriver.FirefoxOptions()
  options.add_argument("--headless")
  browser = webdriver.Firefox(options=options)
  ```

### 2. Write The Best Code That You Can

Apply the principles you learned from refactoring and other coding best practices you have learned.

That includes using separate functions for different tasks, and avoiding cludges.

### 3. Determine Link Status Without Fetching the Page

To test the status of a URL, send a HEAD request.  This returns only the page metadata and status code, which is much faster than getting the entire page.

Python's `urllib` and the `requests` package are both good tools for this.

You should instruct the code to follow redirects instead of returning a 30X status code (the default behavior).

### 4. Parse URLs to Remove Query, Params, Fragment, etc.

URLs may include the following elements:
```
schema://host.doma.in/path;parameter?query1=value1&query2=value2#fragment
```
A semi-colon indicates the start of url parameters; a "?" starts the query parameters, and "#" indicates a page-frament.  
URL components may be omitted or can appear in a different order.  

Remove parameters, query params, and page fragments from URLs before printing them.

Avoid writing this code yourself (cludgy). Let [urllib.parse][urllib.parse] do it for you. 
There is an example in the [URL Parsing][url-parsing] section.

[urllib.parse]: https://docs.python.org/3/library/urllib.parse.html
[url-parsing]: https://docs.python.org/3/library/urllib.parse.html#url-parsing

### 5. Sorting by Domain Components in Reverse Order

It would be helpful if URLs from related domains are displayed together, such as:
```
https://apple.com
https://images.google.com
https://mail.google.com
https://www.cpe.ku.ac.th
https://eng.ku.ac.th
https://www.iup.ku.ac.th
https://www.ku.ac.th
```
Here's a hint:
```python
parse_result = urllib.parse.urlparse(url)
# hostname may be None
hostname = parse_result.hostname or ""
hostname.split(".")
# now reverse the order
```

### Example Output

This example shows the output format. Actual output may not match this example.   

```bash
cmd> python linkscanner.py https://cpske.github.io/ISP/

Valid URLs
https://classroom.googleapis.com/v1/
https://www.infoworld.com/article/2615765/application-development/10-practices-of-highly-ineffective-software-developers...
https://realpython.com/
https://api-m.paypal.com/v1/invoicing/invoices
https://www.scrumguides.org/scrum-guide.html
https://realpython.com/python-pep8/
https://www.youtube.com/watch
https://cpske.github.io/ISP/about/
https://cpske.github.io/ISP/introduction/
https://cpske.github.io/ISP/software-process/
https://cpske.github.io/ISP/images/SDLC.png
https://cpske.github.io/ISP/images/tcp-ip-packet-layout.gif
http://git-school.github.io/visualizing-git/
https://yangsu.github.io/pull-request-tutorial/

URLs Requiring Authorization or Payment
https://classroom.googleapis.com/v1/courses
https://api-m.paypal.com/v1/invoicing/invoices

Bad URLs
https://cpske.github.io/ISP/projects/2023
https://learngitbranching.js.org/sandbox
https://mail,google.com
https://mail+google.com/login
```

### References

HTTP Response Codes <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>

