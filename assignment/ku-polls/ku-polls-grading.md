## KU Polls Grading Guidance

Please assign only integer-value scores. Allow minor mistakes (no deduction).

We mainly want to see that students applied a good development process
and tried to do the work.


### HW5.2 [KU Polls Iteration 2](iteration2)

You can probably grade this by inspection on Github.

- [3 pt] Iteration 2 Plan in wiki with **Goal** and major work (features) to implement.
  - Not required to list detailed tasks (those are on project board).
  - Deduct points for poor writing, incomplete sentences, very poor Markdown formatting.
- [4 pt] Iteration 2 Project Board with tasks covering work in Iteration Plan.
  - All or nearly all tasks should be done. OK if a couple of tasks are incomplete.
- [1 pt] Has `iteration2` branch on Github, already merged into `master`.
- [4 pt] `polls/models.py Question` class has `can_vote` and `is_published` methods.
- [4 pt] In `settings.py`, externalize at least `SECRET_KEY` and `DEBUG`.
  ```
  DEBUG = config('DEBUG', default=False, cast=bool)
  SECRET_KEY = config('SECRET_KEY', ... )
  ```
- [4 pt] Improved navigation: the poll details page (shows question and choices) and voting results page both contain a hyperlink to the polls index page.

**Total: 20 pt**


### HW 8.1 KU Polls CI (Week 8 Assignment)

You can grade this by inspection on Github.

- [5 pt] Have a Travis-CI "badge" in README.md that is a **valid link** to latest Travis build.  Also has a `.travis.yml` file in repository.
- [5 pt] Have a CodeCov "badge" in README.md that is a **valid link** to latest CodeCov report.  The report **must not** show no coverage (that would happen if they forgot to run coverage in the Travis yaml file).

**Total: 10 pt**


### HW 11.1 [Iteration 3](iteration3) (Week 11 Assignment)

This assignment let's evaluate based mostly on function.
Only a few points for process artifacts.

If you are feeling kind, you may give the student 1 chance to fix a mistake such as `polls.json` data is not compatible with the final database schema.

Suggested point values (**you can change these point values**):

- [5 pt] Github has Iteration 3 Plan and Project Board with several tasks.
  Tasks should mostly be done now.
- [5 pt] Has polls and users fixture files that work -- you can loaddata.
  - Edit `polls/fixtures/polls.json` to check/update the end date on polls before import.  The end date may have past already.
- [2 pt] README.md lists login & password of two users, and they work.
- [4 pt] User can login and logout.
- [10 pt] Each user gets 1 vote per poll.  If you change your vote, the vote totals for the poll are updated correctly.
- [4 pt] You cannot "vote" without being logged in.

**Total: 30 pt**


Suggestions for how to review work after you clone it.

1. Edit `polls/fixtures/polls.json` and check the end date on polls.  If necessary, change the end date:
   ```json
   {
    "model": "polls.question",
    "pk": 1,
    "fields": {
      "question_text": "What is your favorite programming language?",
      "pub_date": "2021-09-09T08:24:02Z",
      "end_date": "2021-09-09T08:25:10Z"  <--- CHANGE THIS, e.g. "2021-12-09"
     }
   },
   ```

2. If there is a `db.sqlite` file, delete it.

3. Run migrations and load the data fixtures:
   ```
   python3 manage.py migrate
   python3 manage.py loaddata users polls
   ```

4. When you perform "loaddata" if it gives an error like:
   ```
   Choice model has no field votes
   ```
   it means the student did not update the fixture (polls.json) for the 
   revised domain model.  In the revised model, the Choice class does not
   have a `votes` field. Instead, there is a Vote class to record votes.    
   Please give the student one chance to fix this.    
   He/she needs to recreate the polls.json file using the final code on master.

5. Create a `.env` file so avoid problems running the app. Most envvars won't 
   be needed, but you only need to create this file once and copy it to each
   project:
   ```
   DEBUG = True
   SECRET_KEY = "1234567890ABCDEFGHIJKL"
   ALLOWED_HOSTS = localhost, 127.0.0.1, testserver
   DATABASE_URL = sqlite:///db.sqlite3
   ```

6. View README.md to get the login and password for the demo users. 

7. (If needed) If there are no demo users, deduct points. Then create the users yourself.  You can do it by running this script ([makeusers.py](makeusers.py)):
   ```python3
   # makeusers.py
   from django.contrib.auth.models import User
   # use any (username, password) that you like
   for (username,pw) in [("harry", "hacker1"),
                         ("sally", "hacker2")]:
       print(f"add user {username} passwd {pw}")
       try:
           User.objects.create_user(username, password=pw)
       except Exception as e:
           print(e)
   print("All Users:")
   for user in User.objects.all():
       print(user.username)
   ```
   and run it using:
   ```
   python3 manage.py shell < makeusers.py
   ```

8. Run server: `python3 manage.py runserver`

9. Perform tests of login/logout and voting.


