## Movie Rental Part 2

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