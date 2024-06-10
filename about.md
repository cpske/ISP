---
title: About
navigation_order: 5
---

## About the Course

| Lecture      | Mon 13:00-15:00, CPE room 202. Please come on time.
|--------------|--------------------------------------------------------
| Lab          | Tue 13:00-16:00, CPE Room 202. May extend past 16:00 some weeks.
| Google Classroom       | Announcements, schedule, and assignments. [Classroom Link][google-classroom] or use class code **TBA**
| Schedule & Assignments | [Google Classroom > Classwork][classroom-classwork].
| Github       | [Github](https://github.com) to submit coding work & quiz. You need a Github account. 
| Discord                | Q&A, discussion, meet with TAs.  |
| Scores       | <https://bit.ly/isp2024-scores> for classwork, labs, and homework.

[google-classroom]: https://classroom.google.com/c/NjE0ODE4Mzg4ODEz
[google-classroom-invite]: https://classroom.google.com/c/NjE0ODE4Mzg4ODEz?cjc=5zjkval
[classroom-classwork]: https://classroom.google.com/w/NjE0ODE4Mzg4ODEz/t/all

#### Preparation & Sign-up

Please do this [Sign-up and Preparation](assignment/week1/signup-and-software) before the first lab.


#### Instructors and Teaching Assistants

| Name                        | Email
|:----------------------------|:---------------
| [Jim Brucker](https://github.com/jbrucker), lab instructor |  `email("J", "Brucker", 7)`
| [Napasakorn](https://github.com/Savetang19) (นภัสกร), TA |  `email("Napasakorn", "Boonkerd")`
| [Pawitchaya](https://github.com/GToidZ) (ปวิชญา), TA | `email("Pawitchaya", "Chaloeijanya", 2)`
| [Punn](https://github.com/Halcyon905) (ปัณณ์), TA  | `email("Punn", "Chunwimaleung", 2)`
| [Preawpan](https://github.com/Tezigudo), TA | `email("Preawpan", "Thamapipol")`
| [Sahanon](https://github.com/Sahanon-P), Project Advsor | `email("Sahanon", "Phisetpakasit")`


#### Code for Email

```python
DOMAIN = "ku.th"

def email(firstname: str, lastname: str, nlast: int = 1) -> str:
    """Return the email address for a KU person."""
    # \u0040 is Unicode for 'at' symbol
    return f"{firstname}.{lastname[0:nlast]}\u0040{DOMAIN}"
```

#### *Why obfuscate email addresses?*    

Software "bots" scan everything on the web and collect email addresses for spam and phishing.  

[Have I Been Pwned?](https://haveibeenpwned.com)

To check if your email address or password has been exposed 
in a data breach, visit [haveibeenpwned.com](https://haveibeenpwned.com).
