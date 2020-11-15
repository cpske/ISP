---
title: Feedback on Movie Rental refactoring problem
---

After refactoring your code should have:

1. `Customer.statement()` does not calculate price of a rental. 
   * `statement` calls `self.get_total_charge()` to get total charge (OK to use a different method name).
   * `self.get_total_charge()` calls `rental.get_charge()` for each rental and returns the sum.
   * WRONG: Customer class computes the charge for each rental itself.

2. `Customer.statement()` does not compute frequent rental points.
   * structure is just like computing the rental charges.
   * `statement` calls `self.get_rental_points()` (or similar method).
   * `self.get_rental_points()` calls `rental.get_rental_points()` for each rental and returns the sum
   * WRONG: Customer class computes the rental points for each rental itself.

3. `Customer.statement()` the loop to create a list of rentals should look like:
   ```python
   def statement(self):
       ...
       for rental in self.rentals:
           statement += fmt.format(
                       rental.get_movie().get_title(), # See Item 4
                       rental.get_days_rented(),
                       rental.get_charge())
       # footer: total charges
       statement += "\n"
       statement += "{:32s} {:6s} {:6.2f}\n".format(
                     "Total Charges", "", self.get_total_charge())
       statement += "Frequent Renter Points earned: "+str(self.get_rental_points())+"\n"
   ```
   **Wrong**: summing the rental charge or rental points in the "for" loop.    
   **Good**: f-strings are more concise than `string.format`.  OK to write:
   ```python
       line_text = "Total Charges"
       statement += f"{line_text:39s}  {self.get_rental_points():6.2f}\n"
   ```

4.  Writing `a.getB().getC()...` is called "*traversing the object graph*" and is considered something to avoid.  It is better to add a `get_title()` to Rental that returns `movie.get_title()` and then write:
   ```python
   for rental in self.rentals:
       statement += fmt.format(
                       rental.get_title(),  
                       rental.get_days_rented(),
                       rental.get_charge())
   ```
   - Adding `rental.get_title()` seems pointless, but what if you decide to rent things *other* than movies?  Like Chromecast devices?
   - It is OK to traverse the object graph for stable APIs like the Java SE API or PyGame API. For a List of Number objects in Java, it would be fine to write `list.get(k).doubleValue()`

5. `Customer.get_total_charge()` asks Rental for the charge of a rental. Don't try to compute the charge in Customer by getting the price code.
   ```python
   def get_total_charge(self):
       """Get the total charge for all rentals."""
       total = sum(rental.get_charge() for rental in self.rentals)
       return total
   ```

6. `Customer.get_rental_points()` asks Rental for the rental points, exactly as done with charge. 

7. PriceCode is polymorphic.  In `Rental.get_price()` there is no "if ... else if ..." to compute the charge based on type of movie.     
   Rental simply gets the price code from Movie and uses it:
   ```python
   # In Rental class

   get get_charge(self):
       return self.movie.get_price_code().price(self.days)

   get get_rental_points(self):
       return self.movie.get_price_code().rental_points(self.days)
   ```

## The Acid Test

Here's a test of how well-factored and extensible your code is.

The movie rental store decides to rent Chromecast USB devices.

The Chromecast rental charge is $1 + $0.1 per Gigabyte of content viewed (which we can get from Google).  Customer gets 1 rental point per 10 Gigabytes of content purchased.

So you write:
```python
import random

class Chromecast:
    """
    Represents a Google Chromecast device.
    Each device has a unique device id that can be used to get usage data.
    """
    def __init__(self, device_id: str):
        self.device_id = device_id
        random.seed(device_id)
        self.usage_data = random.randrange(1000, 100000)

    def get_usage(self):
        """Return the number of megabytes of content consumed.

        In reality we would use a Google API to get usage data from Google.
        For testing, we just return some generated values.
        """
        return self.usage_data

    def __str__(self):
        return f"Chomecast device {self.device_id}"
```

```python
class ChromecastRental(Rental):
    def __init__(self, chromecast):
        self.chromecast = chromecast

    def get_title(self):
        return str(self.chromecast)

    def get_charge(self):
        """Chromecast rental costs $1 per $0.1 per gigabyte of content"""
        megabytes = self.chromecast.get_usage()
        charge = 1.0 + 0.1 * math.ceil(megabytes/1000.0)
        return charge

    def get_rental_points(self):
        """Chromecast rental earns 1 point for each 10GB usage"""
        megabytes = self.chromecast.get_usage()
        return math.floor(megabytes/10000.0)
```

### The Test

Can you add a `ChromecastRental` to a Customer's rentals, without making any changes to Customer, Movie, or Rental?

Does your code print a correct statement?

```python
customer = Customer("Movie Addict")
movie = Movie("Mulan", PriceCode.new_release)
customer.add_rental(Rental(movie, 5))

# Watch unlimited stuff on a Chromecast
device = Chromecast("a3:b0:00:13:4c:88")
customer.add_rental(ChromecastRental(device))

# the acid test
print(customer.statement())
```

## Movie Rental Refactoring Part 2

1. Move the price code to the rental class.
   ```python
   class Rental:
       def __init__(self, movie, days_rented, price_code):
           ...
   ```
2. There are no price code variables in `movie.py`.    
   WRONG:
   ```python
   class Movie:
       NORMAL = 0
       CHILDRENS = 1 
       NEW_RELEASE = 2 
   ```
   Also wrong:
   ```python
   class Movie:
       NORMAL = PriceCode.normal
       etc.
   ```

3. Add Attributes to Movie. Use underscore to indicate the variables are private and provide "get" methods.  This is simple programming.
   ```python
   class Movie:
       def __init__(self, title, year, genre: List):
           self.__title = title
           self.__year  = year 
           self.__genre = genre

       def get_title(self):
           return self.__title

       def get_year(self):
           return self.__year

       def get_genre(self):   # OK to name this get_genres
           return self.__genre

       def is_genre(self, genre: str) -> bool:
           return genre in self.__genre
   ```
   Wrong: the `genre` should be a list, not a string with `|`.    
   Wrong: "get" methods are not intended to be used like properties:
   ```python
       @property
       get get_title(self):
   ```

4. Class method to determine the price code.  It makes sense that this should be part of the `PriceCode` class.  If we add a new `PriceCode` the changes affect only one class.
   ```python
   class PriceCode(Enum):

       @class_method
       def for_movie(cls, movie: Movie):
           this_year = datetime.now().year
           if movie.get_year == this_year:
               return PriceCode.NEW_RELEASE
           if movie.is_genre("Childrens"):
               return PriceCode.CHILDRENS
           # everything else is considered a normal rental
           return PriceCode.NORMAL
   ```

5. Factory Method for movies.  This part had the most number of errors.



6. Wrong file name.  Some students used names like these. They do not use the Python naming convention:
   ```
   Movie.py
   movieCatalog.py
   MovieCatalog.py
   ```

