# vote in views.py

Codes that are distinct enough or have unique logic (even if not good logic):

Chanathip, Metaras, Pattarin, Nuttapol, Sahanon, others.

## Anusid

f-strings are faster and easier to read than `string.format(...)`.
`string.format` is useful when the format values are long or complex, 
which is not the case here.

```python
@login_required(login_url='/accounts/login/')
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        logger.info(
            '{user} voted on {question} (id = {id})'.format(user=request.user,
                    question=question, id=question.id))
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        messages.error(request, "You didn't select a choice.")
        return render(request, 'polls/detail.html', {'question': question,})
    else:
        if question.vote_set.filter(user=request.user).exists():
            previous_vote = question.vote_set.get(question=question, user=request.user)
            previous_vote.choice = selected_choice
            previous_vote.save()
        else:
            selected_choice.vote_set.create(question=question, user=request.user)
```

## Bheem

```python
@login_required(login_url='/accounts/login/')
def vote(request, question_id):
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
        already_vote = Vote.objects.filter(question=question_id, user=request.user).exists()
        if already_vote:
            get_vote = Vote.objects.get(user=request.user)
            get_vote.choice_id = selected_choice.id
            get_vote.save()
            logger.info('[Vote Submit]: Username: {}, Poll ID: {}'
                  .format(request.user, question_id))
        else:
            get_vote = Vote.objects.create(question=question, user=request.user,
                       choice=selected_choice)
            get_vote.save()
            logger.info('[Vote Submit]: Username: {}, Poll ID: {}'
                        .format(request.user, question_id))
```

## Chayapol

```python
@login_required
def vote(request, question_id):
    user = request.user
    question = get_object_or_404(Question, pk=question_id)
    print("current user is", user.id, "login", user.username)
    print("Real name:", user.first_name, user.last_name)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if question.vote_set.filter(user=user).exists():
            vote = question.vote_set.get(user=user)
            vote.choice = selected_choice
            vote.save()
        else:
            selected_choice.vote_set.create(user=user, question=question)
        logger.info(f"User {user.username} submit a vote for question {question.id} ")
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

## Jakkrathorn - same as Chayapol except for Vote.update_or_create

```python
@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    user = request.user
    print("current user is", user.id, "login", user.username)
    print("Real name:", user.first_name, user.last_name)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if question.vote_set.filter(user=user).exists():
            selected_vote = question.vote_set.get(user=user)
            selected_vote.choice = selected_choice
            selected_vote.save()
        else:
            Vote.objects.update_or_create(question=question, choice=selected_choice, user=request.user)
        logger.info(f"user: {user.username} has voting on {get_client_ip(request)} ")
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

## Pittayut - same as Jakkrathorn but no print statements

```python
@login_required
def vote(request, question_id):
    """Check selected vote choice and update vote score."""
    question = get_object_or_404(Question, pk=question_id)
    user = request.user
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if question.vote_set.filter(user=user).exists():
            selected_vote = question.vote_set.get(user=user)
            selected_vote.choice = selected_choice
            selected_vote.save()
        else:
            Vote.objects.update_or_create(question=question, choice=selected_choice, user=request.user)
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

## Panida - same as Jakkrathorn

```python
@login_required
def vote(request, question_id):
    """Def about vote and go to result page."""
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
        Vote.objects.update_or_create(user = user, question=question,
                                      defaults={'choice': selected_choice})
        loggings.info(f"{user.username} is voting in question id {question_id}, {user.username}'s IP address is {get_client_ip(request)}")
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

## Pitchapa - same as Panida except omitted logging

```python
@login_required
def vote(request, question_id):
    """Show results page when the web visitor vote."""
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
        Vote.objects.update_or_create(user=user, question=question,
                                      defaults={'choice': selected_choice})
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

```

## Narawish - same as Jakkrathorn except for unnecessary "for choice in ..." loop

You should delete the `Choice.votes` attribute. Use a `votes` property that sums the votes for a choice when invoked.

