---
title: Movie Rental Refactoring Part 2
---

This is a continuation of the Movie Rental refactoring assignment.
Before you start, verify that you correctly implemented the refactorings
from the previous assignment.

Even if your refactoring is correct, please revise it to be similar
to this.

## Verify The Previous Refactorings

**PriceCode** is a class or enum for price codes.
Either way, it should have the 2 methods shown below.
If you are using Python and a class hierarchy, 
OK not to have static constants for `new_release`, `normal`, `childrens`.

OK to use uppercase for constants (NEW\_RELEASE, NORMAL, CHILDRENS).


<table border="1" style="width:32em">
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

**Movie** knows the price code and title, not much else.

**NO** methods for `get_price`, `get_rental_points`.  Movie provides only the price code. Rental computes price and frequent rental points.

<table border="1" style="width:32em;">
<tr><th>Movie</th></tr>
<tr><td>
<u>title</u> <br/>
<u>price_code</u> <br/>
</td>
</tr>
<tr><td>
get_title(): string <br/>
get_price_code(): PriceCode
</td>
</tr>
</table>

**Rental** has methods to compute the rental charge and frequent rental points.

**Good** if Rental also has a `get_title` that returns the movie title.  This was described in the feedback from last assignment.

<table border="1" style="width:32em;">
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

**Customer** is a class with methods to add a rental, get total charges, get total rental points, and get a statement.

<table border="1" style="width:32em;">
<tr><th>Customer</th></tr>
<tr><td>
name: string <br/>
rentals: List[Rental]
</td>
</tr>
<tr><td>
add_rental(rental): <br/>
get_name(): string <br/>
get_rental_points(): int <br/>
get_total_charge(): float <br/>
statement(): string
</td>
</tr>
</table>

## Assignment - More Refactorings

### 1. Move PriceCode

Movie has a `price_code` attribute, but Movie doesn't use it for anything.
Only `Rental` uses the price code.

From a modeling perspective, "price code" is not a characteristic of movies.
"Price code" seems like a construct part of a specific rental business.

> Not only that, but the price code may change!    
> "Mulan" is a "New Release" now, but in 2021 it won't be, 
> even though the Movie is the same.

So, we should put `price_code` in Rental instead of Movie.

Refactoring Signs and Design Principles:

* The code show *Feature Envy* but the solution is the opposite of what is suggested on Refactoring Guru.
* The code has *Message Chains* rental -> Movie -> PriceCode.
* Moving price code improves *encapsulation*, since only the Rental class uses it.

### 2. Add Attributes to Movie

The Movie class only has a title, after you refactor price code (above). That's an anemic class. Add some important features of real movies.

Add:
* `year` - the year the movie was released
* `genre` - list, tuple, or set of Strings representing *genre*.
* `is_genre(string)` - returns true if the string parameter matches one of the movie's *genre*.  Use case-insensitive match. 

Make Movie **immutable**. There is no reason for other classes to modify a Movie.

By making Movie immutable, it is safe to use the same Movie object in several Rental objects.

In Java this is easy: make attributes private and no "set" methods.

In Python, use a leading underscore in attribute names and write either `get_something` methods or read-only properties.  In this app we've already used `get_title`, etc., so for consistency use "getters".

### 3. Add a Movie Catalog

In the code you have now, someone would create a movie like this:
```
movie = new Movie("Mulan", 2020, ["Action","Adventure","Drama"])
```

That's a lot of data.  Make it easier to create movies by adding a Factory.

Name the factory `MovieCatalog`.


4. Create a MovieCatalog as described in class.  It should have a `get_movie(title)`
   method that returns a movie by title.  MovieCatalog creates movies by reading data from CSV file.  Note that in `Movie` the *genre* is a list of string, not a single string.

5. You don't need to submit this, but know the answer:
   * Which "Code Smell" suggests the `price_code` belongs in Rental?
   * 


> 
so we 


1. Add some new attributes to movie:
   ```
   year - the year the movie was released
   genre - a list of genre, as strings
   ```
   to make everyone's code similar use this constructor:
   ```python
   # Mulan is a drama and rated for children (2 genre)
   movie = Movie("Mulan", 2020, ["Drama","Children"])
   ```

2. Refactor the Movie class and Rental class so that price code is part
   of `Rental` instead of Movie.  The pricing and renter points calculation
   is done by rental so it makes sense for price code to be in rental.

3. Use a *Factory Method* for rentals instead of constructor:
   ```python
   movie = Movie("No Time to Die", 2020, ["Action","Thriller"])
   # rent it for 4 days
   rental = Rental.create_rental(movie, 4)
   ```
   `create_rental` is a **classmethod**. It returns a `Rental` object. The rules for price code are:
   * If the movie was released this year, its *New Release*
   * Otherwise, if one of the *genre* is "Children" its a Chilren's movie
   * Otherwise it's a Normal movie
