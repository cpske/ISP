---
Title: User Stories for Authenticated Voting in Django Polls
---

Everyone will implement these in your Django Polls project.

<p>
<table border='1' width="90%" align="center">
<tr>
<th>#1. User Login</th>
</tr>
<tr>
<td>A user can login with username and password at the 
URL /accounts/login/.    
After login, the polls index page is displayed,
except as in User Story 4 below.
</td>
</tr>
<tr>
<td>
How to Demo: demo along with story #2.
</td>
</tr>
</table>
</p>

<p>
<table border='1' width="90%" align="center">
<tr>
<th>#2. Polls Page Greets User by Name</th>
</tr>
<tr>
<td>The polls index page greets the visitor by first name (if known)
or username otherwise, if he is logged in.
<br/>
If visitor is not logged in, there is a message "Please login to vote"
with "login" a hyperlink to the login page.  Unauthenticated visitors
can view list of polls and view poll details page, but cannot vote.
</td>
</tr>
<tr>
<td>
How to Demo: user visits polls index page and sees visual indication
that he can login, such as login button or link.  He follows link and
sees that it goes to /accounts/login/.  After login, he is redirected
to polls index, and is greeted by first name (if known) or username.
Since he is already logged in, there is no login link/button.
</td>
</tr>
</table>
</p>

<p>
<table border='1' width="90%" align="center">
<tr>
<th>#3. User Can Logout</th>
</tr>
<tr>
<td>A user can logout at the URL /accounts/logout/.    
After logout, redirect the user to the polls index page a confirmation message is displayed.
</td>
</tr>
<tr>
<td>
How to Demo:  login and browser around as in US #2.  Then logout using a link or navigating to /accounts/logout.  User should be redirected to polls index (or other "home" page) with visual confirmation he is not logged in.
</td>
</tr>
</table>
</p>

<p>
<table border='1' width="90%" align="center">
<tr>
<th>#4. User Must Login to Vote</th>
</tr>
<tr>
<td>When someone visits a poll details page,
if he is not logged in then the "Submit" button is replaced
by the message "Please login to vote" with "login" a hyperlink to login page.

If user clicks the "login" link and logs in, he is returned
to the same poll details page, and now the "Submit" button is shown.

If a non-logged in user submits a vote (bypassing the UI)
then the view automatically redirects him to the login page.
After logging in, he is returned to the poll details page 
showing choices.
</td>
</tr>
<tr>
<td>
How to Demo:  as a non-authenticated visitor, navigate to a polls detail page.  There should not be any "Vote" or "Submit" button to vote. Instead there should be a "Please login to vote" message with link to login page.  Aftr logging in, visitor is redirected to polls detail page, and now he can submit a vote. 
Verify that the vote was counted.    

Next, as a non-authenticated visitor go directly to http://host:port/polls/n/vote/ where n is a poll id.  Should be redirected to the login page.
</td>
</tr>
</table>
</p>

<p>
<table border='1' width="90%" align="center">
<tr>
<th>#5. Vote for a Poll Replaces Previous Vote</th>
</tr>
<tr>
<td>When a visitor votes for the same poll more than once,
his choice replaces his previous choice.  In effect, a user
only gets one vote per poll, but he can change it.
</td>
</tr>
<tr>
<td>This will require some changes to the models,
and the views that count votes.
</td>
</tr>
<tr>
<td>How to Demo: vote for a poll and view totals.  Vote for a different choice on same poll and view that totals have changed correctly.

Repeat the above, but logout, close browser, reopen browser, and re-login between votes.
</td>
</tr>
</table>
</p>

<p>
<table border='1' width="90%" align="center">
<tr>
<th>#6. Poll Details Page Shows a Visitor's Previous Vote</th>
</tr>
<tr>
<td>When a visitor views a poll details page  (voting page),
if he has previously submitted a vote then that choice is pre-selected
so he knows what he already voted for.
</td>
</tr>
</table>
</p>

<p>
<table border='1' width="90%" align="center">
<tr>
<th>#7. Poll Details Page Contains Links to View Results and List of Polls</th>
</tr>
<tr>
<td>The poll details page contains a link to view the poll results (without
voting) and a link to the list of polls. 
</td>
</tr>
</table>
</p>
