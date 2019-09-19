# Questions about Agile Practices

PAD refers to the book *Practices of an Agile Developer*, mentioned in class last week.
For some questions you are asked to name a "Tip" from the PAD book or PAD Quick Reference.
You can use the number and name from either the book or Quick Reference.
The numbers are the same, but text is different.  Either one is OK.

Questions 6-8 refer to assertions.  Assertions are very useful for detecting programming errors in development, and available in many programming languages.  At Microsoft, developers are *required* to use assertions.  Please use the web or a good Python book to learn about assertions and how to use assert.

## Questions

Q1. PAD Tip 17 (p.69) recommends using short iterations.  What are two benefits to the project of using short iterations? (don't give vague answers like "keep your balance" or "stay focused") 

Q2. To ensure that your code is on the "right track", and encourage you to write smaller, more cohesive code, what does PAD recommend?  Enter the Tip *number* and *title* from the PAD Quickref or PAD book.

Q3. Why should we "treat warnings as errors"? (PAD Tip 34)

Q4. PAD Tip 2 is "Quick Fixes Become Quick Sand" (or "Don't Fall for the Quick Hack").  What does this mean?

Q5. What are 3 things the PAD book recommends you do to avoid or correct quick fixes?
- [ ] Use Test-driven-development.
- [ ] Encourage team members to review and understand all code.
- [ ] Use unit tests; they help you design code into manageable pieces and provide runnable documentation.
- [ ] Assign ownership of parts of the code to individual team members.
- [ ] Never implement a fix without fully understanding the code and cause of the problem.

> **Questions 6-8**
>
> In writing a function or method, there are 4 ways to handle a problem or unexpected condition:
>
> - return a special value (such as -1 or null) 
> - throw an Exception
> - use an Assert statement to check parameters and preconditions, and raise an AssertionError
> - print a message on the console, then return
>
> For the situations below, which is the best solution?

Q6. As part of a public library of math functions that anyone can use, you write a `fibonacci(n)` function that returns Fibonacci numbers for `n >= 0`. 
What should you do if `fibonacci(n)` is called with a value `n < 0`?
- [ ] Return -1 to indicate invalid parameter value.
- [ ] Use an Assert statement to validate the value, such as `assert n >= 0`.
- [ ] Throw an exception, such as ValueError.
- [ ] Print an error message on the console and return 0.

Q7. You write a `index_of(list, value)` method that returns the index of the first element in `list` that matches `value`. 
For example, `index_of(['ant','dog','cat'], 'dog')` returns 1. 
What should you do if `value` is not in the list?
- [ ] Return -1 to indicate value is not in list.
- [ ] Use an Assert statement to raise an AssertError.
- [ ] Throw an exception, such as NotFoundError.
- [ ] Print an error message on the console and return 0.

Q8. Inside a game you wrote using Arcade is a method named `jump(how_much)`.  This method is called only by your own code and it should always be called with `how_much >= 0`.  What should you do if its called with a negative value?
- [ ] Do nothing.
- [ ] Use an Assert statement to validate the value, such as `assert how_much >= 0`.
- [ ] Throw an exception, such as Python ValueError.
- [ ] Print an error message on the console.

Q9. This code returns a list of words read from a URL:

```python
import urllib.request

def read_dictionary():
    """Read a dictionary of words and return them as a list"""
    # the list of words read from dictionary
    words = []
    try:
        input = urllib.request.urlopen("http://se.cpe.ku.ac.th/dict.txt")
        for line in input:
            # convert line from bytes to unicode, strip whitespace and newline
            words.append( line.decode().strip() )
    except HTTPError:    # catch HTTPError condition
        return []        # return an empty list
    return words
```
Which Tip from PAD tells you that you should improve this code?  Write the **number** and **title** of the Tip on the PAD Quick Ref or PAD Book.

Q10. What would PAD suggest about the comments in the `read_dictionary` function?

Q11. Is there anything else about `read_dictionary` that is a bad coding practice?  Describe it.

Q12. What are good uses of comments? (Check all correct answers.)
- [ ] Make is easy for inexperienced programmers to understand the code.
- [ ] Describe the purpose of code, e.g. what it is trying to do.
- [ ] Explain the code, line by line.
- [ ] Document preconditions or constraints.
- [ ] Document what value a variable holds, such as "# first name" for a variable `first_name`.
- [ ] Document what exceptions the code may raise (throw) under what conditions.


## References

* [Practices of an Agile Developer][pad-refcard] quick reference (or try se.cpe)
* [Practices of an Agile Developer][pad] book (or try se.cpe)
* [Clean Code][clean-code] by Robert Martin
* [7 Habits of Highly Effective Programmers][7-habits-programmer] applies Steven Covey's *7 Habits* to programming.

<!-- the references in this file.  They won't appear in formatted output. -->

[sebooks]: https://se.cpe.ku.ac.th/doc/books/Programming/
[clean-code]: http://www.investigatii.md/uploads/resurse/Clean_Code.pdf "Clean Code by Robert Martin"
[pad-refcard]: https://media.pragprog.com/titles/pad/PAD-pulloutcard.pdf "Practices of an Agile Developer Quick Reference"
[pad]: https://github.com/mart0/Useful-materials---books-presentations-ant-etc./raw/master/Others/Practices%20of%20an%20Agile%20Developer.pdf "Practices of an Agile Developer, on Github"
[pragmatic-programmer]: https://www.nceclusters.no/globalassets/filer/nce/diverse/the-pragmatic-programmer.pdf "The Pragmatic Programmer by Andrew Hunt"
[7-habits-programmer]: https://simpleprogrammer.com/7-habits-highly-effective-programmers/ "7 Habits of Highly Effective Programmers"
