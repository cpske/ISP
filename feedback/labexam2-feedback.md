---
title: Feedback on Django Tests
---


Test 3: Test that /todo/id/done/ redirects to index.
   -5 points if only test the `status_code`.


## Common Weaknesses in Code

```python
todo = Todo.objects.create(description="Just do it")
resp = self.client.get('/todo/')
self.assertQuerySetEqual(resp.context['todo_list'],
                    ['<Todo: Just do it>'])
```
1. Assumes context variable `todo_list`.
2. Requires `todo__str__` return `<Todo: {description}>`.

These are **brittle** (easy to break when software changes).
Better
```python
self.assertContains(resp, "Just do it")
```

Not Using Python Naming Convention:
```python
def test_Save_Todo(self)
```

You should not set the Todo id. The ORM does that:
```


## How I Tested

1. Run the tests. They should all pass. Definitely no Errors.
2. Inspect the test code.


