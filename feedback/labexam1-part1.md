---
title: Feedback on Labexam 1 part 1
---

## Evaluation

Code improvement in `contacts.py`.

|  # | Change          | Description |
|----|-----------------|-------------|
|  1 | Contact         | Class name should start with capital letter  |
|  2 | Class docstring | a) inside class, b) Complete sentence with initial capital **and** period.|
|  3 | `__init__`      | Inside method, first line is **complete sentence** followed by blank line.|
|  4 | `Arguments:`    | Word "Arguments:" or "Args:" or "Parameters:" in docstring.|
|  5 | `phone_number`  | Rename phoneNumber to `phone_number`. |
|  6 |  age(self)      | Rename Age(self) to `age` |
|  7 | `Returns:`      | Add "Returns:" to docstring for at least 1 method.  |
|  8 | `get_name(self)`| Rename getName(self) to `get_name`. |
|  9 | `__eq__`        | Logic: change "or" to "and" |
| 10 | `__eq__` long line | split long line |

Code Formatting:

|  # | Change          | Description |
|----|-----------------|-------------|
| 11 | 1-2 blank lines | before class |
| 12 | 1 blank line    | before each method |
| 13 | space around =  | always leave 1 space around = |
| 14 | space around -  | in age: `today.years - bday.years` |
| 15 | space around <  | in age: `(year,month,day) < (year,month,day)` |
| 16 | space after ,   | in eq: `not isinstance(other, Contact)` |

flake8 would find and display most of these problems, but not the logic error (9).
