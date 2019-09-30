## Midterm Topics

In the programming part of the exam there will two parts:

1. add something to an existing Django project.  You will add 1 or 2 new urls, new views, and templates to show what is requested.  For *example*
    * a URL and view to display a list of choices with a link to perform an action on that choice. Just like the Polls app shows a list of poll questions  with links to vote on each poll.
    * a URL with dynamic part (e.g. `/polls/<int:question_id>/`) that passes the dynamic part (`question_id`) to a view.  Just like the url and view used to vote an a poll.

2. unit testing using Python unittest or Django unittest, using the standard assertions.   

## Suggested Study for Django (Programming Exam)

#### 1. Know the flow of request processing

When a browser sends a request to a server running
Django, what happens?

Django parses the request to create an HttpRequest object.

It looks for a "route" that matches the request URL; 
the "route" specifies what view should handle the request.

Django gives the request to a view.  
If the view contains annotations (Django calls them "decorators")
such as `@auth_required`, it performs those first.
A decorator may forbid calling the view function or
redirect to someplace else.

The view is responsible for converting the user's request
into something the application's services and models can
perform, and return an HttpResponse.
The view should invoke methods of other objects to perform
application logic, instead of doing everything itself.

> We haven't covered design, but a "best practice"
>  in using the MVC pattern is for a controller to 
>  delegate application logic to other objects, known as
>  "*fat models, skinny controllers*",
>  or sometimes "*skinny models, skinny controllers, fat services*".

If your view functions contain many lines of code
and logic, consider refactoring.

And more specifically...

#### 2. URL routing and views

Know how to define a route in `urls.py` and
a view function to handle it.  If the URL involves
a variable part, like `/store/product/3/` how
do you pass "3" (variable part) to the view function?
```
   path('product/<id:int>/', views.product_detail, name='detail')
```
unfortunately, Django requires the view parameter
name to exactly match the name in the url pattern.
So be careful in modifying views.

#### 3. Return Value from a View

What can a view return?  

A view should always return *some kind* of HttpResponse,
but there are many ways to do that and many subclasses.  
You should know how to use:

* render(request, 'template', context)
* HttpResponseNotFound("Oops. I can't find that page.")
* HttpResponseRedirect
* redirect('reference or path'[, param=value, param2=value2])

#### 4. How to Use Templates

Templates are HTML with placeholders and some programming
constructs.  Know how to use these:
{% raw %}
```html
{% extends base %}
{% block content %}  - block to insert into the "content" section of "base.html"
Conditional:
{% if condition %} 
    something
{% else %} 
    something else 
{% endif %}
Loops:
{% for x in product_list %}
<p> {{x.id}}  {{x.description}} </p>
{% endfor %}

How to use "url" in a link:
<a href="{% url 'polls:detail' 2 %}">Show Poll 2</a>
```
{% endraw %}

#### 5. Display data as a table

Know how to create an HTML table in a template
where each row of the table is one object in a collection.

Suppose your `store` app has a `Product` model like this:
```python
class Product(models.Model):
    upccode = models.CharField('UPC code',max_length=14)
    description = models.CharField('Description', max_length=60)
    price = models.DecimalField("Unit Price", 
            max_digits=9, decimal_places=2)

    def quantity_in_stock(self):
        """Compute and return number of units in stock"""
```

And a view creates a list of Products named `products`.
Can you write a template containing an HTML table to display the product data for each product in `products`? 

`Product` contains a method `quantity_in_stock`.  Can you invoke that method inside a template?  How?

| UPC Code   | Description       | Qnty in Stock | Unit Price |
|:-----------|:------------------|---------------|-----------:|
| 1012223333 | Sun dried banana  |    20         |   25.00    |
| 1013334444 | Brown Rice, 5kg   |    65         |  180.00    |
| etc.       | ...               |    ...        |  ...       |

**Practice**: Modify the Polls ugly "results" template to use a table.
Even better, sort the rows by number of votes for each choice (most to fewest).

#### 6. Django Unit Testing Classes

Know how to use `django.test.TestCase` and `django.test.Client`.

Django TestCase extends Python's `unittest.TestCase` so it has
all the methods of Python's TestCase plus many more than are
helpful for testing web apps.

For example:
```python
response = client.get('/polls/')
# should use the index.html template
assertTemplateUsed(response, 'polls/index.html' )
# should contain my poll question
assertInHTML("What's your favorite web framework?", response.content )
```

`django.test.Client` is useful to test routing and views.
It had methods like:
```python
response = client.get('/index/')
queryparams = {'name': 'bird'}
response = client.get('/person', queryparams)   # "/person?name=bird"
response.content
# prints body of the reply

response = client.post('/polls/1/vote/', {'choice_id': 3})
response.status_code
# prints 200 or 404
```

#### 7. App Can Have Other Classes and Services

An application can contain more than just Views (or controllers),
Models, and Templates.  

Your app may have objects for "factories", "services", "adapters", and a lot more 
to implement the logic of your application.  We have not
needed those so far in the polls app.

