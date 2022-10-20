### Did not add Vote class to `main` or `master`

- Chinapat
- Kittiporn
- 

## Bad Or Unneeded Code is Clear Sign of COPYING

1. Redundant save (`create` already saves object in database):
   ```python
   Vote.objects.create(...).save()
   ```
2. Duplicate test. `@login_required` implies `user.is_authenticated == True`.
   ```python
   @login_required
   def vote(request, question_id):
       user = request.user
       if not user.is_authenticated:   <--- test ALWAYS fails
           return redirect('login')    <--- forgot to add next to context
    ```
3. Unnessary `else` after `except`.

## Other Signs
1. Identical comments (my comments).


### Danita

```python
def vote(request, question_id):
    """Vote for a choice on a question (poll)."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        user = request.user
        if not user.is_authenticated:
            return redirect('login')
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            voted = Vote.objects.get(user=user, choice__question=question)
            voted.choice = selected_choice
            voted.save()
        except Vote.DoesNotExist:
            Vote.objects.create(user=user, choice=selected_choice).save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```


### Kodchakan
```python
@login_required
def vote(request, question_id):
    """Vote for a choice on a question (poll)."""
    user = request.user
    question = get_object_or_404(Question, pk=question_id)

    if not user.is_authenticated: # if not authenticated return to login page
        return redirect('login')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        has_voted = Vote.objects.filter(choice__question=question, user=user)
        if has_voted: # already vote
            old_vote = has_voted[0]
            if old_vote != selected_choice: # vote on new choice
                old_vote.delete()
        new_vote = Vote(user=user, choice=selected_choice)
        new_vote.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

### Panitta

1. Check for `can_vote` is done late (inefficient).
2. First assignment to `vote` is never used (useless statement).

```python
@login_required
def vote(request, question_id):
    """To vote a choice for each question."""
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        dict_return = {'question': question}
        dict_return['error_message'] = "You didn't select a choice"
        return render(request, 'polls/detail.html', dict_return)
    else:
        if not question.can_vote():
            messages.error(request, 'User cannot vote')
            return HttpResponseRedirect(reverse('polls:index'))
        chk = Vote.objects.filter(user=request.user, choice__question=question)
        vote = chk
        if chk.count() == 0:
            vote = Vote(user=user, choice=selected_choice)
        else:
            vote = chk[0]
            vote.choice = selected_choice
        vote.save()
        reverse_result = reverse('polls:results', args=[question.id],)
        return HttpResponseRedirect(reverse_result)
```

### Isaraa

```python
@login_required
def vote(request, question_id):
    """Save a Voting choice from a question objects that user voted."""
    user = request.user
    # If a user is not authenticated, a user must login first
    if not user.is_authenticated:
        return redirect('login')
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            q = question.choice_set.all()
            vote = Votes.objects.get(user=user, choice__in=q)
        # Create a new vote if it does not exists.
        except Votes.DoesNotExist:
            selected = Votes.objects.create(user=user, choice=selected_choice)
            selected.save()
        # Replace a choice with a new choice.
        else:
            vote.choice = selected_choice
            vote.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```


### Jindaporn

```python
@login_required
def vote(request, question_id):
    """
    Record the vote when user submit it.
    """
    user = request.user
    if not user.is_authenticated:
        return redirect('login')

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if not question.can_vote():
            messages.error(request, "You cannot vote this poll.")
            return HttpResponseRedirect(reverse('polls:index'))
        else:
            try:
                # get vote from previous vote if it already existed.
                current_vote = Vote.objects.get(user=request.user,
                                                choice__question=question_id)
            except Vote.DoesNotExist:
                current_vote = Vote.objects.create(user=request.user,
                                                   choice=selected_choice)
            # save vote with selected choice
            current_vote.choice = selected_choice
            current_vote.save()
            return HttpResponseRedirect(reverse('polls:results',
                                                args=(question.id,)))
```

### Khemissara
```python
@login_required
def vote(request, question_id):
    """Vote for a choice on a question (poll)."""
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            vote_object = Vote.objects.get(user=user)
            vote_object.choice = selected_choice
            vote_object.save()
        except Vote.DoesNotExist:
            Vote.objects.create(user=user, choice=selected_choice).save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

### Kulisara
```python
@login_required
def vote(request, question_id):
    """Vote for voting button."""
    question = get_object_or_404(Question, pk=question_id)
    user = request.user
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            current_vote = Vote.objects.get(user=user,
                                            choice__question=question_id)
        except Vote.DoesNotExist:
            current_vote = Vote.objects.create(user=user,
                                               choice=selected_choice)
        current_vote.choice = selected_choice
        current_vote.save()
        return HttpResponseRedirect(reverse
                                    ('polls:results', args=(question.id,)))
```

