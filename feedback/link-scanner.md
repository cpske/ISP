---
title: Feedback on Link Scanner
---

How I graded:

I ran the link scanner with a local version of the ISP github.io site as URL.
The page includes a few special links including:
* "a" tag without an "href" attribute
* "a" tag where the "href" is only a page fragment (`href=#breakfast`), which is legal and common
* "href" where the hostname cannot be resolved, e.g. misspelled hostname
* "href" with an invalid path part, e.g. https://ku.ac.th/does/not/exist

I deducted points for each the errors listed below and anything else that
caused an exception to be raised. 
Each time the app failed with exception I fixed the error and ran it again.

If more than 3 errors, the score is zero.

Common mistakes were:

1. (**E1**, -1 pt) Using `urllib.get` or `requests.get` to test each link:
   ```python
   response = requests.get(url)
   ``` 
   This wastes too much bandwidth for a link scan.
   If the url is a 20MB PDF file, "get" will download the whole file just to test the link.  The assignment instructions **explicitly stated** you should use "head" instead of get:
   ```python
   response = requests.head(url)
   ``` 

2. (**E2**, -2 pt) Hard-coding a path to the chromedriver or firefox driver on your computer:
   ```python
   browser = webdriver.Chrome("C:/Users/ihatecoding/Downloads/chromedriver.exe")
   ```
   This will fail (**obviously**) on anyone else's computer.    
   The correct solution is to put chromedriver.exe is a directory on your **path** and then write:
   ```python
   browser = webdriver.Chrome() # finds chromedriver on the path
   ```
3. (**E3**, -1 pt each place in code that throws exception) Not catching all exceptions.  If the hostname in the URL cannot be resolved, many codes throw exception due to overly specific "except" block.

4. (**E3**, -1 pt, throws exception) Not checking for "a" tags without "href" attribute.
   ```python
   for element in elements:
       url = element.get_attribute("href")
       if "#" in url:
           url = url[0: url.find("#")]
       elif "?" in url:
           url = url[0: url.find("?")]
       if 'http' in url:
           href_list.append(href)
   ```
   throws `TypeError: argument of type "NoneType" is not iterable`.     
   You can't write `if foo in url` in case that the `url` is None.

5. (**E3**, -1 pt, throws exception) Not checking the case where URL contains only a page frag, such as:    
   ``<a href="#section-two">See section two</a>``
   After the code removes the page fragment, the url is empty so when the code calls `is_valid_url`, it fails.

6. (**E4**, No penalty) Using global variables for browser or browser options.

### Using Global Variables

You should avoid using global variables. Only two people used globals.

```python
from selenium import webdriver
import requests, sys

driver = webdriver.Chrome()

def get_links(url):
    driver.get(url)
```

Either create the driver instance inside `get_links` or write
a separate function to do that.  Either way, there is no reason
for the browser to be a global variable.

If you specify driver options, 
then a separate function is a good way to isolate the code:

```python
def create_browser():
    """Initialize a headless browser"""
    options = Options()
    options.headless = True
    return webdriver.Firefox(options=options)

def get_links():
    browser = create_browser()
```

### Using IndexError instead of testing arg count in main

It is better to test a condition using "if" than
to catch an exception.  It is faster, too.

```python
def main():
    try:
        all_links = get_links(sys.argv[1])
    except IndexError:
        print(f"Usage: python3 {os.path.basename(sys.argv[0])} url")
        print()
        print("Test all hyperlinks on the given url.")
```

Better:

```python
def usage():
     """Print a help message and exit."""
     print(f"Usage: python3 {os.path.basename(sys.argv[0])} url")
     print("\nTest all hyperlinks on the given url.")
     sys.exit(1)

def main():
    if len(sys.argv) != 2:
       usage()
    all_links = get_links(sys.argv[1])
    ...
```

### Unnecessary Manual Checks of URL syntax

You should not try to manually validate the URL systax.
Let the url package (urllib or requests) do that.

NO (what if the protocol is written "HTTP"?)
```python
if "http" in url:
    # accept this url
    ...
```

NO 
```python
SYMBOL = "://"
if SYMBOL in url:
    # accept this url
```
 

## Not using the Python API

Code to clean the URL, the hard way:

```python
new_url = ""
for i in url:
     if i=='#' or i=='?':
         break
     new_url += i
```

this creates a lot of strings (or worse!).

A few simpler ways used by students:

```python
if '#' in url:
    url = url[:url.index('#')]
# use "if" not "elif" here:
if '?' in url:
    url = url[:url.index('?')]
```

or
```python3
url = url.split('#',1)[0]
url = url.split('?',1)[0]
```
