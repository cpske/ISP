---
title: Auction Rules
---

The rules on an auction are:

1. A person can submit one or more bids. Each bid must have
   a bid price > 0 and be at least the best bid so far plus 
   a minimum increment (`min_increment`, the default value is 1).
   If a bid is <= 0 then a ValueError is raised.
   If a bid is > 0 but too low then an AuctionError is raised.
2. The `min_increment` is specified as a constructor parameter when creating an Auction. The default value is 1.
2. The `bid` method defines the required values of parameters, such as bidder name.
4. The application must call auction.start() to enable bidding,
   and auction.stop() to disable bidding.  
   start() and stop() can be called multiple times. 
   `auction.is_active()` tests if bidding is enabled.
5. Bids are allowed only when an auction is active.
   If bid() is called when auction is inactive (stopped),
   an AuctionError is thrown.
6. At any time, `best_bid()` can be called to get best bid so far,
   and `winner()` to get the name of the top bidder.
 
Example:

```
>>> auction = Auction("TDD with Python, 2nd Edition")
>>> print("Minimum bid increment is", auction.increment)
Minimum bid increment is 1
>>> auction.start()
>>> auction.bid("Jim", 250)
>>> auction.bid("Harry", 300)
>>> auction.bid(" biRD ", 400)
>>> auction.best_bid()
400
>>> auction.winner()
'Bird'
>>> auction.bid("Jim", 400.1)
Traceback (most recent call last):
  ...
auction.AuctionError: Bid is too low
>>> auction.bid("", 1000)
Traceback (most recent call last):
  ...
ValueError: Missing bidder name
>>> auction.is_active()
True
>>> auction.stop()
>>> auction.bid("Jim", 1000)
Traceback (most recent call last):
  ...
auction.AuctionError: Bidding not allowed now
>>> auction.start()
>>> auction.bid("mai", 402.50)
>>> auction.best_bid()
402.5
>>> auction.winner()
'Mai'
```
