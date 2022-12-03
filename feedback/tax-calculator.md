---
title: Feedback on Tax Calculator Refactoring
---

Refactoring #1 and #2 are 5 points each. The others are 10 points each.

## 1. Replace nested conditional with guard condition

**5 Points** for correct code similar to this:
```python
def __eq__(self, other):
    if not isinstance(other, Person):    # The "guard"
        return False
    return (self.id, self.last_name) == (other.id, other.last_name)
```

**No Credit** for this because it does not return *anything* if the test is False:

```python
def __eq__(self, other):
    if isinstance(other, Person):
        return self.id == other.id and self.last_name == other.last_name
```

**No Credit** for this for same reason as above, plus the `elif` is not necessary (should be "if").

```python
def __eq__(self, other):
    if not isinstance(other, Person):
        return False
    elif self.id == other.id and self.last_name == other.last_name:
        return True
```

**No Credit** for this becuase it fails to achieve the goal of "remove nested conditional". There is still a nested "if".

```python
def __eq__(self, other):
    if isinstance(other, Person):
        if self.id == other.id and self.last_name == other.last_name:
            return True
    return False
```

**1 Point** for this. After a "guard clause" you should not need `else`.

```python
def __eq__(self, other):
    if isinstance(other, Person):
        return self.id == other.id and self.last_name == other.last_name:
    else:
        return False
```


## 2. Remove unnecessary "if"

(**5 Points**) Either of these are OK but the first solution is better (a true "guard")

```python
def __eq__(self, other):
    if not isinstance(other, Person):
        return False
    return self.id == other.id and self.last_name == other.last_name
```
or
```python
def __eq__(self, other):
    if isinstance(other, Person):
        return self.id == other.id and self.last_name == other.last_name
    return False
```
## 3. Preserve Whole Object

Change TaxCalculator parameter to be a `Person` **and** save the Person reference in TaxCalculator. 

Requires changes in `main`, `TaxCalculatorTest.setUp`, and `TaxCalculator.__init__` and `compute_and_print_tax`.

```python
# main.py
if __name__ == '__main__':
    taxpayer = Person("1409900123456", "Fatalai", "Jon")
    tax_calc = TaxCalculator(taxpayer)
```
In `tax_calculator.py`:
```python
class TaxCalculator:
    def __init__(self, taxpayer: Person):
        self.taxpayer = taxpayer
```
and in `test_tax_calculator.py`:
```python
    def setUp(self):
        person = Person(...)
        self.tc = TaxCalculator(person)
```

**6 Points** for passing whole object and then saving only Person attributes in TaxCalculator:

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

    ...similar code for dividend

    ...similar code for interest
```

**Simple Solution**: One method to compute the same thing as the above. This is not the best refactoring because in the code you often need only one of the two values (sum of income or tax withheld).

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

**Better Solution**: extract one method to sum income and one method to sum tax withheld, by income type. This solution makes the other code much cleaner and simpler.

Here's the code after refactoring #10 (replace tuple with an `Income` class)
```python
    def sum_income_by_type(self, income_type: IncomeType) -> float:
        """The sum of all income for a given income_type."""
        return sum(income.amount
                   for income in self.incomes 
                   if income.income_type == income_type)

    def sum_tax_withheld_by_type(self, income_type: IncomeType) -> float:
        """The sum of all tax withheld for a given income_type."""
        return sum(income.tax_withheld
                   for income in self.incomes 
                   if income.income_type == income_type)
```

**5 Points** for writing separate methods for each income category, as below. These methods *still* contain duplicate code, it is just moved someplace else.

```python
    # in compute_and_print_tax
    ordinary_income, ordinary_tax_withheld = self.sum_ordinary_income()
    interest_income, interest_tax_withheld = self.sum_interest()
    dividend_income, dividend_tax_withheld = self.sum_dividend()
