## Navigate to a Web Page

driver.get("https://www.google.com")

## Find an element on the page

Suppose we want to find:
```
<input type="text" id="input_username" name="username" 
       placeholder="Type your name" />
```

We could use:

```
# find type id
element = driver.find_element_by_id("input_username")
# find by name
element = driver.find_element_by_name("username")
# XPath expression
# Careful! If expression matches multiple elements, only the first is returned.
element = driver.find_element_by_xpath("//input[@id='input_username']")
```

What if nothing matches?
* May throw `NoSuchElementException`.
* Possible to return `None`


## Don't Load Images (Make the Webdriver More Efficient)

For Firefox, use:
```
from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference('permissions.default.image', 2)
profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver = webdriver.Firefox(firefox_profile=firefox_profile)
```







## Reference

[Navigating](https://selenium-python.readthedocs.io/nagivating.html) in the [Selenium Python Docs][selenium-python-rtd]


[selenium-python-rtd]: https://selenium-python.readthedocs.io/index.html
