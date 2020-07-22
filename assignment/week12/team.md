---
title: Iteration Planning and Github Site Setup (Team Assignment)
---

On your Github project homepage (README.md), please include in this order:

1. Description of the project.  At least one paragraph.

2. Team members

3. A section titled "Project Documents" including links to these document:
   * Link to your **Iteration Plans** in Github Wiki or shared Google Doc.
       - Can put all plans in one file or separate file per iteration
       - When someone clicks on this link it should actually show a list of iteration plans (if you have more than one) or directly open the iteration plan document.  Just linking to the wiki is not good enough.
   * Links to your **task board**, showing tasks for current iteration
       - Tasks have details, person, estimated time
   * Link to other project documents, such as:
       - Code Review Script and Checklist
       - Project Proposal
       - design documents
       - mockups or screen flow diagram
    * You can put all this in project Wiki, which makes it easy to organize and use


You may have other information on the home page. 

Showing CI status is good, but it should be accurate.

### Iteration Plan

Create a plan for the current iteration, and do it for all future iterations.

Each Iteration Plan includes:

* **Dates** Start date and end date of iteration
* **Goal(s)** for this iteration.  A "goal" can be descriptive such as
  > Identify most use-cases, and record them in project wiki with brief description of each use case.    
  > Implement "play game" use case 
* **Milestone(s)** 
    * A "milestone" is something that shows progress toward finishing the project.
    * Is concrete and verifiable.
    * Milestone is usually related to running software -- not documents.  But in first 1-2 iterations a milestone can be a non-code artifact.
    * **Not** a milestone: "Learn to use xxx".
    * Some early iteration milestones:
    > "Create a domain model for game, and produce a working prototype that shows questions."       
    > (This is only a "milestone" if you make a good, *written* domain model and put it online.)  
    > "Demo User can view/answer questions and his score is recorded"
* List of **features** to implement in this iteration or **major work**. In first iteration, there may not be any features.
    * Don't write detailed tasks. Those go in your task board.
* **Summary** of Retrospective.
    * Record import results of iteration.
    * Note any features, tasks, milestones you **didn't** achieve, and why.
    * No plan is perfect. Expect to "miss" milestones and goals, and be honest about it.

### Write Good Iteration Plans

Iteration Plans should be clear about the work to be done and goal of the iteration.
Several iteration plans reviewed so far need improvement.  Check your current iteration plan

* [ ] Goals are clearly stated and precise.  Goals should be something the app can **do**, or some characteristic it **possesses**.
    * functional ("doing") goal:  a user can authenticate himself and view list of current polls.
    * non-functional goal: app is deployed to AWS EC2, configuration data removed from `settings.py`.
    * Poorly written goals: "Implement basic UI", "Connect Django to React", "Separate data into categories" (a task not a goal, and its too vague), "make index page" (also a task)
* [ ] Tasks are clearly stated and specific.  Tasks are something for a person to do.  Avoid tasks that are too broad or vague.
* [ ] Milestones involve work products that show progress toward finishing the project.


### Descriptive Tasks with Time and Team Member

Many tasks are poorly written. The descriptions are vague, lack detail, don't contain time estimates (or actual time for "done" tasks), or the name of person performing the task.

1. Tasks should be added to task board during the iteration planning meeting. New unplanned tasks can be added during the iteration.
2. Task names should be clear and specific.  Use the body of task item to provide additional information.
3. Tasks should have an estimated time, and completed tasks should have the actual time spent.  For learning, it is good to be honest about actual time spent and compare the estimated and actual times.

| Poor task description   |  Reason |
|-------------------------|---------|
| *Add more unit tests*   | Too vague, not specific, and too broad. |
| *CI*                    | Not something to do. Better: "Setup CI using Travis." |
| *Hotfix security*       | Fix *what*?  Why is it a "hotfix"? |

### Iteration "Script" - How to Do Iteration

This is a guide to get started, based on typical Agile project workflow.

Adapt it to suit your team process. You should do iteration planning (with written output), iteration review/demo, and retrospective.

<table border="1">
<tr valign="top">
  <th>Activity</th>
  <th width="80%"> Description </th>
</tr>
<!-- Introduction -->
<tr valign="top">
<td align="center" markdown="span">
Planning Meeting    
(start of iteration)
</td>
<td align="left" markdown="span">

1. Review results of previous iteration.     
    - Any unfinished work from last iteration?  Add it to Project Backlog.    
    - Any new work you discovered? Add that to Project Backlog, too.    
    - Any major problems or risks you should address?  How?    
2. Decide on...    
    - major work to do this iteration    
    - goal(s)    
    - milestones - markers that demonstrate real progress    
    - Get help with issues you don't know how to solve (TA/instructor)    
3. Revise or write current iteraion plan in Wiki or Google docs.    
4. Plan the work!    
    - update your software design or user-interaction model    
    - decide on tasks and add them to Task Board as Iteration Backlog    
    - annotate tasks: a) write detailed description or steps, b) estimate time    
</td>
</tr>
<tr valign="top">
<td align="center" markdown="span">
Output of 
Planning Meeting    
</td>
<td align="left" markdown="span">

- Iteration plan in Wiki/Google Docs    
- Goals and Milestones recorded    
- Tasks in iteration backlog (or Sprint backlog) on task board    

</td>
</tr>
<tr valign="top">
<td align="center" markdown="span">
During Iteration
</td>
<td align="left" markdown="span">

- Update task status and details     
- Record person doing task and time spent    
- Meet regularly to share progress    
- Test and review work    
- Use Github issues to record issues    

</td>
</tr>
<tr valign="top">
<td align="center" markdown="span">
End of Iteration
</td>
<td align="left" markdown="span">

- Stabilize, test, and review finished work    
- Demo work products    
- Hold a short retrospective    
- Write the key results in "Summary" of iteration plan    

</td>
</tr>
</table>
