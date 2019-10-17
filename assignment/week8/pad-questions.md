### Create 3 good questions concerning important things for a software developer to know.  Submit on Github.

Create 3 questions with answers and references.

2 questions should relate to process or best practices, such as in the book *Practices of an Agile Developer*.

1 question should relate to technical skill or knowledge.  This includes basic refactoring or testing, version control, and design principles or design patterns.

Submit your answers to this Github Assignment: https://classroom.github.com/a/C6UQUlz7

Use a file named `questions.md`.  You may also commit other files, such as images, a file of code, or PDF used in your questions.

The questions can be related to:

* Software process 
* Good practices or habits, as in *Practices of an Agile Developer* or *The Clean Coder*
* Code related practices, such as using git, Github flow, coding style, unit testing
* Anything you have learned that you think is important for a software developer, **even things we did not cover in this course**

1. Please make your questions clear, not tricky, and test the reader's understanding.  
2. Try to ask in a way that the reader's answer can be objectively verified as correct or not.
3. Provide at least one reference where someone could learn how to answer it.

Questions can be:

- [ ] multiple choice  
- [ ] fill in blanks (with or without a word list)
- [ ] short answer (one sentence)
- [ ] match left side items to right side
- [ ] find faults in code and identify or correct them.  But not syntax errors.
- [ ] identify poor code and how to improve it.

A question can instruct user to answer based on some short reading (e.g. "according to this article, what is xxx?"), such as a Tip from PAD, a section from *Clean Code*, or a short article on the web.  

**Format**     

1. Create a file named `questions.md` in this Github Classroom Project.
2. Use Markdown format.
3. **Numbering:** Number questions Q1, Q2, ..., Q5 and answers A1, A2, ..., A5.
This will avoid the Markdown processor renumbering your questions.

### Grading

| Description   | Score |
|---------------|-------|
| Copy of a question already given in this course |  0  |
| Markdown error so question does not display correctly | 0 |
| Trivial or shallow. A lay person could easily guess   | 1 |
| Question OK but poorly worded or multiple grammar errors. | 2-3 |
| Good question that tests understanding. | 5 |

Practice "code review". Ask someone else to review your questions and give feedback.

### Example

Q1: 
Some student teams hatiually wait until almost the end of each iteration
to finish and test their work.  They may have a few members who start early
and finish early, but they are held back by others not doing their part.
Usually the outcome is one of these:

* the application doesn't run at end of iteration
* application works, but code review shows there are defects and poor code that need to be revised in next iteration

What Tips would PAD offer to improve their process?

Q2. How could you use project tools or process to spot these problems?

## Answers

A1: Tip 9 *Tackle tasks before they bunch up* and Tip 13 *Keep your project releasable* apply here.

Some tips that **don't** apply are:
* 14. *Integrate early, integrate often* - that presumes you have code ready to integrate.  The problem here is not pacing their effort level.
* 28. *Write code in short edit/build/test cycles* - that is an individual coding practice. It doesn't keep members from procrastinating.
* 44. *Review all code* - the problem here is that code is finished too late for review.  

Q2. There are many tools and practices that could help.  Here are a few.

* Activity on Github, by member.  You can see how much each person is committing over time.
* Activity on task board.  If tasks aren't progressing, its a bad sign.
* Use smaller tasks, to better show progress.
* Daily stand-up meetings, as in Scrum, so members report what they did. Students aren't full-time developers, so meetings may be less often.  There should be a commitment by everyone on when they will work on the project. Schedule meetings based on that.
* Frequent milestones, even small ones, to indicate progress.


---

[pad]: https://se.cpe.ku.ac.th/doc/books/Programming "Practices of an Agile Developer"
[fowler-architects]: https://www.martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf "Who Needs an Architect?"
