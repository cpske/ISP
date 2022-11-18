---
Title: Solutions to Questions on Agile Tips
---

1. Which of the Tips stress writing readable code?
   - Program Intently and Expressively
   - Communicate in Code
   - Quick Fixes Become Quicksand

2. What are 2 things a team can do to avoid code littered with quick fixes?    
   According to the book:
   - [x] Use unit testing
   - [x] Do regular code reviews

3. What kinds of information should you provide in docstring comments on methods and functions?
   - [x] Meaning of parameters and return values
   - [x] Preconditions and post-conditions
   - [x] Exceptions thrown, and under what conditions
   - [x] Purpose of the function or method

4. What kinds of information should you provide in comments in the method body?
   - [x] Why the code is doing a specific computation

5. The assigned Tips this week primarily relate to what?
   - [x] Code quality and maintainability

6. When you encounter a problem, you can find a solution for it on StackOverflow.  You try the solution and it works.  So, you use it and continue work.    
   Which **2** Tips advise you that you should do something more? (One Tip you have to interpret beyond the explanation given in the book.)
   - [x] Quick fixes become quicksand
   - [x] Question until you understand

7. Explain how *Code in Increments* can help you write Cohesive Code.
   - By coding in increments, you have more opportunities to take a break and reflect on why you are writing a piece of code. That reduces a tendency to write code that goes beyond the original intent (less cohesive).
   - In those breaks, you may often think of ways to make the code shorter and more concise. That also can result in more cohesive code.
   - No Credit Due of Circular Logic:  "*Writing and Testing incrementally, tend to create methods that are smaller and classes that are more cohesive.*"
   - Partial Credit: "*You will create code that's clearer, simpler, and easier to maintain.*" (that does not mean it is cohesive)

8. Which Tip offers advice about Technical Debt?
   - Tip 2. Quick fixes become quicksand

9. Which Tip (any Tip in the book) suggests that waiting until deployment to adopt a PostreSQL database (instead of SQLite) may cause problems?
   - Best Answer: Different makes a difference
   - Acceptable: Integrate Early, Integrate Often

10. What reason does the Tip give for this?
    - Differences in software versions, OS, databases, and other tools may affect how your application works, the results it gives, and even whether it runs at all.  These differences are often unexpected and hard to anticipate, so you should test your code in the production environment from early in development, to find and correct any problems.

    - Github Actions will let you run tests in multiple environments. You can specify multiple version of Python, different operating systems, and different enviroments. So you could change the database by putting the database URL in the environment.
