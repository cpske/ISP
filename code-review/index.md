---
title: Code Review
---

Presentation: [Code Reviews](Reviews.pdf)

## Benefits of Code Review

* *Find defects* including coding and logic errors, performance problems, security vulnerabilities
* *Better code quality* improve the implementation, readability, uniformity, and (as a consequence) maintainabiility
* *Finding better solutions* by sharing new ideas
* *Knowledge Transfer* - approach and technology used, and rationale for the implementation/solution.  Code reviews are a good way for more experienced developers to share knowledge with others.
* *Increase Collective Ownership* of code
* [Improving Software Quality through Inspections](Improving Software Quality through Inspections.pdf) a classic paper

## Code Review versus Testing

Studies have found that code reviews find 60-70% of *latent defects*, versus 30-40% discovery rate for testing.  There is some disagreement as to whether formal code inspection finds more defects than informal reviews.

Testing often discovers coding errors and deviations from the specification, whereas code review uncovers more problems related to maintainability or failure to meet requirements.  

Code review is also more effective at finding security vulnerabilities, provided that reviewers look for them!

## Kinds of Code Review

1. **Self Review** the developer carefully reads and reviews his own code.  Some guidelines are:
    - must take a break between writing code and reviewing it
    - be mentally "fresh". Don't review at the end of a day's work
    - plan what you will review for: code defects? standards defects? security issues?
    - use a separate reading for different review purposes. If you try to combine too many objectives in one reading you will miss many problems.
    - use a checklist and guidance
    - record errors you find, but finish the reading before you try to fix them

2. **Desk Check** ask another developer to review your code (at his desk).  Informal and useful to find defects and get ideas for improvement.

3. **Walkthrough** code review meeting with a small number of people, where one person presents or "walks through" the code line by line, while others look for defects, ask questions to improve their understanding, and share ideas for alternate implementations.

4. **Pair Programming** one person writes code while the other reviews and "navigates". Maybe not a "review" since it occurs at time of creation.

5. **Regular change-based reviews** whenever new code is committed to the code repository it is reviewed and approved by other team members.  This can be done remotely.
   - change-based reviews should have specific goals and be done as carefully as desk check
   - Pull Requests are example

6. **Formal Inspection** or **Code Review** a methodical review of artifacts (often using printouts) by a group, for the purpose of finding defects.  
   - Reviewers must prepare for inspections by reviewing the code individually before, and record issues and questions.
   - One person is designated as moderator, to facilitate an orderly meeting, make sure everyone has chance to speak, and ensure issues receive rapid follow-up and closure
   - Defects are acknowledged, refuted, or marked for further study during the inspection.
   - A written record is produced describing who participated, what was inspected, a list of defects or issues found with line ranges, and follow up status.
   - The code author must follow up on all issues and respond to each.
   - Reviewers subsequentally approve the author's resolution to each issue, or ask (with explanation) for further investigation


### Effective Review Rate

The rate depends on the programming language, experience of reviewers, and other factors, but in general should be at most **200 - 300 lines per hour**. Wikipedia has 200-400 lines/hr, but other sources cite 300 as upper limit, based on experical studies.

If you review too fast then you will overlook defects or lose opportunity to share understanding of the code.

## Checklists

A checklist will make your code reviews more consistent.

Good example checklists:

* [DZone Code Review Checklist](https://dzone.com/articles/sample-code-review-checklist) with 14 items.
* DZone [Java Review Checklist](Java-Code-Review-Checklist.pdf) with 5 categories of items
* [Stop More Bugs with our Code Review Checklist](https://blog.fogcreek.com/increase-defect-detection-with-our-code-review-checklist-example/) from Fog Creek Software.  Considered "pretty universal".
* [Checklist for Effective Code Reviews](http://www.evoketechnologies.com/blog/code-review-checklist-perform-effective-code-reviews/) by Surrender Gutha has basic and detailed versions.
* [Java Code Review Checklist](https://dzone.com/articles/java-code-review-checklist) nice -- divides review items into categories.
* Concise, practical [Checklist PDF](https://courses.cs.washington.edu/courses/cse403/12wi/sections/12wi_code_review_checklist.pdf) from U. of Washington.
* [Things to Include in your Checklist](https://www.codementor.io/blog/code-review-checklist-76q7ovkaqj) from codementor.io. High-level categories for reviews.
* [PSP Review Script Checklist](PSP-Review-Script-Checklist.pdf)

## Advise for Reviewers and Reviewees

[Thoughtbot](https://github.com/thoughtbot/guides/tree/master/code-review) describes how to approach code reviews and communicate effectively.

During reviews:

* Question, don't criticise.
* If you must criticise, criticize code not people.
* Try to see the author's perspective. Assume he had a reason for each thing.
* Be humble.
* Be explicit in writing, so others can clearly understand what you mean.
* Avoid hyperbole ("always", "never", "useless"); don't use sarcasm.

For authors of code under review:

* Don't take it personally. Review is about code, not you.
* Be grateful for suggestions.
* Assume best intention of reviewers.
* Be humble.
* Try to respond to every comment, and explain the code.

## Tools

* Notebook (paper) - project notebook is probably the best tool to get started.
* Gerrit tool for online code review, integrates with git.
* [Review Board][review-board] a web-based code review tool from MIT.
    - free if self-hosted, monthly fee if used as a hosted service
    - [reviewboard][review-board-github] on Github


### Important Security Vulnerabilities

Code Reviews should look for security vulnerabilities including:

- [ ] format string errors and exploits
- [ ] using or displaying unsanitized user input
- [ ] race conditions, where behavior may depend on timing of events.
- [ ] memory leaks (probably not an issue in Python)
- [ ] buffer overflows


## Resources

* Overview of [Code Review on Wikipedia](https://en.wikipedia.org/wiki/Code_review)
* [Reviews](Reviews-Stellman-and-Greene.pdf), Chapter 5 in *Applied Software Project Management* by Stellman and Greene.

* [Best Kept Secrets of Peer Code Review](www.codereviewbook.com) free download at  www.CodeReviewBook.com.  Describes 5 types of peer code reviews and how to do them.
  - Mirror [Best Kept Secrets of Peer Code Review](https://static1.smartbear.co/smartbear/media/pdfs/best-kept-secrets-of-peer-code-review_redirected.pdf)
* Summary of [Best Practices For Peer Code Review](https://www.kessler.de/prd/smartbear/BestPracticesForPeerCodeReview.pdf) from SmartBear.com
  - Their results seems biased.  They sell a tool for remote code review.

[review-board]: https://www.reviewboard.org/
[review-board-github]: https://github.com/reviewboard/reviewboard
