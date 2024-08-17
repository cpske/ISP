> This is an example Project Plan for KU Polls. 
> You may use it, but you should carefully read and customize it.

# KU Polls Project Plan 

Author:  James Brucker    
Revised: 17 Aug 2024

## Development Process

The application will be implemented using an iterative process with 4 iterations. Each iteration has a length of one week starting on Monday and ending on Sunday.

## Project Documents

Project documents and technical documents will be stored in the project wiki on Github.

Project documents include:
- Project Plan
- Iteration Plan for each iteration
- Summary of Retrospectives

Tasks and other work for each iteration are recorded in a Github Project attached to the repository. The Github Project contains a Task Board for each iteration. 

Github issue tracker is used to record defects and other issues. 

## Workflow

Each iteration starts on Monday and ends on Sunday. 

- At the start of each iteration, the Vision, Project Plan, and Requirements are reviewed and updated. 
- A goal for the iteration and at least 1 milestone are defined and written in the Iteration Plan.
- Major work for the iteration is defined and recorded in the Iteration Plan.
- The application design is reviewed and revised (if needed) for new features to be added. 
- The Iteration Plan, including the goal, milestone(s), and major work, is added to the wiki.
- A Github *task board* is created to record and track work in this iteration.
- *Github Flow* is used to manage code. 
  - For each iteration a new branch is created from `main` and work is committed to that branch.
  - At the end of the iteration, after the work is tested a Pull Request is opened to initiate a final review.  
  - When the work is satisfactory, the branch is merge into `main` and the Pull Request is closed. *Note: Github can do both of these in one click.*
- Defects, tasks, and other issues are recorded in a Github *Issue Tracker*.
  - *Note: Github can automatically add Tasks to the issue tracker. You don't need to enter the tasks twice.*

## Technology and Tools

- The application is written in Java using the Play web framework.
- Github for source code management, issue tracking, and automated testing.
- Github Wiki for project documents.
- Github Project for backlog, task planning, and iteration task boards.
- Eclipse IDE for coding and running tests.


## Timeline

|   Week    | Major Work and Features |
|:---------:|-------------------------|
|     1     | Learn fundamentals of creating a web app using Django. |
|           | App displays a list of recent poll questions. |
|           | Detail page for each poll question displays the question and a list of choices.|
|           | Visitor can choose a poll question and submit a "vote" on it. His/her selection is counted toward the total.|
|           | The poll questions, responses, and vote count are saved in a database.|
|           | A UML class diagram of the domain model is added to project wiki. |
|     2     | Learn and apply page styling with CSS. |
|           | Separate sensitive configuration data from source code.|
|           | Each poll has an end date that is the final date for submitting a choice. |
|           | Improved Navigation. Can navigate between pages without voting and without using the browser "back" button. |
|           | Unit tests and code coverage are run automatically when new code is pushed to Githbu. |
|     3     | Add authentication in order to vote. A visitor must authenticate ("log in") to submit a choice. |
|           | An authenticated user can view and change his/her previous "vote". |
|     4     | Create data fixtures to initialize users and polls data.|
|           | Enable application to run on different operating systems; provide installation instructions. |
|           | Review and cleanup all code.|

### Milestones

| Iteration | Milestone |
|:---------:|-----------|
|     1     | Application displays a list of active poll questions and detail pages with the choices available for each question. |
|           | A visitor can select and submit a choice ("vote") for a poll question. |
|           | Application correctly shows total "votes" for each choice in each poll. The results are persistent across app restarts. |
|           | Domain model established and recorded in wiki as a UML diagram. |
|     2     | Navigation links allow access to any page without using browser "back" button. |
|           | A visitor can view poll results without voting. |
|           | Sensitive configuration parameters and secret can be modified without changing the source code. |
|     3     | Revised domain class model that includes User and Votes owned by a User is on the wiki. |
|           | Username-password authentication works. |
|           | Users are required to authenticate in order to vote. |
|     4     | Application runs on platforms meeting the software requrements. |
|           | Installation includes data to easily create initial user credentials and poll questions. |

