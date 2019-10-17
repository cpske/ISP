## Code Coverage Assignment

Learn about [Code Coverage](/testing/code-coverage).
Then add code coverage analysis to your unittesting project.


1. Use the Python [coverage][coverage-docs] package to analyze
how well your fraction tests cover code in the Fraction class.
    * If coverage of the `fraction.py` code is less than 90% then improve
your tests.  You really want nearly 100% for this project.
    * If you have a "main" block in fraction.py, exclude it from the analysis using a `.coveragerc` file.
    * Add the .coveragerc file to your Git repo and push to Github.

2. Add the [CodeCov.io](https://codecov.io) service to your unittesting
project, and modify your `.travis.yml` file so that Travis runs coverage when testing you project, then uses Codecov to send the data to codecov.io.
   * Got to https://codecov.io, click the "Get Started" link, and follow instructions.  It is similar to the way you gave Travis-CI permission to pull your project.
   * You need to modify your `.travis.yml` file to make it work.
   * You must understand what is going on, not just copy someone else's .travis.yml file.

3. Add a CodeCov icon ("badge") to your project README.md to show the coverage result.
   * The "badge" should include a clickable link to your project on codecov.io


## Resources

* Python [Coverage Documentation][coverage-docs]
* [Introduction to Code Coverage][dzone-code-coverage] on DZone has example using Javascript and links to some popular code coverage tools.
* [CodeCov.io](https://codecov.io) online code coverage service.
* [Using CodeCov with Python and Travis-CI](https://medium.com/datadriveninvestor/beginners-guide-to-using-codecov-with-python-and-travis-ci-c17659bb711) short guide for beginners.

[coverage-docs]: https://coverage.readthedocs.io/ "coverage.py documentation"

[dzone-code-coverage]: https://dzone.com/articles/an-introduction-to-code-coverage "An Introduction to Code Coverage"

[jacoco]: https://www.eclemma.org/jacoco/


