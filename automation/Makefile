# Makefile for the ancient unix build program.
#
# Run:
# make test  - run unit tests
# make lint  - run code checker
# make clean - remove python cache files

# Set PYTHON to the name of your python command (python or python3)
# For coverage, change python to "coverage run"
PYTHON=python3

# Let Python unittest module find and run tests itself
test:
	$(PYTHON) -m unittest discover -p "*_test.py"

# Run linter on code
lint:
	flake8 stats.py

# This is the Linux command to remove a directory
clean:
	/bin/rm -rf  __pycache__ 
