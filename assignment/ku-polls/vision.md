---
title: Sample Vision & Scope of KU Polls Application
---

> This is an example Vision & Scope for KU Polls. 
> You may use it, but please carefully read and customize it.
>
> Review and update the Vision during the project.

Author:  James Brucker    
Rev Date: 17-8-2024

## Background

KU staff and students often want to conduct polls or surveys
within KU, or within an organization or group at KU.
The polls or surveys provide input for making decisions,
planning events, learning others' preferences, and feedback
such an evalution form for an event.

The most common poll or survey questions are multiple choice, 
where the respondant selects a choice from a list of choices.
Other common formats are ratings such as 1 to 5, and short answer items.

There are existing applications for this on the Internet,
such as Google Forms and SurveyMonkey, but they
have limitations or unwanted features. 

Google Forms provides many different poll formats, such as multiple choice,
check box, linear scale (1-5), short answer, date selection, and choice grids.
Some limitations are that it cannot set opening and closing date/times for poll questions,
the poll creator must carefully set options to ensure that each user can submit only 1 response
and be able to edit a prior response, and no way to restrict who
can submit an answer. 
G-Suite customers can restrict responses to their organization,
but no finer granularity.


SurveyMonkey has even poll question types similar to Google Forms and better formatting,
but it is a commercial product with limits on free forms, 
including limit on the number of survey items and number of responses.
The survey creator can limit the total number of responses,
IP addresses of allow respondants, or create a password (one password
used by everyone) to limit respondants, but no way to limit based
on domain or individual identity. 

### Stakeholders and Their Needs

| Stakeholder | Goal or Needs                                     |
|:------------|:--------------------------------------------------|
| Event Organizer | Easy way to get custom user feedback on an event.    |
| Student Groups  | Query members' preferences or opinions, see ongoing results.  |
| Poll Respondant | Find and respond to a poll quickly, have my identity protected, see a summary of how others have responded. |
| Event Participant | See how everyone responds to a poll about the event. |


## Vision

For the KU community
who want to conduct surveys and polls within the community,
and who may wish to specify start/end dates for a survey or poll,
our product is an easy to use web application that 
provides ability to submit a choice on poll items,
and view or modify one's choice any time during a polling period.

Our product provides a simple web interface for creating polls,
responding to polls, and allows everyone to see the results 
of a poll or survey.


## Additional Detail

The opening and closing dates for each poll/survey question are optional.  
A question is not visible to web visiters before the opening date,
and responding or modifying an existing response is not allowed after
the closing date, but the poll/survey and results can be 
viewed after the closing date.

## Alternative Solutions

There are other free and paid web-based applications for conducting polls and surveys as described in the [Background](#background).
Two such products are:

* Google Forms - has several types of survey items including multiple choice, matrix, short answer, and free-form long answer. The form owner can manually enable/disable collecting responses and limit the scope to a Google organization (only for G-Suite customers), but cannot specify start/end dates.

* Survey Monkey - has several types of survey items and limit poll dates, but free version has many limitations.

## Main Features

1. Poll or survey questions have multiple choices where the respondant chooses one. Each poll question can have its own specific start and end date (the polling period). If not specified then a poll remains open indefinitely.
2. Authenticated users can submit a response to any poll question during the polling period.
3. A user can revisit a poll page to view his/her response, and can change it during the polling period.
4. No responses or change to a response are allowed after a poll's end date.
5. Poll questions are not visible before a poll's starting date.
6. Anyone can view the results of a poll question at any time after the starting date, but only authorized users can vote for a poll. 
7. Voting may be restricted to people with a KU login.
8. The application will be portable with a simple installation procedure.

## Optional Features For Staged Release

These features will not be in the initial release, but may be added to future releases.

1. Any authorized person can create poll or survey questions with multiple choices and a specified start and end date (the polling period). These date are optional; if not specified then a poll remains open indefinitely.
2. Other poll item formats, such as linear scale (e.g. 1-5), ability to select multiple responses, or short answer poll questions.
3. Use OAuth for authentication as an alternative to username and password.

## Features Not To Be Implemented

1. Limiting responses based on IP address or a list of allowed usernames or email addresses.
2. User interface for adding "users" with username and password. The framework provides two mechanisms for this:
   - admin interface to add users and passwords
   - a data import function that can import user data from a JSON or CSV file


## References

1. [Advantis](https://www.edvantis.com/blog/project-vision-in-software-development/) has good suggestions on creating a vision.
