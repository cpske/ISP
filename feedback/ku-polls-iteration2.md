---
title: Feedback on KU Polls Iteration 2
---

Most projects look good.

## Unwanted Files Still in Repo

1. Still have `.DS_Store` files in repo on `iteration2` branch:
   - Jitpanu
   - Sittanat
   - Kollawat
   - Thanida
   - Woraphan
   - Setthanan

2. Committed `.idea` to `iteration2`:
   - Kulisara
   - Ratthicha
   - Pakorn

3. No work on KU Polls.  Did they drop ISP?
   - Jiratchaya T.
   - Tanakorn
   - Vorakorn


## Specifying Default Dates for Polls

This code for the default value doesn't work.
All the questions with have the same default date.

```python
Question class:
    pub_date = models.DateTimeField('Publication Date',
                      default=timezone.now())
    end_date = models.DateTimeField('Voting End Date',
                      default=timezone.now() + datetime.timedelta(days=7))
```

Django prints a warning when you run this.  Why?

https://stackoverflow.com/questions/51970023/how-to-set-django-model-date-field-default-value-to-future-date
