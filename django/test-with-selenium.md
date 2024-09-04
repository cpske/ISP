---
title: Django Testing with Selenium
---

See <https://docs.djangoproject.com/en/stable/topics/testing/tools/#django.test.LiveServerTestCase>

Django has a `LiveServerTestCase` and `StaticLiveServerTestCase` that are subclasses of TestCase.

Some useful code for Selenium tests:

- `self.live_server_url` (inside a test method) is the base URL of the server
