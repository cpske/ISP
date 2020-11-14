---
title: About
navigation_order: 4
---

Monday 10-12, 13-16 starting 10 Aug 2020.   
**Location:** class is online. Some meetings and live lectures in room E204.     
**Online Meeting Location:** Google Meet using the link shown on Google Classroom for this course. Just click on the Meet link or icon.    
[Google Classroom](https://classroom.google.com) for assignments and announcements. Join using class code **3blhnrs**    
Github Classroom Organization [ISP2020](https://github.com/org/ISP2020) for programming work.    
[Sign-up form](https://forms.gle/fh9SqvmA9yPh1ur6A) - so we know your Github ID

[Introduction to Course](/ISP/introduction/index)

### Teaching Assistants (TAs)

[Mai Norapong](https://github.com/MaiNorapong)  `email("Mai","Norapong",2)`

[Pakanon Pantisawat](https://github.com/pknn) `email("Pakanon","Pantisawat")`

```python
DOMAIN = "ku.th"

def email(firstname: str, lastname: str, nlast: int = 1) -> str:
    """Return the email address for a KU person"""
    # \u0040 is Unicode for 'at' symbol
    return f"{firstname}.{lastname[0:nlast]}\u0040{DOMAIN}"
```

