---
title: Feedback on Movie Rental Refactoring Problem
---

[Movie Rental Part 1](#movie-rental-refactoring-part-1)    
[Movie Rental Part 2](#movie-rental-refactoring-part-2)

## Movie Rental Refactoring Part 1

After refactoring your code should have:

1. In Customer there is a method to compute the **total charge**
   * OK: Method name may be different
   * **Wrong** if the method just computes the charge for *only one* movie.
   * **Wrong** `get_total_charge()` tries to compute the charge for each movie itself, instead of calling `rental.get_charge()`.
   * **Wrong** `get_total_charge()` is using the price code. Only Rental needs to use the price code.
   * **Wrong** saving the result (total charge) as an attribute.  The method should **return** the result.
     ```python
     def get_total_charge(self):
         """Compute the total charge for all rentals."""
         return sum(rental.get_charge() for rental in self.rentals)
         #          ^^^^^^^^^^^^^^^^^^^ rental computes the charge itself
     ```
   * OK: pass the `rentals` as a parameter. It's at attribute of "self", but no harm in using a parameter instead.

2. Customer `get_rental_points()` computes and returns the total rental points.
   - It calls `rental` to get rental points for one rental
   - OK: Method name may be different
   - **Wrong** computes rental points for only one movie (should be all movies in the rental)
   - **Wrong** using pricecode to compute the rental points for each rental in this method. Only Rental needs the price code.
   - **Wrong** saving the result (total rental points) as an attribute.  It should **return** the result.
     ```python
     def get_rental_points(self):
          """Compute the total rental points for all rentals"""
          return sum(rental.get_rental_points() for rental in self.rentals)
          #          ^^^^^^^^^^^^^^^^^^^^^^^^^^
     ```
   
3. `Customer.statement()` does not calculate price of a rental or sum the charges itself.
   * `statement` calls `self.get_total_charge()` to get total charge
   * `statement` calls `self.get_rental_points()` to get total rental points
   * **WRONG**: Customer class computes the charge or rental points as part of the loop that prints the rental details.
     ```python
     def statement(self):
         # many ways to do this -- student code may not look like this
         statement = f"Rental Report for {self.name}\n\n"
         fmt1 = "{:32s}    {:4s} {:6s}\n"
         statement += fmt1.format("Movie Title", "Days", "Price")
         fmt2 = "{:32s}    {:4d} {:6.2f}\n"
        
         # add rental detail to statement
         for rental in self.rentals:
             statement += fmt2.format(rental.get_movie().get_title(), 
                                      rental.get_days_rented(),
                                      rental.get_charge())
             # Should not sum rental points or charges here

         # footer: summary of charges
         statement += "\n"
         statement += fmt1.format("Total Charges", "", self.get_total_charge())
         statement += f"FRP earned: {self.get_rental_points()}\n"
         return statement
      ```

4.  Writing `a.getB().getC()...` is called "*traversing the object graph*" and is considered something to avoid.  
   - add a `get_title()` to Rental that returns `movie.get_title()`. 
   - **OK:** instead of `get_title()`, Rental can use `__str__()` for this.
   - Then in `Customer.statement()` write:
   ```python
   for rental in self.rentals:
       statement += fmt2.format(
                       rental.get_title(),       # <---- no call chain
                       rental.get_days_rented(),
                       rental.get_charge())
   ```
   - Adding `rental.get_title()` seems pointless, but what if you decide to rent things *other* than movies?  Like Chromecast devices or DVD players?

5. Remove the static constants `REGULAR`, `NEW_RELEASE`, and `CHILDRENS` from `Movie`.  
   - Replace with price codes that encapsulate behavior for computing price and rental points.

6. PriceCodes know how to compute their own rental price and rental points. 
   - PriceCode (may have a different name) is polymorphic.  
   - In `Rental.get_price()` there is no "if ... else if ..." to test the type of movie.
   - Refactoring 1: Rental gets the price code from Movie and uses it:
     ```python
     class Rental:

         get get_charge(self):
             return self.movie.get_price_code().price(self.days)

         get get_rental_points(self):
             return self.movie.get_price_code().rental_points(self.days)
     ```
   - Refactoring 2: the price codes are moved to the Rental class. Code may be:
     ```python
     class Rental:

         get get_charge(self):
             return self.price_code.price(self.days)

         get get_rental_points(self):
             return self.price_code.rental_points(self.days)
     ```


## Movie Rental Refactoring Part 2

After this refactoring, you should have:

1. The price code is part of the Rental class. 
   ```python
   class Rental:
       def __init__(self, movie, days_rented, price_code):
           self.movie = movie
           self.days_rented = days_rented
           self.price_code = price_code
   ```
   - Better: **no** `price_code` parameter. Compute by call to a staticmethod (see item 5 below).

2. There are no price code variables in `movie.py`.
   Wrong:
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
       CHILDRENS = PriceCode.childrens
       etc.
   ```

3. Add `year` and `genre` attributes to Movie.
   ```python
   class Movie:
       def __init__(self, title, year, genre: List[str]):
           self._title = title
           self._year  = year 
           self._genres = genre

       def get_title(self):
           return self._title

       def get_year(self):
           return self._year

       def get_genres(self):   # OK to name this get_genre or genre()
           return self._genres
   ```
   - **Wrong**: the `genres` should be a list, not a string with `|`.    
   - **Wrong**: "get" methods are not intended to be used as properties:
     ```python
     @property
     get get_title(self):
     ```
     If you want to use properties, omit the `get_` prefix.

4. Add `is_genre` to Movie:
   ```python
       def is_genre(self, genre: str) -> bool:
           return genre in self._genres
   ```

5. Class method to determine the price code in the PriceCode class or Enum.
   - PriceCode class or Enum should compute the price code itself.
   - It must be a class method
   ```python
   class PriceCode(Enum):

       @classmethod
       def for_movie(cls, movie: Movie):
           this_year = datetime.now().year
           if movie.get_year == this_year:
               return PriceCode.NEW_RELEASE
           if movie.is_genre("Childrens"):
               return PriceCode.CHILDRENS
           # everything else is considered a normal rental
           return PriceCode.NORMAL
   ```

6. Rental gets the price code itself, using the class method:
   ```
   class Rental:
       def __init__(self, movie, days_rented):
           self.movie = movie
           self.days_rented = days_rented
           self.price_code = PriceCode.for_movie(movie)
   ```

7. MovieCatalog and a Factory Method for Movies.
   - See [MovieCatalog](#movie-catalog) below.

## MovieCatalog

The Movie Catalog reads movie data from a CSV file. 

It should have:

- `get_movie(title: str)` method to find and return a movie with matching title.

I'm disappointed by the poor logic and poor code, but that is
an issue beyond this assignment.

Please just check that it does what it's supposed to do (even if badly).

----

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

-----

## Code Problems and Their Solutions

Some really bad code in MovieCatalog:

1. Reads the CSV file every time `get_movie` is called.
2. Saves the CSV file as a bunch of string, and repeatedly creates new movies from the strings in `get_movie`.  Better to create each Movie once and return the same thing (Movie is immutable).
3. Fail to handle the case where a movie title is not found.


### What is Wrong with This Code?

Find:

* Inefficient code that will make the app slower than necessary
* Incorrect logic that may cause loss of data
* Not using a common refactoring goal
* Misleading variable names
* A line where meaning is hard to understand

```python
# in MovieCatalog

def get_movie(self, title: str) -> Movie:
    with open("movies.csv", 'r') as file:
        rows = csv.reader(file)
        next(rows)
        for reader in rows:
            if title == reader[1]:
                movie = Movie(reader[1], int(reader[2]), reader[3].split("|"))
                break
        return movie
```
another example:
```python
    def get_movie(self, title: str) -> Movie:
        file = open("movies.csv")
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[1] == title:
                movie = row
                name = movie[1]
                year = movie[2]
                genre = movie[3].split('|')
                file.close()
                return Movie(name, year, genre)
```

### Incomplete Method

This code works in Python, but it is not good programming style. In a language like Java or Kotlin, it won't even compile!

Why is the `get_movie` method "incomplete"?

```python
# in MovieCatalog
    DATA_FILE = "movies.csv"

    def __init__(self):
        # better: read the movie data only one time
        self.movies = self.read_movies(MovieCatalog.DATA_FILE)

    def get_movie(self, title: str):
        for movie in self.movies:
            if movie.get_title() == title:
               return movie

    def read_movies(self, filename):
        # code omitted
```

### Memory Hog

This code may use lots of memory if the movies file is large.  
It's slow and unnecessary.

```python
# in MovieCatalog

def read_movies(self, filename):
    movie_list = open(filename, "r").read().splitlines()

    # WTF is "[1:]" ?
    for line in movie_list[1:]:
        # bad variable name
        movie = line.split(",")
        # error: didn't create a list for genres
        movies.append(Movie(movie[1], movie[2], movie[3]))

    return movie_list
```

1. `read().splitlines()` reads the entire file and returns a list of strings. It's not necessary.
2. Forgot to close the file, which consumes resources.
3. *Assumes* that the first line is a comment (skips it) instead of checking, and *assumes* no other lines in the data file are comments.
4. Does not check for (and ignore) any blank lines.

### Test All Your Own Code

You should test all your code.  

Submitting code that doesn't run is the antithesis of a good Software Process.

```python
if __name__ == '__main__':
    mc = MovieCatalog       # Syntax error
    mc.get_movie("Mulan")   # discards return value
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

### Using a CLASS variable as in INSTANCE variable

A variable defined inside a class (not in a method) is a *class variable*.
If you try to access `self.x` (an *instance variable*) then Python will
first look for `x` in the object's own namespace (dictionary),
and next in the class's namespace. 

```python
class Pizza:
    # this defines a class variable named topping
    topping = 'Cheese'

# access via the class's namespace
Pizza.topping
'Cheese'
# access via an object's namespace
p = Pizza()
p.topping
'Cheese'
```

This is similar to Java, where you can access static attributes using
instance notation. In Java, however, you cannot have an instance variable
(attribute) that has the same name as a class (static) variable.

In Python, if you try to *assign* a value to a class variable using
an instance, then Python creates a **new** variable with the same name
as part of the object's own namespace.

```python
p = Pizza()
p.topping
'Cheese'
# creates a new "topping" variable as part of p object's namespace
p.topping = 'Seafood'
p.topping
'Seafood'
# the class variable is not modified
Pizza.topping
'Cheese'
```

To understand this clearly, read about **namespaces** in Python.
<https://docs.python.org/3/tutorial/classes.html>

That page explains the difference between class variables 
and instance variables (attributes).

```python
class MovieCatalog:
   DATA_FILE = "movies.csv"

   def __init__(self):
       movies = read_movies(self.DATA_FILE)
```

This works but it relies on Python accessing a *class* variable via an *instance* reference.  It would be clearer to write `MovieCatalog.DATA_FILE`.

Experiment with this code:
```python
class Pizza:
    # a class variable
    topping = 'Cheese'

    def __str__(self):
        return f"A {self.topping} pizza"
```

```
cmd> p = Pizza()
cmd> print(p)
A Cheese pizza
cmd> p.topping = "Seafood"
cmd> print(p)
A Seafood pizza
# the class variable didn't change
cmd> Pizza.topping
Cheese

# another pizza
cmd> q = Pizza()
# change the class's topping
cmd> Pizza.topping = "Veggie"
# does that change affect q?  Is q a Cheese pizza or Veggie pizza?
cmd> print(q)
???
# does it change p.topping?
cmd> print(p)
???
```
