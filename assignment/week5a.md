# Homework for Week 5, Part 1.

1. Read the *Practices of an Agile Developer* (PAD) [Quick Reference][pad-refcard].  For some items you'll need to read the section in the *Practices of an Agile Developer* [book][pad].

2. Answer these questions in the Week5 Classwork on [Google Classroom][google-classroom].

The questions and references are posted here because
Google Crummy Classroom doesn't enable text formatting in questions.

------

## Answers

1. Why dev in increments (Tip 17)?
   * Get feedback --> reduce risks
   * Helps developers stay focused
   * Achieve frequent milestones and demonstrate progress. An agile axiom is running code is the only real measure of progress.
   * Not correct: "Keep your code deployable at all times". You could do that without using incremental development.

2. Stay on track, write small, cohesive code.
   A: 28. Write code in short edit/build/test cycles.
   5pt: 17. Develop in increments.
   5pt: 30. Keep classes focused and components small.

3. Why treat warnings as errors (Tip 34)?
   * Some warnings are really semantic or logic errors.
   * Improves quality of code (e.g. unused variable or import).
   *

4. What does "quick fixes become quicksand" mean (Tip 2)?
   * Code is hard to maintain.
   * Clarity goes down. Cannot be modified.
   * Incorrect: "Invest the energy to keep code clean and out in the open." this is advise but does not explain what the phrase means or why quick fixes become quicksand.

5. 3 things to avoid quick fixes.
   * Encourage team ... understand code.
   * Use unit tests.
   * Fully understand code before fixing it.

6. fibonacci(-4)
   - [x] Throw exception.
     OK: Assert error

7. game.moveto(piece,x,y) x,y invalide
   - [x] Assert error
   - OK: Throw exception

8. indexOf(array,item)
   - [x] return -1

9. Code ignoring exceptions.
   36. Handle or propagate all exceptions.

10. Good use of comments?
   * Describe purpose of code.
   * Document preconditions.
   * Dcoument exceptions.
   2pt each correct answer.
   checking incorrect answers: no penalty for 1 incorrect,
     -1 for 2-3 incorrect.
------

## Questions

These questions refer to material in *Practices of an Agile Developer* ([Refcard][pad-refcard] and [book][pad]). *[Clean Code][clean-code]* is also useful for answering these question.
If these links don't work, try the [se books][sebooks] collection.

1. Why develop in increments? (PAD Tip 17)

2. To ensure that your code is on the right path, and encourage you to write smaller, more cohesive code, what does PAD recommend?  Enter the Tip *number* and *title* from the PAD Quickref, such as: *1. Blame doesn't fix bugs.*

3. Why should we "treat warnings as errors"? (PAD Tip 34)

4. PAD Tip 2 is "Quick Fixes Become Quick Sand" (or "Don't Fall for the Quick Hack").  What does this mean?

5. What are 3 things the PAD book recommends you do to avoid or correct quick fixes?
  - [ ] Use Test-driven-development.
  - [ ] Encourage team members to review and understand all code.
  - [ ] Use unit tests; they help you design code into manageable pieces and provide runnable documentation.
  - [ ] Assign ownership of parts of the code to individual team members.
  - [ ] Never implement a fix without fully understanding the code and cause of the problem.

In writing a function or method, there are 4 ways to handle a problem or unexpected condition:

   - do nothing and return, or return a special value (such as -1 or null) 
   - throw an Exception
   - use an Assert statement to check parameter values and raise an Assert error
   - print a message on the console (Java `System.out`), then return

For each of the situations below, which is the best solution?

6. As part of a library, you write a `fibonacci(n)` method that returns Fibonacci numbers, for `n >= 0`. 
What should you do if `fibonacci(n)` is called with a value `n < 0`?
   - [ ] Return -1 to indicate invalid parameter value.
   - [ ] Use an Assert statement to raise AssertError when `n < 0`.
   - [ ] Throw an exception, such as Python TypeError or Java IllegalArgumentException.
   - [ ] Print error message on the console and return 0.

7. A chess game has an 8x8 chessboard with a graphical UI (GUI).  When user makes a move on the GUI, the controller receives the input and calls `void game.moveTo(x,y)`, similar to TicTacToe.  What should `game` do if the controller calls `game.moveTo(x,y)` with values not on the chessboard, such as `x` > 8 or `y` > 8?
   - [ ] Just do nothing (return). 
   - [ ] Use an Assert statement to raise AssertError when `x` or `y` are invalid.
   - [ ] Throw an exception, such as Python TypeError or Java IllegalArgumentException.
   - [ ] Print an error message (e.g. "Invalid Move") on the console and return.

8. You write a `indexOf(array[],value)` method to return the index of `value` 
in an array. What should you do if `value` is not in the array?
   - [ ] Return -1 to indicate value not in array.
   - [ ] Use an Assert statement to raise AssertError.
   - [ ] Throw an exception, such as NotFoundException.
   - [ ] Print error message on the console and return 0.

9. Suppose your application reads a list of words from a URL, such as this:
```python
import urllib.request
import urllib.error

def read_dictionary():
    """Read a dictionary of words and return them as a list"""
    words = []
    try:
        input = urllib.request.urlopen("http://se.cpe.ku.ac.th/dictionary.txt")
        for line in input:
            # convert line from bytes to unicode, strip whitespace and newline
            words.append( line.decode().strip() )
    except HTTPError:    # this is like Java "catch(HttpError e)"
        return []        # return an empty list
    return words
```
Which Tip from *Practices of an Agile Developer* Reference Card tells you that you should improve this code?  Write the **number** and **title** of the Tip on the Quick Ref, such as: *1. Blame doesn't fix bugs.*

10. What are good uses of comments? (Check all correct answers.)
  - [ ] Make is easy for inexperienced programmers to understand the code.
  - [ ] Describe the purpose or code, e.g. what it is trying to do.
  - [ ] Explain the code, line by line.
  - [ ] Document preconditions or constraints.
  - [ ] Document what value a variable holds, such as "// first name" for firstName.
  - [ ] Document what exceptions and thrown under what conditions.


## References

* [Clean Code][clean-code] by Robert Martin
* [The Pragmatic Programmer][pragmatic-programmer] by Andrew Hunt, another classic
* [Practices of an Agile Developer][pad-refcard] quick reference
* [Practices of an Agile Developer][pad] book download. This is newer than *Pragmatic Programmer*
* [7 Habits of Highly Effective Programmers][7-habits-programmer] applies Steven Covey's *7 Habits* to programming.

<!-- the references in this file.  They won't appear in formatted output. -->

[sebooks]: https://se.cpe.ku.ac.th/doc/books/Programming/
[clean-code]: http://www.investigatii.md/uploads/resurse/Clean_Code.pdf "Clean Code by Robert Martin"
[pad-refcard]: https://media.pragprog.com/titles/pad/PAD-pulloutcard.pdf "Practices of an Agile Developer Quick Reference"
[pad]: https://github.com/mart0/Useful-materials---books-presentations-ant-etc./raw/master/Others/Practices%20of%20an%20Agile%20Developer.pdf "Practices of an Agile Developer, on Github"
[pragmatic-programmer]: https://www.nceclusters.no/globalassets/filer/nce/diverse/the-pragmatic-programmer.pdf "The Pragmatic Programmer by Andrew Hunt"
[7-habits-programmer]: https://simpleprogrammer.com/7-habits-highly-effective-programmers/ "7 Habits of Highly Effective Programmers"
[google-classroom]: https://classroom.google.com/u/0/c/MTQ5OTI2OTQ3MTJa "Classroom for ISP2018"
