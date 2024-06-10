---
title: Lab Schedule
---

> The **official** weekly schedule and assignments are on
> **[Google Classroom][google-classroom]**.

[google-classroom]: https://classroom.google.com/w/NjE0ODE4Mzg4ODEz/t/all

### Preparation

Please do this before the first week lab.

- [Sign-up and Install Required Software](assignment/week1/signup-and-software)
- Read [About the course](about) for how to contact TAs and Instructors.


### Lab 1 

- Code warm-up and Github Classroom practice.
- Review of Python and OO.
- Coding skill assessment, submitted to Github Classroom.
- [Scrum](agile/scrum)
  - Watch [Scrum in Under 10 Minutes](https://www.youtube.com/watch?v=XU0llRltyFM) on Youtube
  - Read [Scrum Guide](https://www.scrumguides.org/scrum-guide.html), at least first part.
  - Answer [Questions about Scrum]() and submit on Google.

- [Introduction to the course](introduction/)
- [Introduction to software process](software-process/)


### Homework for Lab 1

1. Read and study the official [Scrum Guide](https://www.scrumguides.org/scrum-guide.html). Anything on this page may be in a quiz.
   - Thai translation: 
2. Learn the style rules for writing Python code. 
   - [How to Write Beautful Python Code with PEP8](https://realpython.com/python-pep8/) on [Real Python](https://realpython.com/)
   - For docstring comments, we use the Sphinx style EXCEPT use *type hints* instead of parameter and return types in comments. Type hints are more useful!
     ```python
     def gcd(a: int, b: int) -> int:
         """Compute the greatest common divisor of a and b.

         :param a: first value to compute gcd of.
         :param b: second value to computer gcd of.
         :returns: greatest common divisor of a and b. It is always positive,
                   unless both a and b are zero.
         :raises:  TypeError if a or b is not an integer
         """
      ```


### Lab 2

- [Git](git/) concepts, Git commits as a graph, managing files and using Git history. 
- Exercise: use the [Git Visualizer](http://git-school.github.io/visualizing-git/) to see a git graph
- Exercise: Git practice (submit on Github)
- [Git branch and merge](git/branch-and-merge)
- Exercise: practice merge and conflict resolution
- [Git remotes](https://cpske.github.io/ISP/git/Git-Remotes.pdf)
- Exercise: use `gitk` tool that is included with git
- [Using Github](git/Using-Github) (you probably already know this)
- Github Flow and Pull Requests - [Github's Intro](https://guides.github.com/introduction/flow/)
- Exercise: Github Flow questions (Google form)
- Exercise: KU Cafe

### Homework for Week 2

1. Complete parts 1-2 of [Learn Git Interactive](https://learngitbranching.js.org/). The section on *Moving Work Around* is highly recommended.
2. Complete Part 1 of the Git commands "cheat sheet" on Github.  Clone the template repository (contains questions) and commit your answers to Github.
3. Read [Github Flow](https://guides.github.com/introduction/flow/) (very short)
4. Read [Pull Request Tutorial](https://yangsu.github.io/pull-request-tutorial/) (also short).
   - Github Flow uses *Pull Requests* before merging, so you need to know how to use them!

Optional:
  - [Commenting on Pull Requests](https://help.github.com/en/articles/commenting-on-a-pull-request)

