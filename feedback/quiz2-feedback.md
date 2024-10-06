

```python
@login_required
def delete_vote(request, vote_id: int):
    """Delete the user's vote, if it exists."""
    this_user = request.user
    try:
        vote = Vote.objects.get(pk=vote_id)
    except Vote.DoesNotExist:
        # LOGIC-1
        messages.error(request, "You have no vote.")
        return redirect("polls:myvotes")
    if vote.user != this_user:
        # LOGIC-2
        messages.error(request, "You have no vote.")
    else:
        # LOGIC-3
        """did not check if voting is allowed"""
        # LOGIC-4
        messages.success(request,
                         f"Your vote for {vote.choice} has been removed.")
        vote.delete()
    return redirect("polls:myvotes")
```

## Logic Errors

The first two messages are incorrect, and the 3rd one may be incorrect.
All of the above messages are either incorrec

| Tag     | Explanation           |
|---------|:----------------------|
| LOGIC-1 | The user **may** have a vote, with a different `vote_id`. |
| LOGIC-2 | The user **may** have a vote, but he is not owner of **this** vote.| LOGIC-3 | Did not check if voting is allowed before deleting vote. |
| LOGIC-4 | What if `vote.delete()` raises exception, and user refreshes page? You should create the `success` message **after** deleting the vote.  |

## Duplicate Code

In each of the `if ... elif ... else ...` branches the code returns the same thing.

**Factor out common code** from the `if` block.

Code should be:
```python
@login_required
def delete_vote(request, vote_id: int):
    """Delete the user's vote, if it exists."""
    this_user = request.user
    try:
        vote = Vote.objects.get(pk=vote_id)
    except (Vote.DoesNotExist, ValueError):
        messages.error(request, "The requested vote does not exist or is invalid.")
        return redirect("polls:myvotes")

    if vote.user != this_user:
        messages.error(request, "Cannot delete another user's vote.")
    elif not vote.choice.question.can_vote():
        messages.error(request, "Voting is closed for that poll question.")
    else:
        try:
            vote.delete()
            messages.success(f"Your vote for {vote.choice.choice_text} was deleted.")
        except Exception as ex:
            logger = logging.get_logger(__name__)
            logger.error(f"Failed to delete vote {vote.id}. Exception {ex}")
            messages.error(f"Unable to delete vote {vote.id}")
    return redirect("polls:myvotes")
```
