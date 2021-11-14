## Selenium

Selenium is a tool for *browser automation*.  You can programmatically
control what the browser does.

It is often used for testing, but can also be used for other applications.

## Installation

For Python, use:
```
pip install selenium
```
You also need a **web driver** for each browser you want to automate.
Drivers for different browsers are available at these links.
* [Chrome](https://sites.google.com/chromium.org/driver/)
* [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* [Firefox](https://github.com/mozilla/geckodriver/releases) also called "geckodriver". 
* [Safari](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari)
  - MacOS includes Safari webdriver at `/usr/bin/safaridriver`, no need to install anything
  - web page has example Python unittest code for Selenium webdriver with Safari


## Getting Started

Here's how to start a browser and display a web page using Firefox.
For this to work, Firefox needs to someone on your search PATH.
You can use another browser instead of "Firefox", provided you have a webdriver.

### The Goal

We will use code to tell a browser to visit <https://duckduckgo.com> and search for "Kasertsart University". Then we will look for hyperlinks in the search results.

```python
from selenium import webdriver

# URL to fetch and display
url = "https://duckduckgo.com"

# create a browser instance. You can use Chrome or Safari instead of Firefox.
driver = webdriver.Firefox()
driver.get( url )
```

Or do the same thing using Chrome. The parameter (`chromedriver`) is needed **only** if it is not on your shell search path.

```python
driver = webdriver.Chrome('/path/to/chromedriver')
driver.get( url )
```

The page contains a search box (input field) with ID 
`search_form_input_homepage`.
>
> You can discover the element ID yourself by right-clicking on the search box and choosing Inspect in Firefox or Chrome.
>

Tell the browser to select this element:
```python
field_id = 'search_form_input_homepage'
input_field = browser.find_element_by_id(field_id)
```

Enter some text in the field and press RETURN to search:
```python
from selenium.webdriver.common.keys import Keys

input_field.send_keys(search_phrase)
input_field.send_keys(Keys.RETURN)
```

## Searching Data on a Page

The next step is to get the search results, and
to get the URL for each search result.  There are
many "`find_element_by`" methods in WebDriver to do this.



## Use Type Hints to Improve Coding with Selenium

Use Python **type hints** to enable the IDE to offer better command
completion, syntax help, and automatic type checking.
It will help you code faster and reduce defects.

In Selenium, the classes you interact with most often are WebElement
and WebDriver, plus the Python list class (for results).

```python
from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

# somewhere in code you create a web browser
# it will be a subclass of selenium.webdriver.remote.webdriver.WebDriver

browser: WebDriver = webdriver.Firefox()

# you get a page
browser.get("https://www.google.com/search?q=Kasetsart+University")

# when you search for elements, you get a List of WebElements
elements: List[WebElement] = browser.find_element_by_tag_name("a")

```

For example, after you get a page, how can your search it?
If you type `browser.find` (and maybe Ctrl+SPACE) your IDE will display all the "find" methods along with the parameters they accept.


## Resources

[Test Automation using Selenium](https://blog.testproject.io/2019/07/16/set-your-test-automation-goals/) a good 8-part tutorial about automatic testing. Has explanations of the code.

[Getting Started](https://selenium-python.readthedocs.io/getting-started.html) in [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/) has good explanation and easy to read.

[Web Automation with Python and Selenium](https://realpython.com/modern-web-automation-with-python-and-selenium/) automate a browser to play music on bandcamp.com, article on RealPython.com.  
Another good example of using selenium.  Shows how to run browser in headless mode.

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


## Running Firefox in Headless Mode

A *headless* browser is one without a visible window as user interface.
It runs entirely without any UI.

To run Firefox in headless mode with Selenium, use:
```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

my_options = Options()
my_options.set_headless()
# test that it worked
assert my_options.headless
browser = webdriver.Firefox(options=my_options)
browser.get("https://duckduckgo.com")
```

On my Linux system, the `set_headless()` option had no effect.
What does work is to add a Firefox command line flag:

```python
my_options = Options()
my_options.add_argument("--headless")
...
```

## Running Chromedriver as a Service

If you use selenium in unit tests, the tests usually start a browser
before each test and stop it after each test, which uses a lot of time.
You can run Chrome as a service to reduce start-up time.

See [Chrome Driver Getting Started](https://sites.google.com/a/chromium.org/chromedriver/getting-started).

## Using a Headless Browser

Running a browser without the GUI interface makes it faster.
This is useful for testing, esp. on a CI server where you *must* 
run Selenium tests in headless mode.

Firefox and Chrome can be used in headless mode.
For Java, there is a HmtlUnitDriver that also runs in headless mode.

[Selenium Headless Browser Testing](https://www.toolsqa.com/selenium-webdriver/selenium-headless-browser-testing/) has a good explanation of how to
configure different browsers for headless mode. Examples use Java.

[selenium.webdriver.remote.webdriver.WebDriver]: https://selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html#module-selenium.webdriver.remote.webdriver
[selenium.webdriver.remote.webelement.WebElement]: https://selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html#module-selenium.webdriver.remote.webelement

