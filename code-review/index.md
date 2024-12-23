---
title: Code Review
---

Presentation: [Software Reviews][reviews-presentation]

[reviews-presentation]: https://docs.google.com/presentation/d/1eSf80RFttyndaX9wokqxCUXdY1wottco/

Software Reviews include reviews of
- documents
- designs
- test plans and other plans
- code

That is, almost any work product.  The more important the work product,
the more effort should be put into reviewing it.

A review can be done by 1 person or many people.

In general, someone *other* than the author should review each piece of work.

An Agile motto is: *Review Everything*.


## Benefits of Software Reviews

- *Saves time*
  > According to a report by the Software Engineering Institute, it costs more to not do inspections than it does to do them. (Stellman & Greene, p 75).
* *Find defects* including coding and logic errors, security vulnerabilities
  > Code Reviews find more defects than unit tests.
* *Better code quality* - improves implementation, readability, uniformity, and (as a result) maintainabiility
* *Find better solutions* by sharing ideas
* *Knowledge Transfer* between team members.
* *Increase Collective Ownership* of project documents, designs, and code.

## Code Review versus Testing

Code Eeviews find 60-70% of **latent defects**, versus 30-40% discovery for testing.  

A **latent defect** is an error in the code that has not yet resulted in a mis-function of the program because the conditions (inputs, environment, state of the software, etc.) to activate the defect haven't occurred.  

*Latent Defect in a Self-Driving Car*

A self-driving car stops at a red light.  There is a truck on the other side of the intersection with a big green light on top. If the truck's light is brighter than the stop light, the software thinks it's a green traffic light and goes through the intersection.  

This defect doesn't appear until those conditions actually occur. So it's *latent*... and may not be tested for!

* Testing often discovers coding errors and deviations from the specification

* Code review discovers problems related to maintainability or failure to meet requirements

* Code review is more effective for finding security vulnerabilities, provided that reviewers look for them!


## Kinds of Code Review

1. **Self Review** the developer carefully reads and reviews his own code.  Some guidelines:
   - take a break between writing code and reviewing it
   - be mentally "fresh". Don't review at the end of a day's work
   - plan what you will review for: code defects? standards defects? security issues?
   - use a separate reading for different review purposes. If you combine too many objectives in one reading you will miss many problems.
   - use a checklist and guidance
   - record errors you find, but finish the reading before you try to fix them

2. **Desk Check** ask another developer to review your code (at his desk).  Informal and useful to find defects and get ideas for improvement.

3. **Walk Through** code review meeting with a small number of people, where one person presents or "walks through" the code line by line, while others look for defects, ask questions, and share ideas for alternate implementations.
   - Reviews should try to understand the code

4. **Pair Programming** one person writes code while the other reviews and "navigates". Maybe not a "review" since it occurs at time of creation.

5. **Regular change-based reviews** whenever new code is committed to the code repository it is reviewed and approved by other team members.  This can be done remotely.
   - change-based reviews should have specific goals and be done as carefully as desk check
   - Pull Requests are example

6. **Formal Inspection** or **Code Review** a methodical review of artifacts (often using printouts) by a group, for the purpose of finding defects.  
   - Reviewers must prepare for inspection by reviewing the code individually before, and record issues and questions.
   - One person acts as moderator, to facilitate an orderly meeting, make sure everyone has chance to speak, and ensure issues receive rapid follow-up and closure
   - Defects are acknowledged, refuted, or marked for further study during the inspection.
   - A written record is created. It describe who participated, what was inspected, a list of defects or issues found with line numbers, and follow up status.
   - The code author must follow up on all issues and respond to each.
   - Reviewers subsequentally approve the author's resolution to each issue, or ask (with explanation) for further investigation


### Effective Review Rate

The rate depends on the programming language, experience of reviewers, and other factors.

If you review too fast then you will overlook defects or lose opportunity to share understanding of the code.

General guidance is the rate should be at most **200 - 300 lines per hour**. Wikipedia has 200-400 lines/hr, but other sources cite 300 as upper limit, based on studies.

## Checklists

A checklist will make your code reviews more consistent and avoid forgetting to check for some kinds of problems.

Good checklists:

