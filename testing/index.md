---
layout: page
title: Software Testing
---

Introduction to Testing: [PDF](Intro-to-Testing.pdf) [PPT](Intro-to-Testing.ppt)

There are many types of testing used in software projects

* Unit testing for testing individual components (classes and methods)
* Integration testing to test that components and services interact correctly
* Functional or end-to-end testing to test the entire application flow and behavior
* Acceptance testing, often required when delivering a software product 

## Verification and Validation

**Verification**
: 1. Checking that a program performs according to the specifications (how it was specified & designed it to behave) [Kaner]
: 2. Confirm that the software performs and conforms to its specification. [U.W.]
: 3. "*Are we building it right?*" (informal interpretation)

**Validation**
: 1. Checking that a program beaves according the the user or system requirements (what the customer said the program should do) [Kaner]
: 2. Confirm that the software performs to the user's satisfaction. Assure that the software meets the user's (specified) needs. [U.W.]
: 3. "*Are we building the right thing?*" (informal interpretation)

Note: definition 2 is the most descriptive. Definition 3 is not an acceptable answer on quiz or exam.

Two broad appoaches to perform V & V.

1. Dynamic
   - exercising (running) the software and oberving its behavior, i.e. testing

2. Static
   - inspection and analysis of the software representation (e.g. code to discover problems
   - inspections, mathematical models and proofs

Security Testing Example:

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

## Unit Testing

* Why do unit testing?

* How to design test cases?

* Python Unit Testing: [PDF](PythonUnitTesting.pdf) [PPT](PythonUnitTesting.ppt)
  - Python standard unittest (similar to JUnit) and doctest
  - [PyTest](https://www.pytest.org) is another popular, light-weight testing framework

* [Code Coverage](code-coverage.md) - using tools to assess how much of your code is really being tested by unit tests.

## Testing (Incomplete) Software Under Development

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
  * **+** not biased by development perspective

## Axioms and Guides for Testing

1. The probability of more, undedecting defects increases with the number of detected defects
2. Assign the best programmers to testing
3. Exhaustive testing is impossible
4. You will never know when you have found the last bug -- cannot guarantee software is defect=free
5. It takes more time than you have to test less than you would like
6. You will run out of time before you run out of test cases
   * If that's not true, you should be looking for more test cases

## Web Testing

* Web Testing [PDF](WebTesting.pdf) [PPT](WebTesting.ppt)

## Java Testing

* Intro to JUnit: [PDF](JUnit.pdf) [PPT](JUnit.ppt)

* [JUnit Parameterized Tests](JUnitParams-tutorial.pdf)

* New design of JUnit 5

* Mock Objects in Java
