---
title: Agile Development Questions
---

These questions are based on these Tips from *Practices of an Agile Developer*. Each Tip is 3-4 pages:
   - Tip 2. Quick Fixes Become Quicksand
   - Tip 8. Question Until You Understand
   - Tip 25. Program Intently and Expressively
   - Tip 26. Communicate in Code
   - Tip 28. Code in Increments
   - Tip 30. Write Cohesive Code

Another important Tip:
   - Tip 19. Put Angels on Your Shoulders (value of testing)

Please read the Tips before answering the questions.

```
return self.size.value + 20*len(self.toppings)
```
---

### Instructions

You can change your answers after submission and resubmit up until the deadline.

### Questions

1. Which of the 6 "Tips" from Practices of an Agile Developer stress writing readable code?  4 points
   - [ ] Quick Fixes Become Quicksand
   - [ ] Question Until You Understand
   - [ ] Program Intently and Expressively
   - [ ] Communicate in Code
   - [ ] Code in Increments
   - [ ] Write Cohesive Code
   - key: 3 are correct. 1 pt each correct, +1 if totally correct (no wrong answers)

2. What are 2 things that a *team* can do to avoid code that is littered with quick fixes?  4 points
   - [ ] Require all methods be short (say, at most 20 lines).
   - [ ] Do regular code review.
   - [ ] Use code quality checkers like pylint for Python code.
   - [ ] Use unit testing (with high code coverage).
   - [ ] Use end-to-end tests (functional tests) to verify the application works.
   - 2 pt each correct. No credit if more than 2 answers checked.

3. What kind of information should you provide in documentation comments (docstring, Javadoc, etc.)?  5 points
   - [ ] The meaning of parameters and the return value.
   - [ ] Why the code is doing a specific computation.
   - [ ] The meaning of local variables.
   - [ ] Preconditions (requirements) and post-conditions (promises) of the method.
   - [ ] Exceptions thrown.
   - [ ] Detailed explanation of what each line of code does.
   - [ ] Purpose of the function or method.
   - Key: 4 are correct. 1 pt each + 1 if entirely correct. -1 ea for excessive wrong answers (checking everything)

4. What kind of information should you provide in single line comments that are in the method body (// comment in Java, #comment in Python)?  3 points
   - [ ] The meaning of parameters and the return value.
   - [ ] Why the code is doing a specific computation.
   - [ ] The meaning of local variables.
   - [ ] Preconditions (requirements) and post-conditions (promises) of the method.
   - [ ] Exceptions thrown.
   - [ ] Detailed explanation of what each line of code does.
   - [ ] Purpose of the function or method.
   - Key: only #2 is correct. 3pt, 2 pt if one incorrect checked, 1 pt if two incorrect checked.

5. Explain how the Tip "Code in Increments" can also help you write Cohesive Code (another tip). Answer in 1-2 complete sentences. Try to be concise.  4 points

   - Coding in short increments and taking breaks helps you to maintain perspective. You tend to stick to the purpose of writing the code, resulting in smaller, more cohesive code.

6. When writing an application in Django (or any web framework), it is tempting to put a lot of logic and code in a "view" method (other frameworks call this the "controller").  For example, first check the user is authenticated, then query the database to find all the information for that user, then select the info that the view wants, sort it, and render it in a template.  What Tip suggests that this is a bad idea?  Why?

   - Tip 30: Write Cohesive Code. When controller is doing too much it is difficult to test or understand and verify the code. Also makes it more likely to need changes.

7. What properties or principles are being violated by the view described in the previous question?
  - [ ] Low Coupling
  - [ ] Cohesion
  - [ ] Clarity
  - [ ] Single Responsibility
  - [ ] Testability


8. The Tips assigned this week primarily relate to what? Choose one best answer.
  - [ ] Adopt Agile development processes
  - [ ] Code quality and maintainability
  - [ ] Team work and/or iterative development
  - [ ] Testing and Verification
  - [ ] Incremental Development


## Part 2: Find the Tip

7. Many teams development plan has "Deploy to Heroku" scheduled for the end of November or start of Decemeber.  Which Tip explains why waiting until the end of the project for this is a bad idea?

8. What reason does the Tip give?

9. When you encounter a problem, you can often find a solution for it on StackOverflow.  You test the solution in some sample code and it works.  So, you use it your code.  Which 2 Tips advise you that you should do something more?


