---
title: About
navigation_order: 3
---

## About the Course

| Lecture      | Mon 10:00-12:00, CPE room 507.
| -------------|--------------------------------------------------------
| Lab          | Tues 13:00-16:00, CPE Room 202.
| Google Classroom       | Announcements, schedule, and assignments. [Classroom Link][google-classroom] or use class code **5zjkval** 
| Schedule & Assignments | [Google Classroom > Classwork][classroom-classwork].
| Github       | [Github](https://github.com) to submit coding work & quiz. You need a Github account. 
| Collection of Course Material | <https://cpske.github.io/ISP>, but some content may not match this course.
| Discord                | Q&A, discussion, meeting with TAs. Join using this [Invite Link][discord-invite].
| Sign-up & Preparation  | Please do this [Sign-up and Preparation](assignment/week1/signup-and-software) before the first lab.
| Scores       | <https://bit.ly/isp2023-scores> for classwork and homework 


[google-classroom]: https://classroom.google.com/c/NjE0ODE4Mzg4ODEz
[google-classroom-invite]: https://classroom.google.com/c/NjE0ODE4Mzg4ODEz?cjc=5zjkval
[classroom-classwork]: https://classroom.google.com/w/NjE0ODE4Mzg4ODEz/t/all
[discord-invite]: https://discord.gg/gy2gbFNa


### How to Join [Google Classroom][google-classroom] and Join a Meeting

1. Join the course's [Google Classroom](https://classroom.google.com).  Use the Class Code in the table above.
2. To join a meeting, click on the "Meet" link (video icon) on the Google Classroom page: [classroom meet icon](images/google-meet-icon.png)
3. Complete this [Student Info Form](https://forms.gle/WE3jN4miDKabFBje8) so we know your Github ID.


### [Introduction to the Course](introduction/index)

(click the above line for course intro doc)

### Teaching Assistants

[Napasakorn](https://github.com/Savetang19) (นภัสกร) @savetang `email("Napasakorn", "Boonkerd")`
 
[Pawitchaya](https://github.com/GToidZ) (ปวิชญา) @GToidZ `email("Pawitchaya", "Chaloeijanya
", 2)`

[Punn](https://github.com/Halcyon905) (ปัณณ์) @halcyon.1111 `email("Punn", "Chunwimaleung", 2)` 

*In addition to the regular TAs we are lucky to also have...*

[Sahanon](https://github.com/Sahanon-P) @pst\_ping `email("Sahanon", "Phisetpakasit")`

[Preawpan](https://github.com/Tezigudo) `email("Preawpan", "Thamapipol")`

<!--
[Siratee](https://github.com/sirateek) `email("Siratee", "Kittiwitchawoakul")` Line: (on request)
 -->

### Instructors

[Sirisilp](https://github.com/sirisilp) `email("Sirisilp", "Kongsilp")`

[Jim](https://github.com/jbrucker) `email("J", "Brucker", 7)`

#### Code for Email

```python
DOMAIN = "ku.th"

def email(firstname: str, lastname: str, nlast: int = 1) -> str:
    """Return the email address for a KU person."""
    # \u0040 is Unicode for 'at' symbol
    return f"{firstname}.{lastname[0:nlast]}\u0040{DOMAIN}"
```

*Why obfuscate email addresses?*    

Software "bots" scan the web for email addresses 
and use them to send spam and phishing attacks.

[Have I Been Pwned?](https://haveibeenpwned.com)

To check if your email address or a password you use has been exposed 
in a data breach, visit [haveibeenpwned.com](https://haveibeenpwned.com).

