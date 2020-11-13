---
title: Movie Rental Refactoring Part 2
---

This is a continuation of the Movie Rental refactoring assignment.

Before you start, verify that you correctly implemented the refactorings
from the previous assignment.

Even if your refactoring is correct, you may want to change some method names to match this.

## Verify The Previous Refactorings

**PriceCode** is a class or enum for price codes.
Either way, it should have the 2 methods shown below.
If you are using Python and a class hierarchy, then it is
OK not to have static constants for `new_release`, `normal`, `childrens`.

For Java, use uppercase for constants (NEW\_RELEASE, NORMAL, CHILDRENS).
The constants are (of course) static references to PriceCode (or subclass) objects.

<table border="1" style="width:24em">
<tr><th width="40%">PriceCode</th></tr>
<tr><td>
<u>new_release</u> <br/>
<u>normal</u> <br/>
<u>childrens</u> <br/>
</td>
</tr>
<tr><td>
price(days: int) <br/>
frequent_rental_points(days: int)
</td>
</tr>
</table>

---
**Movie** has only a title and price code.

**NO** methods for `get_price` or `get_rental_points`.  Movie has an accessor for price code and title, only. Rental computes price and frequent rental points.

<table border="1" style="width:24em;">
<tr><th>Movie</th></tr>
<tr><td>
title <br/>
price_code <br/>
</td>
</tr>
<tr><td>
get_title(): string <br/>
get_price_code(): PriceCode
</td>
</tr>
</table>

---

**Rental** has methods to compute the rental charge and frequent rental points.

**Good** if Rental also has a `get_title` that returns the movie title.  This was described in the feedback from last assignment.

<table border="1" style="width:24em;">
<tr><th>Rental</th></tr>
<tr><td>
movie: Movie <br/>
days_rented: int
</td>
</tr>
<tr><td>
get_charge(): float <br/>
get_rental_points(): float <br/>
get_title(): string <br/>
</td>
</tr>
</table>

---

**Customer** is a class with methods to add a rental, get total charges, get total rental points, and get a statement.

<table border="1" style="width:24em;">
<tr><th>Customer</th></tr>
<tr><td>
name: string <br/>
rentals: List[Rental]
</td>
</tr>
<tr><td>
add_rental(rental): <br/>
get_name(): string <br/>
compute_rental_points(): int <br/>
compute_total_charge(): float <br/>
statement(): string
</td>
</tr>
</table>

&nbsp;

## Assignment - More Refactorings

### 1. Move price code

Movie has a `price_code` attribute, but Movie doesn't use it for anything.
Only `Rental` uses the price code.

From a modeling perspective, "price code" is not a characteristic of movies.
"Price code" is a construct that's part of the rental business.

> Not only that, the price code may change!    
> "Mulan" is a "New Release" now, but in 2021 it won't be.    

So, `price_code` should be in Rental instead of Movie.

Refactoring Signs and Design Principles that support this change:

* The code shows *Feature Envy* but the solution is the opposite of what is suggested on Refactoring Guru.
* The code has *Message Chains* Rental -> Movie -> PriceCode.
* Moving price code improves *encapsulation*, since only the Rental class uses it.

### 2. Add Attributes to Movie

The revised Movie class has only a title. That's an anemic class. Add some useful features of real movies.

Add:
* `year` - the year the movie was released
* `genre` - list, tuple, or set of Strings representing *genre*.
* `is_genre(string)` - returns true if the string parameter matches one of the movie's *genre*.  

Make Movie **immutable**. There is no reason for other classes to modify a Movie.

By making Movie immutable, it is safe to use the same Movie object in several Rental objects.

In Java this is easy: define attributes as private and don't provide any "set" methods.

In Python, use a leading underscore on attribute names and write either `get_something` methods or read-only properties.  In this app we've already used `get_title`, etc., so for consistency use "getters".

### 3. Add a Movie Catalog

In the code you have now, someone would create a movie like this:
```
movie = new Movie("Mulan", 2020, ["Action","Adventure","Drama"])
```

That's a lot of data.  Make it easier to create movies by adding a Factory.

Name the factory `MovieCatalog`.

* Create a MovieCatalog as described in class. It gets movie data from a CSV file (reference below).
* It has a `get_movie(title)` method that returns a movie with matching title.
* Try to be reasonably **efficient** - don't read the file every time `get_movie` is called!
```python
catalog = MovieCatalog()
movie = catalog.get_movie("The Joy of C++")
```

For a programming challenge, try to use *lazy instantiation*.
- define a generator that reads one line of data from the CSV file and yields a movie
- get_movie(title) first checks if the `title` matches the title of movies already in the catalog. If not, it calls the generator to read more data (and create movies) until a matching title is found or end of data.

### 4. Define a Factory Method for Price Codes

How does Rental assign a price code to a movie?

The rules for price code are:

* If the movie was released this year, it's a *New Release*
* Otherwise, if one of the movie's *genre* is "Children" it's price code is "childrens"
* Otherwise it's a Normal movie

Where to put this code?  

For high cohesion and low coupling, it should be in `PriceCode`.

In Python, define a **class method** named `for_movie(movie)` that returns a `PriceCode`.

In Java, define a **static method** named `forMovie(movie)`.

```python
# Example of getting price code
catalog = MovieCatalog()
movie = catalog.get_movie("Mulan")
price_code = PriceCode.for_movie(movie)
print(price_code)

new_release
```

### Movie Rental Data

The data is in the file `movies.csv` in repository:

https://github.com/jbrucker/movierental

Lines beginning with a '#' symbol are comments and should be ignored.

I will add some more movies to the small file that is there now.
