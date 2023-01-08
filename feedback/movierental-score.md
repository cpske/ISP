---
title: Scoring of Movie Rental Refactoring Problem
---

## Part 1

`Customer`

1. `get_total(self)` [or similar name] returns total rental price using rentals
   ```python
   def get_total(self):
       return sum(rental.get_price() for rental in self.rentals)
   ```
   - `statement` calls this method instead of computing total charg itself

2. `get_rental_points(self)` [or similar] returns total rental points
   ```python
   def get_rental_points(self):
       return sum(rental.get_rental_points() for rental in self.rentals)
   ```
   - `statement` calls this method instead of computing sum itself

3. `statement` creates & returns statement only.
   - no "if ... elif" statement using price code
   - calls `get_total` and `get_rental_points` once each **only**.

4. *Inline Temp Variable* in `statement` for amount (charge) and rental points.
   - calls `rental.get_charge` where it is needed and uses value w/o assignment to temp
   - calls `rental.get_rental_points` where it is needed and uses value w/o assignment to temp 

5. `PriceCode` is an enum or class hierarchy.
   - one PriceCode for each category of movie rental

6. Code Quality
   - Code is readable.
   - 1 pt: Correctly formatted, blank lines, no long lines or multi-statement lines.
     ```python
     # wrong
     REGULAR = {"price": lambda x: 1.5*x
   - 1 pt: Docstring on PriceCode enum or PriceStrategy class.

## Part 2

**All unit tests must pass for credit.**

**2 point each**
0. All tests pass.
   - no credit if multiple errors.
   - I correct 1 minor error and deduct points.

1. `Rental` has `price_code`, `get_price`, and `get_rental_points`
   - constructor has only 2 parameters: `movie` and `days_rented`
   - `get_rental_points` that invokes `price_code.get_rental_points(days)`
   - `get_rental_price` that invokes `price_code.get_price(days)`
   - uses logging for errors

2. `price_code_for_movie(movie)` method in Rental or top-level function in pricing.
   - `Rental` calls `price_code_for_movie` to determine `price_code`. 
   - `price_code` is in Rental, and not in Movie
  - **no** 2022 for this year.

3. `Movie` has attributes title, year, genres.
  - init(title, year, genres)
  - **no** `price code` in movie
  - **no** `get_price` or `get_rental_points` in Movie
  - `is_genre(genre: str) -> bool`

4. `MovieCatalog` (Factory)
   - reads movie data only once
   - a separate method to read data, not the constructor
   - ignores blank lines and lines starting with '#'
   - log errors using logging
   - is a Singleton

5. `MovieCatalog.get_movie(title [, year])` 
   - returns same Movie object for same query multiple times
   - always returns 1 Movie object or None


## Copying

### Khemissara
```python
class MovieCatalog:

    def __init__(self):
        self.movies = []

        with open("movies.csv") as file:
            movies = csv.reader("movies.csv")
            for movie in movies:
                if len(movie) == 4 and ("m" not in movie[0]):
                    movie_object = Movie(movie[1], int(movie[2]), movie[3].split("|"))
                    self.movies.append(movie_object)

    def get_movie(self, title, year):
        movies_title = [movie.title for movie in self.movies]
        if title not in movies_title:
            return []
        if year == 0:
            return [movie for movie in self.movies if movie.title == title][0]
        return [movie for movie in self.movies if (movie.title == title) and (movie.year == year)]
```

### Panitta
```python
class MovieCatalog:
    def __init__(self):
        self.movies = []
        with open('movies.csv') as csv_file:
            movies = csv.reader(csv_file, delimiter=',')
            for m in movies:
                if len(m) == 4 and ('#' not in m[0]):
                    mv_object = Movie(m[1], int(m[2]), m[3].split('|'))
                    self.movies.append(mv_object)
                else:
                    logging.warning(f'Unrecognized format "{m}"')

    def get_movie(self, title: str, year: int = 0):
        movies_name = [x.title for x in self.movies]
        if title not in movies_name:
            return []
        if year == 0:
            return [x for x in self.movies if x.title == title][0]
        return [x for x in self.movies if (x.title == title) and (x.year == year)]
```

### Ratthicha
```python
class MovieCatalog:

    def __init__(self):
        self.movie = []
        with open('movies.csv') as csv_file:
            movies = csv.reader(csv_file)
            for movie in movies:
                if len(movie) == 4 and '#' not in movie[0]:
                    movie_object = movie[0], movie[1], movie[2].split("|")
                    self.movie.append(movie_object)
                else:
                    pass

    def get_movie(self, title: str, year: int):
        name = [movie[1] for movie in self.movie]
        if year == 0:
            return [movie for movie in self.movie if movie[1] == title][0]
        if title not in name:
            return []
        return [movie for movie in self.movie if(movie[1] == title) and movie[2] == [year]]
```


