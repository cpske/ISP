---
title:  Selenium URL Testing
---

1. Write a Python program in a file named `link_scan.py` that implements the functions described below.

2. Submit your code to Github Classroom. The assignment URL is listed on Google Classroom for this assignment.

3. In your code, use Firefox or Chrome as the browser invoked by Selenium.  Don't use Safari or Microsoft Edge.

4. Efficiency: when testing links on the ISP homepage on a network connection with throughput at least 1 Mbps, the application should finish and print all bad links within approximately 90 seconds.  During testing, I may add more bad links.


### 1. Function to Find and Return All Hyperlinks

Write a function named `get_links(url: str)`.

The `url` parameter is a String containing the URL
of a web page to scan for hyperlinks.

Use Selenium to find all the "a" tags on the page and
return the URLs as a list, without page fragments or query params.

Return: a list of strings containing the URLs
for all hyperlinks ("a" tags) on the page.  
Each URL should appear only once in the list (no duplicates).
* Return urls without page fragments -- the end of a URL starting with `#` sign,
such as `#breakfast` in https://kucafe.com/menu#breakfast
* Also remove query parameters beginning with "?", as in https://kucafe.com/?q=breakfast.

```python
def get_links(url):
    """Find all links on page at the given url.

       Returns:
          a list of all unique hyperlinks on the page,
          without page fragments or query parameters.
    """
    # TODO your solution
```


### 2. Function to Test a Single URL 

Write a function named `is_valid_url(url: str)` to test if
a url is reachable (valid) or not.

Return True if the URL is OK, False otherwise.
Also return False is the URL has incorrect syntax -- *don't* try
to validate the url syntax yourself! Let whatever Python library
you use do that -- it will raise an exception of the URL is invalid.

There are several ways to test a URL. Some choices are:

1. Python httplib, urllib, or requests package
2. Selenium WebDriver 

If you use Python httplib, requests, or urllib, you don't need to actually
fetch the page -- that is slow and uses a lot of bandwidth.
For `urllib`, simply **open** a connection to the URL.  
If the URL is bad or unreachable it will raise an HTTPError. Check the error 
code in the HTTPError.  Any error code except 403 is a bad link.
Be sure to *close* the URL connection before returning from the function.

For any of the 3 libraries, send a HEAD request instead of GET request. 
HEAD requests only the response header without the page content, 
which is *much* faster and smaller. It may be faster even if you don't
actually read the response.

### 3. Function to test a list of URLs

Write a function named `invalid_urls(urllist: List)`
to test a list of urls (as Strings).

This function returns a new list containing only the invalid URLs.
If no invalid URLs, return an empty list. Don't modify the list parameter.

Obviously, you should use your `is_valid_url` for this.

### 4. Main Function: Scan a web page, print links, and bad links

Write a `__main__` block that accepts a URL as a command line
argument, gets the web page, and prints (a) all the links found
on the page, and then (b) all the bad links.

So, someone can type:

```
cmd> python3 link_scan.py  https://cpske.github.io/ISP/

http://git-school.github.io/visualizing-git/
https://asana.com/
https://cpske.github.io/ISP/ 
https://cpske.github.io/ISP/2019/ 
https://cpske.github.io/ISP/about.html 
https://cpske.github.io/ISP/agile/agile 
https://cpske.github.io/ISP/agile/scrum 
https://cpske.github.io/ISP/bad/index
https://cpske.github.io/ISP/assignment/ku-polls/ 

Bad Links:
https://cpske.github.io/ISP/bad/index 
```

to test all the links on the ISP home page and print the bad ones.

If no command line argument is given, print a usage message:

```
cmd> python3 link_scan.py
Usage:  python3 link_scan.py url

Test all hyperlinks on the given url.
```

Note that `sys.argv` contains all command line arguments and
`sys.argv[0]` is the name of the python file being invoked.
The other elements of `argv` are the command line arguments.

`sys.argv[0]` may include a path.
To get the name of the python file without the path, 
use `os.path.basename(sys.argv[0])`.

**Careful Programming**: this is not required, but what if the command
line argument (the URL to check) is not an HTML page?
Then it's useless to scan the page for hyperlinks using Selenium.

You cannot determine the content type just by examining the URL as a string,
but there any many other ways to determine the content type of a URL.
A careful program would print a message if the URL is not an HTML page.


## More Info

[My Intro to Selenium](/ISP/testing/Selenium-intro)

[My Intro to Page Scraping](/ISP/testing/Selenium-scraping)

[Selenium API Docs](https://selenium.dev/selenium/docs/api/py/), best for API reference

[ReadTheDocs for Selenium](https://selenium-python.readthedocs.io/api.html) unofficial docs, has API and also info about installing and using Selenium.

[Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html) in the Selenium docs.
in [Selenium Docs](https://selenium-python.readthedocs.io/locating-elements.html) (unofficial docs).
