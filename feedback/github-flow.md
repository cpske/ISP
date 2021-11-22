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
|-------------------------------------|:--------:|
| Pull master to your local machine   |     0     |
| Create a local branch for your work |     1    |
| Push your branch to Github          |     3     |
| Implement and **test** your feature |     2     |
| Open a Pull Request                 |     4     |
| Open an issue with tag "Pull Request" |    X   |
| Implement team suggestions and rerun tests  |   6   |
| Wait for the team to comment on your work |   5   |
| Merge your branch into master (on your machine)    |   10     |
| Merge master into your branch, then rebase master |   X  |
| Push your copy of master to Github  |     11   |
| Pull master to your local machine   |     9    |
| Push your branch to Github          |    7      |
| Team agrees the code should be merged | 8 |
| Close the Pull Request or Issue     |    `12    |

