---
title: Feedback on Tax Calculator Refactoring
---

## 1. Replace nested conditional with guard condition.

```python
def __eq__(self, other):
    if not isinstance(other, Person):       # The "guard"
        return False
```

**No Credit** for this because it doesn't return *anything* if
the test is False:

```python
def __eq__(self, other):
    if isinstance(other, Person):
        return self.id == other.id and self.last_name == other.last_name
```

**No Credit** for this (adds unnecessary "elif" and also fails to return a boolean in one case):

```python
def __eq__(self, other):
    if not isinstance(other, Person):
        return False
    elif self.id == other.id and self.last_name == other.last_name:
        return True
```

**No Credit** for this becuase it fails to achieve the goal of "remove nested conditional":

```python
def __eq__(self, other):
    if isinstance(other, Person):
        if self.id == other.id and self.last_name == other.last_name:
            return True
    return False
```

**1 Point** for this. After a "guard clause" then you should not need `else`.

```python
def __eq__(self, other):
    if isinstance(other, Person):
        return self.id == other.id and self.last_name == other.last_name:
    else:
        return False
```


## 2. Remove unnecessary "if"

Either of these are OK but the first solution is better (a true "guard")

```python
def __eq__(self, other):
    if not isinstance(other, Person):
        return False
    return self.id == other.id and self.last_name == other.last_name
```

```python
def __eq__(self, other):
    if isinstance(other, Person):
        return self.id == other.id and self.last_name == other.last_name
    return False
```
## 3. Preserve Whole Object

Change TaxCalculator parameter to be a `Person` **and** save the Person reference in TaxCalculator. 

Requires changes in `main`, `TaxCalculatorTest.setUp`, and `TaxCalculator` `__init__` and `compute_and_print_tax`.

```python
# main.py

if __name__ == '__main__':
    taxpayer = Person("1409900123456", "Fatalai", "Jon")
    tax_calc = TaxCalculator(taxpayer)
```

```python
# tax_calculator.py

class TaxCalculator:
    def __init__(self, taxpayer: Person):
        self.taxpayer = taxpayer
```

**6 Points** for this:

```python
class TaxCalculator:
    def __init__(self, taxpayer: Person):
        self.tax_id = taxpayer.tax_id
        self.first_name = taxpayer.first_name
        self.last_name = taxpayer.last_name
```

## 4. Extract Method for Computation Done 3 Times

In the original code there are 3 blocks similar to this:

```python
    # total ordinary income and tax withheld on ordinary income
    ordinary_income = 0
    ordinary_tax_withheld = 0
    for k in range(len(self.incomes)):
        (income_type, _, amount, tax) = self.incomes[k]
        if income_type.lower() == "wages":
            ordinary_income += amount
            ordinary_tax_withheld += tax

    # similar code for dividend

    # similar code for interest
```

**First Solution**: One method to compute same thing as the above. This is not recommended because in the code you often want only one of the two values.

```python
    def sum_income_by_type(self, income_category: str):
        """Sum income items for a given income category."""
        total_income = 0
        total_withheld = 0
        for income in self.incomes:
            (category, _, amount, withheld) = income
            if category.lower() == income_category:
               total_income += amount
               total_withheld += withheld
        return total_income, total_withheld
```

then in `compute_and_print_tax`:
```python
    ordinary_income, ordinary_tax_withheld = self.sum_income_by_type("wages")
    interest_income, interest_tax_withheld = self.sum_income_by_type("interest")
    dividend_income, dividend_tax_withheld = self.sum_income_by_type("interest")
```

**Second Solution**: extract one method to sum income and one to sum tax withheld by income type. This solution makes the code much cleaner and simpler.

Here's what it looks like after refactoring #10 (use an Enum for income types):
```python
    def sum_income_by_type(self, income_type: IncomeType) -> float:
        """The sum of all income for a given income_type."""
        return sum(income.amount
                   for income in self.incomes 
                    if income.income_type = income_type)

    def sum_tax_withheld_by_type(self, income_type: IncomeType) -> float:
        """The sum of all tax withheld for a given income_type."""
        return sum(income.tax_withheld
                   for income in self.incomes 
                    if income.income_type = income_type)
```

**5 Points** for writing separate methods for each income category, as below. These methods *still* contain duplicate code, it is just moved someplace else.

```python
    # in compute_and_print_tax
    ordinary_income, ordinary_tax_withheld = self.sum_ordinary_income()
    interest_income, interest_tax_withheld = self.sum_interest()
    dividend_income, dividend_tax_withheld = self.sum_dividend()
```

**5 Points** for passing the sum as a parameter. This is an anti-refactoring (code smell: modifying a parameter) and serves no purpose.

```python
    ordinary_income = 0
    ordinary_tax_withheld = 0
    ordinary_income, ordinary_tax_withheld = self.sum_income_by_type(
                      "wages", ordinary_income, ordinary_tax_withheld)
```

**5 Points** for code like this, because it **still** contains redundant code, just rearranged.  Plus, if we add any new income type we have to modify the method.

```python
    def get_incomes(self):
        ordinary_income = 0
        interest_income = 0
        dividend_income = 0
        for income in self.incomes:
           (itype, _, amount, _) = income
           if itype.lower() == "wages":
              ordinary_income += amount
           elif itype.lower() == "interest":
              interest_income += amount
           elif itype.lower() == "dividend":
              dividend_income += amount
        return ordinary_income, interest_income, dividend_income
```

**No Credit** for the following code, because:

