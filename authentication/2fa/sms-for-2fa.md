---
title: Why Do Thai Finance Cos use SMS for OTP?
---

Thai banks, Thai brokerages, and many others use only SMS for 2-factor authentication (OTP codes).  SMS can be hacked and the NIST has been recommending against the use of SMS for years.

How easy is to hack SMS?

- If you can get access to the user's phone (or hack it), install mSpy. It lets you remotely read a phone's SMS messages.
- Buy a hardware [SMS Intercepter](https://www.smsbroadcaster.com/post/sms-interceptor). There are a variety of these at the previous link, or you can buy one on Alibaba for about $100. These devices intercept SMS and wifi, and even send SMS to phones nearby (within 300m - 2 km).
- SIM jacking. Get a replacement SIMM card or e-SIMM for the victim's phone number and take control of their phone number.  In the U.S., this is pretty easy via social engineering. In Thailaand, it should be harder (*is it?*).


## Even Worse than SMS

KGI, a stock broker in Thailand, sends OTP codes via both SMS and email, simultaneously. If you want to hack the account of a KGI customer, hack their email first.  Then you can easily intercept OTP codes.  If the customer is really stupid, he/she may use the same password for their email account as their brokerage account.

