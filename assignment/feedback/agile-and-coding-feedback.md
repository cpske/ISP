---
title: Answers to Agile and Coding Practices Assignment
---

Q1. Why develop in increments (Tip 17)?
   * Get quicker feedback which reduces risk from misunderstanding between customer and developers
   * Helps developers stay focused on current task(s) since deadline and scope of work is smaller
   * Achieve frequent milestones and demonstrate progress. An agile axiom is running code is the only real measure of progress.
   * Not correct: "Keep your code deployable at all times". You could do that without using incremental development.

Q2. How to stay on track, write small, cohesive code.
   * Tip 28. Write code in short edit/build/test cycles.
   * 1pt: 17. Develop in increments.
   * 1pt: 30. Keep classes focused and components small.

Q3. Why treat warnings as errors (Tip 34)?
   * Some warnings are really semantic or logic errors, but the compiler or other tools can't be sure its an error, so they issue a warning.
   * Improves quality of code (e.g. warnings for unused variable or import or bad practices).
   * In Python where variable types are dynamic, a warning might actually be an error, but the tool issuing the warning (e.g. IDE) can't be sure.
   * Warnings are given for deprecated features.  This is something that is allowed now but may be removed in the future.  A Python example is `TestCase.assertEquals( )`.  Python warns you to use `assertEqual` instead and may eventually remove `assertEquals` from the API.
   * Incorrect Answer: "*warnings may become errors in the future*". Too vague and lacks explanation.
   * Incorrect Answer: "*if you ignore warnings they will become big problem in the future*". Too vague and not true.

Q4. What does "quick fixes become quicksand" mean (Tip 2)?
   * Code becomes hard to maintain when its riddled with quick fixes.
   * Clarity goes down.  Makes code difficult to modify or enhance.
   * Incorrect: "Invest the energy to keep code clean and out in the open." this is advise but does not explain what the phrase means or why quick fixes become quicksand.
   * Incorrect: any answer copied from the book.  Don't copy.
   * Incorrect: "*if you use quick fix you're code will have big problem in the future*"  Doesn't answer the question and not necessarily true.

Q5. 3 things to avoid quick fixes.
   * Encourage team to review and understand code.
   * Use unit tests.
   * Fully understand code and the cause of the problem before fixing it.

Q6. fibonacci(-4)
   - [x] Throw exception.
   - Reason: fibonacci is part of a public API.  If a programmer calls it with an invalid parameter that's violating the "contract" of the API.  The code should inform him that he made a mistake. The best solution is to throw an Exception.

Q7. indexOf(list, item)
   - [x] return -1
   - OK but not good: Throw exception.
   - Reason:  searching for something that isn't in the collection is still a legitimate use of `indexOf`, so return a special value to indicate not found.  The Java String methods do this. Python throws an exception, but I think its a bad design.

Q8. An Arcade game has a `jump(how_much)` method called from within the game only.  If `how_much` is negative, what should the method do?
   - [x] Use an Assert statement to catch the invalid parameter value.
   - Reason: Assert is used in development to help find bugs and a form of documentation in code.  The programmer shouldn't call `jump` with `how_much < 0`, and since its his code he should be aware of this.  `how_much < 0` probably indicates a bug somewhere in the code, so use assert to flag the problem.  When code is released to users, you can disable asserts.
   - In Production you can disable Asserts (you can't disable ordinary Exceptions).  A game where the player sometimes refuses to jump is better than a game that crashes with an Exception message.

Q9. The code is ignoring exceptions.
   * Tip 36. Handle or propagate all exceptions.
   * OK (but not as good): Tip 26. Comment to Communicate (Communicate in Code)
   * Not: Tip 37 Present useful error messages. (you have to do Tip 36 before this, and the caller should decide if the error is something to present to the user.)

Q10. What about the comments in `read_dictionary`?
   * They just repeat what is obvious from reading the code.  That's not a good use of comments.
   * Tip 26: Comment to Communicate.

Q11. What else needs improvement in `read_dictionary`?
   * The URL to read is hard-coded as a string.  That's always a bad practice.  The URL should be a parameter to the function, or (at least) assigned to a string constant so it can be easily found if you need to change it.
   * The line `words.append( line.decode().strip() )` is complex and maybe hard to understand.  Break it into 2 statements and use an *explanatory variable* such as:
    ```python
    # input line is a b-string and may contain whitespace chars. Normalize it.
    word = line.decode().strip()
    #TODO: could the dictionary contain blank lines? Verify len(word) > 0
    words.append( word )
    ```

Q12. Good use of comments?
   * Describe the purpose of code.
   * Document preconditions and constraints.
   * Docoument exceptions that might be thrown.
   * Explain *why* a block of code is needed.
   * Incorrect: explain code to inexperienced programmers.
   1 point each, +1 if all correct.

------

## References

* [Practices of an Agile Developer][pad-refcard] quick reference
* [Practices of an Agile Developer][pad] book download. 
* [Clean Code][clean-code] by Robert Martin
* [7 Habits of Highly Effective Programmers][7-habits-programmer] applies Steven Covey's *7 Habits* to programming.

<!-- references in this file won't appear in formatted output. -->

[sebooks]: https://se.cpe.ku.ac.th/doc/books/Programming/
[clean-code]: http://www.investigatii.md/uploads/resurse/Clean_Code.pdf "Clean Code by Robert Martin"
[pad-refcard]: https://media.pragprog.com/titles/pad/PAD-pulloutcard.pdf "Practices of an Agile Developer Quick Reference"
[pad]: https://github.com/mart0/Useful-materials---books-presentations-ant-etc./raw/master/Others/Practices%20of%20an%20Agile%20Developer.pdf "Practices of an Agile Developer, on Github"
[pragmatic-programmer]: https://www.nceclusters.no/globalassets/filer/nce/diverse/the-pragmatic-programmer.pdf "The Pragmatic Programmer by Andrew Hunt"
[7-habits-programmer]: https://simpleprogrammer.com/7-habits-highly-effective-programmers/ "7 Habits of Highly Effective Programmers"
[google-classroom]: https://classroom.google.com/u/0/c/MTQ5OTI2OTQ3MTJa "Classroom for ISP2018"