```python
@login_required()
def vote(request, question_id):
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
        user = request.user
        Vote.objects.update_or_create(user=user, question=question,
                                      defaults={'choice': selected_choice})
        for choice in question.choice_set.all():
            choice.votes =
              Vote.objects.filter(question=question).filter(choice=choice).count()
            choice.save()
    date = datetime.now()
    log.info("User: %s, Poll's ID: %d, Date: %s.", user, question_id, str(date))
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

## Kongtapp - same unnecessary "for choice in ..." loop

```python
@login_required()
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    user = request.user
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        messages.error(request, "You didn't make a choice")
        return render(request, 'polls/detail.html', {
            'question': question,
        })
    else:
        Vote.objects.update_or_create(defaults={'choice': choice},
                                      question=question, user=user)
        for choice in question.choice_set.all():
            choice.votes =
               Vote.objects.filter(question=question).filter(choice=choice).count()
            choice.save()

        messages.success(request, "Your choice successfully recorded. Thank you.")
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

## Auttakrit

```python
@login_required
def vote(request, question_id):
    """Redirect to vote page."""
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
        if not (question.can_vote()):
            messages.warning(request, "This question is expired.")
            return HttpResponseRedirect(reverse('polls:index'))
        if question.vote_set.filter(user=user).exists():
            vote = question.vote_set.get(user=user)
            vote.choice = selected_choice
            vote.save()
        else:
            selected_choice.vote_set.create(user=user, question=question)
        logger.info(f'User: {request.user.username} ip: {get_ip(request)} voted the poll, question id = {question.id}. ')
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
```

## Kittitouch - unnessary assignment to request.session

```python
@login_required
def vote(request, question_id):
    """Check vote and count vote."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        messages.error(request, "You didn't make a choice.")
        return render(request, 'polls/detail.html', {'question': question, })
    else:
        if not (question.can_vote()):
            messages.warning(request, "This polls are not allowed.")
        elif Vote.objects.filter(user=request.user, question=question).exists():
            previous_vote = Vote.objects.get(user=request.user, question=question)
            previous_vote.choice = selected_choice
            previous_vote.save()
        else:
            question.vote_set.create(choice=selected_choice, user=request.user)
            messages.success(request, "Your choice successfully recorded.")
        request.session['choice'] = selected_choice.id
        logger.info(f'User {request.user.username} voted on polls id: {question.id}')
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

## Peerasu - same grammar error in warning message and same assignment to request.session as Kittitouch

```python
@login_required
def vote(request, question_id):
    """Vote view."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if not (question.can_vote()):
            messages.warning(request, "This polls are not allowed. ")
        elif Vote.objects.filter(user=request.user, question=question).exists():
            this_votes = Vote.objects.get(user=request.user, question=question)
            this_votes.choice = selected_choice
            this_votes.save()
        else:
            question.vote_set.create(choice=selected_choice, user=request.user)
        logger.info(
            f'User {request.user.username} voted for question id number
                   {question.id} from {get_client_ip(request)}')
        messages.success(request, "Vote successful, thank you for voting. ")
        request.session['choice'] = selected_choice.id
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

## Panitan - same as Kittitouch (both have unnessary assignment to request.session)

"Successfull" is misspelled. Punctuation error in another message.

```python
@login_required
def vote(request, question_id):
    """Return function that show vote."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        messages.success(request, "Your vote is succesfull.")
        if not (question.can_vote()):
            messages.warning(request, "This polls are not allowed.")
        elif Vote.objects.filter(user=request.user, question=question).exists():
            this_votes = Vote.objects.get(user=request.user, question=question)
            this_votes.choice = selected_choice
            this_votes.save()
        else:
            question.vote_set.create(choice=selected_choice, user=request.user)
            messages.success(request,"Vote sucessful,thank you for voting. ")
            logger.info('user {user} voted on polls id: {id}'.format(
                user=request.user,
                id=question_id
            ))
        request.session['choice'] = selected_choice.id
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

## Bhatara

```python
@login_required
def vote(request, question_id):
    """Add vote function to each poll."""
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
        log.info(f'{request.user} submitted a vote for question {question.question_text} form ip: {get_client_ip(request)} date: {now()}  ')
        Vote.objects.update_or_create(user = request.user, question = question,
                                      defaults= {'choice': selected_choice})
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```

## Jirawadee and Kasadit 

```python
@login_required
def vote(request, question_id):
    """Update the vote for choice that have been voted."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        configure()
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        configure()
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if Vote.objects.filter(pk=question_id, user_id=request.user.id).exists():
            configure()
            user_vote = question.vote_set.get(user=request.user)
            user_vote.choice = selected_choice
            user_vote.choice.votes += 1
            user_vote.choice.save()
            user_vote.save()
        else:
            configure()
            selected_choice.vote_set.create(user=request.user, question=question)
   return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
```

