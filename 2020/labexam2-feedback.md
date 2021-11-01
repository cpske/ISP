---
title: Feedback on Django Tests
---

## Problem 1. If you create a new Todo and save it, the Todo appears on the todo index page.

### What Do You Need to Know?

- how to create a Todo and save to the database?

- how to send a request to Django and get the response?

- how to test if the Todo is shown on index page?

### What you know from KU Polls

- Create a Todo:
  ```python
  todo = Todo(description="Just do it!", done=False)
  todo.save()

  # Django convenience method does both at once
  todo = Todo.objects.create(description="Just do it!", done=False)
  ```

- Send a request using the `django.test.Client` class.
  ```python
  client = Client()
  response = client.get('/todo/')

  # Better: TestCase object has a client attribute:
  response = self.client.get('/todo/')
  ```

- How to test the response?    **Answer:** Read the django.test API.
  > I recommended (many times) everyone **install the docs on their own computer** and **bookmark** important pages.   
  > It will save you time.

  ```python
  # From the Django docs "Testing Tools" page
  self.assertContains(response, text)
  self.assertNotContains(response, text)
  self.assertRedirects(response, url)

  # this is better than just comparing urls as strings:
  self.assertURLEqual(url1, url2)
  ```

- For problem 1:
  ```python
  self.assertContains(response, todo.description)
  ``` 

## Problem 2. If you create and save a new todo, then invoke the URL `/todo/id/done/` (using the todo's id), then verify that 2 things occur: 
 - (a) todo.done is `True`
 - (b) the todo is **not** on the index page

### What Do You Need to Know?

- How to get the id of a Todo object?
- How to create a URL containing data value (todo id)?
- How to ensure the todo's data is in sync with data in database?

Item (b) has two solutions:
```python
# the basic way:
url = f"/todo/{todo.id}/done/"
# using django reverse:
url = reverse("todo:done", args=(todo.id,))
```

Ensure a todo object is in sync with the database:
```python
# the simple way - go get it again
todo = Todo.objects.get(id=todo.id)

# use built-in method:
todo.refresh_from_db()
```

```python
todo_text = "Study refactoring"
todo = Todo.objects.create(description=todo_text)
# it should be shown on index
response = self.client.get('/todo/') 
self.assertContains(response, todo_text)
# mark it as done
self.client.get(reverse('todo:done', args=(todo.id,)))
# did the todo status change?
todo.refresh_from_db()  
self.assertTrue(todo.done)
# is it on the index page?
response = self.client.get(reverse('todo:index'))
self.assertNotContains(response, todo_text)
```

## Brittle Code

"Brittle code" means code that it is easy to break by changing other parts of the code.

```python
todo = Todo.objects.create(description="Just do it")
resp = self.client.get('/todo/')
self.assertQuerySetEqual(resp.context['todo_list'],
                    ['<Todo: Just do it>'])
```
This test is brittle because:

1. Assumes the context variable name is `todo_list`. 
2. Assumes `todo.__str__` returns only `self.description`.

More robust (not brittle):

```python
self.assertContains(resp, "Just do it")
```

## Common Mistakes

1. Not Using Python Naming Convention:
   ```python
   def test_Save_Todo(self)
   ```
2. Not leaving blank line(s) between methods:
   ```
   def create_todo(text):
       return Todo.objects.create(description=text, done=False)
   class TodoTest(django.test.TestCase):
       ...
	```
3. Explicitly setting the Todo id. The ORM does this when you save a todo.
   ```
   todo = Todo(5, description="Just do it")
   ```
4. Not using named parameter for description. The first **positional parameter** is the `id`.    
   This will **fail** when you save the Todo.
   ```python
   todo = Todo("Do something")  # should be Todo(description="...")
   ```
5. Ignoring result of an operation:
   ```python
   response = self.client.get('/todo/')
   response.content.decode('utf-8')   # does NOT change content
   self.assertContains(response.content, "something")
   ```
   Second statement does **not modify** `response.content`.  Just like:
   ```python
   s = "I AM IMMUTABLE"
   s.to_lower()    # does not change the string
   ```
6. `reverse` does NOT send a request:
   ```python
   todo = Todo(...)
   reverse('todo:done', args=(todo,id,))   # does NOTHING
   self.assertTrue(todo.done)
   ```
7. Forgot to use a tuple for args in `reverse`. 
   ```python
   url = reverse('todo:done', args=todo.id)
   ```
   Django prints an error telling you what is wrong.


## How I Tested

1. Run the tests. They should all **pass**. Definitely no **Errors.**
2. Inspect the test code for test correctness.:
3. Almost no partial credit -- test is correct or not correct.
   * Test 3: Test that /todo/id/done/ redirects to index.    
    -2 points if only test the `status_code`.
