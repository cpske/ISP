---
title:  Link Scanner and Validator
---

Write Python functions as described below to test hyperlinks and create a list of bad or unreachable links on a web site.

Add your code to the `link-scanner` you did in week 13.

<!--
Create your own public Github repository named `link-scanner` containing this file.
 -->


Time Limit & Efficiency: when testing links on the ISP homepage using a network connection with throughput at least 1 Mbps, the application must finish and print all bad links within 90 seconds.  During testing, I may add bad links to the ISP homepage or use a different page on cpcke.github.io.


### 1. Function to Find and Return All Hyperlinks

This was done in the Week 13 link scanner using Selenium.

A function that accepts a string of a URL to scan.

Return: a list of unique strings containing the URLs for all hyperlinks ("a" tags) on the page.  


### 2. Function to Test a Single URL 

Write a function named `is_valid_url(url: str)` to test if
a url is valid & reachable or not.

Return True if the URL is OK, False otherwise.
Also return False is the URL has invalid syntax. **Don't** try
to validate the url syntax yourself! Let the Python library
you use do that -- it will raise an exception if the URL is invalid.

Use a Python library to query URLs instead of Selenium (slow and ineffective).
You may use httplib, urllib, or the Requests package.

For efficiency, **don't** use GET to actually fetch the web page;
that is slow and uses a lot of bandwidth.

* `urllib`: simply **open** a connection to the URL. If the URL is bad or unreachable it will raise an HTTPError. Check the error code in the HTTPError.  Any error code except 403 (Permission Denied) is a bad link.
  - Be sure to *close* the URL connection before returning from the function.

* `httplib` or `Requests`: send a HEAD request instead of GET request.  HEAD requests only the response header without the page content, which is *much* faster and smaller. It may be even faster if you don't try to read the response. Test the response code to decide if the url is valid and reachable. Also catch exceptions in case the URL is malformed.


### 3. Function to test a list of URLs

Write a function named `invalid_urls(urllist: List)`
to test a list of URLs (given as strings).

This function returns a new list containing only the invalid 
or unreachable URLs from the parameter list.
If no invalid URLs, return an empty list. 
**Don't modify** the list parameter. 
(This is a general programming guideline: don't modify parameters.)

Obviously, you should use your `is_valid_url` to test individual urls.

```python
def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
```

### 4. Main block: Scan a web page, print links and bad links

Write a `__main__` block that accepts a URL as a command line argument, 
gets the web page, and prints (a) all the links found on the page, 
and then (b) all the bad links.

So, someone can test all the links on the ISP home page by entering:

```
cmd>  python3 link_scan.py https://cpske.github.io/ISP/

http://git-school.github.io/visualizing-git/
https://asana.com/
https://cpske.github.io/ISP/ 
https://cpske.github.io/ISP/2021/ 
https://cpske.github.io/ISP/about.html 
https://cpske.github.io/ISP/agile/agile 
https://cpske.github.io/ISP/agile/scrum 
https://cpske.github.io/ISP/assignment/ku-polls/ 
https://cpske.github.io/ISP/bad/index

Bad Links:
https://cpske.github.io/ISP/bad/index 
```

If no command line argument is given, print a usage message:

```
cmd> python3 link_scan.py
Usage:  python3 link_scan.py url

Test all hyperlinks on the given url.
```

### How to Read Command Line Arguments

`sys.argv` is a list of all command line arguments and
`sys.argv[0]` is the name of the python file being invoked.
The other elements of `argv` are the command line arguments.

`sys.argv[0]` may include a path.
To get the name of the python file without the path, 
use `os.path.basename(sys.argv[0])`.

**Careful Programming**: this is not required, but what if the command
line argument (the URL to check) is not an HTML page? Such as a PDF file.
Then it's useless to scan the page for hyperlinks using Selenium.

You cannot determine the content type just by examining the URL as a string,
but you can test the Content-type header after getting a URL.
A careful program would print a message if the content type is not HTML.

## More Info

[My Intro to Selenium](/ISP/testing/Selenium-intro)

[My Intro to Page Scraping](/ISP/testing/Selenium-scraping)

[Selenium Official Docs](https://www.selenium.dev/documentation/) has lots of useful help for getting started and using Selenium.

[ReadTheDocs for Selenium](https://selenium-python.readthedocs.io/api.html) unofficial docs, has API and info on using Selenium.

[Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html) in the unofficial Selenium docs.