## Nattapol - same as Jirawadee & Kasadit but added unnecessary code

This code uselessly calls `get_client_ip` 4 times and ignores the return value each time.  Other parts same as Jirawadee and Kasadit.

```python
@login_required
def vote(request, question_id):
    """Vote function for polls app."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        configure()
        get_client_ip(request)
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        configure()
        get_client_ip(request)
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if Vote.objects.filter(question_id=question_id,
                               user_id=request.user.id).exists():
            configure()
            get_client_ip(request)
            user_vote = question.vote_set.get(user=request.user)
            user_vote.choice = selected_choice
            user_vote.save()
        else:
            configure()            
            get_client_ip(request)
            selected_choice.vote_set.create(user=request.user, question=question)

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
```

## Chananya - multiple calls to configure() same as others



## Similar configure() code in Chananya, Jirawadee, Kasadit 

Several students wrote this function nearly identically.

It is better to configure logging in `settings.py` instead of
in views.

```python
def configure():
    filehandler = logging.FileHandler("demo.log")
    filehandler.setLevel(logging.NOTSET)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
    filehandler.setFormatter(formatter)
    root = logging.getLogger()
    root.addHandler(filehandler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    formatter = logging.Formatter(fmt='%(levelname)-8s %(name)s: %(message)s')
    console_handler.setFormatter(formatter)
    root.addHandler(console_handler)
```


## Similar "vote_for_poll" method

```python

# Jirawadee

def vote_for_poll(request, pk):
    """Check that polls the polls can vote or not."""
    q = Question.objects.get(pk=pk)
    if not(q.can_vote()):
        messages.error(request, "poll expires")
        return redirect('polls:index')
    return render(request, "polls/detail.html", {"question": q})

# Kasidit/ku-polls/polls/views.py

@login_required
def vote_for_poll(request, question_id):
    """Check the poll is avalable to vote."""
    question = Question.objects.get(pk=question_id)
    if not(q.can_vote()):
        messages.error(request, "poll expires")
        return redirect('polls:index')
    return render(request, "polls/details.html", {"question": question})

# Nuttapol/ku-polls/polls/views.py

@login_required
def vote_for_poll(request, pk):
    """Show the detail only valid question."""
    previous_selected_vote_text = ""
    has_previous_vote = False
    question = get_object_or_404(Question, pk=pk)
    previous_selected_vote = Vote.objects.filter(question=question).filter(user=request.user).first()
    if previous_selected_vote is None:
        previous_selected_vote_text = ""
    else:
        previous_selected_vote_text = previous_selected_vote.user_choice.choice_text
        has_previous_vote = True
    # if a is None:
    #     a = "None"
    if not question.can_vote():
        messages.error(request, "This Question can not vote")
        return redirect('polls:index')
    return render(request, 'polls/detail.html',
            {'question': question, 'previous_selected_vote_text': previous_selected_vote_text,
            'has_previous_vote': has_previous_vote})

# Pitchapa/ku-polls/polls/views.py
@login_required
def vote_for_poll(request, pk):
    """Show error messages when the question not allowed to vote or render question detail page when it can."""
    question = get_object_or_404(Question, pk=pk)
    already_voted = False
    if not question.can_vote():
        messages.error(request, "Voting is not allowed.")
        return redirect('polls:index')

# Pittayut/ku-polls/polls/views.py

def vote_for_poll(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if not question.can_vote():
        messages.error(request, f"This poll isn't in vote period.")
        return redirect('polls:index')
    return render(request, 'polls/detail.html', {'question': question})

# Sahatsawat/ku-polls/polls/views.py
def vote_for_poll(request, question_id):
    choice_id = request.POST['choice']
    if not choice_id:
        messages.error(request, "You didn't make a choice")
        return redirect('polls:someplace')

    messages.success(request, "Your choice successfully recorded. Thank you.")
    return redirect('polls:results')

```

### Bad Logging Code in views.py

At top level, several students wrote this.

The code is executed when the file is imported and variables are global.
Better to configure logging in the application `settings.py`.

```python

import logging

logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
```