```

**5 Points** for passing the sum as a parameter. This is an anti-refactoring (Code Smell: *modifying a parameter*) and serves no purpose.

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

**5 Points** for code like this. (1) Did not remove redundant subtraction, (2) local variable for 60,000 Bt deduction. The goal of refactoring is it improve the code.  This is only a partial improvement.
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

**No Credit** for code that has 2 identical methods for computing "ordinary income tax" and "combined income tax" that use the same formula.  That is still **duplicate code**.


## 6. Inline Temp and Replace "elif" with "if"

Eliminate assignment to the local variable `tax` in the code above. Simply return the tax. When you do that, you can also replace "elif" with "if" and remove the final "else" clause:
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
- `print_tax`  - print the tax form

In my code, I refactored `compute_tax` into two parts:

- `total_tax` - (property) compute the total tax liability
- `total_tax_withheld` - (property) returns total tax withheld.

`compute_tax` is just 1 line of code and `total_tax` is simpler because it does not need the tax withheld. 

Example solution is given at the end of this file.

**5 Points** if `compute_tax` calls `print_tax`.

**5 Points** if `print_tax` requires that the caller first invoke `compute_tax` to set attributes that `print_tax` uses (Sequential Coupling).

**<= 5 Points** if `print_tax` prints incorrect values.

**No Credit** if `print_tax` duplicates the tax calculation in `compute_tax`.


## 8. Extract Variable for a Sum Computed Several Times

The sum of the tax on the income types is computed at least **6 times**:

```python
if ordinary_income_tax+interest_tax+dividend_tax > total_tax_withheld:
    # owes some additional tax
    print(format2.format("Amount of Tax Owed",
        ordinary_income_tax + interest_tax + dividend_tax 
        - total_tax_withheld)
    )
```

Introduce a **local** variable (`total_tax`) for the sum:

```python
total_tax = ordinary_income_tax + interest_tax + dividend_tax 
if total_tax > total_tax_withheld:
    # owes some additional tax
    print(format2.format("Amount of Tax Owed", 
                         total_tax-total_tax_withheld) )
```


## 9. Eliminate Flag Variable

The flag variable is `separate_income_types`.  The only thing it is used for is to decide which tax calculation to use for the total income tax.

```python
if total_tax <= all_income_tax:
    # use the tax computed separately on each income category
    separate_income_types = True
else:
    # use the tax computed on combined incomes
    separate_income_types = False
```

You can eliminate it by assigning the tax choice to a variable:

```python
if total_tax > all_income_tax:
    # use the combined tax computation since it gives less tax
    total_tax = all_income_tax
```
or (if you prefer):
```python
total_tax = min(total_tax, all_income_tax)
```

And after that, use `total_tax` and eliminate the `if` using flag variable.
> In retrospect, `simplified_tax` would be better name for `all_income_tax`.

**No Credit** if you simply replace `separate_income_types` with `total_tax <= all_income_tax` in if tests.  The purpose if this refactoring is to eliminate the unnecessary conditional cases and duplicate code.

We want to replace this duplicate code:

```python
if total_tax <= all_income_tax:
    print(format.format("Total Tax & Total Tax Withheld",
                        total_tax, total_tax_withheld)
          )
    print()
    # Does he get a tax refund or owe additional tax?
    if total_tax > total_tax_withheld:
        # tax owed = total taxes - total tax withheld
        print(format2.format("Amount of Tax Owed",
                             total_tax - total_tax_withheld)
              )
    else:
        # tax refund = total tax withheld - total tax
        print(format2.format("Amount of Tax Overpaid",
                             total_tax_withheld - total_tax)
              )
else:
    print(format.format("Total Tax & Total Tax Withheld",
                        all_income_tax, total_tax_withheld)
          )
    print()
    # Does he get a tax refund or owe additional tax?
    if all_income_tax > total_tax_withheld:
        print(format2.format("Amount of Tax Owed",
                             all_income_tax - total_tax_withheld)
              )
    else:
        print(format2.format("Amount of Tax Overpaid",
                             total_tax_withheld - all_income_tax)
              )
