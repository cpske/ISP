---
title: Django Authorization 
---

Django uses **Permissions** assigned to each **User** to determine
their access rights to model objects.

Instead of assigning permissions directly to each user (time-consuming
and error-prone), Django uses **Groups**.
A User belongs to one or more Groups.
Each Group has Permissions associated with it.

### How to Perform Authorization

Authorization refers to the privileges that a user has.
In Django, there are 3 choices to enforce authorization.

1. Logged in user: any logged in user is permitted 
2. Group membership: users who are members of a specific group are permitted
3. Permissions: users assigned a specific permission are permitted

For example, in the Django Polls tutorial we allowed any
authenticated user to vote:
```python
@login_required
def vote(request, question_id):
    """user casts a vote for a choice in question_id"""
```

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
This defines two permissions.  After defining permissions in a model
you must create a migration and apply it.

To check permissions in a view function, use a decorator:
```python
@permission_required('polls.can_vote')
def vote(request, question_id):
    """Vote for a poll question"""
    ...
```

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
