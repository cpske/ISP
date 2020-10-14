---
title: Feedback on KU Polls Iteration 2
---

Most projects look good.

*Copying without thinking* in `config.cfg`:
```
[flake8]
ignore =
    E302         # expect 2 blank lines, found 1
```
It would be better **not** to ignore this. Really.


This code for the default value doesn't work if the application runs continuously:

```python
end_date = models.DateTimeField('date end', 
               default=timezone.now() + datetime.timedelta(days=1))
```

Django prints a warning when you run this.  Why?

https://stackoverflow.com/questions/51970023/how-to-set-django-model-date-field-default-value-to-future-date
