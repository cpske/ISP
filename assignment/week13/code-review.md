---
title: Code Review Assignment
---

This is a team assignment, but **everyone** should do the reading and study.

1. Read Code Review best practices 
2. Write your own code review procedure or "script".
3. Study some example checklists and create your own.
4. Perform a code walkthrough and create a written summary.


### 1. Read Code Review Best Practices

1.1 Read these Code Review Best Practices (they are short).

* SmartBear: <https://www.kessler.de/prd/smartbear/BestPracticesForPeerCodeReview.pdf>
* Perforce: <https://www.perforce.com/blog/qac/9-code-review-best-practices>
* JetBrains: <https://blog.jetbrains.com/upsource/2018/08/30/code-review-best-practices/>

1.2 Which best practices will you apply to your project?  Choose the ones that are practical and useful. List them.

### 2. Create your own Code Review Procedure

Create a procedure or "script" for how you will do group code "walk-through".
The procedure helps everyone know what to expect and what needs to get done.

Before:

- What should be done before the review?
- What materials should be available for the review?

During:

- What should you do during the code review?
- Be specific

After:

- What should be done after the code review?  
- Who does it?


### 3. Create a Practical Checklist Tailored to Your Needs

A checklist reminds you what you should do during a review, walk-through, or individual review (such as a Pull Request).

- It should be things **that apply to your project**
- You should **update it** as you get experience doing reviews
  - add, remove, refine items in the checklist
- Write what you *actually* find useful to look for
- Try to make it short
- **No B.S.** copied from examples
- (Optional) Group items into categories so its easier to check them

Some examples (please don't copy them!):

- [Vacseen Project Checklist](https://docs.google.com/document/d/1sJqZ3WlXeycAEXh6zB1JEkJHjNAY0ihp8oIT0eFlDfk/edit) (2019)
- [KooCook Project Script & Checklist](https://docs.google.com/document/d/1GSI0FGx4NZyqwAVUOYt641X0tsdqfeRz3O-R3XnfGFE/edit) (2019)
- [KU Event Regis](https://docs.google.com/document/d/1pRlqTeCQEq9T0g3NPf8yt26aUKCSKC3rqEyI3L4xy_I/edit#heading=h.imm89g97i44a) (2019)
- [Real Estate Rental](https://docs.google.com/document/d/1plSBYDK-mYTJ-u1JY7BV-esmCcP8XGtpmY4gUwgzB0g/edit) (2020)

Poor Examples:

- [2019 Project](https://docs.google.com/document/d/1yKp1QEeML1Y40vKWtDQXcF1b86ywMhAMUPt1jFsnZ90/edit) 
  - some items are OK but most are too general and vague. 
  - Too vague or generic to be useful: "Refactor", "Check logic of the function", "Test quality", "Check line-by-line code" 
- [2020 Project](https://github.com/Jomsaruj/DEK-COM/wiki/Code%20Review%20Checklist) most things don't apply to code review. It is more like an "agile project checklist".


## 4. Perform a Code Walk-through & Create a Summary

- The whole team should participate.
- One person should write notes of issues raised, defects, work to follow up on.
- You might use a Google Doc so that everyone can write in it.
- Create Issues for defects & any work to follow-up on (even if not bugs). Write details in the Issue rather than in the summary report.
- (Optional) Use **tags** on issues to categorize them.

Written Summary should include: 

- what artifact was reviewed, including version number and URL (if online).
- why did you do the walk-through? what was the goal?
- who participated
- start & finish times, date
- summary of issues & important points. This can include defects, unanswered questions, suggestions for improvements, and more.
- to avoid duplication, write details of issues directly in your issue tracker and refer to them in your summary. Include a few words to describe it,  e.g. "Issue #42. Exception not handled or reported".
  - If you write the report in your Github wiki, there is markdown to reference issues.
- try to keep it short & don't waste time on beauty.
- no one reads long reports.

> Write the summary as if for a team member who missed the walk-through, or who wants to review it later.  Write just enough to inform him/her.


## What to Submit

1. Put the checklist and procedure (script) in your project wiki and provide **link(s)** in the main landing page of your project "Information Hub".
2. Create a summary (with date) on your Information Hub.  If you write the summary as a Google Doc, then include a link to it.  Be sure to share it with everyone.

## Grading Criteria

1. Use of good English in Checklist & Script.
2. Clarity and consistency.
3. Applies to your project and shows some thought. Not copied from examples.
   - No nonsense or stuff you don't actually do.
4. Content should be specific and practical.
5. Make use of automation tools. If something can be checked using a tool then do that instead of manual review; Coding style, for example.


