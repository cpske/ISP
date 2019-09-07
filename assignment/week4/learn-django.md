## Learn Django by Implementing the Tutorial App

We will use Django and the Django tutorial app to learn several concepts.    
You will add to this app in future weeks, so don't fall behind on this assignment.

* Learn about Django at [https://www.djangoproject.com/start/][django-start].
* Install Django on your computer.
* *Recommended:* Install the [Django Documentation][django-docs] and bookmark it in your browser.  
    - On the [Django Documents][django-docs] page look for "Download" (right-side column).
    - For finding stuff, the "Detailed table of contents" is good starting point.
* Use Python 3.6 or newer.  v3.6 adds several useful features, including [f-strings][f-strings].

### Assignment

1. Do the Django Tutorial **parts 1 - 5** at Django [Getting Started][django-tutorial].
    - The tutorial is part of the [Django docs][django-docs] download; if you install the docs locally then you can do the tutorial offline.
2. Replace the (stupid) example question "What's up?" with **2 poll questions** of your own choice.  Ask some friends to take your polls.
3. Create a local git repo for your work and do this:
    - Add a `.gitignore` to ignore files you should not commit to the repository.  You can use Github to see examples of what to put in this file (as demoed in class) or see my "Git Basics" slides.  
    - Be sure to ignore the database (`db.sqlite3`), Python compiler output, and IDE project files.
4. Commit your work to the **master branch**. OK to use dev (feature) branches during your work, but merge into master before pushing to Github.  
    - You'll use other branches for future work.

### What to Submit & Evaluation

1. Push your work to Github.  Create a Github repo named `django-polls` in your individual Github account (*not* the ISP19 organization).
    - Github repo name must be **django-polls** (lowercase).  No credit if you use any other repo name on Github.(*)
    - Example of correct repo location: `https://github.com/fatalaijon/django-polls`
    - Github repo name does **not** need to be the same as your local project directory.
    - Include your `.gitignore` in the Github repo.
    - For professional looking work, include a `README.md` that describes the project and features you implement.  Include notes about interesting items.  Keep this file up-to-date.
2. Instructor and/or TAs will ask questions to test your understanding, based on the tutorial.  Most of your score depends on how well you answer the questions.

---
(*) If you use the wrong repo name on Github, then rename it in the "Settings" tab.  After renaming on github, you also need to change your local URL for `origin` using `git remote set-url`.

[django-start]: https://www.djangoproject.com/start/
[django-docs]: https://docs.djangoproject.com
[django-tutorial]: https://docs.djangoproject.com/en/2.2/intro/
[f-strings]: https://realpython.com/python-f-strings/