1. still contains redundant calculation, just rearranged.
2. relies on side effects (saving to an attribute instead of returning a value)
3. assumes the method is called only once (otherwise result is wrong)
4. large, unnecessary change in organization of the code by promoting local variables to attributes. Refactoring should be small changes.

```python
    def total_incomes(self):
        for income in self.incomes:
           (itype, _, amount, _) = income
           if itype.lower() == "wages":
              self.ordinary_income += amount
           elif itype.lower() == "interest":
              self.interest_income += amount
           elif itype.lower() == "dividend":
              self.dividend_income += amount
         # returns nothing
```

## 5. Extract Method for Duplicate Computation

The long formula for ordinary income tax is written twice in `compute_and_print_tax`:

```python
    deduction = 60000
    if ordinary_income-deduction <= 150000:
        ordinary_income_tax = 0
    elif ordinary_income-deduction <= 300000:
        ordinary_income_tax = 0.05*(ordinary_income-deduction - 150000)
    elif ordinary_income-deduction <= 500000:
        ordinary_income_tax =   7500 + 0.10*(ordinary_income-deduction - 300000)
    elif ordinary_income-deduction <= 750000:
        ordinary_income_tax =  27500 + 0.15*(ordinary_income-deduction - 500000)
    elif ordinary_income-deduction <= 1000000:
        ordinary_income_tax =  65000 + 0.20*(ordinary_income-deduction - 750000)
    elif ordinary_income-deduction <= 2000000:
        ordinary_income_tax = 115000 + 0.25*(ordinary_income-deduction - 1000000)
    elif ordinary_income-deduction <= 4000000:
        ordinary_income_tax = 365000 + 0.30*(ordinary_income-deduction - 2000000)
    else: # net income over 4,000,000
        ordinary_income_tax = 965000 + 0.35*(ordinary_income-deduction - 4000000)
```

This code is screaming to be a separate method and eliminate the redundant `ordinary_income-deduction`.

```python
def get_income_tax(self, net_income):
    """Compute the ordinary income tax on net_income.
    :param net_income: net ordinary income after deductions
    """
    if net_income <= 150000:
        tax = 0
    elif net_income <= 300000:
        tax = 0.05*(net_income - 150000)
    elif net_income <= 500000:
        tax =   7500 + 0.10*(net_income - 300000)
    elif net_income <= 750000:
        tax =  27500 + 0.15*(net_income - 500000)
    elif net_income <= 1000000:
        tax =  65000 + 0.20*(net_income - 750000)
    elif net_income <= 2000000:
        tax = 115000 + 0.25*(net_income - 1000000)
    elif net_income <= 4000000:
        tax = 365000 + 0.30*(net_income - 2000000)
    else: # net income over 4,000,000
        tax = 965000 + 0.35*(ordinary_income-deduction - 4000000)
    return tax
```

OK to replace the `if ... elif` with a loop over a list of tax brackets and tax rates **provided** they are local variables or class constants (not global constants). However, I think that makes the code *harder to understand*.

**5 Points** for code like this (did not remove redundant substraction). The goal of refactoring is it improve the code.  This is only a partial improvement.
```python
def get_income_tax(self, income):
    """Compute the ordinary income tax on income."""
    deduction = 60000
    if income-deduction <= 150000:
        tax = 0
    elif income-deduction <= 300000:
        tax = 0.05*(income-deduction - 150000)
    elif income-deduction <= 500000:
        tax =   7500 + 0.10*(income-deduction - 300000)
    ...etc...
    return tax
```

## 6. Inline Temp and Replace "elif" with "if"

Eliminate assignment to the local variable `tax` in the code above. Insted, simply return the tax. When you do that, you do not need "elif" either:
```python
def get_income_tax(self, net_income) -> float:
    """Compute the ordinary income tax on net_income.

    :param net_income: net ordinary income after deductions
    :return: the ordinary tax on net income
    """
    if net_income <= 150000:
        return 0
    if net_income <= 300000:
        return 0.05*(net_income - 150000)
    if net_income <= 500000:
        return   7500 + 0.10*(net_income - 300000)
    if net_income <= 750000:
        return  27500 + 0.15*(net_income - 500000)
    if net_income <= 1000000:
        return  65000 + 0.20*(net_income - 750000)
    if net_income <= 2000000:
        return 115000 + 0.25*(net_income - 1000000)
    if net_income <= 4000000:
        return 365000 + 0.30*(net_income - 2000000)
    # otherwise, net income over 4,000,000
    return 965000 + 0.35*(ordinary_income-deduction - 4000000)
```

**8 Point** for code that replaces assignment to temp with `return` but did not replace `elif` with `if`.

## 7. Divide Long Method Doing Two Things

Create separate methods for tax computation and printing a tax summary.
- `compute_tax` - compute and return the tax owed or amount to refund
- `print_tax`  - print the tax due

Notice that in `compute_tax` you do not need the tax withheld at all.
If you wrote separate methods for Refactoring #5 then your code is much simpler.

Example solution is listed after the last refactoring.

## 8. Extract Variable for a Sum Computed Several Times

This is the sum of different income types is computed several times.
In the final solution, you may not have this sum anymore.
In that case, you get credit if your refactoring produced a *clean* solution
where the sum is not needed.



```python
Separate tax computation 
## Please Stop Writing Loops Like This

Iterate over elements in a list:

```python
# Don't do this
for k in range(len(self.incomes)):
    income = self.incomes[k]
    ...
```

This looks like a C programmer writing C code in Python. It's not fluent use of Python.

Simpler and more flexible (works with *any* Collection or *any* Iterable):

```python
for income in self.incomes:
   ...
```

And, of course, consider if a *list comprehension* can replace the for loop.
