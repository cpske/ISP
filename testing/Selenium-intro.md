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

Presentation: [Selenium Exercise](SeleniumExercise.pdf)

Here are the steps start a browser and display a web page using Firefox.
For this to work, Firefox needs to someone on your search PATH.
You can use another browser instead of Firefox, provided you have a webdriver.

### The Goal

We will write code to tell a browser to visit <https://duckduckgo.com> and search for "Kasetsart University". Then we will look for hyperlinks in the search results.

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
browser = webdriver.Chrome('/path/to/chromedriver')
browser.get( url )
```

> What is `browser`?    
> `type(browser)`
> 
> It is an instance of a subclass of selenium.webdriver.remote.webdriver.WebDriver

The page contains a search box (input field) with ID 
`search_form_input_homepage`.
>
> You can discover the element ID yourself by right-clicking on the search box and choosing Inspect in Firefox or Chrome.
>

Tell the browser to select this element:
```python
field_id = 'search_form_input_homepage'
input_field = browser.find_element_by_id(field_id)
# did it work?
assert input_field != None
```

Enter some text in the field and press RETURN to search:
```python
from selenium.webdriver.common.keys import Keys

# note: look at the browser window -- you can see the text
# appear in the search field after you call send_keys()
input_field.send_keys("Kasetsart University")
input_field.send_keys(Keys.RETURN)
```

## Searching Data on a Page

The next step is to get the search results, and
to get the URL for each search result.  WebDriver has
many `find_element_by` and `find_elements_by` methods.
- find by HTML tag
- find by class name
- find by CSS selector
- find by element id attribute
- find by XPath expression (quite powerful)

A simple but stupid technique is to look for all "a" tags.

```python
elements = driver.find_elements_by_tag_name("a")
len(elements)
```
too many!   
Try Right-Click -> Inspect on a search result to discover its structure.
You will see that the actual search result URLs have a class name of `result__url`.

Try:
```python
elements = driver.find_elements_by_class_name("result__url")
len(elements)
```

> `elements` is a list of selenium.webdriver.remote.webdriver.WebElement objects.    
> Your code will frequently use `WebElement` for testing things.

Print one URL from the results:
```python
url = elements[0].get_attribute('href')
print(url)
```

Simulate clicking on a hyperlink:
```python
elements[0].click()
```
go back:
```python
browser.back()
```
try another link:
```python
elements[1].click()
```

## Question About `WebElement` Methods

Why does `WebElement` have both `find_element_by_name` and `find_elements_by_name`, and `find_element_by_id` and `find_elements_by_id`?    

Isn't that redundant?

What could go wrong with this code?

```python
elements = driver.find_elements_by_class_name("result__url")

if len(elements) > 0:
    url = elements[0].get_attribute('href')
    browser.get(url)
```

## Selenium `find_element` Method and `By` Class

Selenium WebDriver has a general `find_element` method that can handle
all the above cases:
```python
from selenium.webdriver.common.by import By

# find a Login link
element = driver.find_element(By.LINK_TEXT, "Login")

# find an element with id 'login'
element = driver.find_element(By.ID, 'login')
```

[Locating Elements](https://selenium-python.readthedocs.io/locating-elements.html) in the Selenium docs has explanation and examples of using "By".


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

## Writing Unit Tests with Selenium

A good tutorial to get started is
[Test Automation using Selenium](https://blog.testproject.io/2019/07/16/set-your-test-automation-goals/) a good 8-part tutorial about automatic testing. Has explanations of the code.

The tutorial uses `pytest`, but you can do the same thing using `unittest`.

The [Safari WebDriver](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari) page also has examples of unit testing with Selenium.

To run your unit tests on a CI server, run the browser in [headless mode](#web-browser-in-headless-mode), which means no browser window is shown. Headless mode is much faster, too.


## Resources

[Test Automation using Selenium](https://blog.testproject.io/2019/07/16/set-your-test-automation-goals/) a good 8-part tutorial about automatic testing. Has explanations of the code.

[Getting Started](https://selenium-python.readthedocs.io/getting-started.html) in [selenium-python.readthedocs.io](https://selenium-python.readthedocs.io/) has good explanation and easy to read.

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



