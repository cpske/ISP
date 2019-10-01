## Week 5 Database Assignment

**Good:** On questions 1 - 3 many students used sqlitebrowser 
or DBeaver to explore their database, and even
draw an ER diagram of the tables.  That's a great way to get
familiar with databases, and shows effort.

On question 3 some students drew a diagram but did not indicate in the diagram
*how* data in polls_question is related to data in polls_choice.  1 point deduction for this.

A good answer is (some students wrote this):    
> In `polls_choice` table, the `question_id` contains
> the id of the question for that choice. 
> We can join the two tables using 
> ```sql
> polls_choice.question_id = polls_question.id
> ```

## Question 4 on Database Assignment

Write a Python function to count all the votes for a poll with given id.
```python
    def vote_count(id):
```

Too many students submitted nearly exactly the same
**poor solution** shown below.    
I'm sure some of these are **copied**.  Hence, no credit for the following code:

```python
def vote_count(id):
    count = 0
    choices = Choice.objects.all()
    for i in choices:
        if i.question_id == id:
            count += i.votes
        else:
            pass
    return count
```
There are 2 problems with this code:

1. It forces Django to create Choice objects for **all** the choices in the database, even the ones you don't want.  This wastes time and memory, and could be a *lot* of Choice objects.  Better to retreive **only the choices you want** using `Choice.objects.filter(id=id)`.
    > In general, avoid database queries that return ALL the data or LOTS of
    > data unless you really need all the data.    
    > You want to write code that "scales" to larger datasets, not just small ones.

2. Writing `else: pass` has no purpose!  You can omit `else` after an `if`, so why write an empty `else` block?


I think many students who wrote answers like this also **copied code**,
but gave credit anyway since its not so definitive:

```python
def vote_count(id):
    """Return total votes for a given poll. id is poll id"""
    count = 0 
    for i in Question.objects.get(pk=id).choice_set.all():
        count += i.votes
    return count
```

1. Stringing together a long chain of references and method calls should be avoided.  It makes code hard to read and can be fragile. *Clean Code* discusses this. Instead, assign an intermediate result to an *explanatory variable*.
2. `i` is not a descriptive variable name. 
3. Only some student's code use `pk` as attribute in Question. In others, the variable for primary key is `id`.

Better to write:
```
    question = Question.objects.get(pk=id)
    for choice in question.choice_set.all():
        count += choice.votes
```

## Question 5 on Database Assignment

Most people wrote something like this:
```python
def find_polls_for_text(text):
    """Return list of Questions for all polls containing some text"""
    return Question.objects.filter(question_text__contains = text)
```
`filter()` returns a `QuerySet` not a `list`.   
You need to create a list from the QuerySet, which is easy:
```python
   polls = Question.objects.filter(question_text__contains = text)
   return list(polls)
```

## Near Identical Code in Question 4

Does this code look like copying to you?

Apipark:
```python
def vote_count(id):
    count = 0
    number_of_choices =  Choice.objects.all()
    for i in number_of_choices:
        if i.question_id == id:
            count += i.votes
        else:
            pass
    return count
```

Kasidit:
```python
def votes_count(id):
    vote = 0
    choice = Choice.objects.all()
    for i in choice:
        if i.question_id == id:
            vote += i.votes
        else:
            pass
    return vote
```

Natapol:
```python
def vote_count(id):
    count = 0
    polls_choice = Choice.object.all()
    for i in polls_choice:
        if i.question_id == id:
            count += i.votes
        else:
            pass
    return count
```

Natthaphon:
```python
def votes_count(id):
   votes_amount = 0
   choices = Choice.object.all()
   for i in choices:
       if i.question_id == id:
           votes_amount += i.votes
       else:
           pass
   return votes_amount
```

Pakkapon:
```python
def votes_count(id):
   count = 0
   choices = choice.objects.all() # typo: should be "Choice"
   for i in choices:
       if i.question == id:
           count +=  i.votes
       else:
           pass
   return count
```

Pawaris:
```python
def vote_counts(id):
    num_vote = 0
    choice_list = Choice.objects.all()
    for i in choice_list:
        if i.question_id == id:
            num_vote =+ i.votes
        else:
            pass
    return num_vote
```

Supakorn:
```python
def votes_count(id):
    vote = 0 
    choice = Choice.objects.all()
    for i in choice:
        if i.question_id == id:
            vote += i.votes
        else:
            pass
    return vote
```

Wikrom:
```python
def votes_count(id):
   count_votes = 0
   all_choice = Choice.objects.all()
   for i in all_choice:
       if i.question_id == id:
           count_votes += i.votes
       else:
           pass
    return count_votes
```

## QuerySets and Lazy Instantiation

The Django [QuerySet API](https://docs.djangoproject.com/en/2.2/ref/models/querysets/) explains:

> a QuerySet can be constructed, filtered, sliced, and 
> generally passed around **without actually hitting the 
> database**. No database activity actually occurs until 
> you do something to evaluate the queryset.

This is sometimes called "lazy instantiation" and most ORM do it.  It means, "don't go get something until you need it" (be lazy).

For example, `Question.objects.all()` returns a `QuerySet` but doesn't access the database yet.    
If you write:
```python
top_ten = Question.objects.all()[0:10]
```
it only retrieves the first 10 rows from the database.  
No other data is retrieved.

A QuerySet is *iterable* and the first time you use it in
an iterator it will retrieve data from the database.    
If you write:
```python
    for choice in queryset:
        votes += choice.votes
```
then you are using `queryset` as an iterator and **all** the data will be retrieved as objects. (Actually, its an "iterable" that creates an "iterator".)

The Django [QuerySet API](https://docs.djangoproject.com/en/2.2/ref/models/querysets/) describes when QuerySets access the database.

