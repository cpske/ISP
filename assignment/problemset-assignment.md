---
title: Create One Good Question or Problem 
---

Create one question or problem related to software development that *you think everyone in the class should know* or would benefit from knowing.

The best submissions will be used on the final exam.

You can create more than one question if you want.  If so, please email me so I watch for them.

Some suggested topics are given below.  

#### Guidelines

1. The question should be something where the answer can be objectively evaluated as correct or not.
2. Please make your question or problem clear, not tricky, and test the reader's understanding of the subject or ability to perform.  
3. You may provide background information to help other students understand the problem.
   - especially if its a topic we have not covered in class
   - this is encouraged. Help your fellow students learn.
4. For technical questions, you may need to include some instructional information.  For example, describe a refactoring pattern and then ask students to apply it to code.
5. Provide at least one reference where someone can learn how to answer the question.  
   - the reference should be *specific*, not a whole book!

#### Sample Question Areas

* Software process-related question
* Question based on one or more tips from *Practices of an Agile Developer* or *The Clean Coder* (another famous book similar to *PAD*)
* Refactoring, such as identify and perform a refactoring of code
* Mock objects for testing
* Any other testing skill
* Apply basic design principles, like the SOLID principles
* Basic design patterns
* Anything you have learned that you think is important for a software developer to know

#### How to Submit

1. Clone the master branch of https://github.com/isp19/problems
  * Students who **still** haven't joined the ISP19 Organization need to watch for and respond to invitation.
  * It may help to clone from the initial commit (instead of head), to avoid cloning others' work
2. Create a new **branch** using your first name, such as `fatalai` for Fatalai Jon.
3. Put all your content in a folder that describes the topic or problem.  Use lowercase names with "-" (no space or underscore).
   ```
   git branch fatalai
   git checkout fatalai
   mkdir refactor-classes
   cd refactor-classes
   git add README.md
   git add person.py
   git add ...
   ```
4. After verifying your code and documents, push the branch to Github.
    - check markdown and hyperlinks
    - use pylint to check code
    - use Google Docs or Office 360 to check English
    - ask a friend to try your problem
5. Open a **Pull Request**.  Wait for students, TAs, and instructor to offer feedback and recommendation.
    - Everyone should help review problems.
    - If you approve a branch, add a comment with "+1" and some text.
    - If you think its not suitable or needs more work, add a comment with "-1" and text explaining why. 
6. Instructor and TAs will merge branch into master.


#### Some Question Formats 

- multiple choice
- fill in blanks (with or without a word list)
- short answer (one or two sentences)
- match left side items to right side
- find faults in code and identify or correct them.  But not syntax errors.
- identify poor code and how to improve it.
- give some code and ask reader to do something with it (refactor, apply design pattern, write a test, identify design pattern)
- give partial code and ask reader to complete a critical part.
     * this is a good format because it focuses students' effort and is easier to evaluate


A question can instruct to answer based on some short reading (e.g. "according to this article, what is xxx?"), a Tip from PAD ("what would Tip 19 recommend you do for ..." or "which PAD tip would help fix this problem"), a section from *Clean Code*, or a short article on the web.  


### Grading

| Description   | Score |
|---------------|-------|
| Copy of a question already given in this course |  0  |
| Markdown errors so question does not display correctly | 0 |
| Trivial or shallow. A lay person could easily guess   | 1 |
| Question OK but poorly worded or multiple grammar errors | 3-4 |
| Good question that tests understanding | 5 |
| Good question that also teaches something new | 5+ |


### Example

Question 1:    
Some student teams habitually wait until almost the end of each iteration
to finish and test their work.  They may have a few members who start
and finish early, but they are held back by others not doing their part.
Usually the outcome is:

* the application doesn't run at end of iteration, or
* application works, but code contains defects or poor code that need to be revised in next iteration

What Tips would PAD offer to improve their process?

Question 2:    
How could you use project tools or process to spot these problems?

More Examples:   
Look for more examples in the repository, including branches.

## Answers

Answer 1:    
Tip 9 *Tackle tasks before they bunch up* and Tip 13 *Keep your project releasable* apply here.  However, its up to team members to follow the recommendations.  The team leader, as coach or facilitor, can help by working with procrastinators to find out why they are late and suggest solutions.

Some tips that **don't** apply are:
* Tip 14. *Integrate early, integrate often* - that presumes you have code ready to integrate.  The problem here is not pacing their effort level.
* Tip 28. *Write code in short edit/build/test cycles* - that is an individual coding practice. It doesn't keep members from procrastinating.
* Tip 44. *Review all code* - the problem here is that code is finished too late for review.  

Anwswer 2:    
There are any tools and practices that could help?  Here are a few.

* Activity on Github, by committer.  You can see *when* and *how much code* each person is committing over time.    
    If someone repeatedly waits 'til end of iteration to commit it, its a warning sign.
* A task board.  Tasks should show progress over time.
* Daily stand-up meetings, as in Scrum. Members report what they did since prior meeting. Students aren't full-time developers, so meetings may be less often.  There should be a commitment by everyone on when they will work on the project. Schedule meetings based on that.
* Frequent milestones, even small ones, to indicate progress.     
At start of iteration, agree on a date that milestone should be done.
* Weekly Milestones are helpful if iteration is longer than one week.


---

[pad]: https://se.cpe.ku.ac.th/doc/books/Programming "Practices of an Agile Developer"
[fowler-architects]: https://www.martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf "Who Needs an Architect?"
