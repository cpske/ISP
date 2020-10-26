---
title: Feedback on Movie Rental refactoring problem
---

After refactoring your code should have:

1. `Customer.statement()` does not calculate price of a rental. It calls `rental.get_charge()` or `rental.getCharge()` (Java).
   * OK to use a different method name like `get_price()`.
   * WRONG: Customer class computes the charge for each rental itself.
   * In `Customer.statement()` the loop to print a list of rentals should look like:
   ```python
   def statement(self):
       self.total_amount = 0.0
       for rental in self.rentals:
           statement += fmt.format(
                       rental.get_movie().get_title(), # See Note
                       rental.get_days_rented(),
                       rental.get_charge())
           self.total_amount += rental.get_charge()
   ```
   and in `get_charge()` write:
   ```python
   def get_charge(self):
       return self.total_amount
   ```
   * **Note**: writing `a.getB().getC()...` is called "*traversing the object graph*" and is considered something to avoid.  It is better to add a `get_title()` to Rental that returns `movie.get_title()` and then write:
   ```python
   for rental in self.rentals:
       statement += fmt.format(
                       rental.get_title(),  
                       rental.get_days_rented(),
                       rental.get_charge())
	```
   - This seems trivial, but what if you decided to rent things *other* than movies?
   * It is OK to traverse the object graph for stable APIs like the Java SE API or PyGame API. For a List of Number objects in Java, it would be fine to write `list.get(k).doubleValue()`

2. `Customer.statement()` uses a query for charge (as shown above) instead of a temp variable.  According to the assignment, this is incorrect: 
   ```python
   for rental in self.rentals:
       amount = rental.get_charge()  # Incorrect: using a temp variable
       statement += fmt.format(
                       rental.get_movie().get_title(),
                       rental.get_days_rented(),
                       amount)
       total_amount += amount
   ```
 
3. Customer has a `get_frequent_rental_points` method to compute the frequent renter points.    
   CORRECT:
   ```python
   def get_frequent_renter_points(self):
       """Compute frequent renter points for all rentals."""      
       renter_points = sum([rental.get_rental_points() for rental in rentals])
       return renter_points
   ```
   **WRONG**: Computing the frequent renter points in `statement()` and returning it in `get_renter_points`
   ```python
   def get_frequent_renter_points(self):
       return self.renter_points
 
   def statement(self):
       self.renter_points = 0
       for rental in self.rentals:
           self.renter_points += rental.get_rental_points()
		   ...
   ```
   **WHY THIS IS WRONG**: It *assumes* you always call `statement()` *before* calling `get_frequent_renter_points`. That is a form of coupling.   
   This is similar to the CoinPurse or BankAccount where `getBalance()` computes the balance itself; it does not rely on `deposit` and `withdraw` to update a balance attribute (there is none).
4. Rental computes rental points and charge itself, using the price code from Movie:
   ```python
   class Rental:
       # RIGHT
       def get_rental_points(self):
           return self.movie.price_code.get_rental_points(self.days_rented)
	   def get_charge(self):
	       return self.movie.price_code.get_charge(self.days_rented)
   ``` 
   **WRONG**: Compute `charge` and `rental_points` in the `Movie` class:
   ```python
   class Movie:
       # WRONG:
       def get_charge(self, days_rented):
	       return self.price_code.get_charge(days_rented)
	   def get_rental_points(self, days_rented):
	       ...
   class Rental:
       def get_charge(self):
	       return self.movie.get_charge(self.days_rented)
	   def get_rental_points(self):
	       return self.movie.get_rental_points(self.days_rented)
   ```
   - "Rental charge" and "Rental points" are associated with renting something, so it should be the Rental class's responsibility to compute them.
   - the Movie class focuses on characteristics of a movie.
   
5. PriceCode is polymorphic.  In `Rental.get_price()` there is no "if ... else if ..." to compute the charge based on type of movie.  Below are 2 ways to implement it.

5.1 PriceCode Using Enum:
- Code for `PriceCode` is in README.
- In Rental you would have:
  ```python
  class Rental:
      def get_rental_points(self):
          return self.movie.price_code.get_rental_points(self.days_rented)

      def get_price(self):
          retrun self.movie.price_code.get_price(self.days_rented)
    ```

5.2 PriceCode Using Subclasses for the movie price codes:
 ```python
class PriceCode:
    def get_price(self, days_rented):
        return 0.0
    def get_rental_points(self, days_rented):
        return 0

class NewRelease(PriceCode):
    def get_price(self, days_rented):
        return 3.0*days
    def get_rental_points(self, days_rented):
        return days_rented
```
The code in `Rental` is the same for both Enum and subclass objects, but how you create PriceCode objects to set into a Movie instance is different:
```python
# Enum for PriceCode
movie = Movie("Mulan", PriceCode.new_release)

# Classes for price code
movie = Movie("Mulan", NewRelease())
```

Even better: use a MovieFactory to encapsulate and hide this stuff.
```python
movie = MovieFactory.findByName("Mulan")
```

## The Acid Test

Here's a test of how well-factored and extensible your code is.

The movie rental store decides to rent ChromeCast USB devices.

The ChromeCast rental charge is $5 + $1 per Gigabyte of content viewed (which we can get from Google).  Customer gets 1 rental point per 10 Gigabytes of content purchased.

So you write:
```python
def ChromeCastRental(Rental):
    def __init__(self, device_id):
        self.device_id = device_id

    def get_title(self):
        return f"ChromeCast with id {self.device_id}"

    def get_price(self):
        mb = google.chromecast.get_usage(self.device_id, GOOGLE_API_KEY)
        return 5.0 + 0.001*mb  # convert MB to GB

    def get_rental_points(self):
        mb = google.chromecast.get_usage(self.device_id, GOOGLE_API_KEY)
        return math.floor(mb/10000.0)
```

Can you add a `ChromeCastRental` to a Customer's rentals, without making any changes to Customer, Movie, or Rental?

```python
customer = Customer("Movie Addict")
movie = Movie("Mulan", PriceCode.new_release)
customer.add_rental(Rental(movie, 5))

# Watch unlimited stuff on a ChromeCast
chromecast = ChromeCastRental("a3:b0:00:13:4c:88")
customer.add_rental(chromecast)

# the acid test
print(customer.statement())
```

## 6. The Missing Refactoring

Something is still in the wrong class, in my opinion.

What do you think?