### Jiratchaya

```python
@login_required(login_url='/accounts/login/')
def vote(request, question_id):
    """Vote function that increase a value of vote and save to vote result."""
    user = request.user
    print("current user is", user.id, 'login', user.username)
    print("Real name:", user.first_name, user.last_name)
    if not user.is_authenticated:
        return redirect('login')
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    try:
        vote_object = Vote.objects.get(user=user, question=question)
        vote_object.choice = selected_choice
        vote_object.save()
    except Vote.DoesNotExist:
        Vote.objects.create(user=user,
                            choice=selected_choice, question=question).save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```


### Jirasak
```python
@login_required
def vote(request, question_id):
    """ 
    Show error message and return to detail page you did not select a choice.
    """
    # require login to vote
    user = request.user
    if not user.is_authenticated:
       return redirect('login')

    print("current user is", user.id, "login", user.username)
    print("Real name:", user.first_name, user.last_name)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            vote_ = Vote.objects.get(user=user, choice__question=selected_choice.question)
        except Vote.DoesNotExist:
            vote_ = Vote.objects.create(user=user, choice=selected_choice)
        vote_.choice = selected_choice
        vote_.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

### Pichaiyuth
```python
@login_required
def vote(request, question_id):
    """Vote for a choice on a question (poll)."""
    question = get_object_or_404(Question, pk=question_id)
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if Vote.objects.filter(question=question, user=user).exists():
            vote = Vote.objects.get(
                user=user, choice__in=question.choice_set.all())
            vote.choice = selected_choice
            vote.save()
        else:
            vote = Vote.objects.create(
                question=question, user=user, choice=selected_choice)
            vote.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id)))
```



### Kollawat
```python
@login_required
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/templates/polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            user_vote = Vote.objects.get(choice__question=question, user=request.user)
            user_vote.choice = selected_choice
            user_vote.save()
        except Vote.DoesNotExist:
            Vote.objects.create(choice=selected_choice, user=request.user)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```



### Phukit
```python
@login_required
def vote(request, question_id):
    """Login before voting."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        try:
            user_vote = Vote.objects.get(user=request.user,              choice__question=question)
            user_vote.choice = selected_choice
            user_vote.save()
        except Vote.DoesNotExist:
            Vote.objects.create(choice=selected_choice, user=request.user)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```


## Students Who Checked if Voting is Allowed 

Use `question.can_vote()`.

### Jitpanu

```python
@login_required
def vote(request, question_id):
    """Vote for a choice on a question (poll)."""
    user = request.user
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            })
    else:
        if question.can_vote():
            try:
                user_vote = question.vote_set.get(user=user)
                user_vote.choice = selected_choice
                user_vote.save()
            except Vote.DoesNotExist:
                Vote.objects.create(user=user, choice=selected_choice,
                                    question=selected_choice.question).save()
        else:
            messages.error(request, "You can't vote this question.")
            return HttpResponseRedirect(reverse('polls:index'))
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

### Kaopong

```python
@login_required
def vote(request, question_id):
    """Vote for a choice on a question (poll)."""
    user = request.user
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
            })
    else:
        if question.can_vote():
            try:
                user_vote = question.vote_set.get(user=user)
                user_vote.choice = selected_choice
                user_vote.save()
            except Vote.DoesNotExist:
                Vote.objects.create(user=user, choice=selected_choice,
                                    question=selected_choice.question).save()
        else:
            messages.error(request, "You can't vote this question.")
            return HttpResponseRedirect(reverse('polls:index'))
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

### Napasakorn

In this code, the check for voting allowed is done sooner (which is better).
```python
@login_required
def vote(request, question_id):
    """Voting process on detail view."""
    question = get_object_or_404(Question, pk=question_id)
    user = request.user

    if not question.can_vote():
        messages.error(request,
                       f"Poll number {question.id} is not available to vote")
        return redirect("polls:index")

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Please select some choice!",
        })
    else:
        try:
            vote = Vote.objects.get(user=user, choice__question=question)
            vote.choice = selected_choice
            vote.save()
        except Vote.DoesNotExist:
            Vote.objects.create(user=user, choice=selected_choice).save()
        return HttpResponseRedirect(
            reverse("polls:results", args=(question.id,)))
```


## Inefficient: Using "for" loop instead of filter

### Pakorn

```python
def vote(request, question_id):
    """Add vote to choice of the current question."""
    user = request.user
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        vote_select = Vote.objects.filter(user=user)
        for select in vote_select:
            if select.question == question:
                select.choice = selected_choice
                select.save()
                return HttpResponseRedirect(reverse('polls:results',
                                                    args=(question.id,)))
        new_vote = Vote.objects.create(user=user, choice=selected_choice)
        new_vote.save()
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))
```

### 