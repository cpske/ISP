---
title: Gunicorn and Nginx Configuration for Django
---

Django includes a web server for development, but this server has
low performance and may not be secure.  The recommended way to deploy
Django is:

- use a production-level web server for Django and static content, such as Nginx or Apache httpd
- the web server can serve static content itself
- the web server forwards Django requests to a WSGI-compliant interface, which in turn invokes Django
- Good WSGI implementations are Gunicorn, uWSGI, and `mod_wsgi` for Apache

## Features of Gunicorn and other WSGI Servers

- can spawn multiple worker processes or threads that run in parallel
- built-in logging
- better security
- speed

## Configure Gunicorn

Add Gunicorn to `requirements.txt` and/or install the package:

```
pip install gunicorn
```

Create a Gunicorn configuration file, e.g. `gunicorn.py` containing:
```
command=


## References

<https://www.youtube.com/watch?v=N2t7L_K5LXo> part of a series on "Very Academy" Youtube channel.

Source code: <https://github.com/veryacademy/yt-nginx-mastery-series>

