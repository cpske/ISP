## Django Messages Framework

* When a user clicks the "Save" button your app saves something
then returns to the current page.   
  > How does the user know that "save" succeeded?

* User submits a vote but the app was unable to save his vote.    
  > How do you inform the user that his vote *was not* recorded?

The Django Messages Framework addresses these situations and more.

`messages` is an object that is automatically part of the
context to every HTML template.  You set messages in a view
(see example below) and a template can retrieve and display them.
You don't need to add messages to the context yourself!

Messages are cleared after a response is successfully returned,
so the next request will have a clean, empty messages object.

## Configuration to Use Messages

The default `settings.py` contains all the required messages components.
They are:

* **INSTALLED_APPS** includes `django.contrib.messages`

* **MIDDLEWARE** includes
    - `django.contrib.sessions.middleware.SessionMiddleware`
    - `django.contrib.messages.middleware.MessageMiddleware`

* **TEMPLATES** the `context_processors` list includes:
    - `django.contrib.messages.context_processors.messages`


## Using Messages in a View

Messages usually originate in a view.  A view wants to notify the user
of some event or problem, e.g. "Your vote was recorded"
or "Sorry, that's not a valid choice".

Example:

```python
from django.contrib import messages

def vote_for_poll(request, question_id):
    choice_id = request.POST['choice']
    if not choice_id:
        # no choice_id was set
        messages.error(request, f"You didn't make a choice")
        return redirect('polls:detail', question_id)
    # TODO: Record the vote (choice)
    messages.success(request, "Your choice was successfully recorded.")
    return redirect('polls:results')
```
### Using Messages in a Template

Messages is a collection; each message has its own level and CSS tags. 
If there are no messages to display then `if messages` is `False`.

To display messages in an html template, use code such as:

{% raw %}
```html
{% if messages %}
<ul class="messages">
  {% for msg in messages %}
    <li class="{{msg.tags}}">{{ msg }}</li>
  {% endfor %}
</ul>
{% endif %}
```
{% endraw %}


## Django Message Levels and CSS Tags

Message levels control which messages are displayed and their appearance.
The levels are quite similar to Logging levels.
The higher the level, the more important the messages are:

| Level Name | Value  | CSS Tag  | Purpose                            |
|------------|--------|----------|:-----------------------------------|
| DEBUG      | 10     | debug    | Messages for development purposes. |
| INFO       | 20     | info     | Informational messages for user.   |
| SUCCESS    | 25     | success  | Indicate an action was successful. |
| WARNING    | 30     | warning  | Something unusual or unexpected, but not a failure. |
| ERROR      | 40     | error    | An error or failure occurred.      |


## Message Severity

By default, Django only displays messages of level 20 or higher.    

The idea is that normally you want to show a user only messages that are
useful to him/her.

To change the threshold value for messages, in `settings.py` write: 
```python
   MESSAGE_LEVEL = 10    # show debug messages and higher
```
You can also set the messages threshold level in code:
```python
from django.contrib  import messages
messages.set_level( request, messages.DEBUG )

# or, reset it to the default
messages.set_level( request, None )
```

### Methods for Setting Messages

Use these methods in your views to set a message.

| `django.contrib.messages` method |
|----------------------------------|
| `messages.debug`(request, "Message text") |
| `messages.info`(request, "Message text") |
| `messages.success`(request, "Message text") |
| `messages.warning`(request, "Message text") |
| `messages.error`(request, "Message text") |
| `messages.add_message`(request, level: int, "Message text") |

You can define your own message severity:

```python
CRITICAL = 50
messages.add_message(request, CRITICAL, "Database error occurred.")
```
All methods accept an `extra_tags` parameter to add additional CSS tags:
```python
messages.info(request, "Your vote was recorded", extra_tags='alert')
```
---


### Messages in Forms

For errors in Form fields, forms have another way of setting and displaying error messages.
Each form field has an `errors` attribute.
For example, if you have a form with two fields `name` and `email`,
then you can display error messages in a template
using `form.name.errors` and `form.email.errors`.

The Django [Working with Forms][django-forms] page has explanation and examples.

### How to Get All Messages

This is useful for unit tests to verify a message was set:
```python
from django.contrib import messages

response = client.post(url, post_data)
request  = response.request

storage = messages.get_messages(request)
for message in storage:
    # todo check the message
```

### Using Messages with Bootstrap

[Django Tips: Using the Messages Framework][django-tips-messages] (bottom of page) shows how to use Bootstrap styles with messages.


### Limitation: Messages in Shared Browsing Context (old browsers only)

If one client submits multiple, overlapping requests (such as using
several tabs for the same session) in the same *browsing context*,
then Django does not guarantee the messages will be delivered 
to the correct window (response).
The [Django Messages Framework][messages-framework] has more explanation.

The [documentation][messages-framework] states that:

> ...this will become a non-issue in HTML5,
> where each window/tab will have its own browsing context.

All major browsers are now HTML5 compliant, so you can probably
ignore this.

---
### References

* [Django Messages Framework][messages-framework]
* [Django Tips: Using the messages framework][django-tips-messages], first part is same as the Django Messages docs.
* [Working with forms][django-forms] in the Django docs
* Other web frameworks also have "messages".  In Play Framework they are called
*flash messages*.

[django-tips-messages]: https://simpleisbetterthancomplex.com/tips/2016/09/06/django-tip-14-messages-framework.html, "Django Tips 14 Using the Messages Framework"
[django-forms]: https://docs.djangoproject.com/en/2.2/topics/forms/
[django-shortcuts]: https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/
[messages-framework]: https://docs.djangoproject.com/en/2.2/ref/contrib/messages/
