> This is an example Project Plan for KU Polls. 
> You may use it, but you should carefully read and customize it.

# KU Polls Project Plan 

Author:  Fatalai Jon    
Revised: 18 Aug 2024

## Statement of Work

The project will produce a web application for conducting polls and surveys that satisfies 
the requirements as specified in [[Requirements]].  The application will be written in Python and runnable
on Windows, Linux, or MacOS hosts containing the required software.

## Development Process

Development will use an iterative process with 4 iterations. Each iteration has a length of one week starting on Monday and ending on Sunday.

## Project Documents

Project documents and technical documents are stored in the project wiki on Github.

Project documents include:
- [[Project Plan]]
- [[Requirements]]
- [[Vision and Scope]] statement
- Iteration Plan for each iteration
- Summary of Retrospectives
- Software design documents

Tasks and other work for each iteration are recorded in a Github Project attached to the repository. The Github Project contains a Task Board for each iteration. 

Github issue tracker is used to record defects and other issues. 

## Workflow

Each iteration starts on Monday and ends on Sunday. 

- At the start of each iteration, the Vision, Project Plan, and Requirements are reviewed and updated. 
- A goal for the iteration and at least 1 milestone are defined and written in the Iteration Plan.
- Major work for the iteration is defined and recorded in the Iteration Plan.
- The application design is reviewed and revised (if needed) for new features to be added. 
- The Iteration Plan, including the goal, milestone(s), and major work, is added to the wiki.
- Tasks are defined and written in the Project Backlog on Github.
- A Github *Task Board* for this iteration is created to track work in this iteration.
- *Github Flow* is used to manage code. 
  - For each iteration a new branch is created from `main` and work is committed to that branch.
  - At the end of the iteration, after the work is tested a Pull Request is opened to initiate a final review.  
  - When the work is satisfactory, the branch is merge into `main` and the Pull Request is closed. *Note: Github can do both of these in one click.*
- Defects and other issues are recorded in a Github *Issue Tracker*.
  - *Note: Github can automatically add Tasks to the issue tracker, too.*

## Technology and Tools

- The application is written in Java using the Play web framework.
- Bitbucket for source code management, issue tracking, and automated testing.
- Github Wiki for project documents.
- Github Project for backlog, task planning, and iteration task boards.
- Eclipse IDE for coding and running tests.
- Line mobile app for chatting, ordering coffee and food, playing games.


## Timeline

|   Week    | Major Work and Features |
|:---------:|-------------------------|
|     1     | Learn fundamentals of creating a web application using Django. |
|           | App displays a list of recent poll questions. |
|           | Detail page for each poll question displays the question and a list of choices.|
|           | Visitor can choose a poll question and submit a "vote" on it. His/her selection is counted toward the total.|
|           | The poll questions, responses, and vote count are saved in a database.|
|           | A UML class diagram of the domain model is added to project wiki. |
|     2     | Apply page styling using CSS. |
|           | Separate sensitive configuration data from source code.|
|           | Each poll may have an end date that is the final date for submitting a choice. |
|           | Improved Navigation. Can navigate between pages without voting and without using the browser "back" button. |
|           | Unit tests and code coverage are run automatically when new code is pushed to Github. |
|     3     | Add authentication in order to vote. A visitor must authenticate ("log in") to submit a choice. |
|           | An authenticated user can view and change his/her previous "vote". |
|           | Unauthenticated visitors can view polls and results, but cannot vote. |
|     4     | Create data fixtures to initialize users and polls data.|
|           | Ensure application is runnable on different operating systems. |
|           | Create and test installation instructions. |
|           | Review, document, and cleanup all code. |

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
|     3     | Revised domain class model that includes User and Votes owned by a User is recorded on the wiki. |
|           | Username-password authentication works. |
|           | Users are required to authenticate in order to vote. |
|     4     | Application runs on platforms meeting the software requrements. |
|           | Installation includes data to easily create initial user credentials and poll questions. |

