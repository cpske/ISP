## Selenium

Selenium is a tool for *browser automation*.  You can programmatically
control what a web browser does.

It is often used for testing, but is also useful for other applications.

## Installation

Install Selenium For Python:
```
pip install selenium
```
You also need a **browser driver** for the web browser you want to automate.

[Install Web Browser drivers](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/) explains different ways to get drivers.

- Selenium Manager - automates everything
- [WebDriver Manager for Python](https://github.com/SergeyPirogov/webdriver_manager) code to automatically update your WebDriver, but requires you write extra Python code
- Download the driver yourself and **put it on your PATH**. (This is the original way.)

These instructions use the 3rd approach.

1. Download a browser driver.
   - [Firefox][GeckoDriver]: <https://github.com/mozilla/geckodriver/releases>
   - [Safari][SafariDriver]: already installed as `/usr/bin/safaridriver`. But visit the link for examples of how to use it.
   - [Chrome & Chromium][ChromeDriver]: <https://chromedriver.chromium.org/downloads>
   - Other browser: <https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#quick-reference>

2. Install it in a directory on your shell PATH.
   - For most users, `$HOME/bin` works.
   - Preferrably use a directory **without spaces in the path**.


[ChromeDriver]: https://sites.google.com/chromium.org/driver/
[EdgeDriver]: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
[GeckoDriver]: https://github.com/mozilla/geckodriver/releases
[SafariDriver]: https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari


## Getting Started

Presentation: [Selenium Exercise](SeleniumExercise.pdf)

Here are the steps start a browser and display a web page using Firefox.
For this to work, Firefox needs to someone on your search PATH.
You can use another browser instead of Firefox, provided you have a webdriver.

### The Goal

What are the Top 10 Web Pages for a search of "Kasetsart University"?

We will write code to tell a browser to visit <https://duckduckgo.com> and search for "Kasetsart University". Then we will look for hyperlinks in the search results.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# URL to fetch and display
url = "https://duckduckgo.com"

# create a browser instance. You can use Chrome or Safari instead of Firefox.
driver = webdriver.Firefox()
driver.get( url )
```

Or do the same thing using Chrome. The parameter (`/path/to/chromedriver`) is needed **only** if it is **not** on your shell search PATH.

```python
browser = webdriver.Chrome('/path/to/chromedriver')
browser.get( url )
```

The Duckduckgo home page contains a **search box** (input field) with ID 
`search_form_input_homepage`.
>
> You can discover the element ID yourself by right-clicking on the search box and choosing **Inspect** in Firefox or Chrome.
>

Tell the browser to select the element using its 'id' attribute:
```python
input_field = browser.find_element(By.ID, 'search_form_input_homepage')
# did it work?
assert input_field != None
```

Enter some text in the field and press RETURN to search:
```python
from selenium.webdriver.common.keys import Keys

# text appear in the search field when you call send_keys()
input_field.send_keys("Kasetsart University")
input_field.send_keys(Keys.RETURN)
```

## Searching Data on a Page

The next step is to get the search results, and
to get the URL for each search result.   

WebDriver has `find_element(by,value)` and `find_elements(by,value)` 
methods to find things on a page.  The `by` parameter can be:
- By.CLASS\_NAME (css class)
- By.ID
- By.LINK\_TEXT or By.PARTIAL\_LINK\_TEXT
- By.NAME
- By.TAG\_NAME

A simple technique is to look for all "a" tags.

```python
elements = browser.find_elements(By.TAG_NAME, "a")
len(elements)
117
```
Too many results!   

Instead, search for hyperlinks containing the text "Kasetsart":
```python
elements = browser.find_elements(By.PARTIAL_LINK_TEXT, "Kasetsart")
len(elements)
17
```

The values returned by `find_elements` are WebElement objects 
for parts of the web page's Document Object Model (DOM).
WebElements may contain:

- text
- attributes
- other WebElements

Print the value of `href` for the first result:
```python
>>> elements[0].get_attribute('href')
'https://duckduckgo.com/?q=Kasetsart%20University&t=h_'
```
this link refers to something on Duckduckgo itself, not what we want.

Try another:
```python
>>> elements[w].get_attribute('href')
'https://en.wikipedia.org/wiki/Kasetsart_University'
```

Simulate clicking on a hyperlink:
```python
elements[2].click()
```
it should show the Wikipedia page for KU.

Go back:

```python
browser.back()
```

## Question About `WebElement` Methods

Why does `WebElement` have both `find_element` and `find_elements` methods?

Isn't that redundant?




## Use Type Hints to Improve Coding with Selenium

Python **type hints** enable the IDE to offer better command
completion, syntax help, and automatic type checking.

In Selenium, the classes you interact with most often are WebElement
and WebDriver, plus the Python list class (for results).

```python
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

# add type hints to improve code completion in IDE

browser: WebDriver = webdriver.Firefox()

# you get a page
browser.get("https://www.google.com/search?q=Kasetsart+University")

# when you search for elements, you get a List of WebElements
elements: List[WebElement] = browser.find_element(By.TAG_NAME, "a")
```

## Writing Unit Tests with Selenium

A good tutorial to get started is
[Test Automation using Selenium](https://blog.testproject.io/2019/07/16/set-your-test-automation-goals/) a good 8-part tutorial about automatic testing. Has explanations of the code.

The tutorial uses `pytest`, but you can do the same thing using `unittest`.

The [Safari WebDriver](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari) page also has examples of unit testing with Selenium.

To run your unit tests on a CI server, run the browser in [headless mode](#web-browser-in-headless-mode), which means no browser window is shown. Headless mode is much faster, too.


## Resources

[Test Automation using Selenium](https://blog.testproject.io/2019/07/16/set-your-test-automation-goals/) a good 8-part tutorial about automatic testing. Has explanations of the code.

[Getting Started](https://selenium-python.readthedocs.io/getting-started.html) in [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/) how to install and start using Selenium.

[Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html) in the Selenium docs explains use of "By" with examples.

[Web Automation with Python and Selenium](https://realpython.com/modern-web-automation-with-python-and-selenium/) automate a browser to play music on bandcamp.com, article on RealPython.com.  

[Selenium Headless Browser Testing](https://www.toolsqa.com/selenium-webdriver/selenium-headless-browser-testing/) has a good explanation of how to
configure different browsers for headless mode. Examples use Java.

[Chrome Driver Getting Started](https://sites.google.com/a/chromium.org/chromedriver/getting-started).


## Selenium API Docs

* [Official API Docs](https://selenium.dev/selenium/docs/api/py/), best for API reference
* [ReadTheDocs Version](https://selenium-python.readthedocs.io/api.html) also has other info about installing and using Selenium

The two most important classes are `WebDriver` and `WebElement`:

* [selenium.webdriver.remote.webdriver.WebDriver][selenium.webdriver.remote.webdriver.WebDriver]
   - this is the class that the browser implements
   - provides `get(url)`, `back()`, `find_element_by_*(value)`, `quit()`, `save_screenshot()`, and more

* [selenium.webdriver.remote.webelement.WebElement][selenium.webdriver.remote.webelement.WebElement]
   - represents an element on a web page
   - this is how you interact with a web page 
   - WebElement is returned when you invoke `find_element_by_*(value)` or (in list) `find_elements_by_*(value)`

[selenium.webdriver.remote.webdriver.WebDriver]: https://selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html#module-selenium.webdriver.remote.webdriver
[selenium.webdriver.remote.webelement.WebElement]: https://selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html#module-selenium.webdriver.remote.webelement


## Web Browser in Headless Mode

A *headless* browser is one without a visible window as user interface.
It runs entirely without any UI.
Running a browser without the GUI interface makes it faster.
This is useful for testing, esp. on a CI server where you *must* 
run Selenium tests in headless mode.

To run Firefox in headless mode with Selenium, use:
```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

my_options = Options()
my_options.headless = True     # deprecated: options.set_headless()
# test that it worked
assert my_options.headless
# this should NOT show a browser window
browser = webdriver.Firefox(options=my_options)

# gets page, but nothing shown
browser.get("https://duckduckgo.com")
```
This also works for Chrome (change the import).

On Linux, if options.headless = True doesn't work, 
you can also set it as a command-line flag:

```python
my_options = Options()
my_options.add_argument("--headless")
...
```

## Running Chromedriver as a Service

If you use selenium in unit tests, the tests usually start a browser
before each test and stop it after each test, which uses a lot of time.
You can run Chrome as a service to reduce start-up time.
