Using Github Flow, in what order would these actions be done?
Assign only one sequence number to each line in the table,
but one action (Push your branch to Github) appear twice, 
so you can assign a different sequence number to each occurence.  

Assume that you do merging on your local machine.
It is sometimes possible to merge branches on Github,
but it's safer to merge on your local machine (why?)
and then push the results to Github.

In a real project, you would probably want to push your work many times.
For this exercise, indicate the 2 times (in the sequence) that are
*most critical* to the workflow.

Two actions don't occur in the flow. Write "N/A" for those actions.


| Action                              | Sequence |
|-------------------------------------|----------|
| Create a local branch for your work |     1    |
| Push your branch to Github          |          |
| Implement and **test** your feature |          |
| Open a Pull Request                 |          |
| Open an issue with tag "Pull Request" |        |
| Implement team suggestions and rerun tests  |          |
| Wait for the team to comment on your work |      |
| Merge your branch into master       |          |
| Merge master into your branch, then rebase master |    |
| Push your copy of master to Github  |          |
| Pull master to your local machine   |          |
| Push your branch to Github          |          |
| Close the Pull Request or Issue     |          |

