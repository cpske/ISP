## Pizzashop Refactors

Exercise from Week 10, submitted on Github Classroom
Starter code at https://github.com/ISP2022/pizzashop

In the students' final code should have:

| Points | Description                                 |
|--------|---------------------------------------------|
| **4**  | **Pizza**                                   |
|    1   | Rename `getPrice`  -> `get_price`    |
|    1   | Rename `addTopping` -> `add_topping` |
|    1   | Replace "if..elif" `get_price` with `self.size.value`
|    1   | No LARGE, MEDIUM, SMALL in Pizza
|    -   | `__str__` describes pizza
|  **3** | **Pizzashop**
|    1   | Type hint: `def order_pizza(pizza: Pizza)`
|    1   | Remove `describe`, move to `Pizza.__str__` |
|    1   | Eliminate temp: in `order_pizza` no `description = ...` 
 `self.size.value`
|  **3** | **PizzaSize**
|    2   | Create `PizzaSize` enum with value of each size
|    1   | Add `jumbo` size to `PizzaSize`.
|        | **Errors**
|   -1   | Logic or Syntax errors |

## Common Errors


```python
# -1 did not remove unused constants
LARGE = 'large'
MEDIUM = 'medium'
SMALL = 'small'

class Pizza:

    def get_price(self):
        try:
            return self.size.price + 20*len(self.toppings)
        except:
            # -1 LOGIC ERROR
            # if value of size is *really* unknown, then
            # this will throw exception, too:
            raise ValueError("unknown pizza size " + self.size.name)
```

