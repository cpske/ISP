---
title: Auction Test 
---

This is a Github Classroom assignment.  The assignment includes starter code for Auction, `auction_test.py`, and a README with details of the assignment.

Write tests (in `auction_test.py`) that the Auction class behaves according to the specification.  The Auction class is in `auction.py`, but this code may **contain bugs**.

You should write tests for how the code **should** behave based on the **specification**. Do not test for how the sample Auction code **actually** hehaves.

The sample code may contain errors! 

Documentation for the Auction class is in 2 places:

1. docstring comments in the Auction class (the docstrings are correct)
2. online PDF file

If there are inconsistencies between the PDF and the docstrings, 
use the docstring comments as authoritative. 
Please notify me of inconsistencies or anything that is not clear.


## Github Runs Your Tests

You should first run your tests locally (of course).

When you push code to Github, it will automatically run your tests
using a Github Action.  Click the **Action** tab to view the results.

The build should **fail**. Here's why...

The Action will test your code using **8 different versions** of Auction.

Version 1: Auction code is correct. Your tests should **all pass**.    
Version 2-8: At least 1 error in Auction. Some tests should **fail** or **error**.

Because all 8 versions are tested in one "build" and some tests will fail, the entire build fails.  The build output contains lots of messages.  When it is testing version 1 (the correct code) the build output will show:
```
----------------------------------------------------------------------
AUCTION CODE 1: All methods work according to specification. Tests should PASS.
----------------------------------------------------------------------
test_best_bid (auction_test.AuctionTest) ... ok
test_bid_active (auction_test.AuctionTest) ... ok
.
.
.
test_winning_bid (auction_test.AuctionTest) ... ok

----------------------------------------------------------------------
Ran 11 tests in 0.002s
```

Similar output for "AUCTION CODE 2", "AUCTION CODE 3", etc.


## Assignment

1. Write tests for all the Auction requirements.
   - any test that fails for this code is useless because it's a false positive.
2. Try to make your tests PASS for Auction code 1 and at least one test FAIL or ERROR for the others.
3. Analyze the unittest output on Github Actions and try to identify the nature of each error. Complete the table below.

## What to Submit

Push to Github:

1. your `auction_test.py`
2. your README.md containing a completed table containing your analysis of any errors you find in the code.  A template for the table is in README.


[Specification for Auction Class](AuctionTest.pdf)

