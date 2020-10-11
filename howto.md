---
title: Jekyll How To
---

## Variables

[Jekyll Docs](https://jekyllrb.com/docs/)

[Jekyll Variables](https://jekyllrb.com/docs/variables/)

Access variable values using "dot" notation inside double braces.

[Defining Permalinks](https://jekyllrb.com/docs/permalinks/)


### Site Variables `site.`

* `site.url` from `url: http://mysite.com` in `_config.yml` {{ site.url }}
* `site.html` {{ site.html }}
* `site.data` {{ site.data }}
* `site.foo`  from `foo: xxx` in `_config.yml` site.markdown = {{ site.markdown }}

### Page Variables `page.`

* `page.title` from front matter, {{ page.title }}
* `page.url` may be over-ridden in front matter, {{ page.url }}
* `page.dir` may be over-ridden by `permalink:` in front matter, {{ page.dir }}
* `page.path` {{ page.path }}
