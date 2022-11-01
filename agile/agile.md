---
title: Agile Software Development
---

"Agile" is a mindset based on a set of **values**.
The values are elaborated in a collection of 12 principles.

There are many practices and methodologies to help you apply Agile, but the mindset is the most important factor for success in applying practices or methods, according to experts.

Agile is *not* a software process -- Agile values and practices are part of many software processes.

## Presentations

[Intro to Agile](agile.pdf) my slides    
[Practices of an Agile Developer](PracticesOfAnAgileDeveloper-slides.pdf) based on the book    
[Scrum Questions & Answers](Scrum-Questions-and-Answers.pdf)    
[Introduction to Agile](https://www.agilealliance.org/agile101/agile-basics/introduction-to-agile/) video by James Newkirk


## Agile Manifesto

The *manifesto* states the core values for agile software development.

1. **Individuals and Interactions** over *Processes and Tools*
   - People respond to business needs and direct the development process

2. **Working Software** over *Comprehensive Documentation*
   - "Just enough" documentation - the customer wants software, not lots of software docs.
   - If requirements are likely to change, writing up-front docs can be a waste.
   - This is not an excuse to _not_ write documentation.

3. **Customer Collaboration** over *Contract Negotiation*

4. **Responding to Change** over *Following a Plan*

These **values** are the reason "why" agile uses specific practices.

Ref: [Agile Alliance](https://www.agilealliance.org/agile101/the-agile-manifesto/)

Agile encourages frequent delivery of running software, customer collaboration,
face-to-face meetings, and self-organizing teams.


## Why Emphasize "Values"?

When people consider adopting Agile, they usually start with Agile "practices". James Newkirk says this approach is likely to fail.

**Values** explain *why* you are doing the practices.  If you don't embrace and agree with the "why", then the practices will fail.  
When the team encounters a problem, if they have "practices" without the "values", they won't have a basis to decide how to resolve the problem.

This is explained in the video by James Newkirk, starting at 40:00 minutes.

Each organization has its own set of values.
Newkirk summarized *his* values and XP values as:

| Newkirk's Agile Values    | Extreme Programming Values  |
|---------------------------|-----------------------------|
| Minimalism                | Simplicity                  |
| Feedback                  | Feedback                    |
| Tranparency               | Communication               |
| Sustainability            | Courage                     |


## Agile Values & Practices

From the video [Introduction to Agile](https://www.agilealliance.org/agile101/agile-basics/introduction-to-agile/) by James Newkirk, starting at 40:00.

Value: **Feedback**

Practices:
- Test-first programming
- Incremental Design
- Ten minute build
- Continuous Integration/Continuous Delivery
- Short development cycle (iteration)

*James Newkirk strongly recommends Continuous Integration*.

Value: **Transparancy**

Practices:
- Collective ownership
- Sit together (no eating in work area, no phones)
- Whole team - devs, testers, project managers all work together
- Informative workspace - Task board with photos so everyone knows what others are doing; burndown chart, cumulative flow chart to show progress

Value: **Sustainability**

Practices:

- Weekly Cycle - avoid overtime and overwork
- Energized work - focus while at work
- Plan for Slack time
- Try to maintain a *sustainable pace*.  Don't overwork. 
- Avoid "big bang" effort near end of project.

Fact:

- Your productivity and skill goes down if you overwork. Error rates increase after 6-8 hours.

Keeping a Balance:

- Balance "*Productivity - Productive Capacity*" (P/PC), as described by Stephen Covey in *The 7 Habits* ("*Sharpen the saw*").

Value: **Minimalism**

Practices:

- Incremental Design
- User Stories
- Minimum Viable Product & Progressive Refinement
- Weekly Cycles


What is a *Minimum Viable Product*?

| Wrong                        | Right                             |
|:-----------------------------|:----------------------------------|
| The crappiest product you could possibly release. | The smallest product release that successfully achieves it's desired outcomes. |
|                              | The smallest thing you can create to prove or disprove an assumption. |

Source: Jeff Patton, *User Story Mapping*


## Twelve Agile Principles

Source: [12 Principles](https://www.agilealliance.org/agile101/12-principles-behind-the-agile-manifesto/) at Agile Alliance.
[Another version, with commentary](https://www.smartsheet.com/comprehensive-guide-values-principles-agile-manifesto#the-twelve-agile-manifesto-principles).    
[Nice interpretation of the 12 principles](http://www.consultparagon.com/blog/12-principles-of-agile-methodologies) at Paragon Consulting.    

1. *Satisfy the Customer* through early and frequent release of software. Collaboration and communication with Customer.
2. *Accommodate change*
   - Welcome changing requirements, even late in development.
   - Change means you are getting closer to client's true needs.
3. *Deliver frequently*  (Didn't they already write this in #1?)
4. *Collaborate between stakeholders and developers*
5. *Support, trust, and motivate the people involved*
6. *Enable face-to-face interactions* within team and between team-customer.
7. *Working software is the primary measure of progress*
8. *Maintain a Sustainable Pace* - be able to deliver quality iteration-after-iteration, project after project; maintain work/life balance.
   - P-PC Balance (Stephen Covey's Principle of Effectiveness).
   - Avoid overtime.
9. *Continuous Attention to Excellence* - attention to technical detail and design enhances agility, improves the product, enables change.
10. *Keep it Simple* – develop just enough for current goal.
    - "Maximizing the amount of work not done"
    - Not an excuse for bad design or poor code (principle 9)
11. *Self-Organizing Teams* encourage the best results.    
    Quality products come from skilled and motivated team members who have decision-making power, take ownership, communicate regularly, and share ideas.
12. *Regular Reflection* on how to become more effective.
    - (What are some *actions* that might result from reflection?)

## Methods based on Agile Values

* Scrum and XP are development-focused methods based on Agile values.
* "Plan Based" or "Plan Driven" processes are considered non-agile, but this is not really true -- Plan based projects can incorporate agile values.
  - Unified Process (UP) is main example.
  - Plan-based vs Agile process is a continuum of choices, not either-or.

## Agile Practices You Can Use

* User Stories - requirements from the user's perspective
* Test-Driven Development - write tests before writing the code
* Code Review - review all your code and ask others to review it, too.
* Pair Programming - one person codes (focus on the code) while another thinks and reviews (how code fits the overall design)
* Time-boxed iterations 
* Maintain a Sustainable Pace - do work early and regularly, not at the deadline. Avoid overwork.
* [Retrospectives](#retrospectives) - reflect on how to do better, and take action
* Continuous Integration - automate build and testing of your product, so you have constant feedback.
* Task Board - so everyone is aware of what others are working on.
* Burndown chart - monitor your progress daily.


## Story Map versus Task Board

A **Task Board** shows tasks for the current iteration and their status.
A task board can also be used for a release (shows release backlog).

A **Story Map** shows relationships between stories. It shows:

* "core" or "foundation" stories
* stories that build on other stories
* stories ordered by release

![example story map](/ISP/images/story-map-example.png)
## Burn down and Burn up charts

A **burn down** chart shows the remaining work versus time.
The y-axis (remaining work) is measured in hours or story points.

In a **burn up** chart, there is a top line for the total number of points (scope) of the iteration.  The top line may change as: (a) work is added or removed (unplanned tasks), (b) tasks are re-estimated.  The graph shows the tasks done, measured in hours or story points.

## Retrospectives

Purpose of retrospective is to improve the team's development process.

1. Set the stage - ensure everyone understands the goal and focus of retrospective. Give people a chance to talk at start of the meeting; so they will be more open later one.

2. Gather data - look at events of last sprint. Walk through work done and decisions made.  Get team to express view/feeling of the events.

3. Generate insights. Zero in on problematic events. Identify causes and try to trace them to "root" causes.

4. Decide what to do.  Create a plan for improvements or changes to make in the next sprint.

## Agile Practice Exam

[Sample Questions from agileexams.com](https://www.agileexams.com/sample/) many of them just knowing the names of things (poor questions -- understanding the *meaning* and *reason* is more important).


## Learn More 

* [Agile 101](https://www.agilealliance.org/agile101/) at Agile Alliance.    
* *Practices Of An Agile Developer* - we will study some parts of this book
  - [slides from the book](PracticesOfAnAgileDeveloper-slides.pdf)
  - [Quick Reference Card](../resources/PAD-quickref.pdf)
  - Book excepts - URL given in class
* Video [Introduction to Agile](https://www.agilealliance.org/agile101/agile-basics/introduction-to-agile/) starting at 36:00, by James Newkirk, explains importance of Agile values and practices related to values.
* *Learning Agile* by Stellman and Green (O'Reilly). The best book about Agile.  The content is similar to *Head First PMP* (lots of stories and example questions) but *Learning Agile* is much shorter.
* [Agile Practice Guide](Agile-Practice-Guide.pdf) from Agile Alliance.


Interesting, but less valuable:

* Video: [Agile at Microsoft](https://www.youtube.com/watch?v=-LvCJpnNljU) about the Visual Studio Team Services transition to agile. Interesting, but some fuzzy use of buzzwords like "team owns X", "team is empowered to ...". 41 minutes.

## Agile Books

*Learning Agile* by Stellman & Greene (O'Reilly 2013). The authors have practiced, taught, and written about Agile for 20 years. Covers the same topics as *Head First Agile*.

*Head First Agile* by Stellman & Greene (2017) - very memorable explanation and examples of Agile practices and values; many review questions and sample questions from PMI Exam. But long. *Learning Agile* has the same content in fewer pages, without the cute examples and review questions.

*Agile Practice Guide* by AgileAlliance and PMI. Short, precise guide to applying Agile. Appendix X3 is a tool to assess how suitable Agile is to a project. Tool is similar to Barry Boehm's book *Balancing Agility and Discipline*.
