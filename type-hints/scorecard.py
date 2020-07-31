"""
Example code containing common errors that can 
be detected by static type checking.  
Please don't fix this code by inspection -- use
it to see what a static type checker can do.

When you add typing hints to this code, 
then your IDE *should* detect the errors.
This works in PyDev (Eclipse), PyCharm (based on IntelliJ IDEA),
and VS Code with IntelliCode.

Useful tools:
- install mypy for static code analysis (mypy works with almost any IDE)
- for VS Code users, recommend installing the Pyright extension,
  a Microsoft project. It performs very good type checking 
  and type inference, and enables better command-completion
  in VS Code.

For more info on type hints, see Mai's problem in the ISP Github repo.
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
    print("Input 2 scores.  The average will be printed.")
    scores = Scorecard()
    n = input("input 1st score: ")
    scores.add_score(n)
    n = input("input 2nd score: ")
    scores.add_score(n)

    print("The average is "+scores.average())
