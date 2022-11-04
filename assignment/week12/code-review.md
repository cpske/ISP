---
title: Code Review Assignment
---

This is a team assignment, but **everyone** should do the reading and contribute.

1. Read the Code Review best practices.
2. Write your own code review procedure.
3. Study some example checklists and create your own checklist.
4. Perform a code walkthrough and create a written summary.

For this course, "code review" means walk-through.


### 1. Read Code Review Best Practices

Read these Code Review Best Practices. They are short and each one has some unique ideas.

* SmartBear: <https://www.kessler.de/prd/smartbear/BestPracticesForPeerCodeReview.pdf>
* Perforce: <https://www.perforce.com/blog/qac/9-code-review-best-practices>
* JetBrains: <https://blog.jetbrains.com/upsource/2018/08/30/code-review-best-practices/>

Choose the best practices that you think are useful for your code reviews and apply them.

### 2. Create your own Code Review Procedure

Create a procedure for how you will do group code "walk-through".
The procedure helps everyone know what to expect and what needs to be done.

Don't try to be formal or comprehensive. The procedure should be brief instructions for "*How we do code walk-throughs*".

You probably want to include:

*Preparation*:

- What should be done before the review?
- What materials should be available for the review?

*Perform The Review*:

- What should you do during the code review?
- Be specific

*Afterwards or Follow-up*:

- What should be done after the code review?  
- Who does it?
- What should be the final result?
- Result should include where the written summary of the walk-through posted on your wiki or Google Docs.


### 3. Create a Practical Checklist Tailored to Your Needs

Create a checklist of things you should do for a review, walk-through, or individual review (such as a Pull Request).

- It should be things **that apply to your project**
- You should **update it** over time, based on experience
  - add, remove, refine items in the checklist
- Write what you *actually* find useful
- Be minimalist. Try to make the checklist short, at least initially.
- Checklist can include things to do other than reviewing code.
- (Optional) Group the items into categories so its easier to do them

Some examples (please don't copy them!):

- [KU Event Regis](https://docs.google.com/document/d/1pRlqTeCQEq9T0g3NPf8yt26aUKCSKC3rqEyI3L4xy_I/edit#heading=h.imm89g97i44a) (2019)
- [Real Estate Rental](https://docs.google.com/document/d/1plSBYDK-mYTJ-u1JY7BV-esmCcP8XGtpmY4gUwgzB0g/edit) (2020)

Poor Examples:

- [2019 Project](https://docs.google.com/document/d/1yKp1QEeML1Y40vKWtDQXcF1b86ywMhAMUPt1jFsnZ90/edit) 
  - some items are OK but most are too general and vague. 
  - Too vague or generic to be useful: "Refactor", "Check logic of the function", "Test quality", "Check line-by-line code" 
- [2020 Project](https://github.com/Jomsaruj/DEK-COM/wiki/Code%20Review%20Checklist) most things don't apply to code review. It is more like an "agile project checklist".


## 4. Perform a Code Walk-through & Create a Summary

- The whole team should participate.
- One person should write a summary of issues raised, defects, work to follow up on.
- Consider using a Google Doc so that everyone can write at the same time.
- Create Issues for defects & any work to follow-up on (even if not bugs). Write details in the Issue rather than in the summary report.
- (Optional) Use **tags** on issues to categorize them.

Written Summary should include: 

- what artifact was reviewed, including version number and URL (if online).
- why did you do the walk-through? what was the goal?
- who participated
- start & finish times, date
- summary of issues & important points. This can include defects, unanswered questions, suggestions for improvements, and more.
- to avoid duplication, write details of issues directly in your issue tracker and refer to them in your summary. In the summary, write only a few words to describe it and refer to the issue,  e.g. "Issue #42. Exception not handled or reported".
  - The Github wiki has markdown syntax to reference Github issues.
- try to keep it short. Don't waste time on beauty.
- no one reads long reports.

> Write the summary as if for a team member who missed the walk-through, or who wants to review it later.  Write just enough to inform him/her.


## What to Submit

1. Put your code review checklist and procedure in your project wiki and provide **link(s)** in the main landing page of your "Information Hub".
2. Create a summary (with date) of your code walk-through on your Information Hub.  If you write the summary as a Google Doc, then include a link to it.  Be sure to share with everyone.

## Grading Criteria

1. Use of good English in Checklist & Script.
2. Clarity and consistency.
3. Applies to your project and shows some thought. Not copied from examples.
   - No nonsense or stuff you don't actually do.
4. Content should be specific and practical.
5. Make use of automation tools. If something can be checked using a tool then do that instead of manual review; Coding style, for example.
