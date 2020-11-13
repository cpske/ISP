---
title: Feedback on Projects
---

## 1. Use What You Already Learned

In KU Polls iteration 2 you learned how to separate configuration data
from code, which is a good practice for **any** software.

Are you applying it in your projects?

| Project            | External configuration? | Secret settings on Github?  |
|:-------------------|------------------|:----------------------------|
| Covid19 Tracker    | No               | SECRET KEY, OAuth secrets   |
| DEK-COM            | No               | SECRET KEY                  |
| EveHolder          | django-environ   | none                        |
| Sleep Helper       | No               | SECRET KEY                  |
| JIX                | No               | SECRET KEY, OAuth secrets   |
| KU-Hub             | decouple         | none                        |
| Kvent              | decouple         | none [see Note]             |
| Noxus              | No               | SECRET KEY                  |
| Real Estate Rental | No               | SECRET KEY, OAuth secrets   |
| TELLING            | No               | SECRET KEY                  |
| TEWMA              | No               | SECRET KEY                  |
| Your Fitness Pal   | No               | SECRET KEY                  |


### Secure Development

The software industry unanimously recommends:

> Security must be part of the development process, not added at the end.

You should apply basic security practices from the start. 
Think about security during code reviews, too.

If your `SECRET_KEY` has been exposed, you can generate a new one.


**Note**: Kvent `settings.py` has: 

```python
ALLOWED_HOSTS = ['*']
DEBUG = config('DEBUG', default=True)
```

You should add `ALLOWED_HOSTS` to the external config, and restrict it
when in a development environment. You should be careful that `DEBUG`
is False on a deployed server, since `DEBUG=True` can be used to discover 
environment variables (your secrets). 

Hence, the safe default is `False`.
