---
title: Code Review Best Practices
---

[Code Review Best Practices from SmartBear](#best-practices-from-smartbear)    
[Code Review Best Practices from Perforce](#best-practices-from-perforce)    
[Code Review Best Practices from JetBrains](#best-practices-from-jetbrains)    


## Best Practices from SmartBear

Ref: [Best Practices for Peer Code Review](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review)    

1. Review fewer than 400 lines of code at a time

2. Aim for an inspection rate less than 400 LOC/hour (was: 300-400 LOC/hour)

3. Do not review for more than 60 minutes at a time
    - effectiveness drops after 60 minutes

4. Set goals
   - not a vague, fuzzy goal like "find more bugs"
   Capture Metrics
   - *What else*?

5. Author should annotate his source code before the review begins
   By annotating his own code: 
   - author finds many bugs himself
   - helps reviewers understand the code, saves time

6. Use a checklist.  
   - Checklists improve results
   - start with a standard checklist
   - add a personal checklist of your own common mistakes, or things you forget to review

7. Have a process to fix defects.
   - Verify that defects are actually recorded & fixed!

8. Foster a positive code review culture 
   - *positive* view toward finding defects (it improves the code!)
   - fosters good communication
   - don't criticize developers when defects are found
   > Someone asked Thomas Edison if he was discouraged after 1,000 failures
   > to create an electric light.
   > Edison replied positively, *each failure meant he was getting closer to the solution*

9. Embrace the subconscious implications of peer review
   - be aware of "Ego effect"

10. Practice Lightweight code review
    - lightweight review takes only 20% of a formal review but finds just as many bugs
    - "*a light-weight, tool-assisted process is recommended*"


## Best Practices from Perforce

Ref: [9 Code Review Best Practices](https://www.perforce.com/blog/qac/9-code-review-best-practices)

> For Participating in Peer Code Reviews

1. Know What to Look for in Code Reviews

2. Build and Test Before Code Reviews

3. Don't Review Code for Longer Than 60 Minutes

4. Review No More than 400 Lines at a Time

5. Give Feedback That Helps (Not Hurts)
   - be constructive in feedback, not critical
   - ask questions rather than making statements
   - give (sincere) praise along with constructive feedback
   - approach code review as a learning process

> For Running Code Reviews

6. Communicate Goals and Expectations
   - be clear what the goals are, and what you expect from reviewers
   - give reviewers a checklist to ensure consistent reviews

7. Include Everyone in the Code Review Process

8. Foster a Positive Culture
   - teams should appreciate code reviews, not dread them

9. Automate to Save Time
   - use tools to automate what you can. Don't waste reviewers' time.
   - static code analysis 
   - style checker(s)
   - IDE to find syntax errors


## Best Practices from JetBrains

Ref: [Code Review Best Practices][jetbrains] and [Video](https://youtu.be/EjwD7Pi7J_0)

[jetbrains]: https://blog.jetbrains.com/upsource/2018/08/30/code-review-best-practices/) 

Some of the best practices in the video apply to online reviews where reviewers work separately and asynchronously.  

I extracted the best practices that also apply to face-to-face reviews.

1. Automate as much as possible (JetBrains: *automate everything*)

2. Agree on Goals for Code Review

3. Use a Check List of what to review

4. Prepare for review
    - author should check his own code
    - annotate (comment) to help reviewers understand

5. During Review
    - Respond timely
    - Set clear expectations
    - Try to resolve issues quickly

6. Close the Review when everyone is satisfied

