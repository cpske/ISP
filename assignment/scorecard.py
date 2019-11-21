"""
Example code containing common errors that can 
be detected by static type checking.  
Please don't fix the code by inspection -- use
it to see what a static type checker can do.

When you add typing hints to this code, 
then your IDE *should* detect the errors.

Useful tools:
- install mypy for static code analysis (works 
  with almost any IDE)
- for VS Code users, recommend installing the Pyright extension,
  a Microsoft project. It performs very good type checking 
  and type inference, and enables better command-completion
  in VS Code.

For more info on type hints, see Mai's problem
in the ISP19 Github repo for student-created exercises.
"""

class Scorecard:
    """Accumulate scores and compute their average."""

    def __init__(self):
        self.scores = []
    
    def add_score(self, score):
        self.scores.append(score)

    def average(self):
        """return average of all scores"""
        return sum(self.scores)/len(self.scores)


if __name__ == "__main__":
    scores = Scorecard()
    n = input("input a score: ")
    scores.add_score(n)
    n = input("input another score: ")
    scores.add_score(n)

    print("The average is "+scores.average())
