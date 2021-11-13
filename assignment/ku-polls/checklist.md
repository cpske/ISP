## KU Polls Checklist

Here is a list of what the TAs will check.  Each item contributes to score:

### [Iteration 2](iteration2) (Week 5 Assignment)

- [ ] Iteration 2 Plan in wiki with Goal and major work to Implement.
- [ ] Iteration 2 Project Board with tasks covering work in Iteration Plan.
     - All tasks should be done.
- [ ] `iteration2` branch on Github, already merged into `master`.
- [ ] Unit tests for `can_vote` and `is_published` methods of `Question` class.
- [ ] In `settings.py`, externalize at least `SECRET_KEY` and `DEBUG`, but supply defaults in case the `.env` file is missing.
  ```
  DEBUG = config('DEBUG', default=False, cast=bool)
  SECRET_KEY = config( ... )
  ```
- [ ] The poll detail and poll voting results pages contain hyperlinks so visitor can go back to polls index page.
- [ ] Improved formatting of polls results page. Not a bulleted list.

### KU Polls CI (Week 8 Assignment)

- [ ] Added CI to run tests and code coverage. 
- [ ] Have a Travis-CI "badge" in README.md that is link to latest Travis build.
- [ ] Have a CodeCov "badge" in README.md that is link to latest CodeCov report.

### [Iteration 3](iteration3) (Week 11 Assignment)

- [ ] Iteration 3 Plan in wiki with Goal and major work listed.
- [ ] Iteration 3 Project Board with tasks. Tasks should be done now.
- [ ] `iteration3` branch on Github with work, merged into `master`.
- [ ] Added User model so each user gets 1 vote per poll.
- [ ] User can login and logout.
- [ ] Create 2 demo users and write their login & password in README.md.
     - These users should be in your users.json fixture file.

### [Data Fixture](https://cpske.github.io/ISP/assignment/week12/ku-polls-data) (Week 11 Assignment)

- [ ] Have data files "polls/fixtures/polls.json" and "polls/fixtures/users.json".
- [ ] Data fixtures **work** with latest code on `master`. Try the test below.
- [ ] Please remove any old fixture files in other directories. (avoid confusion)


## The Test - Does Your Code Work?

Anyone should be able to do this:

1. Clone the `master` branch of your KU Polls from Github.
2. There **should not** be a `db.sqlite3` in the repo, but if there is then **delete it**.
3. Run these commands (they should work!):
   ```
   python3 manage.py migrate
   python3 manage.py loaddata users polls
   # this may need a .env file to work if author didn't provide defaults
   python3 manage.py runserver
   ```
4. (Optional) Prepare a `.env` file:
   - If the repo has a `.env-sample` or `sample.env`, then rename it to `.env`.
   - If not, create a `.env` containing:
     ```
     # Some of these values may not be needed by your app.
     # These are the most common settings that someone may externalize.
     SECRET_KEY = "1234567890ABCDEFGHIJKL"
     DEBUG = True
     ALLOWED_HOSTS = localhost, 127.0.0.1, testserver
     DATABASE_URL = sqlite:///db.sqlite3
     ```
5. View README.md to get the login and password for a demo user.
   - Many students used values based on in-class demo:
     ```
     demo1  password: Vote4me!
     demo2  password: Vite4me2 
     ```
6. Navigate to <http://localhost:8000/polls>. 
   - There should be a list of polls.
   - There should be a login button or link.

7. Verify these features for Iteration 2 and Iteration 3.
   - One user one vote, and can change his vote later.
   - Improved navigation links.
   - Improved display of poll vote results (no bulleted list).


Ask a friend to try this with your code!

Be nice & test a friend's code.
