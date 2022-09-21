---
title: UML Sequence Diagram Exercise
---
Submit your diagram embedded in a Google Doc to the assignment on Google Classroom.

1. Draw a Sequence Diagram of what happens when `Main.run` is invoked.
   - Use the "found" notation to show `run` is invoked. 
   - "found" is drawn as an arrow from the left side that points to the activation box for "run", with the word `run` on the arrow.

```python
class Money:
    def __init__(self, value: float, currency: str):
        self.value = value
        self.currency = currency

    def __add__(self, other: Money):
        if other.currency != self.currency:
            raise ValueError("Can't add different currencies")
        sum_value = self.value + other.value
        return Money(sum_value, self.currency)

class Main:
    def run(self):
        m1 = Money(50, "RMB")
        m2 = Money(20, "RMB")
        sum = m1 + m2
```


## References

- UML Sequence Diagram Design Elements <https://www.conceptdraw.com/examples/found-message-sequence-diagram>
- *UML Distilled* by Martin Fowler. Has a short chapter on Sequence Diagrams.
- Diagram tool <https://sequencediagram.org/>