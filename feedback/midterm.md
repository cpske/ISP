---
title: Feedback on Midterm
---

## Sequence Diagram

### Mistake: Code that Cannot be Deduced from the Sequence Diagram

```python
class Player:
    def __init__(self):
        self.alive = True       # NOT KNOWN

    def is_alive(self)->bool:
        return self.alive       # NOT KNOWN

class Game:
    
    def __init__(self):         # CONSTRUCTOR NOT KNOWN
        self.players = []       # NOT KNOWN. MAY NOT BE A LIST!!        

    def remove(self, player: Player):
        self.players.remove(player)  # NOT KNOWN WHAT THE METHOD DOES

```

### Deduction: Points Deducted for Errors in Code

Points deducted for writing code that is:

- syntax or semantic error
- totally inconsistent with the Sequence Diagram

```python
class Player:
    # This does not make sense
    def __init__(self, player: Player):
        self.player = player


class Game:
    # This does not make sense
    def __init__(self, player: Player):
        self.player = player
```

`Game` is **not** a subclass of `Player`:
```python
class Game(Player):

```

### Self-less Methods

No deduction for 1-2, but deduction for a method that uses "self".

```python

class Player:

    def take_turn():
        pass

    def is_alive() -> bool:
        pass

class Game:

    def remove(player: Player):
        pass
```
