## Midterm Programming Exam

The primary purpose of the exam was to test your ability to thoroughly
test a well-defined piece of code, based on the specification.
Unit testing should not make assumptions about *how* the method is
implemented. It should test based the method specification.

Effective, thorough testing is essential to correct software.  On this exam the code to be tested was simple, so students can devote 3 hours to constructing good, *thorough* tests.

## `detag()` method

The `detag` method was worth only 10% since it is only a few lines
of code and the solution was **given** on the exam sheet.
No partial credit except for very minor error that was easy to fix.

## Code Quality

Code quality worth 10%, and includes:

1. Correct naming of classes and files. 
2. Names of methods and functions comply with language's naming convention and unit test framework naming. Test method names should be descriptive.
3. Code correctly indented.
4. Blank line between methods.

## Unit Tests

Unit Tests worth 80% of score.

Tests should be *thorough* and include at least 8 of these cases.
No credit if the expected result is incorrect, and no credit for
redundant tests.

1. Valid start/end tags: `<start>`, `</end>`, `</end> and <start>`
2. Mono or scopeless tags: `<br/>` or `<br />`
3. Mixture of tags and text, NOT only `<tag>text</tag>`. Example: 
    `"Today it <em>may <b>rain</b>!</em> <br /> or maybe not"`
4. Complex tags, like `<p style="font: Courier; size: 18pt" div="{bogus}">` or tag spanning multiple lines (this is legal).
5. Text with no tags, including empty string or only space.    
Borderline Case:
6. Embedded < and >: `<<H1>, <<BR>>`, `<embed<in tag>`    
Invalid Cases:
7. Invalid start tags: `<1H>`, `<$>`, `< H1>`.  NOT JUST TAGS STARTING WITH A SPACE (1/2pt)
8. Invalid end tags: `</1H>`, `</>`, `</$>`, `</H1/>`, `</ >` NOT JUST TAG STARTING WITH A SPACE (1/2pt)
9. Empty tag or tag containing only space: `<>`, `< >`
10. Tag without a closing ">": `Like this <br`, or `like this </end` 
