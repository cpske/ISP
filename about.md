---
title: About
navigation_order: 3
---

Monday 10-12, 13-16 starting 10 Aug 2020.   
**Location:** class will be online. Some meetings and live lectures in room E204.     
**Online Meeting Location:** Google Meet using the link shown on Google Classroom for this course. Just click on the Meet link or icon.    
[Google Classroom](https://classroom.google.com) for assignments and announcements: join using class code **3blhnrs**    
Github Classroom & Org [ISP2020](https://github.com/org/ISP2020) for programming work.    
[Sign-up form](https://forms.gle/fh9SqvmA9yPh1ur6A) - so we know your Github ID

### [Introduction to Course](/introduction/index)

### Teaching Assistants (TAs)

[Mai Norapong](https://github.com/MaiNorapong)  `email("Mai","Norapong",2)`

[Pakanon Pantisawat](https://github.com/pknn1) `email("Pakanon","Pantisawat",1)`

```python
DOMAIN = "ku.th"

def email(firstname: str, lastname: str, nlast: int = 1) -> str:
    """Return the email address for a KU person"""
    # \u0040 is Unicode for 'at' symbol
    return f"{firstname}.{lastname[0:nlast]}\u0040{DOMAIN}"

if __name__ == '__main__':
    print("Contact Mai ", email("mai","norapong",2));
    print("Contact Pakanon ", email("pakanon","pantisawat",1));
```
