---
title: About
navigation_order: 4
---

## About the Course

Monday 10-12, 13-16 starting 9 Aug 2020.   

**Location:** class is online (for now). Meet using 
[Google Classroom](https://classroom.google.com/c/MzczOTE1MjA0NDE4?cjc=ka25cph)

1. Join the Google Classroom.  Use the class code **ka25cph** or this [invitation link][google-classroom-link].
2. To join a meeting, click on the "Meet" link or video icon on the Google Classroom page.
3. Complete the [Student Info From](https://forms.gle/WE3jN4miDKabFBje8) so we know your Github ID.
4. What online platform do you prefer? Please complete [Online Platform Preferences](https://forms.gle/VkG5MBPjgmxRX1xi7).

**Github & Github Classroom** - we use Github for programming work, and Github Classroom for some exerices and quizzes.

[google-classroom-link]: https://classroom.github.com/classrooms/86591180-isp-2021 

### [Introduction to Course](introduction/index)

### Teaching Assistants (TAs)

[Anusid](https://github.com/ttxking)  `email("Anusid", "Wachiroachoroenwong")`

[Sahanon](https://github.com/Sahanon-P) `email("Sahanon", "Phisetpakasit")`

[Chanathip](https://github.com/kaesrel) `email("Chanathip", "Thumkanon", 3)` 

[Sahadporn](https://github.com/Sahadporn) `email("Sahadporn", "Charnlertlakha")` // unconfirmed


```python
DOMAIN = "ku.th"

def email(firstname: str, lastname: str, nlast: int = 1) -> str:
    """Return the email address for a KU person."""
    # \u0040 is Unicode for 'at' symbol
    return f"{firstname}.{lastname[0:nlast]}\u0040{DOMAIN}"
```

```java
// Java - in Java version the 3rd parameter is required,
//        e.g. email("Santa", "Claus", 1)
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
