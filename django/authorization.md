---
title: Django Authorization 
---

**Authorization** refers to the privileges that give a user (or subject)
the ability to perform some action.

In Django, you can authorize a request using any of there 3 criteria:

1. Logged in user: any logged in user is permitted 

2. Permissions: user is assigned specific permissions, assigned individually
   - Drawback: assigning permissions to each user is time-consuming and error-prone.

3. Group membership: users who are members of a specific group have all the permissions of that group

For example, in the Django Polls tutorial we allowed any
authenticated user to vote:
```python
@login_required
def vote(request, question_id):
    """user casts a vote for a choice in question_id"""
```

Django has **Groups** that you define in your app.
A User belongs to one or more Groups, and each group has Permissions 
associated with it.


## Checking Authentication in Code

The `HttpRequest` object passed to each view contains a `user` field.

To check if `user` is authenticated in a view: 
```python
def some_view(request, params):

    if request.user.is_authenticated:
        # logged in user
    else:
        # unauthenticated user
        messages.info("Please login to do that.")
        return redirect('login')
```

## Checking Authorization in Code

Permissions can be assigned to models, using a nested `Meta` class.
For example:
```python
class Question(Model):
    Meta:
        permissions = (('can_vote', 'can submit a vote'),
                       ('can_view_result', 'can review poll results'))
```
This defines two permissions `can_vote` and `can_view_result`.  
After defining permissions in a model you must create a migration and apply it.

To check permissions in a view function, use a decorator:
```python
@permission_required('polls.can_vote')
def vote(request, question_id):
    """Vote for a poll question"""
    ...
```

You can also check permissions inside a view method or function.

## Checking Authentication in Templates

Templates can access info about the current user using the `user` variable,
which is always defined even if no user is authenticated.

{% raw %}
```
{% if user.is_authenticated %}
    Hello, {% user.username %}
{% else %}
    Please <a href="{% url 'login'%}?next={{request.path}}">login</a>.
{% endif %}
```
{% endraw %}

## Checking Authorization in Templates

Templates can access the pre-defined `perms` variables.

If we had a `can_vote` permission defined, we could check that the
current user has this permission using:

{% raw %}
```
{% if perms.polls.can_vote %}
   {# allow user to vote #}
{% endif %}
```
{% endraw %}
