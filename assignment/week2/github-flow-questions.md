---
title: Questions about Github Flow
---

There are other questions in the Google form.

1. What is the One Rule of Github Flow? 

2. You want to implement this new feature in your web app:
   "*Users can login using OAuth*"     
   [when you go to a web site and it has "Login with Google" or "Login with Facebook" buttons, it uses the OAuth protocol to do that]

   What is a good name for this branch (according to the advice in the Github Flow readings)?

3. When you want to request feedback from others on your work, what should you do?

4. You should open a Pull Request when?
   - [ ] you start work on a new feature
   - [ ] you find a bug in your work
   - [ ] you finish work on the branch
   - [ ] you want review and feedback from others
   - [ ] your time on the task exceeds estimated time, so you want Scrum Master to review it

5. After you open a Pull Request, what are some things the team might comment on?
   - [ ] Coding style
   - [ ] Unit tests are missing some test cases or not covering the code
   - [ ] Suggest some refactoring
   - [ ] Bugs or something you forgot to do in your work
   - [ ] Another way you might implement something
   - [ ] Compliment on your good work

6. When you finish work on the feature and it passes your unit tests, what should you to test the application with your feature?
   - [ ] Open a Pull Request and request permission to deploy it
   - [ ] Merge into master so the Continuous Integration system will test it
   - [ ] Merge into master and deploy the application to production site
   - [ ] Deploy from the feature branch to a pre-production site
   - [ ] Any of these 

7. When you (finally) are ready to merge your feature into the master branch, what should you do?
   - [ ] Just do it - merge into master
   - [ ] Merge master into the feature branch to check for conflicts, then reset "master" to point to the branch
   - [ ] Open a Pull Request to request others review and approve the final code
   - [ ] Something else

8. You want to implement a feature that's in the backlog for this iteration. Put the steps in the order you would typically do them using Github Flow.
   - [ ] Open an issue on Github with title "Pull Request".
   - [ ] Push your branch to Github.
   - [ ] Create a local branch for your work.
   - [ ] Merge your branch into master.
   - [ ] Merge master into your branch then rebase.
   - [ ] Wait for the team to review and approve your work. 
   - [ ] Implement and test your feature.
   - [ ] Open a Pull Request.
   - [ ] Pull updates on master to your local machine in prep for merge.

   Correct order:
   - [ ] Create a local branch for your work.
   - [ ] Implement and test your feature.
   - [ ] Push your branch to Github.
   - [ ] Open a Pull Request.
   - [ ] Wait for the team to review and approve your work. 
   - [ ] Pull master to your local machine in prep for merge.
   - [ ] Merge your branch into master.
   Not part of flow:
   - [ ] Open an issue on Github with title "Pull Request".
   - [ ] Merge master into your branch then rebase.
