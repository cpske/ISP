## Refactoring Problem

1. What is the **sign** or **symptom** that this class should be refactored?

2. What refactoring would help?  Use the refactoring name if you know it.

```python
class Person:
    def __init__(self, firstName, lastName, 
                 address_line1, address_line2, 
                 subdistrict, district, province, postalCode):
        self.first_name = firstName
        self.last_name = lastName
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.subdistrict = subdistrict
        self.district = district
        self.province = province
        self.postal_code = postalCode

    def get_address(self):
        address = {'street1': self.address_line1,
                   'street2': self.address_line2,
                   'subdistrict': self.subdistrict,
                   'district': self.district,
                   'province': self.province,
                   'postalcode': self.postal_code
                  }
        return address

```

