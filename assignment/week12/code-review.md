---
title: Code Walk-through Assignment
---

This is a team assignment, but **everyone** should do the reading and contribute.

1. Read the Code Review best practices.
2. Write your own Code Review procedure.
3. Create your own checklist that applies to your team & code.
4. Perform a code walkthrough and create a written summary.

For this course, "*code review*" means **walk-through**.


### 1. Read Code Review Best Practices

Read these Code Review Best Practices. They are short and each one has some unique ideas.

[Code Review Best Practices](https://cpske.github.io/ISP/code-review/code-review-best-practices#best-practices-from-perforce)

Apply whatever practices that you think are useful for your code walk-throughs.

### 2. Create your own Code Review Procedure

Create a simple procedure for how your team will do code "walk-through".
The procedure informs everyone know what to expect and what needs to be done.

Procedure should be brief instructions for "*How we do code walk-throughs*".  Be *specific* but not long or formal.

You probably want to include:

*Preparation*:

- What should be done before the review?
- What items should be available for the review?

*Perform The Review*:

- How is it conducted?  
  - A big monitor everyone can see is great.
  - Do you use a review or code-sharing tool?
- What should everyone do during the code review?
- Be specific

*Afterwards or Follow-up*:

- What should be done after the code review?  
- Who does it?
- What should be the final result?
- should include where the written summary of the walk-through posted on your information hub.


### 3. Create a Practical Checklist Tailored to Your Needs

Create a checklist of things you should check (or do) in a walk-through.

- It should be things **that apply to your project**
- You should **update it** over time, based on experience
  - add, remove, refine items in the checklist
- Write what you *actually* find useful. What defects to you actually make?
- Minimalism. Try to make the checklist short, at least initially.
- Checklist can include things to do other than reviewing code.
- (Optional) Group the items into categories so its easier to do them

Some examples (please don't copy these!):

- [KU Event Regis](https://docs.google.com/document/d/1pRlqTeCQEq9T0g3NPf8yt26aUKCSKC3rqEyI3L4xy_I/edit#heading=h.imm89g97i44a) (2019)
- [Real Estate Rental](https://docs.google.com/document/d/1plSBYDK-mYTJ-u1JY7BV-esmCcP8XGtpmY4gUwgzB0g/edit) (2020)

Poor Examples:

- [2019 Project](https://docs.google.com/document/d/1yKp1QEeML1Y40vKWtDQXcF1b86ywMhAMUPt1jFsnZ90/edit) 
  - some items are OK but most are too general and vague. 
  - Too vague or generic to be useful: "Refactor", "Check logic of the function", "Test quality", "Check line-by-line code" 
- [2020 Project](https://github.com/Jomsaruj/DEK-COM/wiki/Code%20Review%20Checklist) most things don't apply to code review. It is more like an "agile project checklist".


## 4. Perform a Code Walk-through & Write a Summary

1. The whole team should participate.
3. Create Issues for defects & anything else to follow-up on even if not bugs.. 
3. Write **details in the Issue** rather than in the summary report.
4. (Optional) Add **tags** to issues to categorize them. 
   - Example tags: "bug", "enhancement", "suggestion", "question"
5. Write a summary of issues raised, defects, and other work to follow up on.
   - Summary can be a Google Doc to enable shared editing.

Written Summary should include: 

- Date
- Who participated
- what was reviewed, including version number and Github URL (if online).
- table or list of issues & important points. This can include defects, unanswered questions, suggestions for improvements, and more.
- avoid duplication. Write details of issues in your issue tracker.  In the summary write issue number and a brief description.
  - Example "#42. Exception not handled or reported".
  - Github Wiki has markdown syntax to reference Github issues.

The summary should be short. If it's long no one will read it. :-)

> Write the summary for an imaginary team member who missed the walk-through. Write just enough to inform him/her.
> Suppose it was *you* that missed the walk-through. What would you want to know?

## Grading Criteria

1. Use of good English in Code Review Procedure & Checklist.
2. Clarity and consistency.
3. Applies to your project and shows **thought**. Not copied from examples.
   - No nonsense or stuff you don't really do.
4. Content should be specific and practical. Short but complete.
5. Make use of automation tools. If something can be checked using a tool then do that instead of manual review.
