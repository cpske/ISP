---
title: About
navigation_order: 4
---

## About the Course

[google-classroom]: https://classroom.google.com/c/NjkxNTc2NDc5NzM4
[classroom-classwork]: https://classroom.google.com/c/NjkxNTc2NDc5NzM4/t/all

| Lecture      | Mon 13:00-15:00, CPE room 202. Please come on time.
|--------------|--------------------------------------------------------
| Lab          | Tue 13:00-16:00, CPE Room 202. May extend past 16:00 some weeks.
| Google Classroom       | Announcements, schedule, and assignments. [Classroom Link][google-classroom] 
| Schedule & Assignments | [Google Classroom > Classwork][classroom-classwork].
| Github       | [Github](https://github.com) to submit coding work & quiz. You need a Github account. 
| Discord                | Q&A, discussion, meet TAs.  |
| Scores       | <https://bit.ly/isp2024-scores> for classwork, labs, and homework.


#### Instructors and Teaching Assistants

| Name                        | Email
|:----------------------------|:---------------
| Jim Brucker, instructor     | `email("J", "Brucker", 7)`
| Krittin (JJ), TA            | `email("Krittin", "Setdhavanich", 3)`
| Nanthawat (Boom), TA        | `email("Nanthawat", "Duang-Ead", 2)`
| Sirin (Toey), TA            | `email("Sirin", "Phungkun", 2)`
| Yanatchara (Great), TA      | `email("Yanatchara", "Jeraja")`

#### Code for Email

```python
DOMAIN = "ku.th"

def email(firstname: str, lastname: str, nlast: int = 1) -> str:
    """Return the email address for a KU person."""
    # \u0040 is Unicode for 'at' symbol
    return f"{firstname}.{lastname[0:nlast]}\u0040{DOMAIN}"
```

#### *Why obfuscate email addresses?*    

Software "bots" scan web pages and collect email addresses for spam and phishing.  

#### [Have I Been Pwned?](https://haveibeenpwned.com)

To check if your email address or password has been exposed 
in a data breach, visit [haveibeenpwned.com](https://haveibeenpwned.com).

The check is done in your browser -- your email or password are *not* transmitted.
