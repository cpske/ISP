# Homework for Week 5, Part 1.

Answer these questions on Google Classroom.
The questions and references are given here because
Google Crummy Classroom doesn't enable text formatting 
in questions.

## Questions

These questions refer to material in *Practices of an Agile Developer* ([Refcard][pad-refcard] and [book][pad]). *[Clean Code][clean-code]* is also useful for answering these question.
If these links don't work, try the [se books][sebooks] collection.

1. Why keep a solutions log? (PAD Item 33)

2. Why should we "treat warnings as errors"? (PAD Item 34)

3. Give a code example where the compiler or interpretter issues a warning, but it really means an error in your code (often a logic or semantic error).
Use Java or Python, but its *much* easier in Java.
Note: this must be your own example, of course.

4. PAD Tip 2 is "Quick Fixed Become Quick Sand" (or "Don't Fall for the Quick Hack").  What is meant by this?

5. What are 3 things the PAD book recommends you do to avoid or correct quick fixes.
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

6. As part of a library, you write a `fibonacci(n)` method to return Fibonacci numbers, for `n >= 0`. 
What should you do if `fibonacci(n)` is called with a value `n < 0`?

   - [ ] Return -1 to indicate invalid parameter value.
   - [ ] Use an Assert statement to raise AssertError when `n < 0`.
   - [ ] Throw an exception, such as Python TypeError or Java IllegalArgumentException.
   - [ ] Print error message on the console and return 0.

7. A chess game has an 8x8 chessboard with a graphical UI (GUI).  When user makes a move on the GUI, the controller receives the input and calls `void game.moveTo(x,y)`, similar to TicTacToe.  What should `game` do if the controller calls `game.moveTo(x,y)` with values not on the chessboard, such as `x` > 8 or `y` > 8?

   - [ ] Just do nothing (return). 
   - [ ] Use an Assert statement to raise AssertError when `x` or `y` are invalid.
   - [ ] Throw an exception.
   - [ ] Print an error message (e.g. "Invalid Move") on the console and return.

8. You write a `indexOf(array[],value)` method to return the index of `value` 
in an `array` (Python `list`). What should you do if `value` is not in the array?

   - [ ] Return -1 to indicate value not in array.
   - [ ] Use an Assert statement to raise AssertError.
   - [ ] Throw an exception.
   - [ ] Print error message on the console and return 0.

9. Suppose your application reads a list of words from a URL, such as this:
```python
import urllib.request
import urllib.error

def read_dictionary():
    """Read a dictionary of words and return them as a list"""
    words = []
    try:
        input = urllib.request.urlopen("http://se.cpe.ku.ac.th/dictionary.txxxt")
        for line in input:
            # convert line to unicode, strip whitespace and newline
            words.append( line.decode().strip() )
    except HTTPError:    # this is like Java "catch(HttpError e)"
        return []
    return words
```
Which Tip from *Practices of an Agile Developer* Reference Card tells you that you should improve this code? (Write the **number** and **name** of the Tip on the Ref Card.)

10. What are good uses of comments? (Check all correct answers.)
  [ ] Make is easy for inexperienced programmers to understand the code.
  [ ] Describe the purpose or behavior of code, e.g. what it is trying to do.
  [ ] Explain the code, line by line.
  [ ] Document constraints.
  [ ] Document what value the variables hold, such as "// first name" for firstName.
  [ ] Document what exceptions and thrown under what conditions.







## References

* [Clean Code][clean-code] by Robert Martin
* [The Pragmatic Programmer][pragmatic-programmer] by Andrew Hunt, another classic
* [Practices of an Agile Developer][pad-refcard] quick reference
* [Practices of an Agile Developer][pad-book] book download, newer than *Pragmatic Programmer*
* [7 Habits of Highly Effective Programmers][7-habits-programmer]

[//]: #(Links for references in this document)
[//]: #(The reference definitions won't appear on the formatted page)

[sebooks]: https://se.cpe.ku.ac.th/doc/books/Programming/
[clean-code]: http://www.investigatii.md/uploads/resurse/Clean_Code.pdf "Clean Code by Robert Martin"
[pad-refcard]: https://media.pragprog.com/titles/pad/PAD-pulloutcard.pdf "Practices of an Agile Developer Quick Reference"
[pad]: https://github.com/mart0/Useful-materials---books-presentations-ant-etc./raw/master/Others/Practices%20of%20an%20Agile%20Developer.pdf "Practices of an Agile Developer, on Github"
[pragmatic-programmer]: https://www.nceclusters.no/globalassets/filer/nce/diverse/the-pragmatic-programmer.pdf "The Pragmatic Programmer by Andrew Hunt"
[7-habits-programmer]: https://simpleprogrammer.com/7-habits-highly-effective-programmers/ "7 Habits of Highly Effective Programmers"
