## Movie Rental Part 2


0. All unit tests pass.
   - MovieCatalog tests
   - Movie tests
   - Rental tests

1. `Rental` has 
   - `price_code` attribute
   - constructor takes only 2 args: `__init__(self, movie, days_rented)__`
   - constructor calls `get_price_for_movie` to get price code
   - `get_price()` delegates to `price_code`
   - `get_rental_price` delegates to `price_code`

2. `price_code_for_movie(movie)` method in Rental or top-level function in pricing.

3. `Movie` 
   - immutable
   - **only** attributes: title, year, genres
   - **no** `price_code`. `price_code` is in Rental    
   Tested using unit tests:
   - constructor:  `__init__(title, year, genres: Collection)`
   - `is_genre(genre: str) -> bool`. Case insensitive match:
     `movie.is_genre("Action") == movie.is_genre("action")` 
   Tested by inspection:
   - **no** `price code`
   - **no** `get_price` or `get_rental_points`

4. `MovieCatalog` (Factory)
   - reads movie data only once
   - a separate method to read data, not the constructor
   - ignores blank lines 
   - ignores lines starting with '#'
   - does **not** assume first line contains field names
   - log errors using logging

5. `MovieCatalog.get_movie(title [, year])` 
   - tested using unit tests
   - returns same Movie object for same query multiple times
   - always returns 1 Movie object or None

`MovieCatalog.load_movies` method (method name may vary)

| Penalty | Error                                  |
|---------|----------------------------------------|
|   -1    | E1 "movies.csv" is hardcoded in method that loads movies |
|   -2    | E2 blindly discards first line from file  |
|   -1    | E3 does not skip comment lines            |
|   -1    | E4 does not skip blank lines              |
|   -1    | E5 assume first line contains field names |
|   -1    | E6 does not use logging for errors        |
|   -1    | E7 reads movie data in constructor        |
|   -2    | E8 does not use try - except for errors   |
|   -1    | E9 try - except misses some data errors   |
|   -1    | E10 no class docstring in MovieCatalog    |
|  -ALL   | E11 rereads file each time search for movie! |
|   -1    | E12 other error, like misuse of try-except   |


## Bad Code

```python
    @classmethod
    def price_code_for_movie(cls, movie):
        if movie.year == datetime.now().year:
            return NEW_RELEASE

        if "Children" in movie.genre or "Childrens" in movie.genre:  
            # But if a tag has Children in it but is not a children movie then it would be wrong
            return CHILDREN

        return REGULAR
```

What's Wrong? 

1. Inappropriate Intimacy: directly accessing `genre` attribute of movie instead of calling `movie.is_genre("children")`
2. *Don't Fall for the Quick Hack*. He **deliberately** left a potential error in the code.
3. Case dependent match: "Children", "Childrens".


Bad Code #2:

```python
def __load_movies(self, filename: str):
    """Load movies from the CSV file."""
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # reading line by line
        next(reader)   <---------- WHAT IS THIS?   Cludge. Hack.
        for line_num, movie_data in enumerate(reader):
            try:
                movie = Movie(
                        movie_data['title'],
                        int(movie_data['year']),
                        movie_data['genres'].split('|')
                )
                self._movies.append(movie)
            except (TypeError, ValueError):
                format_msg = ",".join(
                        str(value) for key, value in movie_data.items()
                        if key != 'id' and value is not None)
                logging.error('Line %d: Unrecognized format "%s"',
                              line_num + 1, format_msg)
                continue
```

Violations:
- *Don't Fall for the Quick Hack*
- *Code Intently and Expressively*.
- 

What's Wrong?

1. **Assumes** first line contains field names 'title', 'year', 'genres'.
2. Discards first data line without looking at it (it was a movie!).
3. Does not understand how DictReader works. (the line you discarded was **not** the first line of file)
4. Does not understand how `for` loop works: unnecessary `continue`
5. Does not check for blank lines or comment lines anywhere in file.
6. Does not catch KeyError.


## Bad Code #4

```python
    def _load_movies_from_csv(self, filename: str):
        """Load movie from a CSV file"""
        try:
            with open(filename, newline='') as csvfile:
                movie_reader = csv.reader(csvfile)
                next(movie_reader)
                for row in movie_reader:
                    if len(row) != 4:
                        row = ','.join([data for data in row])
                    title = row[1]
                    try:
                        year = int(row[2])
                    except ValueError:
                        continue
                    genres = row[3:]
                    movie = Movie(title, year, genres)
                    self._movies.append(movie)
        except FileNotFoundError:
            print(f"File {filename} not found.")
```

Violates:
- *Report all exceptions*
- *Use Logging*
- *Put Angels on Your Shoulders* (test everything)

1. What happens if `len(row) != 4`?
2. Blindly discards first line.
3. `print` instead of logging.
4. Didn't test the code: `genres = row[3:]`

