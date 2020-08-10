---
title: Software Process
---

Presentation: 
[Introduction to Software Process (PDF)](Introduction-software-process.pdf) 
[(Google Doc)](https://docs.google.com/presentation/d/1IfBcNJ5Pnuiji7cqcFctj_N9SEhx4KwJnJn_vUe3GLI/edit?usp=sharing)

## What is a software process?

Here are definitions of "software process" from some well-known textbooks on software engineering.

---

From *Software Engineering*, 9E by Ian Summerville:

> A *software process* is a sequence of activities that leads to the
> production of a software product.  There are four fundamental activities that
> are common to all software processes. They are:
>
> 1. Software specification
> 2. Software development
> 3. Software validation
> 4. Software evolution

Chapter 2 (*Software Process*) of Summerville's book describes software
process models and activities. It includes common processes, such as Waterfall and RUP.

---

From *Object-Oriented and Classical Software Engineering*, 8E, by William Schach:

> The *software process* is the way we produce software. In incorporates
> the methodology with its underlying software life-cycle model, techniques,
> tools, and the individuals building the software.

This is a round-about definition referring to other terms defined elsewhere.

---

From *Software Engineering, A Practioner's Approach*, 7E by Roger Pressman:

> A *process* is a collection of *activities*, *actions*, and *tasks* that are
> performed to create some work product. 
> An *activity* strives to achieve a broad objective (e.g. communication with
> stakeholders) and is applied regardless of the application...
> An *action* (e.g. architectural design) encompasses a set of tasks that 
> produce a major work product (architecture design model).
> A *task* focuses on a small, but well-defined objective (e.g. conducting a 
> unit test) that has a tangible outcome.

He also writes that:
> ... a process is not a rigid prescription for how to build software
> Rather, it is an adaptable approach that enables the software team
> to pick and choose the appropriate set of actions and tasks.

> A **process framework** identifies a small number of *framework activities*
> (umbrella activities) that are applicable to all projects.

According to Pressman, the "framework activities" are:
* communication
* planning
* modeling
* construction
* deployment

---

"Process Models in Software Engineering" by Walt Scacchi in the *Encyclopedia of Software Engineering*, 2E, defines:

> A *software process model* is a sequence of activities, objects, transformations,
> and events [for] software evolution. 

Activities consist of a sequence of actions, which can be broken down into
"task chains".


## Do You Have a Software Process? 

describe your own software process (if you have one :-)


## 


 and what are its components?
* All devs have a software process, whether they realize it or not.
* If you never thought about your process, then it is *implicit*.  If it changes on each project, then its *ad hoc*.  Both *implicit* and *ad hoc* processes tend to be inefficient and hard to predict the outcomes. 

## The Value of a Defined Process

The problems of software development that drive the need for a good software process are

- complexity
- change
- (high) defects and errors
- need to estimate time and cost
- lack of predictability or consistency
- (un)maintainability

Along with software process you need to know the software development lifecycle, since the process and SDLC influence each other.


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

## Fifth Dimension of a Software Project: Process

* How can you reduce time or effort with reducing scope or quality?
* Can you improve quality without increasing effort or time?

One way is a change in technology: a different language or better development tools.  But these usually don't have a big effect.

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

### Summary of Software Process

Software process models view a process as **activities** broken down into smaller, more specific and tangible **actions** and/or **tasks**.

Activities, actions, and tasks depend on some inputs including work products, guidance, standards, checklists, and more, collectively called **artifacts**.  There is also some output, also a work product.

For any activity, action, or task you need a clear *goal* and a way to know when the task is "done".  That is, an *evaluation criteria*.

In the Waterfall Model, activities match phases of the project life cycle. 
Ideally, a project would progress linearly from the Requirements phase through Maintenance.  In practice, its often necessary to backtrack to previous phases to correct errors or deficiencies.  This often leads to schedule and cost overrun.

In Waterfall or any linear process, engineers feel compelled to "get it right"
the first time,
leading to [Analysis Paralysis](https://en.wikipedia.org/wiki/Analysis_paralysis) -- which aflicts decision-making of all forms.
They prolong work to ensure that nothing is overlooked.
This, too, causes schedule overrun and often fails anyway.

Iterative and Increment Processes, develop a product iteratively.
In each iteration some feature(s) of the product are chosen to implement (the increment) and all activities (requirements, analysis, design, coding, verification) are performed.  When an increment is done, there should be a working, "potentially shippable" product, even though it has limited functionality.

The motivation behind iterative and incremental is provide frequent
opportunities for customer feedback, and opportunity for developers to learn
and improve the product during development.  This reduces risk and
uncetainly, but creates extra develepment work.

The U.P. is a popular software process framework.  It claims to be 
"architecture centric" and emphasizes early risk (of failure) reduction.
The project life cycle consists of of 4 major phases which can be
further subdivided.  Each phase has one or more iterations with defined
goals.
Activities are categorized into *workflows* or *disciplines* and
provide a second dimension to the process (the first dimension being
time or phases).

The UP is often criticized as "document heavy" and overly plan-based.
This criticism isn't really justified.  
Craig Larman's *Applying UML and Patterns* (textbook on software design,
used in Software Spec &amp; Design) explains
that you can tailor the UP to be as light-weight as you want.


## Software Development Life Cycle Models

To plan a project you need some idea of what you're going
to do, and in what order.  That info comes from a SDLC.

Common SDLC's are:

1. Waterfall
2. Iterative and Incremental
3. Unified (Software Development) Process - a framework for software processes.  It is iterative and incremental.

Less common but often mentioned in textbooks are:

* Spiral Model - iterative and incremental with focus on risk
* Rapid Prototype - learn from prototypes.  Many processes do this and its not a complete model.
* Reuse-Oriented Engineering - this isn't a process, it's a strategy for implementing the requirements. Almost all projects reuse software at different levels; for example, using a *framework* for a web application.

You should be familiar with the details of Waterfall, iterative and incremental, and the UP.
Its not sufficient just to know their names and vaguely what they are.


## Online Courses


[Software Development Processes and Methodologies](https://www.coursera.org/learn/software-processes/), U. of Minnesota on Coursera.  A good overview course for the activities in a software process. Some good advise on developer habits.
 * This course is part of a 4-course series "Software Development Lifecycle" by U.M. that looks interesting.

*Engineering Practices for Building Quality Software* on coursera.org (free).
 * Also by U. of Minnesota.

https://www.freestudy.com/best-free-online-software-engineering-courses/ description and links to other software engineering courses.

There are many good courses on edX and Coursera related to this subject.  Many are titled "software engineering" or "software development".

A popular course pair on edX is "Agile Development using Ruby on Rails" by David Patterson and Armando Fox of U.C. Berkeley.

### Reading

* [Software Processes - Summerville, Chapter 2][summerville] from *Software Engineering*, 9E, by Ian Summerville.
  - simple, concise description of software process models and activities

* [Software Life-Cycle Models (ch. 2) and Software Processes (ch. 3)][schach] from *Object-Oriented and Classical Software Engeering*, 8E, by William Schach.
  - more detail than Summerville's explanation, emphasis on the U.P. as model
  - chapter 2 contains most of what you need to know
  - chapter 3 describes the "workflows" in a software process, using the UP as a model

* Pressman, Chapter 2 [Process Models][pressman] is a slightly more abstract introduction to software processes, from *Software Engineering: A Practioner's Approach*, 7E, a well-known book by William Pressman.

* Winston Royce, [Managing the Development of Large Software Systems][royce], the original article describing the waterfall model (Royce didn't call it that). This classic paper is very short.

[summerville]: https://cpske.github.io/ISP/resources/Software-Process-Summerville-ch2.pdf
[schach]: https://cpske.github.io/ISP/resources/Software-Process-Schach-ch2-3.pdf
[pressman]: https://cpske.github.io/ISP/resources/Software-Process-Pressman-ch2.pdf
[royce]: https://cpske.github.io/ISP/resources/Royce1970-Managing-the-Development-of-Large-Software-Systems.pdf
