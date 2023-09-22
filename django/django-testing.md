## Testing Django Applications
 

## Django TestCase

Django has 4 TestCase classes which you should usually use
instead of Python's `unittest.TestCase`.
The Django TestCase classes are *subclasses* of unittest.TestCase.
 
See the Django docs "Testing" section (under "Development Process" in online docs).

Django has these test classes:

* `django.test.SimpleTestCase`
* `django.test.TestCase` the usual superclass for your tests
* `django.test.LiveServerTestCase` like TestCase but also starts the Django web server before tests and stops it after tests.
* `django.test.TransactionTestCase` I'm not sure why you'd use this.

You can use Python's `unittest.TestCase` if your tests don't 
interact or change the database.  The Django TestCase uses
transactions and flushing the database, which makes it slower.

## Testing Models

Use django.test.TestCase and create model objects in the usual way:
```python
import django.test.TestCase

class ModelTest(django.test.TestCase):
    def setUp(self):
        # superclass setUp() reinitializes database, self.client
        super().setUp()
        # create a poll
        poll = Question(question_text="First Poll", ...)
        poll.save()
        self.poll_id = poll.id
        choice1 = Choice(choice_text="Choice 1", question=poll)
        choice2 = Choice(choice_text="Choice 2", question=poll)
        choice1.save()
        choice2.save()
        self.poll = poll

    def test_question_choices(self):
        q = Question.objects.get(id=self.poll_id)
        self.assertEqual(2, q.choice_set.all().count())

    def test_choice_has_no_votes(self):
        for choice in self.poll.choice_set.all():
            assertEqual(0, choice.votes)

    def test_can_vote_for_choice(self):
        choice = self.poll.choice_set.first()
        choice.votes = 999
        choice.save()
        # get choice from database again
        rechoice = Choice.objects.get(id=choice.id)
        self.assertEqual(rechoice.id, choice.id)
        self.assertEqual(999, rechoice.votes)
```
This demonstrates how to write tests, but these are poor tests.
They test only the persistence feature of the Django framework,
not the logic of your models.


## Testing Views with Django Client

`django.test.Client` can simulate sending web requests (GET and POST) and return the HttpResponse, without using an HTTP server. 

Use `client` to submit GET and POST requests, test responses, header fields, and more.

For example:

```python
import django.test
from django.urls import reverse

class MyTest(django.test.TestCase):
    def setUp(self):
        super().setUp()
        self.client = django.test.Client()

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
        html = response.content.decode('utf8')
        self.assertIn('<title>My Home Page</title>', html)

        # This only works if response is retrieved using self.client
        self.assertTemplateUsed(response, 'polls/home.html')

    def test_vote_for_poll(self):
        poll = Question.objects.first()
        choice = poll.choice_set.first()
        # Build the URL to submit a vote for a question (poll)
        url = reverse('polls:vote', args=[poll.id])
        resp = self.client.post(url, data={"choice_id":choice.id})
        # what should be returned? 200? redirect?
        self.assertEqual(200, resp.status_code)
```

## Testing Templates

You can use django.test.Client to test the template used and query body contents.

To fully test the UI, use another tool such as Selenium.

## Useful django.test.TestCase Methods

| Method                        | Meaning                          |
|-------------------------------|----------------------------------|
| assertRedirects(response,url) | HttpResponse is a redirect       |
| assertTemplateUsed(response, template) | test a templates was used      |
| assertContains(response,text) | response contains some text      |

## Useful django.test.Client Methods

- `response = client.get(path)`
- `response = client.post(path, data={"var1": value1, ...})`

## Reference

This StackOverflow page has good information about organizing tests:
[Organizing Django Unit Tests](https://stackoverflow.com/questions/5160688/organizing-django-unit-tests/20932450#20932450)

[Testing in Django - Part 1: Best Practices](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/) example using this test organization. Article also describes use of `coverage` for code coverage and Selenium for UI testing.
