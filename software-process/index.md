---
layout: page
title: Software Process
description: Index page
---

* What is a software process, and what are its components?
* All devs have a software process, whether they realize it or not.
* If you never thought about your process, then it is *implicit*.  If it changes on each project, then its *ad hoc*.  Both *implicit* and *ad hoc* processes tend to be inefficient and hard to predict the outcomes. 
* The problems of software development that drive the need for a good software process are
  - complexity
  - change
  - (high) defects and errors
  - need to estimate time and cost
  - lack of predictability or consistency
  - (un)maintainability
* Along with software process you need to know the software development lifecycle, since the process and SDLC influence each other.

*Process* is one of the key dimensions of a software project that determines speed and outcome.  

## Key Dimensions in a Software Project

1. Budget and effort
2. Features (scope)
3. Time
4. Quality

These may be given to you as requirements or things you have some control over -- that is, you can negotiate them with customer or management.

You can "trade off" one dimension to meet requirements of another.  For example, to meet a time constraint you either reduce features, add effort (more developers), or spend less time on testing and review (reduce quality).

Example:

* Time
    - constraint: For a game, the deadline might be Nov 1 for the Christmas shopping season.  For a NASA space mission, time is dictated by the entire project -- they can't wait for software to be ready.
    - negiotiable: 

## Fifth Dimension: Process

* How can you reduce time or effort with reducing scope or quality?
* Can you improve quality without increasing effort or time?

One way is a change in technology: a different language or better development tools (IDE instead of a text editor).  But these usually don't have a big effect.

Another factor is training and education.  That takes time,
so it may not help a current project.

One factor that *can* have a big effect is **software process**.

A good process helps to:

   - structure development so you get the most done while maintaining quality
       - use iterative development with short iterations and specific milestones
       - have defined roles and responsibilities
   - incorporate practices to make development more efficient or to produce good quality software
       - make "pull requests", code review, and unit testing a part of the workflow
       - "retrospective" meeting after each iteration to improve process
       - use continuous integration (CI) to automatically build and test your software
       - tracking of issues and defects
   - make routine decisions automatic so you don't waste time deciding them
       - a defined set of process steps, 
       - defined workflow for version control (Github Flow)
       - checklist of things to do for a code review
   - provide data and guidance for improving the process
       - keep a record of defects and their causes


[Introduction to Software Process (PDF)](Introduction-software-process.pdf),
[(PPT)](Introduction-software-process.ppt)

## Software Development Life Cycle Models

To plan a project you need some idea of what you're going
to do, and in what order.  That info comes from a SDLC.

Common SDLC's are:

1. Waterfall
2. Iterative and Incremental
3. Unified (Software Development) Process - a framework for software processes.  It is iterative and incremental.

You should be familiar with the details of Waterfall and the UP.
Its not sufficient just to know their names and vaguely what they are.


## Online Courses

These 2 are part of the "Software Development Lifecycle" specialization, offered by University of Minnesota.

*Software Development Processes and Methodologies* on coursera.org (free).

*Engineering Practices for Building Quality Software* on coursera.org (free).

https://www.freestudy.com/best-free-online-software-engineering-courses/ description and links to other software engineering courses.

There are many good courses on edX and Coursera related to this subject.  Many are titled "software engineering" or "software development".

A popular course pair on edX is "Agile Development using Ruby on Rails" by David Patterson and Armando Fox of U.C. Berkeley.

