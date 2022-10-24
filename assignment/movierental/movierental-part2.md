---
title: Movie Rental Refactoring Part 2
---

This is a continuation of the Movie Rental refactoring assignment.

These refactorings assume your code has the methods shown in the UML class diagrams at the end of [Movie Rental Part 1](movierental-part1#uml-class-diagram).

`Customer`, `Rental`, `Movie`, and `PriceCode` (or `PriceStrategy`) should have the methods shown in the UML diagram from part 1.

The `PriceCode` (or `PriceStrategy`) code should be in a **separate file**, not in movies.py or rental.py.  Suggested filename is `pricing.py`.

---

## Assignment

### 1. Refactor Rental Price and Rental Points

The `Customer` class calls `Rental` to get the rental price and rental points, `Rental` calls Movie, and Movie calls `PriceStrategy` to compute these: 

```python
# Rental class
def get_price(self):
    return self.movie.get_price(self.days_rented)

def get_rental_points(self):
    return self.movie.get_rental_points(self.days_rented)
```
Movie delegates these methods to the `price_code`:

```python
# Movie class
def get_price(self, days_rented):
    return self.price_code.get_price(days_rented)

def get_rental_points(self, days_rented):
    return self.price_code.get_rental_points(days_rented)
```

What *Refactoring Signs* or *Design Principles* apply here?

- Middle Man: both Rental and Movie are acting as *middle man* for these methods
- Single Responsibility Principle: Movie is responsible for knowing the information about a movie **and** for knowing the price code, rental price, and rental points. So Movie is responsible to the movie producer (or movie information service) and the rental store.
- Low Cohesion: conceptually, *rental price* and *rental points* are properties of a Rental, not a Movie.

Solution: Apply **Remove Middle Man**. In this case the "Middle Man" is `Movie`.  We can have `Rental` invoke `price_code` methods directly. Eliminate `get_price` and `get_rental_points` in Movie.


### 2. Move `price_code` Attribute

After the above refactoring, only `Rental` uses the price code.  Move it to Rental. Also move `get_price_code` from Movie.

What is a justification for this refactoring?

- what *refactoring signs* (code smells) suggest it?
- what *design principle* suggests it?


### 3. Add Attributes to Movie

The revised Movie class has only a title. That's an **Anemic Class**. Add some useful information about real movies. 

Add:

* `year` - the year the movie was released
* `genre` - a **collection** *genre* names (strings), as a list or set.
* `is_genre(string)` returns true if the string parameter matches one of the movie's *genre*.  Example: `is_genre("action")`. Ignore case of letters.
* `__str__` returns "*Title* (year)" of the movie, e.g. "Mulan (2020)".
* constructor: `Movie(title: str, year: int, genre: Collection[str])`

Make Movie **immutable**.  Making Movie immutable reduces the chance for errors, since multiple Rentals may use the same Movie instance.


### 4. Define a Factory for Movies (MovieCatalog)

In the current code (after #3), to create a movie we need code like this:
```
movie = new Movie("Mulan", 2020, ["Action","Adventure","Drama"])
```

That's a lot of data.  
- Where does the data come from?
- How does the class that *instantiates* a Movie get the data it needs?

Apply two design principles:

- Encapsulation - encapsulate and hide creation of Movie objects
- Separation of Concerns - the classes that *use* movies are separate from the classes that *create* movies

Define a factory class to create and access Movies, named `MovieCatalog`.

- MovieCatalog gets movie data from a CSV file (reference below).
- MovieCatalog is a *singleton*. We want only one instance.
- It has a `get_movie` method that returns a movie with matching title and optional year. If year is omitted, return the *newest* release.
  ```python
  # Get the most recente 'Mulan' movie.
  movie = catalog.get_movie("Mulan")
  # Get 'Mulan' released in 1998
  movie = catalog.get_movie("Mulan", 1998)
  ```
- Try to be *efficient* 
  1. MovieCatalog should read the data file **only once**.
  2. Don't read the whole file into memory as a string. It could be large. Read and process one line at a time.
  3. Save the data as Movie objects, not strings.
- **No Credit** if you violate any of these guides.

Here's how the catalog will be used:
```python
catalog = MovieCatalog()
movie = catalog.get_movie("No Time to Die")
```


### 5. Define a Method for Price Codes

In the current code, when we create a Rental we have to manually assign a price code:

```python
movie = catalog.get_movie("Top Gun: Maverick")
days  = 4
price_code = NEW_RELEASE
rental = Rental(movie, days, price_code)
```

For this refactoring, you will define a class method or top-level function with signature `price_code_for_movie(movie)` that returns the price code for a movie.
The rules are:

- If the movie was released this year, it's a *New Release*
- Otherwise, if any of the movie's *genre* is "Children" or "Childrens" than it's a "Childrens" price code
- Otherwise it's a Regular price movie

This can be a top-level function or a class method.

Do the following:

1. Apply design principles to choose which class (for a method) or module (for a top-level function) should contains this code.  The choices are:
   - Movie class or movie module
   - Rental class or rental module
   - PriceCode class/enum or the pricing module 

2. Document the reason(s) for your choice in README.md in a 2nd level section named `## Price Code Design`.

3. Write the code in the location you chose.

4. Write a unit test for this code in `pricing_test.py`.

5. Modify `Rental` class to determine the price code itself.  Remove the constructor parameter for `rental`, so we can create a rental like this:  
  ```python
  rental = Rental(movie, days_rented)
  ```

Design Principles to consider (you don't need to use all of these):

- *Low Coupling*: choose a class/module that results in minimal coupling or adds the least coupline
- *High Cohesion*: choose a class that is already responsible for price codes, or that closely uses the price codes
- *Single Responsibility Principle*: choose a class/module that is "responsible" to the actor who sets prices
- *Information Expert*: choose a class that already has most of the information needed to determine the price code
- any other design principle or refactoring guide that you apply.

If several principles suggest the *same* class or module, that's a good sign.

> *Hint:* 
> If you aren't sure which class or module to choose, or not sure whether to use a class method versus top-level function (defined outside the class), then try both!
> Implement it multiple ways and see which one gives you the simplest, cleanest code.


### Extra: For Serious Coders

If the movie data is large and you try to process the entire file at start-up, the application will be slow.

You can improve this as follows:

- write a *generator* that returns the *next* movie created from the data file.
- in the `get_movie` method you use logic like this:
  - if a matching movie is found in the collection of Movies already created, then return it.
  - otherwise, call the generator until you find a matching movie.  Each time you call the generator, add the new Movie to the collection of movies.
  - when the generator reads to the end of the file, close the file

This is called *lazy instantiation*.  You "instantiate" objects only when you need them.

Writing a generator is pretty simple.  It's like a function, but use `yield` to return a value instead of `return`.

### Movie Rental Data

The movie data is in a file named `movies.csv` at this URL:

https://cpske.github.io/ISP/assignment/movierental/movies.csv

Each line is one of:
- movie data:  id,title,year,genre1|genre2|... (1 or more genre)
- blank line
- comment line beginning with '#' symbol. These may occur *anywhere* in the file, not just the start or end.

Blank lines and comment lines should be ignored. 
If any data line contains invalid movie data then log an error message:
```
Line 37: Unrecognized format "164179,Arrival,2016"
```
skip the erroneous line but continue processing the CSV file.


## What to Submit

Commit your work to your existing `movierental` repository on Github.
