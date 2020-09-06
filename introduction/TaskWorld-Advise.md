---
title: Developer Habits and Skills, a Perspective from TaskWorld
---

[TaskWorld](https://taskworld.com) makes a project management application that competes with Slack.
It's an international company with high standards that does a lot of development in Bangkok 
and have hired some top SKE graduates.

I asked SKEs at Taskworld what habits and skills they recommend to students
wanting to become professional developers.

Here's a summary of what they had to say...

### Resourcefulness

When working, developers face issues that they have never been taught.
An important skill is how to find answers.
- Understanding stack traces and logs
- Reading API docs
- Using Google to find a solution
- Asking good questions on StackOverflow

### End-to-end software life cycle

One engineer told me, when they were studying and working in a group project,
there is always the same person who will work on operations (e.g. deployment).
Ideally, a developer should be able to bring their ideas to life on their own.
Including:
- Design a solution
- Implement a solution
- Testing
- Manual deployment
- Automated testing
- Continuous integration
- Continuous deployment

### Be Proactive in understanding the fundamentals

Most software nowadays is made by glueing together ready-made parts.
When they parts don’t work as expected, 
if developers don’t know how each part works, 
then fixing the problem is hard.
To be more effective, I sometimes read through the docs of fundamental things, 
even though it's not needed right away.

Many developers learn reactively and just-in-time when they need to solve a problem.
This means they only know few methods that they had to use.
When they encounter a new problem, they try to use what they know little about, and come up with convoluted code, when there is a method that solves it more effectively.

Example, some people write this (Javascript):

    const finishedTasks = _.filter(tasks, task => task.finished)
    const unnishedTasks = _.reject(tasks, task => task.finished)

But having proactively read through the docs of the utility library (`_`), I know that we can do this instead:

    const [finishedTasks, unfinishedTasks] = _.partition(tasks, task => task.finished)

More generally

> *if you are working at the edge of your knowledge you will make more mistakes
> and be less productive because you don't use the capabilities that are
> beyond the edge of your knowledge.*

### Attention to detail

When interviewing prospective hires, they look for people who pay attention to details.
For example, correct spelling and grammar in their resume and repository READMEs.
Consistently using a coding convention, documenting your work, not leaving unfinished
code (e.g. ignored exceptions) around.

Taskworld thinks this is an important habit, since correct software depends on
attention to details.

### Understand and appreciate design principles

I heard that students don’t get much from learning design patterns in OOP.

It feels like they had to remember class diagrams for whatever reason.

I would focus more on getting students to feel the experience of a working but unmaintainable code.
Then, when design principles and patterns come to the rescue, they may have a better appreciation of them.
Refactoring katas may help.

### Understand and appreciate project management tools

One engineer told me that when working in a group project,
they don’t see why they have to use tools like Trello.
So the tool is unused and problems arise.
I would focus on common communication problems that occurs when doing group projects before introducing tools, so students can associate a tool with a problem it’s intended to solve from the beginning.

### Using Git and GitHub with a Git Workflow

I recommend GitHub Flow (https://guides.github.com/introduction/flow/, not the same as Git Flow), and it works in solo projects as well as team projects.
The code in master branch is live in production (automatically deployed by CI).
To not break production, a developer pushes work in progress and changes in a topic branch, opens a pull request early, reviews it, and once tested, merge it into production.
This allows for keeping the master branch stable, which is important later for working in teams.

## Other Suggestions

- Good error handling practices makes debugging easier.
- Most likely, the students will have to work on assignments in other subjects, so time management is essential.
- Automated testing skills — how to write good tests. Tests should make software easier to change safely, not harder. Bad tests prevents the code from being refactored.

