---
Title:  Review of Midterm Exam
---

### Questions

> Questions 1 and 2 are graded by individual review of your answers.    
> Questions 3-9 are based on previous assignments.  

1. (6pt) Here is a method to test that the constructor for a "Money" class raises a ValueError when an invalid value or missing currency are given as parameters:
   ```python
   class MoneyTest(unittest.TestCase):
       def test_invalid_values(self):
           with self.assertRaises(ValueError):
               m1 = Money(-1, "Baht")    # should raise ValueError
               m2 = Money(1, "")         # should raise ValueError
   ```
   - What is the problem with this test code?
   - Explain how it may fail to detect an error in the Money constructor.
   **Answer:**   
   If either of the statements raises ValueError then the test passes, even if one of the statements does **not** raise ValueError (a defect in the code).  If the first statement (m1 =) raises ValueError,then the test passes and second statement is never executed.    

2. (6pt) Two people are working on a project with code shared on Github.  Programmer A pulls the curent version from Github and starts work on file gui.py.  Then, (while A is working) Programmer B also pulls the current version from Github, changes some files, and pushes his work to Github.  Finally, Programmer A finishes revising gui.py, commits his work locally, and does "git push" to push his work to Github.
    
   - What will happen?  
   - What will 'git' tell Programmer A and why? 
   **Answer:**    
   Git will refuse the "push" and inform Programmer A that his local version is "behind" the current HEAD revision on Github.  To prevent lose of work, Git requires that new commits always be based on the most recent commit that is being appended to.

3. (6pt) You are working on a project on your local computer, and have committed all your source code to git (locally, not using Github).  If you accidentally delete the file "player.py" from your working copy, can you recover it?

   - [ ] No, when you deleted it from your working copy it is deleted from the git index, too
   - [ ] No, because you didn't create a "remote" on Github as a backup
   - [ ] Yes, use the command "git reset player.py"
   - [x] Yes, use the command "git checkout HEAD player.py"
   - [ ] Yes, use the command "git recover player.py"
   - [ ] Answer depends on the version of git


4. (6pt) There are 3 "roles" in Scrum.  Write the names of the roles.    
   [**Scrum Master**] - keep everyone on track & project progressing, be a facilitator    
   [**Scrum Team** | Development Team] - the developers.   1pt for "Team Members", 0pt for "Developer" (circular definition)    
   [**Product Owner**] - represents the customer


5. (6pt) What are **2 things** to do in a Sprint retrospective? (3pt each)

   - [ ] Examine the burn-down chart to determine the team's velocity.
   - [x] Review what went right and what didn't work well.
   - [x] Look for areas for process improvement.
   - [ ] Revise the Release Backlog based on work done/not done in the last Sprint.
   - [ ] Demo the Sprint work products.


6. (6pt) What is the purpose of the Daily Scrum? Select the best answer.

   - [ ] Review the previous day's work. (incorrect, but gave **2 pt**)
   - [ ] Review the burn down chart and take corrective action, if needed.
   - [ ] Choose tasks for the coming day.
   - [x] Exchange information between team members about their individual work.
   - [ ] Scrum Master assigns tasks to team for the coming day.


7. (6pt) What is the main reason for using branches (instead of master) when working on a team project?

   - [ ] avoid conflicts between commits by different developers (**3 pt**)
   - [ ] to make the repository easier to understand
   - [ ] to make push and pull faster, since there are fewer files on each branch
   - [x] so the master branch always contains working, tested code
   - [ ] so it is clear who is working on which feature


8. (6pt) What are 3 reasons to use a Pull Request? (select 3 best answers)

   - [ ] to announce the start of work on a new branch
   - [x] to request feedback
   - [x] to request help
   - [ ] to post issues related to a specific branch
   - [x] request a review before merging a branch
   - [ ] request a review after merging a branch


9. (6pt) Which of these statements about iterative and incremental development are true?    
   +2 each correct, -1 each incorrect

   - [ ] Incremental refers to completely implementing one requirement at a time to produce a working product.
   - [x] Incremental refers to implementing a subset of desired functionality into a working product, and evolving it over time.
   - [x] Incremental development creates some extra work (rework) to revise the design and implementation.
   - [ ] Each iteration should add a completed increment to the product's functionality.
   - [x] Iterations repeat the same process activities, but the effort spent on each activity may vary.


10. (6pt) What is the purpose(s) of validation & verification? Check 2 correct answers.

    - [ ] Verify that the software exactly matches the specification.
    - [x] Verify that the system satisfies the specification.
    - [x] Validate that the system meets the stakeholders' expectations.
    - [ ] Validate that the architecture is correct.
    - [ ] Validate that the system works in the customer's operating environment.

11. (6pt) What is the difference between requirements and specification?

    - [x] Requirements are what the stakeholders want, specification is a description of how the system will meet the requirements.
    - [ ] Specifications are what the stakeholders want, requirements are a description of how the system will meet the requirements.
    - [ ] Requirements are implicit, a specification is explicit.
    - [ ] Requirements are written from the system point of view, specifications are written from the users' point of view.
    - [ ] Requirements and specification are really two views of the same thing -- what the system must do.

------


### Feedback on Problem 2: (git)
   2pt: What will happen?   
   2pt: What will 'git' tell Programmer A  [wrong: "conflict"]    
   2pt: and why?   [wrong: "conflict"]    
  -1pt: for referring to "main" branch on Github   

**Correct Answer**:

The "push" will fail. Git will inform Programmer A that his latest commit is not based on the current commit (HEAD) on Github, hence he needs to fetch and merge the HEAD on Github into his local repository before he can push his work.

**Incorrect Answers**:

Many incorrect answers state that git tells the Programmer A there is a "conflict". This is **not** what happens.  

- 'git push' does not check for conflicts. It checks that your work is based on the current HEAD of the branch you are pushing to.

- There may not be a conflict anyway. Programmer A changed **only** `gui.py` and Programmer B perhaps did not change gui.py.

Some incorrect answers mentioned "branches" and telling Programmer A to merge his work into "main" or "master".  This question is not about merging branches, and the situation could occur an any branch.


Other Incorrect Answers:

* "Get conflict can't push to Github. Because the files have changed.  Github will manage the file when it's solving the conflict.  If It can't, Github will tell users to resolve the conflict on user work locally."
  - Incorrect: "push" does not attempt to automatically resolve conflicts

* "Git will show conficts because there are some code that conflicts...."

* "Git gonna send error message (conflict) to Programmer A. Because file of Programmer A have conflict with file that on github."
  - *As stated above, this isn't what happens and there may be any conflicts*

* "Git hup will tell programmer A that have some conflicts. Programer A need to git fetch or git pull before merge again."
  - The second sentence is also correct except "merge again".  Programmer A did not merge anything yet. "Push" does not do a merge.

* "Git tell you have to pull from github first. It's can't be push because it have conflicts"
  - First sentence is correct but second sentence is incorrect.

