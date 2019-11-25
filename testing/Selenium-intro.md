## Selenium

Selenium is a tool for *browser automation*.  You can programmatically
control what the browser does.

It is often used for testing, but can also be used for other applications.

## Installation

For Python, use:
```
pip install selenium
```
You also need a driver for each browser you want to automate.
Drivers for different browsers are available at these links.
* [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* [Firefox](https://github.com/mozilla/geckodriver/releases) also called "geckodriver"
* [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

## Getting Started

Here's how to start a browser and display a web page, using Firefox as example.
```python
from selenium import webdriver

# URL to fetch and display
url = "https://thehackernews.com"

# create a browser instance
driver = webdriver.Firefox()
driver.get( url )
```
For this to work, Firefox needs to someone on your search PATH.

To do the same thing using Chrome:
```python
from selenium import webdriver

# URL to fetch and display
url = "https://thehackernews.com"

# create a browser instance
driver = webdriver.Chrome('/path/to/chromedriver')
driver.get( url )
```
You can omit `/path/to/chromedriver` if it is on your search PATH.


## Resources

[Test Automation using Selenium](https://blog.testproject.io/2019/07/16/set-your-test-automation-goals/) a good 7-part tutorial about automatic testing. Has explanations of the code.

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

## Running Chromedriver as a Service

If you use selenium in unit tests, the tests usually start a browser
before each test and stop it after each test, which uses a lot of time.
You can run Chrome as a service to reduce start-up time.

See [Chrome Driver Getting Started](https://sites.google.com/a/chromium.org/chromedriver/getting-started).

[selenium.webdriver.remote.webdriver.WebDriver]: https://selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html#module-selenium.webdriver.remote.webdriver
[selenium.webdriver.remote.webelement.WebElement]: https://selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html#module-selenium.webdriver.remote.webelement