```

with this:
```
total_tax = min(all_income_tax, total_tax)

tax_owed = total_tax - total_tax_withheld

print(format.format("Total Tax & Total Tax Withheld",
                    total_tax, total_tax_withheld) )
if tax_owed >= 0:
    print(format2.format("Amount of Tax Owed", tax_owed))
else:
    print(format2.format("Amount of Tax Overpaid", -tax_owed))
```
**The Acid Test**:    
Your code should not have 2 print statements for "Amount of Tax Owed" and 2 print statments for for "Amount of Tax Overpaid".



## 10. Define Enum for Income Types

```python
from enum import Enum

class IncomeType(Enum):
    ORDINARY = "Wages"
    INTEREST = "Interest"
    DIVIDEND = "Dividend"

    # __str__ is not required, but useful for printing tax form
    def __str__(self):
        return self.value
```

And in the code to sum income by type:
```python
    def sum_income_by_type(self, income_type: IncomeType) -> float:
        """The sum of all income for a given income_type."""
        return sum(income.amount
                   for income in self.incomes 
                   if income.income_type == income_type)
```

Then modify the constants at the top of `test_tax_calculator.py`:
```python
# constants used in tests
ORDINARY = IncomeType.ORDINARY
INTEREST = IncomeType.INTEREST
DIVIDEND = IncomeType.DIVIDEND
```

**5 Point** if you define an Enum, but just extract the string values everywhere, like this:
```python
# constants used in tests
ORDINARY = IncomeType.ORDINARY.value  # a string!

# or in the test code -- you shouldn't change the tessts!
self.addIncome(IncomeType.ORDINARY.value, "KU", 200000, 50000)
self.addIncome(IncomeType.INTEREST.value, "Bangkok Bank", 10000, 0)
```

## 11. Introduce Parameter Object for Income

The code uses 4 parameters to describe an income item and TaxCalculator saves them as tuples. Using tuples creates awkward code.
```python
def add_income(self, income_type, desc, amount, tax_withheld):
    self.incomes.append(
         income_type, desc, amount, tax_withheld))
```

*Introduce a Parameter Object* for income data. 

Define a dataclass for the income data:
```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Income:
    income_type:  IncomeType   # Enum
    description:  str
    amount:       float
    tax_withheld: float
```
That's it! All the code you need is auto-generated.

In TaxCalculator, modify `add_income`:

```python
    def add_income(self, income: Income):
        self.incomes.append(income)
```

and modify the methods that iterate over `self.incomes` to use `Income` instead of a tuple. 
The code is cleaner & simpler:
```python
    @property
    def total_income(self):
        """The person's total income."""
        return sum(income.amount for income in self.incomes)
```

Finally, in `test_tax_calculator.py` update the `addIncome` adapter method to pass a **parameter object** instead of many parameters:

```python
    def addIncome(self, income_type, description, amount, tax_withheld):
        """Utility method to simplify refactoring of add_income()."""
        self.tc.add_income(
                Income(income_type, description, amount, tax_withheld)
                )
```

**6 Points** if you discard the parameter object in `add_income` and just save a tuple:
```python
    def add_income(self, income: Income):
        self.incomes.append(
                (income.income_type, income.description,
                 income.amount, income.tax_withheld)
            )
```
This violates *Preserve Whole Object* and makes the code more complex.


## Please Do Not Write `for` Loops Like This

Some codes look like this:

```python
# Don't do this
for k in range(len(self.incomes)):
    income = self.incomes[k]
    ...
```
This is not fluent use of Python. It looks like a C programmer writing C code in Python.

It is simpler and more flexible (works with *any* Collection or *any* Iterable) to write:

```python
for income in self.incomes:
   ...
```

Also consider if a *list comprehension* can replace the `for` loop.

The only situation to use `for k in range(...)` is if you need to know the element index (`k`) inside the loop.
