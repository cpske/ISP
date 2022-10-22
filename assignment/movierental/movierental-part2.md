---
title: Movie Rental Refactoring Part 2
---

This is a continuation of the Movie Rental refactoring assignment.

These refactorings assume your code has the methods shown in the UML class diagrams at the end of [Movie Rental Part 1](movierental-part1#uml-class-diagram).

`Customer`, `Rental`, `Movie`, and `PriceCode` (alternate name: PriceStrategy) should have the methods shown in the UML diagram.

&nbsp;

## Assignment - More Refactorings

## 1. Refactor Rental Price and Rental Points

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

2.1 After the above refactoring, only `Rental` uses the price code.  Move it to Rental.

2.2 Write a justification for this refactoring:

- what *refactoring signs* (code smells) suggest it?
- what *design principle* suggests it?


### 3. Add Attributes to Movie

The revised Movie class has only a title. That's an **Anemic Class**. Add some useful features of real movies. 

Add:
* `year` - the year the movie was released
* `genre` - a **collection** *genre* names (strings), as a list or set.
* `is_genre(string)` returns true if the string parameter matches one of the movie's *genre*.  
* `__str__` returns "*Title* (year)" of the movie

Make Movie **immutable**. There is no reason for other classes to modify a Movie.

Making Movie immutable reduces the chance for errors, since multiple Rentals may use the same Movie instance.


### 4. Define a Factory for Movies

In the current code (after #3), someone creates a movie like this:
```
movie = new Movie("Mulan", 2020, ["Action","Adventure","Drama"])
```

That's a lot of data.  
- Where does the data come from?
- How does the class that *instantiates* a Movie get the data it needs?

Apply two design principles:

- Encapsulation - encapsulate and hide creation of Movie objects
- Separation of Concerns - the objects that *use* movies are separate from the objects that *create* movies

Define a factory class to create and access Movies, named `MovieCatalog`.

- MovieCatalog gets movie data from a CSV file (reference below).
- MovieCatalog is a *singleton*. We want only one instance of it.
- It has a `get_movie(title)` method that returns a movie with matching title.
- Try to be *efficient* - **don't** read the file every time `get_movie` is called!
- **No Credit** for a) code that reads the CSV file more than once, b) code that saves all the CSV data as strings (save Movies instead), c) code that tries to save the entire CSV data in memory while creating movies (process one line at a time).

Here's how the catalog will be used:
```python
catalog = MovieCatalog()
movie = catalog.get_movie("Mulan")
```

Some titles have more than one movie. `get_movie` should have an optional second parameter for the `year`.  If `year` is omitted, return the **newest** Movie matching the requested title.  Title must be an exact match, ignoring case.
```python
catalog = MovieCatalog()
old_movie = catalog.get_movie("Titanic", 1953)
new_movie = catalog.get_movie("Titanic")     # returns 1997 "Titanic" movie
```

**Programming Challenge**: use *lazy instantiation*. 

- instead of a method that creates all the movies at once, define a generator 
- a generator reads data from the CSV file and 'yields' a movie
- get_movie(title) first checks if the `title` matches the title of movies already in the catalog. If not, it calls the generator to read more data (and adds more movies to the catalog) until a matching title is found or end of data.
- assume that CSV data is sorted from newest to oldest movies


### 4. Define a Factory Method for Price Codes

How does the movie rental store assign a price code to a movie?

In the current code, the code that creates a rental must assign a price code, which means it has to know the price codes for all movies:

```python
movie = catalog.get_movie("Top Gun: Maverick")
days  = 4
price_code = PriceCode.NEW_RELEASE
rental = Rental(movie, days, price_code)
```

Define a method to automatically compute the price code for a movie.
The rules are:

- If the movie was released this year, it's a *New Release*
- Otherwise, if any of the movie's *genre* is "Childrens" or "Children's" than it's a "childrens" price code
- Otherwise it's a Regular movie

What class should provide this method? Apply some design principles:

- *Information Expert*: choose a class that already has most of the information needed to determine the price code
- *Low Coupling*: choose a class that is already coupled to the price codes
- *High Cohesion*: choose a class that is already responsible for price codes, or that closely uses the price codes

*Information Expert* suggest both Movie and PriceCode (or PriceStrategy).
But adding this method to Movie will couple Movie to the PriceCode, which it is not, and would violate the *Single Responsibility Principle*.

Adding the method to PriceCode (or PriceStrategy) has *high cohesion* but also adds coupling to Movie.

Adding the method to Rental also has *high cohesion* but if you use a `if ... elif ... elif` then it reduces polymorphism.

Which class does *Single Responsibility* suggest?

Define a **class method** named `code_for_movie(movie)` that returns a `PriceCode`.

The Rental object can determine its own price code, so we can simplify
creation of Rentals:

```python
catalog = MovieCatalog()
movie = catalog.get_movie("Mulan")
days_rented = 3
rental = Rental(movie, days_rented)
```

### Movie Rental Data

The data is in the file `movies.csv` in repository:

https://github.com/jbrucker/movierental

Each line contains one of these:
- movie data:  id,title,year,genre1|genre2|... (1 or more genre)
- blank line
- comment line beginning with '#' sympbol.

Blank lines and comment lines should be ignored.
If any data line contains invalid movie data then log an error message:
```
Line 37: Unrecognized format "164179,Arrival,2016"
```
in this example the *genre* field is missing
Lines beginning with a '#' symbol are comments and should be ignored.

## What to Submit

Commit your work to your existing `movierental` repository on Github.
