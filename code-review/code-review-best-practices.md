## Code Review Best Practices from SmartBear

Ref: [Best Practices for Peer Code Review](https://www.kessler.de/prd/smartbear/BestPracticesForPeerCodeReview.pdf), somewhat self-promotional

1. Review fewer than 200-400 lines of code at a time

2. Aim for an inspection rate less than 300-400 LOC/hour

3. Use enough time for a proper, slow review, but not longer than 60-90 minutes
    - reviewer effectiveness drops off after 60 minutes

4. Authors should annotate source code before the review begins.
    By annotating his own code, 
    - author finds many bugs himself
    - helps reviewers understand the code or changes, hence saves time

5. Establish quantifiable goals for code review and capture metrics so you can improve your process
    - this requires you record some data about defect rates, support calls, etc., for comparison
    - not a vague, fuzzy goal like "find more bugs"

6. Use a checklist.  Checklists improve results
    - start with a standard checklist
    - add a personal checklist of your own common mistakes, or things you forget to review

7. Verify that defects are actually fixed!
    - the issues/defects often are not things that go into the project bug tracker
    - use a tool for defect tracking.  For class projects, Github issues are OK.
    - reviewers should verify the issues really were fixed, not just "closed".

8. Managers must foster a good code review culture in which finding defects is viewed positively
    - must take the postive view that finding defects improves the code and improves the developers' skills/knowledge
    - fosters good communication
    - don't criticize developers when defects are found. If you do, they won't look for defects.

9. Beware the "*Big Brother*" effect
    - be careful how metrics are used to avoid discouraging defect reporting
    - don't single out individuals based on metrics

10. The Ego Effect: Do at least some code review
    - Reviews encourage developers to improve their code quality out of a sense of pride or ego

11. Lightweight code reivews are efficient, practical, and effective at finding bugs
    - SmartBear claims that lightweight reviews find almost as many defects as formal inspections, but take less time

## 9 Code Review Best Practices from Perforce

Ref: [9 Code Review Best Practices](https://www.perforce.com/blog/qac/9-code-review-best-practices)

> For Participating in Peer Code Reviews

1. Know What to Look for in Code Reviews

2. Build and Test Before Code Reviews
   - use CI to build and test your code
   - use tools for static analysis and code quality

3. Don't Review Code for Longer Than 60 Minutes
   - and has a fresh mind *before* the review starts

4. Review No More than 400 Lines at a Time
   - if you try to review too much you will miss (overlook) more defects

5. Give Feedback That Helps (Not Hurts)
   - be constructive in feedback, not critical
   - ask questions rather than making statements
   - give (sincere) praise along with constructive feedback
   - approach code review as a learning process

> For Running Code Reivews

6. Communicate Goals and Expectations
   - be clear what the goals are, and what you expect from reviewers
   - give reviewers a checklist to ensure reviews are consistent

7. Include Everyone in the Code Review Process
   - both senior and junior developers should review and have their work reviewed

8. Foster a Positive Culture
   - create a positive culture for code improvement
   - teams should appreciate code reviews, not dread them

9. Automate to Save Time
   - use tools to automate what you can. Don't waste reviewers' time.
   - static code analysis to help find problems
       * Ex: uninitialize or unused variables, wrong parameters passed to function
   - IDE to find syntax errors
   - style checker(s) for coding style

## Best Practices from JetBrains

ref: [Code Review Best Practices](https://blog.jetbrains.com/upsource/2018/08/30/code-review-best-practices/) at https://blog.jetbrains.com. Transcript of their [video](https://youtu.be/EjwD7Pi7J_0)

1. Automate as much as possible
2. Agree on goals for Code Review
3. Use a common check list for review
4. Prepare for review
    * author should check his own code
    * annotate (comment) to help reviewers understand
5. During Review
    * Respond timely
    * Set clear expectations
    * Try to resolve review issues quickly
6. Close the Review when everyone is satisfied

Some of the best practices in the video apply to online reviews where reviewers work separately and asynchronously.  I tried to extratract the best practices that also apply to face-to-face reviews.
