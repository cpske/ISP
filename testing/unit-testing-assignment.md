# Unit Testing

You can do this in Java or Python.

## Assignment

Write two methods (Java) or functions (Python) and a *test suite* for each one.

For each problem do the work in the following order:
1. Write down the input categories in Markdown in a file `test_cases.md` in your project directory.  This helps you think of (and remember) what to test.  You should test:
   * **borderline cases**, such as a list with 0 or 1 elements
   * **typical cases**, such as a list with a few duplicates or no duplicates
   * **impossible cases** where the method should not work
   * **extreme cases**, such as a huge list
2. Create an empty method that just returns a default value (like 0 or null) so it compiles.
3. Write the unit tests using JUnit or Python unittest.  The tests will mostly fail.
4. Write the method until the tests all pass.
5. If you think of additional useful tests, add them to `test_cases.md` and your test code.

Submit your code to Github.

### Where to Submit

In your personal Github account, create a public repository named `unittesting`.
Commit your source, including tests, to this repository.

> Please spell it **exactly** as shown: `unittesting`

I would suggest that you also keep notes on testing, since you will do it a lot.

### Project Structure

Standard Java project structure:
```
testinglab/
    src/  (Source code)
        ListUtil.java
    test/ (Test code)
        ListUtilTest.java
```
Standard Python project structure.  There is no "src" directory, but source is typically in directories named for *packages*. In this lab you can omit the *package*, but you should know how to use them!  Test code is in a directory `tests`.
```
testinglab/
    listutil.py
    tests/    (Test code)
        listutil_test.py
```
See: [Structuring Your Project](https://docs.python-guide.org/writing/structure/) in *The Hitchhiker's Guide to Python*.

## Problem 1: Count Distinct Elements in a List

Java:
```java
public class ListUtil {
    /**
     * Count the number of distinct elements in a list.
     * The list may be empty but not null.
     * TODO: can the list contain null values? Does null count as a unique element?
     *
     * @param list a list of elements
     * @return the number of distinct elements in list
     */
    public static int countUnique(List<?> list)
```

Python:
```python
def count_unique(list):
    """Count the number of distinct elements in a list.

    The list can contain any kind of elements, including duplicates and nulls in any order.

    (In PyDoc there are different formats for parameters and returns. Use what you prefer.)

    :param list:  list of elements to find distinct elements of
    :return: the number of distinct elements in list

    Examples:
    >>> count_unique(['a','b','b','b','a','c','c'])
    3
    >>> count_unique(['a','a','a','a'])
    1
    >>> count_unique([ ])
    0
    """
```

**Question**  There is anything important that is not clearly specified in the problem
statement?

## Problem 2: Binary Search

This is suprisingly hard to code correctly.

Write a method that searches for an element in an array (Java) or list (Python), where the array or list contents are already sorted.  Use binary search.  Return index of the matching element or -1 if the search element is not in the list/array.

Exceptions: if the value to find (`element`) is null, throw an exception:
```java
    throw new IllegalArgumentException("Search element must not be null");
```
or in Python
```python
    raise TypeError("Search element must not be none")
```
Write a unit test to check that this exception is thrown.

The binary search method should always terminate, even if the array or list is not correctly sorted.  That is, don't get stuck in an infinite loop.

Write good method documentation.

Concentrate on writing good test cases before you code.

Java (in the `ListUtil` class):
```java
//TODO write good method Javadoc
public static <T extends Comparable<? super T>> int binarySearch(T[] array, T element)
```

Python (in the `listutil.py` file):
```python
def binary_search(list, element):
    # TODO write good Python DocString
```
