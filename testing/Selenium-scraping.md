## Navigate to a Web Page

driver.get("https://www.google.com")

## Find an element on the page

Suppose we want to find:
```
<input type="text" id="input_username" name="username" 
       placeholder="Type your name" />
```

We can use:

```
# find type id
element = driver.find_element_by_id("input_username")
# or find it by name
element = driver.find_element_by_name("username")
# find by tag name
input_tag = driver.find_element_by_tag_name("input")
# XPath expression
# Careful! If expression matches multiple elements, only the first is returned.
element = driver.find_element_by_xpath("//input[@id='input_username']")
```

What if nothing matches?

* Most methods throw `selenium.common.exceptions.NoSuchElementException`
* Some methods may return `None` or empty List

### Finding Many Matches

The `find_element_by_*` methods have a `find_elements_by_*` that
returns a list of all matches.

### WebElement May Contain Other Web Elements

Each WebElement represents a part of the DOM tree.
It may contain other WebElements.

```python
# element is a WebElement containing the entire <table>...</table> tree
element = browser.find_element_by_tag_name("table")

# now get the rows in the table
rows = element.find_elements_by_tag_name("tr")

# inside of each row, find the columns
for row_element in rows:
   columns = row_element.find_elements_by_tag_name("td")
   # each column is also a WebEelement
   # Get the text in each <td>...</td>
   for column_element in columns:
       print(column_element.text)
```

### Getting the Text

What if you want the text on a hyperlink?

```
element = browser.find_element_by_tag_name("a")
# get the hyperlink url (may throw NoSuchElementException)
url = element.get_attribure("href")
# get the text inside <a>...</a>
text - element.text
```

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

* [Navigating](https://selenium-python.readthedocs.io/nagivating.html) in the [Selenium Python Docs][selenium-python-rtd]

* [Official Python API Docs](https://selenium.dev/selenium/docs/api/py/), best for API reference

* [ReadTheDocs Version](https://selenium-python.readthedocs.io/api.html) also has other info about installing and using Selenium


[selenium-python-rtd]: https://selenium-python.readthedocs.io/index.html
