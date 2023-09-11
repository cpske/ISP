## Django Messages Framework

* When a user clicks a "Save" button your app saves something
then returns to the current page.   
How does user know that "save" succeeded?

* User submits a vote but the app was unable to save his vote.    
  How do you inform the user of this?

The Django Messages Framework addresses these situations and more.

"messages" is an object that is automatically included in the
context to every HTML template.  You can set messages in a view
(see example below) so the template can display them.
You don't need to add messages to the context yourself!

Messages are cleared after a response is successfully returned,
so the next request will have a clean, empty messages object.

## Configuration

The default `settings.py` contains all the required messages components.
They are:

* **INSTALLED_APPS** includes `django.contrib.messages`

* **MIDDLEWARE** includes
    - `django.contrib.sessions.middleware.SessionMiddleware`
    - `django.contrib.messages.middleware.MessageMiddleware`

* **TEMPLATES** in the `context_processors` list include:
    - `django.contrib.messages.context_processors.messages`



## Using Messages

Messages usually originate from a view.  A view wants to notify the user
of some event or problem, e.g. "Your vote was recorded"
or "Sorry, that's not a valid choice".

Here's an example:

```python
from django.contrib import messages

def vote_for_poll(request, question_id):
    choice_id = request.POST['choice']
    if not choice_id:
        messages.error(request, f"You didn't make a choice")
        return redirect('polls:someplace')
    # TODO: Record the vote (choice)
    messages.success(request, "Your choice successfully recorded. Thank you.")
    return redirect('polls:results')
```

Messages is a collection; each message has its own level and CSS tags. If there are no messages to display then `if messages` is `False`.

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

By default, Django will only display messages of level 20 or higher.    
To change the threshold value, in `settings.py` write: 
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

The `django.contrib.messages` module includes these methods:

| `messages` method |
|-------------------|
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

### Messages Don't Require Context Variables

Another way to inject a message into a template is to use 
a [context argument][django-shortcuts], such as this view code:

```python
   q = Question.objects.get(...)
   context = {'question': q, 'message': "Here's your question!"}
   return render(request, 'polls/detail.html', context)
```

The Django messages framework is a more complete solution and easier to use.

Since Django uses the name `messages` for its messages object,
you should avoid the name `messages` for your own context variables.

### Messages in Forms

For errors in Form fields, forms have another way of setting and displaying error messages.
Each form field has an `errors` attribute.
For example, if you have a form with two fields `name` and `email`,
then you can display error messages in a template
using `form.name.errors` and `form.email.errors`.

The Django [Working with Forms][django-forms] page has explanation and examples.


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
