---
title: About
navigation_order: 4
---

## About the Course

Monday 10-12:00 and 13-16:00 starting 9 Aug 2021. 

**Location:** course meets **online** using [Google Classroom][google-classroom-link] and [Google Meet][google-meet-link]. See below for how to join. (Normal classroom is E204.)

**Online Meetings:** Meet using Google Meet at 10:00 AM every Monday. 
See below for how to join. 

**Github**: we use [Github](https://github.com) for programming work, so you must have a Github account. Using Github is described in class.

**Course Schedule**: Weekly Schedule and Assignments are on [Google Classroom/Classwork][classroom-classwork].

**Course Material:** All material is on <https://cpske.github.io/ISP>, with links on [Google Classroom][classroom-classwork].    

**Discord:** For Q&A, discussions, meetings <https://discord.gg/9FrRt4q>

**Preparation**: Please do this [Sign-up and Preparation](assignment/week1/signup-and-software) before the first class.

**Scores**: <https://bit.ly/ISP2021-scores> for classwork and homework 

**Student Github URLs**: [Repository URL Generator](repositories)


[google-classroom-link]: https://classroom.google.com/c/MzczOTE1MjA0NDE4?cjc=ka25cph
[classroom-classwork]: https://classroom.google.com/u/0/w/MzczOTE1MjA0NDE4/t/all
[google-meet-link]: https://meet.google.com/lookup/gufu6342m5


### How to Join [Google Classroom][google-classroom-link] and Join a Meeting

1. Join the [Google Classroom](https://classroom.google.com).  Use class code **[ka25cph][google-classroom-link]** or click this **[invitation link][google-classroom-link]**.
2. To join a meeting, click on the "Meet" link (video icon) on the Google Classroom page:
[![classroom meet icon](images/classroom-meet-icon.png)][google-meet-link]
   - You can also click this [Google Meet Link][google-meet-link] but it may change in the future.
3. Complete this [Student Info Form](https://forms.gle/WE3jN4miDKabFBje8) so we know your Github ID.
4. What online platform do you prefer? Please complete [Online Platform Preferences](https://forms.gle/VkG5MBPjgmxRX1xi7).


### [Introduction to the Course](introduction/index)
(click the above link for Intro)

### Teaching Assistants (TAs)

[Anusid](https://github.com/ttxking)  `email("Anusid", "Wachiroachoroenwong")`

[Chanathip](https://github.com/kaesrel) `email("Chanathip", "Thumkanon", 3)` 

[Pattarin](https://github.com/pattarinn) `email("Pattarin", "Wongwaipanich", 3)` 

[Sahanon](https://github.com/Sahanon-P) `email("Sahanon", "Phisetpakasit")`


```python
DOMAIN = "ku.th"

def email(firstname: str, lastname: str, nlast: int = 1) -> str:
    """Return the email address for a KU person."""
    # \u0040 is Unicode for 'at' symbol
    return f"{firstname}.{lastname[0:nlast]}\u0040{DOMAIN}"
```

```java
// Java - in Java the 3rd parameter is required, e.g. email("Santa", "Claus", 1)
/**
 * Return the Email address for a KU person. Works only for Thai names.
 * @param firstname person's first name
 * @param lastname  person's last name
 * @param nlast number of chars from last name to use
 * @return email address, of course
 */
public static String email(String firstname, String lastname, int nlast) {
    final String DOMAIN = "ku.th";
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
