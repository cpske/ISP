## Django TestCase

Django has its own TestCase class which you should usually use
instead of Python's `unittest.TestCase`. 
See the Django docs "Testing" section (under "Development Process" in online docs).

You can use Python's `unittest.TestCase` if your tests don't 
interact or change the database.  The Django TestCase uses
transactions and flushing the database, which makes it slower.

Django has 4 test classes:

* `django.test.SimpleTestCase`
* `django.test.TestCase` the usual superclass for your tests
* `django.test.LiveServerTestCase` like TestCase but also starts the Django web server before tests and stops it after tests.
* `django.test.TransactionTestCase` I'm not sure why you'd use this.

## Django Client (`django.test.Client`)

This class has functionality for retrieving a page, without using an HTTP server.  For example:

```python
import django.test.TestCase

class MyTest(django.test.TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertIn('<title>My Home Page</title>', html)

        # This only works if response is retrieved using self.client
        self.assertTemplateUsed(response, 'polls/home.html')
```



## Reference

This StackOverflow page has additional information about organizing tests:
[Organizing Django Unit Tests](https://stackoverflow.com/questions/5160688/organizing-django-unit-tests/20932450#20932450)

[Testing in Django - Part 1: Best Practices](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/) example using this test organization. Article also describes use of `coverage` for code coverage and Selenium for UI testing.
