---
title: Movie Rental Refactoring Part 2
---

This is a continuation of the Movie Rental refactoring assignment. 

In this assignment you will add structural-level refactorings to improve the design.

Prerequisites for this assignment:

1. Your code has the classes and methods as shown in the UML class diagrams at the end of [Movie Rental Part 1](movierental-part1#uml-class-diagram).

2. The `PriceStrategy` is in a **separate file** named `pricing.py`.  PriceStrategy should **not** in `movies.py` or `rental.py`.

---

### 1. Refactor Rental Price and Rental Points (*Remove Middleman*)

The `Customer` class calls `Rental` to get the rental price and rental points, `Rental` calls Movie, like this: 

```python
# Rental class
def get_price(self):
    return self.movie.get_price(self.days_rented)

def get_rental_points(self):
    return self.movie.get_rental_points(self.days_rented)
```
Movie ***delegates*** these methods to the pricing strategy:

```python
# in Movie class
def get_price(self, days_rented):
    return self.price_code.get_price(days_rented)

def get_rental_points(self, days_rented):
    return self.price_code.get_rental_points(days_rented)
```

What *Refactoring Signs* and *Design Principles* apply here?

- ***Middle Man***: both Movie is acting as a *middle man*
- Violation of ***Single Responsibility Principle*** (*SRP*): Movie is responsible for knowing the information about a movie **and** for knowing the price code, rental price, and rental points.    
  That's two unrelated sets of responsbilities, which violates *SRP*.
- ***Low Cohesion***: *rental price* and *rental points* are properties of a Rental, not a Movie.  Only Rental needs those values.

Refactor: 

- Apply **Remove Middle Man**. In this case `Movie` is the "Middle Man".  
- Make `Rental` invoke the `price_code` methods directly.
- Remove `get_price` and `get_rental_points` from Movie.


### 2. Move `price_code` Attribute

After the previous refactoring, only `Rental` uses the price code.  Move it to Rental. Also move `get_price_code` from Movie to Rental.

Justify this refactoring. Write your answers in README.md (see [What to Submit](#what-to-submit)).

**2.1** what *refactoring signs* (code smells) suggest this refactoring?

**2.2** what *design principle* suggests this refactoring?  Why?


### 3. Add Attributes to Movie

The revised Movie class has only a title. That's a  [Lazy Class](https://refactoring.guru/smells/lazy-class), aka *Anemic Class*. Let's fix that. 

3.1 Add these useful attributes and methods:

- `year` - the year the movie was released
- `genre` - a **collection** *genre* names (strings), as a list or set.
- `is_genre(string)` returns true if the string parameter matches any of the movie's *genre*.  Example: `is_genre("action")`. Ignore case of letters.
- `__str__` returns "*Title* (year)" of the movie, e.g. "Mulan (2020)".
- constructor: `Movie(title: str, year: int, genre: Collection[str])`

3.2 Make Movie **immutable**.  Make Movie immutable to reduces errors, since multiple Rentals may refer to the same Movie instance.
- to be immutable, the year, title, and genre must be read-only.

**Suggestion**: Define Movie as a Python [dataclass][] with [frozen=True][frozen]. You will only need to write `__str__` and `is_genre`.

[dataclass]: https://docs.python.org/3/library/dataclasses.html
[frozen]: https://docs.python.org/3/library/dataclasses.html#frozen-instances


### 4. Define a Factory for Movies (MovieCatalog)

In the current code (after refactoring #3), to create a movie we need code like this:
```
movie = new Movie("Mulan", 2020, ["Action","Adventure","Drama"])
```

There are problems with creating movies directly in the app: 

- Where does the movie data come from?
- How does the class that *instantiates* a Movie get the data it needs?
- Errors. We might enter the genre or year incorrectly.

Apply these design principles:

- Encapsulation - encapsulate and hide creation of Movie objects
- Separation of Concerns - the class that *uses* movies is separate from the class that *creates* movies

Define a factory class named `MovieCatalog` to create and access Movies.

- MovieCatalog gets movie data from a CSV file, [see below](#the-movie-rental-data).
- MovieCatalog is a *singleton*. We want only one movie catalog!
- It has a `get_movie` method that returns a movie with matching title and optional year. If year is omitted, return the first matching movie.
  ```python
  # Get the Singleton Movie Catalog
  catolog = MovieCatalog()
  # Get the first movie named 'Mulan'
  movie = catalog.get_movie("Mulan")
  # Get 'Mulan' released in 1998
  old_movie = catalog.get_movie("Mulan", 1998)
  ```

- Write an **efficient** implementation: 

  1. MovieCatalog reads the data file **only once**.
  2. Do *not* read the entire data file into memory as a string. The data could be very large. Read and process one line at a time     - Any code that reads the entire movies data file into a string will get **zero** credit.
  3. Save the data as Movie objects, not strings.

- **No Credit** if you violate any of the above guidelines.

Example usage:

```python
catalog = MovieCatalog()
movie = catalog.get_movie("No Time to Die")
if not movie:
   print("Sorry, couldn't find that movie.")
```

### 5. Define a Method to Determine Price Code

In the current code, when we create a Rental we have to manually assign a price code:

```python
movie = catalog.get_movie("Top Gun: Maverick")
days  = 4
price_code = NEW_RELEASE   # or PriceStrategy.NEW_RELEASE
rental = Rental(movie, days, price_code)
```

Define a class method or top-level function with signature `price_code_for_movie(movie)` that returns the price code for a movie.

The pricing rules are:

- If the movie was released this year, it's a *New Release*
- Otherwise, if any of the movie's *genre* is "Children" or "Childrens", then it's a "Childrens" price
- Otherwise it's a Regular price rental

5.1 Decide where `price_code_for_movie` should be implemented.  It can be a class method or top-level function in an existing module.  The choices are: 
   - Movie class or movie module
   - Rental class or rental module
   - PriceStrategy class or `pricing` module 

**5.2** Document the reason(s) for your choice in README.md.  
    Write your answer in README.md, in a section named `Rationale`. 
    Describe where you implement this method and **the reasons** for your choice. Include one or more of these design principles to justify your design and how it applies: 

  - *Low Coupling*: choose a class/module that adds the least amount of coupling when you implement the method
  - *High Cohesion*: choose a class that that closely uses the price codes
  - *Single Responsibility Principle*: choose a class/module that is "responsible" to the actor who sets prices
  - *Information Expert*: choose a class that already has most of the information needed to determine the price code
  - other design principle or refactoring sign that you think is relevant.
  - If several principles suggest the *same* class or module, that's a good sign.

> *Hint:* 
> If you are not sure which class or module to choose, then try them all!
> Implement `get_price_for_movie` in different modules/classes and see which choice gives you the simplest, cleanest code.

5.3 Implement `get_price_for_movie` in the location you chose.

5.4 Write a unit test for this code in `pricing_test.py`.  Use `pytest` or `unittest` syntax so I can run your tests using: `pytest pricing_test.py` (pytest can run unittest style tests)
  - Test that it returns the correct price strategy for each type of movie.
  - Don't use MovieCatalog to get movies.  Tests should not depend on external data like that.

### 6. Modify `Rental` class to determine the Price Code itself

The Rental class should get the price code itself.

In `Rental`, **remove** the constructor parameter for `price_code`, so we can create a rental like this:  

```python
movie = MovieCatalog().get_movie("Oppenheimer")
# rental determines the price code itself
rental = Rental(movie, days_rented)
```


### The Movie Rental Data

The movie data is in a file named `movies.csv` at this URL:

<https://cpske.github.io/ISP/assignment/movierental/movies.csv>

Each line is one of:

- movie data in CSV format with one or more "genre" separated by a vertical bar
  ```
  movie_id,title,year,genre1|genre2|...
  # for example
  202301,Oppenheimer,2023,Biography|Drama|History
  ```
- blank line
- comment line beginning with '#' symbol. Comment lines may occur *anywhere* in the file.

Blank lines and comment lines may be **anywhere in the file**, not just the top of file.
Blank lines and comment lines should be ignored. 

If any data line contains invalid movie data then `log` an error using the Python logging module. Use a log message like this one:
```
Line 37: Unrecognized format "164179,Arrival,2016"
```
Skip the erroneous line but continue processing the CSV file.


## What to Submit

Commit your work to your `movierental` repository on Github.

For your answers to 2.1, 2.2, and 5.2, add a level-2 section named "Rationale" to README.md.  Write your answers there.

### Challenge: *Lazy Instantiation of Movies*

Creating all the movies from data at start-up time will make the app slow and can waste memory.

You can improve performance by creating movies only as needed (*lazy instantiation*).  Here's one way:

- in MovieCatalog, write a *generator* function that returns the *next* movie read from the data file.
- a generator uses `yield` to return the next movie. It uses `return` when there are no more values to generate.
- the `get_movie` method uses logic like this:
  - if a matching movie is found in the collection of Movies already created, then return it.
  - otherwise, call the generator repeatedly until you find a matching movie.  Each time you call the generator, add the new Movie to the collection of known movies.
  - when the generator reaches the end of the data file, the generator closes the file and returns None

Writing a generator is simple.  It's like a function, but use `yield` to return a value instead of `return`.
