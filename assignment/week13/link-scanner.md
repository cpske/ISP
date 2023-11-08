---
title: Link Scanner and Tester using Selenium
---

Write a Python application that finds all hyperlinks on a web page and tests them.  It then prints on the console:

1. All unique URLs of hyperlinks and images on the page, sorted.  
   - Remove parameters, query parameters, and fragments from the URLs.
   - Include URLs found in "a" and "img" tags only. Don't include links inside `<style>`, `<script>`, or audio/video tags.
   - If you can sort by reverse domain names, do so, but this is not required. For example, all the "xxx.ku.ac.th" urls would appear together, including www.iup.ku.ac.th, eng.ku.ac.th, cpe.eng.ku.ac.th, etc. Otherwise, sort the URLs in ordinary dictionary order.

2. Print all URLs that require authentication, authorization, or payment to access.
   - you can determine this using the HTTP response code
   - if there are no such URLs, then skip this part of the output

3. Print all bad or invalid URLs.

Name the file `linkscanner.py`. It should be runnable and accept a URL to scan as command line parameter. For example:
```
cmd>  python linkscanner.py https://cpe.ku.ac.th
```

### Programming Requirements

- The application must *not* open a browser window. Run in headless mode.
- Use a current version of Chrome or Firefox (not Safari).  You can assume that the Chrome and Firefox webdrivers are installed and on the user's PATH.
- To facilitate changing the browser settings, in `linkscanner.py` include a Browser class with `get_browser` class method as described below.
- If your app requires any packages not in the Python standard library, include a `requirements.txt` file.

## What to Submit

Push your code to Github Classroom.


> **Requirement for Individual Work**
>
> This is an individual assignment. Please discover how to implement it yourself. Do not ask other students, including classmates, for help, or share code. You may ask TAs for clarification or technology questions.
>
> There are many ways to implement this assignment, so highly similar codes will be questioned. If copying is detected, everyone involved will receive F for the course. 

### 1. Browser Class to Create a Headless Browser

Write a `Browser` class (in `linkscanner.py`) with a `get_browser` class method that returns a singleton instance of a *headless* Firefox or Chrome `WebDriver` (your choice).    
Usage:

```python
# create a headless Selenium browser
browser = Browser.get_browser()
browser.get("https://some.place")  # nothing is shown on screen
browser2 = Browser.get_browser()
browser2 is browser               # get_browser returns same instance
True
```
- Your code should be portable, so do not specify a path to the Chrome or Firefox webdriver. Assume it is on the search path.
- "Headless" means there is no GUI window for the browser. This makes it much faster.
- A technique that works for both Chrome and Firefox is to use the `--headless` argument:
  ```python
  options = webdriver.FirefoxOptions()
  options.add_argument("--headless")
  browser = webdriver.Firefox(options=options)
  ```
- By simply modifying this code to omit the `options`, then Selenium would open **only one** browser window. This can be useful for testing your code or visually confirming the results.


### 2. Write Seperate Methods or Functions for Each Action

Write the best code that you can and apply principles you learned from refactoring.

That includes using separate functions or methods for different tasks, not one long method that does everything.

### 3. Determine Link Status Without Fetching the Page

To test the status of a URL, send a HEAD request.  This returns only the page header and status code, which is much faster than getting the entire page.

Python's `urllib` and the `requests` package are both good tools for this. You should instruct the code to follow redirects instead of returning a 30X status code.

### 4. Parse URLs to Remove Query, Params, Fragment, etc.

URLs may include the following elements:
```
schema://network.locati.on/path;parameter?query1=value1&query2=value2#fragment
```
Some parts may be omitted and some can appear out of order.  You should remove parameters, query params, and page fragments from URLs before printing them.

Instead of writing code to remove the unwanted parts, let [urllib.parse][urllib.parse] do it for you! 
There is an example in the [URL Parsing][url-parsing] section.

[urllib.parse]: https://docs.python.org/3/library/urllib.parse.html
[url-parsing]: https://docs.python.org/3/library/urllib.parse.html#url-parsing

### Example Output

The example shows the output format. The URL is deliberated incorrect.    
I will try to add an example, but you should create your own example web page containing a variety of URLs. 

```bash
cmd> python linkscanner.py https://cpske.github.io/testpage

Valid URLs
https://cpske.github.io/ISP/about/
https://cpske.github.io/ISP/introduction/
https://cpske.github.io/ISP/software-process/
https://cpske.github.io/ISP/images/SDLC.png
https://cpske.github.io/ISP/images/tcp-ip-packet-layout.gif
http://git-school.github.io/visualizing-git/
https://yangsu.github.io/pull-request-tutorial/
https://classroom.googleapis.com/v1/courses
https://realpython.com/
https://api-m.paypal.com/v1/invoicing/invoices
https://www.scrumguides.org/scrum-guide.html
https://realpython.com/python-pep8/
https://www.youtube.com/watch

URLs Requiring Authorization or Payment
https://classroom.googleapis.com/v1/courses
https://api-m.paypal.com/v1/invoicing/invoices

Bad URLs
https://cpske.github.io/ISP/projects/2023
https://learngitbranching.js.org/sandbox
```

### References

- HTTP Response Codes <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>

