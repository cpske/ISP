---
title: About
navigation_order: 4
---

## About the Course


| **Time**     | Wed 9:00-11:00, Thurs 13:00-16:00 starting 10 Aug 2022. 
| -------------|--------------------------------------------------------
| Location     | CPE Room 204.  Some lectures **online** using Google Meet.
| Github       | We use [Github](https://github.com) for assignments. You need a Github account. 
| Schedule & Assignments | [Google Classroom/Classwork][classroom-classwork].
| Google Classroom       | Class Code **r3466kb** [Classroom Link][google-classroom].
| Course Material        | Collection of material is at <https://cpske.github.io/ISP>, with links on [Google Classroom][classroom-classwork].    
| Discord                | For Q&A, discussions, meeting with TAs 
| Sign-up & Preparation  | Please do this [Sign-up and Preparation](assignment/week1/signup-and-software) before the first class.
| Scores       | <https://bit.ly/ISP2022-scores> for classwork and homework 


[google-classroom]: https://classroom.google.com/c/NDk2ODk1MDE0NTgy
[google-classroom-invite]: https://classroom.google.com/c/NDk2ODk1MDE0NTgy?cjc=r3466kb
[classroom-classwork]: https://classroom.google.com/c/NDk2ODk1MDE0NTgy/t/all
[google-meet-link]: https://meet.google.com/ung-krcz-ojs


### How to Join [Google Classroom][google-classroom] and Join a Meeting

1. Join the [Google Classroom](https://classroom.google.com).  Use the Class Code in the table above or click this [Classroom invitation link][google-classroom-invite].
2. To join a meeting, click on the "Meet" link (video icon) on the Google Classroom page: [classroom meet icon](images/google-meet-icon.png)
3. Complete this [Student Info Form](https://forms.gle/WE3jN4miDKabFBje8) so we know your Github ID.


### [Introduction to the Course](introduction/index)

(click the above link for Intro)

### Teaching Assistants (TAs)

<!--

[Sahanon](https://github.com/Sahanon-P) `email("Sahanon", "Phisetpakasit")`
 -->


```python
DOMAIN = "ku.th"

def email(firstname: str, lastname: str, nlast: int = 1) -> str:
    """Return the email address for a KU person."""
    # \u0040 is Unicode for 'at' symbol
    return f"{firstname}.{lastname[0:nlast]}\u0040{DOMAIN}"
```

```java
// Java - in Java the 3rd parameter is required, e.g. email("Santa", "Claus", 1)
static final String DOMAIN = "ku.th";
/**
 * Return the Email address for a KU person. Works only for Thai names.
 * @param firstname person's first name
 * @param lastname  person's last name
 * @param nlast number of chars from last name to use
 * @return email address, of course
 */
public static String email(String firstname, String lastname, int nlast) {
    return String.format("%s.%s\u0040%s",
           firstname,
           lastname.substring(0, nlast),
           DOMAIN);
}
```
*Why obfuscate email addresses?*    

Software "bots" constantly scan the web for email addresses 
and use them to send spam and phishing attacks.
Some people disguise their email as "santaclaus at christmas dot com",
but that is easily recognized using pattern matching.
