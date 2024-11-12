---
title: UML Sequence Diagram Exercise
---
Draw a UML Sequence Diagram for this code, on paper.

Draw **activation boxes** for the time a method is activated, and only that time.

1. Draw a Sequence Diagram of what happens when `Main.run()` is invoked.
   - Use the "found" notation to show `run` being invoked. 
   - "found" is drawn as an arrow from the left side that points to the activation box for "run", with the word `run` on the arrow.
   - show the operation performed by `add_vat` in a round box (oval) over the activation box

```python
class Money:
    """Money with a value and a currency."""

    def __init__(self, value: float, currency: str):
        self.value = value
        self.currency = currency

    def __add__(self, other: Money) -> Money:
        """Add two money objects if they have the same currency.
        :return: a new Money object that is the sum of this Money and other.
        """
        if other.currency != self.currency:
            raise ValueError("Can't add different currencies")
        sum = Money(self.value + other.value, self.currency)
        return sum

class Main:
    def run(self):
        m1 = Money(50, "RMB")
        m2 = Money(200, "RMB")
        sum = m1 + m2
        self.add_vat(sum)
        return sum

    def add_vat(self, money: Money) -> None:
        """Add 7% VAT onto value, performed in place."""
        money.set_value(1.07 * money.value)
```

2. In `Money.__add__` what if the code was as below.  Would it change your sequence diagram?
```python
    def __add__(self, other: Money) -> Money:
        if other.currency != self.currency:
            raise ValueError("Can't add different currencies")
        new_value = self.value + other.value
        return Money(new_value, self.currency)
```

## References

- UML Sequence Diagram Design Elements <https://www.conceptdraw.com/examples/found-message-sequence-diagram>
- *UML Distilled* by Martin Fowler. Has a short chapter on Sequence Diagrams.
- Sequence Diagram Tool <https://sequencediagram.org/>
  Text-based input, but gives you a lot of control over diagram.
