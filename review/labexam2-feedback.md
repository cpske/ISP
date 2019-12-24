# Lab Exam 2 Grading and Comments

Full score is 100, but its possible to get more than 100 points:

|Problem                 | Points |
|:-----------------------|-------:|
|1. Preserve Object      | 20 |
|2. Define a LineItem    | 20 |
|3. Divide Long Method   | 40 |
|4. Polymorphic Customer | 20 |
|5. Unit Testing of Order| 20 |
|Total                  | 120 |

7 students earned score 100 or above.  Excellent work!


## 1. Preserve Whole Object (20 pt)

Pass the whole `product` object to `order.add_item`.    
First, modify `make_sale()` in `main.py` to invoke:
```python
order.add_item(product, quantity)
```

and in `Order`:
```python
def __init__(self,customer: Customer):
    self.item_quantity: List[int] = []
    self.products: List[Product] = []

def add_item(self, product, quantity: int) -> None:
    """Add an item to the order, or update an existing item."""
    if product in self.products:
        k = self.products.index(product)
        self.item_quantity[k] += quantity
    else:
        self.products.append(product)
        self.item_quantity.append(quantity)
```

#### Common Error 1. Adding a `quantity` attribute to Product!

**Wrong** because:

1. The exam stated **not** to modify Product.
2. Conceptually its a bad idea: "product" represents a kind of item for sale, not a specific purchase of the item.
3. It can cause errors. The same Product instance is returned by `ProductCatalog` each time `find_product(id)` is called with same `id`.  Suppose you have 2 Order objects that include the same product.  They would modify each other's quantity!

#### Common Error 2. Logic Errors in Checking for Product in Order

Bad "if - else" logic, which is described in Problem 2.

## 2. Replace Parallel Arrays with Array of Objects (20 pt)

Define a `LineItem` like this:
```python
class LineItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
```
If you want to make it *easy* to access product attributes then add read-only properties for them:
```python
    # this is not required
    @property
    def id(self):
        return self.product.id

    @property
    def name(self):
        return self.product.name
```
and use a list of `LineItem` objects in `Order` instead of parallel arrays:
```pyton
class Order:
    def __init__(self, customer: Customer):
        self.customer = customer
        # items in the order
        self.line_items: List[LineItem] = []
```


#### Common Error 1. Not Preserving Whole Object

After Problem 1 recommended to *Preserve Whole Object* some people did not do that in LineItem.  Wow!
```python
class LineItem:
    # WRONG: should pass whole product object as parameter to __init__
    def __init__(self, product_id, name, price, quantity):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
```

A few students wrote `class LineItem():` when defining a class. Parens are **not required**.
Please stop writing them.


#### Common Error 2. Logic Errors in `order.add_item()`

After introducing LineItem, how do you check if a product is already part of a sale?  
These codes are incorrect:

```python
    def addItem(self, product, quantity):

       for line_item in self.line_items:
           if product.id == line_item.product.id:
               k = self.line_items.index(line_item)
               self.line_items[k].quantity +=  quantity
           else:
               # Not found, so add a new line item
               self.line_items.append( LineItem(product, quantity) )
```
this "else" clause makes *no sense* but Python permits it:

```python
       for line_item in self.line_items:
           if product.id == line_items.product.id:
               k = self.line_items.index(line_item)
               self.line_items[k].quantity +=  quantity
       else:
           # Not found, so add a new line item
           self.line_items.append( LineItem(product, quantity) )
```

But the logic is still incorrect. One possible correct solution is:
```python
       matched_item = None
       for item in self.line_items:
           if product == item.product:
               matched_item = item
               break   # found a match, so stop looking!
       # is this a new product or existing product?
       if matched_item:
           matched_item.quantity += quantity
       else:
           self.line_items.append( LineItem(product, quantity) )
```

#### Wrong Use of Plurality in Names

A collection name should be **plural**. A variable from a single item should be **singular**.

```python
self.line_item: List[LineItem] = []
```
Should be:
```python
self.line_items: List[LineItem] = []
```

#### Redundant Prefixes on Names

Inside the `LineItem` class, there is no reason to prefix names with `item_` like this:
```python
class LineItem:
    def __init__(self, product, quantity):
        self.item_product = product
        self.item_quantity = quantity
        etc.
```

It makes the code harder to read, as shown here:
```python
    item = self.lineitems[k]
    print(item.item_product.name, item.item_quantity, item.item_product.price)
```
The `item_` prefix is redundant.  See how much easier to read:
```python
    item = self.lineitems[k]
    print(item.product.name, item.quantity, item.product.price)
```

## 3. Divide Long Method (40 pt)

Divide `print_sale` into 4 methods.  This problem has 4 parts. Each part is worth 10 points.

| Method          | Description                 |
|:----------------|:----------------------------|
| `get_total()`   | Compute and return sale total. **Does not print anything**. |
| `get_discount()` | Compute and return discount. **Does not print anything**. |
| `get_loyalty_pts()` | Compute and return member points. **Does not print anything**. |
| `print_sale()`  | Invokes the other 3 methods, and is the only method to print the sale. |

Common Errors:

* Using an attribute to compute and save order total, discount, or member points instead of a local variable.
* `get_total`, `get_discount`, or `get_loyalty_pts` save the value as attribute but don't return it.
* `get_total` prints the line items.
* replacing `print_sale` with another method, or having the main class call several methods to do what `print_sale` did.  *Refactoring is not rewriting*.

## 4. Replace Conditional Logic with Polymorphism (20 pt)

You should define 3 "customer" classes, with one as base class. 
Each class has its own `get_discount(order)` and `get_loyalty_pts(order)` methods.

For example:
```python
class Customer:
    """Base class is for non-members"""

    def get_discount(self, order):
        return 0.0

class Member(Customer):
    """Pricing rules for ordinary members"""

    def get_discount(self, order):
        total = order.get_total()
        return 0.03*total

class GoldMember(Customer):
    """Pricing rules for gold members"""

    def get_discount(self, order):
        total = order.get_total()
        return 0.05*total + 0.05*max(0.0, total-1000)
```

Then, in the `Order` class, the `get_discount` method simply invokes the
customer's own method:
```python
class Order:

    def get_discount(self):
        """Customer needs a reference to the order to compute the discount"""
        return self.customer.get_discount(self)
```

This is an example of the *Strategy Design Pattern*.
Its sometimes called the *State Pattern*, which has the same structure,
but I thick *Strategy* is more correct in this application.

How to create customers in `make_customer`?
Some students wrote a clever solution like this:
```python
    def make_customer(cust_type: str):
        classes = {'m': Member, 'g': GoldMember}
        return (classes[cust_type]() if cust_type in classes 
                else Customer()) 
```
There is no parameter to the class constructors since each customer class already knows its customer type.

## 5. Unit Tests (20 pt)

Most students who got this far wrote good tests.
