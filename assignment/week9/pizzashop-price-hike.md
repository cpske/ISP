## Accommodating Change in Pizza Pricing

Do this **after** you finish and test all the required refactorings
of pizza and pizzashop.


> "Good software can evolve with changing requirements."


## Price Changes

The Pizza Shop wants to increase the price of large pizza to 300 Baht, 
reduce the "jumbo" price to stimulate sales,
and change the topping prices.

The new prices are:

| Pizza Size  | Base Price | Price Per Topping |
|-------------|------------|-------------------|
| small       | 150        | 20 Bt.            |
| medium      | 200        | 25 Bt.            |
| large       | 300        | 30 Bt.            |
| jumbo       | 420        | 30 Bt.            |

The new topping prices depend on size, so the code for computing price needs to change.

How would you implement this change?

Here we describe 2 approaches:

- add topping prices to the PizzaSize enum

- let the enum compute pizza prices itself

## Enum with Dict of Attributes

The `value` of an Enum member can be *anything*, not just a number. 
We can define a dictionary for the base price and topping price:

```python
class PizzaSize(Enum):
    small =  {'base_price': 120, 'topping': 20}
    medium = {'base_price': 200, 'topping': 25}
    large =  {'base_price': 300, 'topping': 30}
    jumbo =  {'base_price': 400, 'topping': 30}

    @property
    def price(self):
        return self.value['base_price']
    
    @property
    def topping_price(self):
        return self.value['topping']
```
Now each PizzaSize knows it's own price.  The properties help make the code more readable and preserves *encapsulation* of data in PizzaSize.

1. Implement this change in PizzaSize.

2. Modify `Pizza.get_price` to use the `topping_price` property.

3. Update the `asserts` in `main.py` with the new prices.

Test it.

Commit this change with a descriptive commit message.


## *Separate the part that varies from the part that stays the same*

This is a design principle from the original Design Patterns book (the "*Gang of 4 Book*").

Since pizza prices vary, we may want to completely separate price computation from the Pizza class.  When the pricing rules change, we need to update the prices in `PizzaSize`, so we may as well make PizzaSize responsible for computing the Pizza price.  Then we need to change only one class when pricing changes.

The `Pizza` class *delegates* the computation to PizzaSize:

```python
# in Pizza

def get_price(self):
    # DELEGATE price computation to PizzaSize
    return self.size.get_price(self) 
```

```python
# in PizzaSize
class PizzaSize(Enum):

    def get_price(self, pizza):
        # TODO
```

**Test** this change.

**Commit** and **push** your work with a descriptive commit message.
