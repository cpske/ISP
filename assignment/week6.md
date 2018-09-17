## Homwork for Week 6

### Part 1. Complete all parts of the Django tutorial. 

Implement on your own computer and bring the runnable project with you to class next week.

**What about "Todo"?** The "Todo" app I mentioned in class is not required.
If you implement a Todo in Django, then add it as an "app" to the tutorial projet and show me in class. Some extra credit for this.

---

### Part 2. Create 5 good questions concerning important things for a software developer to know.  Submit on Github.

Create 5 questions with answers and references.

The questions can be related to:

* Software process 
* Good practices or habits, as in *Practices of an Agile Developer* or *The Clean Coder*
* Code related practices, such as using git, Github flow, coding style, unit testing
* Character or lifestyle related, as is *7 Habits of Highly Effective Developers*
* Anything you have learned that you think is important for a software developer, **even things we did not cover in this course**

Please make your questions clear, not tricky, and test the reader's understanding.  Try to ask in a way that the reader's answer can be objectively verified as correct or not.

Questions can be:

- [ ] multiple choice  
- [ ] fill in blanks (with or without a word list)
- [ ] short answer
- [ ] long answer
- [ ] put a sequence of items in order
- [ ] match left side items to right side
- [ ] find faults in code and identify or correct them.  But not syntax errors.

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
| Good question that tests understanding of fundamentals. | 5 |
| Good question that tests common software practices. | 5 |

Practice "code review". Ask someone else to review your questions and give feedback.

### Example

```
## Questions

Q1: Some software companies have specialists for requirements and software 
architecture (Architects) who are assigned to a project to do a specific job, 
but leave the project once their work is done.  A software architect creates 
a high level and sofware-level design, deployment design, gives these to the 
developers, and his work is done.    

According to [PAD][pad] what are 2 problems with having an architect create
a design, without participating in the implementation?  
Write 1 or 2 sentences to describe each of the problems.

## Answers

Q1: The tip "*Architects must write code*" notes that software design tends 
to evolve over time, and this can require changes in the architecture. 
Some issues are:

1. Its hard to come up with the best design without knowing details of actual 
system, and that understanding comes from building it.  The initial design may 
not be best or may not even be practical, and this won't be evident until some 
implementation is done. (contrary view: the architect may already has 
experience building similar systems.)

2. Handing over a design without conveying the reasons *why* the design is a 
particular way, loses some information.  That lost information could be useful 
in the implementation of the parts of the design.

3. [Martin Fowler][fowler-architects] argues that an architect's job includes 
"mentor the development team, to raise their level so that they can take on 
more comlex issues".

Ref: [PAD][pad] Tip 39 *Architects Must Write Code" and 
Martin Fowler ["Who Needs an Architect?"](https://www.martinfowler.com/ieeeSoftware/whoNeedsArchitect.pdf)

---

[pad]: https://se.cpe.ku.ac.th/doc/books/Programming "Practices of an Agile Developer"
