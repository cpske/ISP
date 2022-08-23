---
title: Software Testing
---


Software projects perform several types of testing:

* *Unit Testing* tests individual components, such as classes and and functions.
* *Integration Testing* tests that components and services interact correctly.
* *Functional* or *End-to-End Testing* tests the entire application flow and behavior.
* *Security Testing* tests for secure flaws or vulnerabilities.
* *Usability Testing* to determine how well and easily users can use the software to perform what they want to do
* *Acceptance Testing* tests that application conforms to requirements and meets the users' needs. Often required before delivering a software product.

---

## Unit Testing

Unit testing tests individual classes, methods, and functions.

Your development workflow should usually be:

- write some code
- write tests for what the code **should** do, based on the spec (not what you actually coded)
- run the tests
- analyze any test failures and correct the code (or tests)
- repeat

In **Test Driven Development** (TDD) you write the tests **before** you write the code.  TDD usually results in better tests and better code under test.

Unit Testing Benefits:

1. avoids errors
2. helps you stay focused on current work
3. makes you think about what code *should* do, even in 'edge' cases
4. avoid re-introducing previously fixed errors, called *regression errors*
5. gives you **confidence** to change the code
6. tests are **required** before doing refactoring
7. enables testing to be automated (unlike manual testing)

How to design test cases?

- test *behavior* not just methods. One test may use several methods.
- test for: edge cases, failure cases, typical cases, extreme cases
- example tests for sqrt:
  - edge case: sqrt(0), sqrt(1.0E-15)
  - failure case: sqrt(-0.1) 
  - typical case: `sqrt(x) for x in [0.25, 0.5, 1, 1.5, 4.0, 26, (10000.5)**2]`
  - extreme case: sqrt(1.8E+308) - `1.8e+308` is the largest floating point value in Python
- things likely to go wrong, or where programmer may make a mistake
  - "off by one" errors - requires some knowledge of the implementation
  - empty input or empty lists
  - using a file that doesn't exist, is empty, or cannot be opened

---

## Python Unit Testing

There are several good unit testing tools & frameworks for Python.
The ones we will cover are:

* [unittest][python-unittest] the most commonly used test framework, included with Python
* [PyTest](https://www.pytest.org) a popular, light-weight testing framework. Results are easy to understand but test conditions are a bit limited.
* [Doctest]() for test-by-example in code. Provides tests and documentation at the same time, but not usually a thorough test.

[python-unittest]: https://docs.python.org/3/library/unittest.html

Presentation: [Python Unit Testing](PythonUnitTesting.pdf)

Resources to learn unittest:

* [Python unittest Docs][python-unittest] are easy to read, many examples.
* [Getting Started with Testing](https://realpython.com/python-testing/) on RealPython introduces testing in general and examples of Python test tools
* [Python Unittest Tutorial](https://youtu.be/6tNS--WetLI) video on Youtube, 39 minutes.
  

### [Code Coverage](code-coverage)

[Code Coverage](code-coverage) uses a tool to measure how much of your code is really being tested by unit tests.
- It is easy to use while running your tests. 
- Helps you find sections of code that you need to write better tests for.

To use code coverage on your own computer, use the [coverage](https://coverage.readthedocs.io/) Python package.

To run code coverage as part of automatic testing (C.I. or Github Actions) try CodeCov or Coveralls.


## Java Unit Testing

Presentation: [Unit Testing with JUnit](JUnit.pdf) may cover only JUnit 4.0

* [JUnit Home](https://junit.org/junit5/) covers JUnit 4 & 5. Many examples.

* [JUnit Parameterized Tests](JUnitParams-tutorial.pdf) parameterize unit tests instead of writing many test methods with nearly the same code

## End-to-End Testing

Test the flow of the application "from start to finish".

An E2E test typically covers one usage scenario, and you may want
to test several scenarios.  However, the goal is not comprehensive
testing of everything.

[What is E2E Testing? E2E Testing Framework with Examples](https://www.softwaretestinghelp.com/what-is-end-to-end-testing/) is a short overview and describes some testing tools.

[The Practical Testing Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) by Martin Fowler describes 3 levels of testing: unit test, integration test, and E2E test.

## Verification and Validation

**Verification**

- Checking that a program performs according to the specifications (how it was specified & designed it to behave) [Kaner]
- Confirm that the software performs and conforms to its specification. [U.W.]
- "*Are we building it right?*" (informal interpretation)

**Validation**

- Checking that a program beaves according the the user or system requirements (what the customer said the program should do) [Kaner]
- Confirm that the software performs to the user's satisfaction. Assure that the software meets the user's (specified) needs. [U.W.]
- "*Are we building the right thing?*" (informal interpretation)

Note: definition 2 is the most descriptive. Definition 3 (informal) is not an acceptable answer on quiz or exam.

Two broad appoaches to perform V & V.

1. Dynamic
   - exercising (running) the software and oberving its behavior, i.e. testing

2. Static
   - inspection and analysis of the software representation (e.g. code to discover problems
   - inspections, mathematical models and proofs

## Security Testing

1. Dynamic V & V
   - penetration testing
   - fuzzing
2. Static V & V
   - examine source code for common problems such as unchecked buffer writes, memory allocation/deallocation, trusting tainted data
   - proofs related to privilege level

* Developers should care about both "building the thing right" and "building the right thing"
* Both Verification and Validation are important
* Both static and dynamic methods are necessary
* Verification is usually cheaper and easier than Validation

## Testing Incomplete Software Under Development

Suppose you are writing `module1` and want to test it,
but `module1` depends on `module2` that has not been written yet.
How can you test `module1`?

1. Write a *stub* for the interface to module2.  These classes and methods don't do anything, but enable you to run module1.
2. Create **Mock Objects** to 'stand in' for module2 and simulate it's behavior for your test cases. You can pre-program the values that module2 should return.

## Who Performs Testing?

Developer

  * **+** understands the software best
  * **-** tests gently, maybe not trying to expose errors
  * **-** driven by deadlines to finish code
  * **-** may be "blind" to his own errors or misunderstanding

Tester

  * **+** tries to break the system
  * **-** must learn the software
  * **+** driven by quality goal
  * **+** not biased by developer's perspective

## Axioms and Guides for Testing

1. The probability of more, undedecting defects increases with the number of detected defects

2. Assign the best programmers to testing

3. Exhaustive testing is impossible

4. You will never know when you have found the last bug -- cannot guarantee software is defect=free

5. It takes more time than you have to test less than you would like

6. You will run out of time before you run out of test cases
   * If that's not true, you should be looking for more test cases

## Web Testing

Presentation: [Web Testing](WebTesting.pdf)

There are special tools for testing web apps and web services.
In this class we will use Selenium, and may cover the Robot Framework.


## References

* [Extensive List of Python Testing Tools](https://wiki.python.org/moin/PythonTestingToolsTaxonomy) on [wiki.python.org](http://wiki.python.org) includes mock objects, web testing, fuzz testing, source code checkers, code coverage, unit test, and acceptance/business logic testing tools.
* [Testing Your Code](https://docs.python-guide.org/writing/tests/) good article introduces testing using unit test, py.test, Hypothesis, and mock.
* Presention: [Intro to Different Kinds of Testing](Intro-Testing.pdf), not relevant to this course


