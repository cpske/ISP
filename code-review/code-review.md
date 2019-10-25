## Benefits of Code Review

* *Find defects* including coding and logic errors, performance problems, security vulnerabilities
* *Better code quality* improve the implementation, readability, uniformity, and (as a consequence) maintainabiility
* *Finding better solutions* by sharing new ideas
* *Knowledge Transfer* - approach and technology used, and rationale for the implementation/solution.  Code reviews are a good way for more experienced developers to share knowledge with others.
* *Increase Collective Ownership* of code

## Code Review versus Testing

Studies find that code reviews find around 60% of *latent defects*, versus 30-40% discovery rate for testing.  There is some disagreement as to whether formal code inspection finds more defects than informal reviews.

Testing often discovers coding errors and deviations from the specification, whereas code review uncovers more problems related to maintainability.  Code review is also effective at finding security vulnerabilities, provided that reviews look for them!

## Kinds of Code Review

1. *Desk Check* the developer carefully reads and reviews his own code.  Some guidelines are:
    - must take a break between writing code and reviewing it
    - be mentally "fresh". Don't review at the end of a day's work
    - plan what you will review for: code defects? standards defects? security issues?
    - use a separate reading for different review purposes. If you try to combine too many objectives in one reading you will overlook many problems.
    - use a checklist and guidance
    - record errors you find, but finish the reading before you try to fix them

2. *Walkthrough* code review meeting with a small number of people, where one person presents or "walks through" the code line by line, while others look for defects, ask questions to improve their understanding, and share ideas for alternate implementations.

3. *Pair Programming* one person writes code while the other reviews and "navigates".

4. *Regular change-based reviews* whenever new code is committed to the code repository it is reviewed and approved by other team members.  This can be done remotely.
    - change-based reviews should have specific goals and be done as carefully as desk check
    - tools can be used to assist change-based reviews such as code checkers and "diff" viewers.

5. *Formal Inspection* a methodical review of code (often using printouts) by a group, for the purpose of finding defects.  
    - Reviewers must prepare for inspections by reviewing the code individually before the meeting, and recording issues they find.
    - One person is designated as moderator, to facilitate an orderly meeting, make sure everyone has chance to speak, and ensure all issues receive rapid follow-up and closure
    - Defects are acknowledged, refuted, or marked for further study in the inspection meeting.
    - A written record is produced describing who participated, what was inspected, a list of defects or issues found with line ranges, and follow up status.
    - The code author must follow up on all issues and write what was done.
    - Reviewers must subsequentally approve the author's resolution to each issue, or ask (with explanation) for further investigation

### Important Security Vulnerabilities

Code Reviews should look for security vulnerabilities including:

- [ ] format string errors and exploits
- [ ] using or displaying unsanitized user input
- [ ] race conditions, where behavior may depend on timing of events.
- [ ] memory leaks (probably not an issue in Python)
- [ ] buffer overflows

### Effective Review Rate

The rate depends on the programming language, experience of reviewers, and other factors, but in general should be at most **200 - 300 lines per hour**. Wikipedia has 200-400 lines/hr, but other sources cite 300 as upper limit, based on experical studies.

If you review too fast then you will overlook defects or lose opportunity to share understanding of the code.

## Tools

* Notebook (paper) - project notebook is probably the best tool to get started.
* Gerrit tool for online code review, integrates with git.
* [Review Board][review-board] a web-based code review tool from MIT.
    - free if self-hosted, monthly fee if used as a hosted service
    - [reviewboard][review-board-github] on Github

## Resources

* Overview of [Code Review on Wikipedia](https://en.wikipedia.org/wiki/Code_review)

* [Best Kept Secrets of Peer Code Review](www.codereviewbook.com) free download at  www.CodeReviewBook.com.  Describes 5 types of peer code reviews and how to do them.
    - Mirror [Best Kept Secrets of Peer Code Review](https://static1.smartbear.co/smartbear/media/pdfs/best-kept-secrets-of-peer-code-review_redirected.pdf)
* Summary of [Best Practices For Peer Code Review](https://www.kessler.de/prd/smartbear/BestPracticesForPeerCodeReview.pdf) from SmartBear.com
    - Their results seems biased to me.  They sell a tool for remote code review.
    - In the Cisco study they did not allow in-person meetings for code review (bias).

[review-board]: https://www.reviewboard.org/
[review-board-github]: https://github.com/reviewboard/reviewboard
