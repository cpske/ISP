---
title: Vision of KU Polls Application
---

> A Vision Statement is an important part of a project.
> There is lots of advice on the Internet for how to write a Vision
> Statement and what it should contain -- and the advise varies a lot.
>
> Many software projects favor a short vision statement based
> on a template such as [this one](https://www.atlascode.com/blog/creating-a-software-product-vision-statement/).   
>
> Other projects write a longer, more detailed vision 
> including background, a business case, and details of
> the envisioned product.
> [Advantis](https://www.edvantis.com/blog/project-vision-in-software-development/) 
> has good suggestions on creating a vision.

## Background

KU staff and students often want to conduct polls or surveys
within KU, or within a unit or organization at KU.
The polls or surveys provide input for making decisions,
planning events, and learning others' preferences and ideas,
but they aren't critical (like voting for a representative).

The most common poll/survey questions are multiple choice, 
where the poll taker selects a choice from a list of choices.

There are applications for this on the Internet,
such as Google Forms and SurveyMonkey, but they all
have limitations or unwanted features.  
Google Forms is clumsy and a returning visitor cannot
see his previously submitted choices, but he can submit
new choices if the form settings are set to allow it.
Google Forms do not have a setting for automatic start 
and end date; the form creator must manually enable/disable responses.

SurveyMonkey has limits on free forms, including the
number of survey items and number of responses.

## Vision

For the KU community
who want to conduct surveys and polls open to the community,
and who may wish to specify starting/ending dates for the survey or poll,
our product is an easy to use web application that 
provides ability to submit a choice on poll items,
and view or modify one's choice any time during the polling period.

Our product has a simple procedure for creating polls,
and allows everyone to see the results of a poll or survey.

## Additional Detail

The opening and closing dates for each poll/survey question are optional.  
A question is not visible to web visiters before the opening date,
and voting or modifying an existing vote is not allowed after
the closing date, but the poll/survey and results can be 
viewed after the closing date.

## Alternative Solutions

There are other free web-based applications for conducting polls and surveys.
Two such products are:

* Google Forms - can have several types of questions including multiple choice, matrix, short answer, and free-form long answer. The form owner can manually enable/disable collecting responses and limit the scope to a Google organization.

* Survey Monkey - (students should write their own summary of this)

## Main Features

1. An authorized person can create poll or survey questions with multiple choices and a specified start and end date (the polling period). These date are optional; if not specified then a poll remains open indefinitely.
2. Authenticated users can submit a response to any poll question during the polling period.
3. A user can revisit a poll page to view his/her response, and can change it during the polling period.
4. No responses or change to a response are allowed after a poll's end date.
5. Poll questions are not visible before a poll's starting date.
6. Anyone can view the results of a poll question at any time after the starting date, but only authorized users can vote for a poll. 
7. Voting may be restricted to people with a KU login.