* [DZone Code Review Checklist](https://dzone.com/articles/sample-code-review-checklist) with 14 items.
* DZone [Java Review Checklist](Java-Code-Review-Checklist.pdf) with 5 categories of items
* [Stop More Bugs with our Code Review Checklist](https://blog.fogcreek.com/increase-defect-detection-with-our-code-review-checklist-example/) from Fog Creek Software.  Considered "pretty universal".
* [Checklist for Effective Code Reviews](http://www.evoketechnologies.com/blog/code-review-checklist-perform-effective-code-reviews/) by Surrender Gutha has basic and detailed versions.
* [Java Review Checklist on DZone](https://dzone.com/articles/java-code-review-checklist) nice -- divides review items into categories.
* [Java Checklist Local Copy](Java-Code-Review-Checklist.pdf),
* Concise, practical [Checklist PDF](https://courses.cs.washington.edu/courses/cse403/12wi/sections/12wi_code_review_checklist.pdf) from U. of Washington.
* [Things to Include in your Checklist](https://www.codementor.io/blog/code-review-checklist-76q7ovkaqj) from codementor.io. High-level categories for reviews.
[PSP](code-review/PSP-Review-Script-Checklist.pdf)

Good Checklists From ISP Students:

- [Vacseen Project Checklist](https://docs.google.com/document/d/1sJqZ3WlXeycAEXh6zB1JEkJHjNAY0ihp8oIT0eFlDfk/edit) (2019)
- [KooCook Project Script & Checklist](https://docs.google.com/document/d/1GSI0FGx4NZyqwAVUOYt641X0tsdqfeRz3O-R3XnfGFE/edit) (2019), very detailed
- [KU Event Regis](https://docs.google.com/document/d/1pRlqTeCQEq9T0g3NPf8yt26aUKCSKC3rqEyI3L4xy_I/edit#heading=h.imm89g97i44a) (2019)
- [Real Estate Rental](https://docs.google.com/document/d/1plSBYDK-mYTJ-u1JY7BV-esmCcP8XGtpmY4gUwgzB0g/edit) (2020)

## Best Practices

[Code Review Best Practices](./code-review-best-practices) from experts at SmartBear, Perforce, and JetBrains.


## How to Approach a Code Review

How to communicate so that the review is effective and positive?

[Thoughtbot](https://github.com/thoughtbot/guides/tree/master/code-review) suggests this:

Reviewers should

- Question, don't criticize.
- If you must criticise, criticize code not people.
- Try to see the author's perspective. Maybe he had a reason you don't know.
- Be humble.
- Be explicit in writing, so others clearly understand what you mean.
- Avoid hyperbole ("always", "never", "useless", "terrible"); don't use sarcasm.

For authors of code under review:

- Code review is about code, not about you.
- Be grateful for suggestions.
- Assume best intention of the reviewers.
- Be humble.
- Try to respond to every comment, and explain the code.


## Tools

(my links were getting old, so I removed them)

### Review for Security Vulnerabilities (Important)

Code Reviews should look for security vulnerabilities including:

- [ ] format string errors and exploits
- [ ] using, storing, or displaying unsanitized user input
- [ ] race conditions, where behavior may depend on timing of events
- [ ] memory leaks (probably not an issue in Python)
- [ ] buffer overflows


## Videos

- [How to review someone else's code](https://www.youtube.com/watch?v=TlXy_i27N3w) 8 minutes, Codecademy
- [How to Do Code Reviews Like a Human](https://www.youtube.com/watch?v=0t4_MfHgb_A) by developer who worked at Microsoft & Google. 10 concrete suggestions.


## Resources

* [Reviews](Reviews-Stellman-and-Greene.pdf), Chapter 5 in *Applied Software Project Management* by Stellman and Greene.

* [Code Review Guidelines for Humans](https://phauer.com/2018/code-review-guidelines/) good article, concrete with illustrations, not too long.

* [Code Review on Wikipedia](https://en.wikipedia.org/wiki/Code_review)

* [Best Kept Secrets of Peer Code Review](www.codereviewbook.com) free download at  www.CodeReviewBook.com.  Describes 5 types of peer code reviews and how to do them.
  - Mirror [Best Kept Secrets of Peer Code Review](https://static1.smartbear.co/smartbear/media/pdfs/best-kept-secrets-of-peer-code-review_redirected.pdf)
* Summary of [Best Practices For Peer Code Review](https://www.kessler.de/prd/smartbear/BestPracticesForPeerCodeReview.pdf) from SmartBear.com
  - Their results seem biased.  They sell a tool for remote code review.

Testing

- <a>Hyperlink without href attribute</a>
- <a>Another lame hyperlink to test your scanner</a>

[review-board]: https://www.reviewboard.org/
[review-board-github]: https://github.com/reviewboard/reviewboard
