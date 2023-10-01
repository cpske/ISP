"""
This code contains common errors that can 
be detected by static type checking.
Please do not fix this code by inspection.

Instead, add type hints and watch your IDE tell
you what the errors are.

Add these hints ONE AT A TIME and SAVE the file
after adding each type hint.
Look for errors detected in the main block.

1) add type to parameter:      add_score(self, score: float)
2) add type to return value:   average(self) -> float
3) add type to list attribute: self.scores: List[float] = []

**NOTE**: `List` is a type from the typing package.
`List` is not the same as Python `list` type and not the same
as collections.abc.List.  When you want to add a type hint for
a list you should use typing.List, not those other "lists".
"""
from typing import List


class Scorecard:
    """Accumulate scores and compute their average."""

    def __init__(self):
        """Iniiialize a new Scorecard."""
        self.scores = []
    
    def add_score(self, score):
        """Add a score to the Scorecard."""
        self.scores.append(score)

    def average(self):
        """Return the average of all scores, 0 if no scores."""
        return sum(self.scores)/max(1,len(self.scores))

    def max_score(self):
        """Return the maximum of the scores."""
        return max(self.scores)


if __name__ == "__main__":
    print("Input 2 scores.  The average will be printed.")
    scores = Scorecard()
    n = input("input 1st score: ")
    scores.add_score(n)
    n = input("input 2nd score: ")
    scores.add_score(n)

    print("The average is " + scores.average())

    print("Max score is " + scores.max_score())
