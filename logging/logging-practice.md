---
title: Logging Practice
---


Create a directory named `logging` and copy (or write yourself) `logging_demo.py`.  

Download URL:  <https://cpske.github.io/ISP/logging/logging_demo.py>

`logging_demo.py` has these functions:

```python
def logging_test(logger):
    """Log messages using each of the standard logging levels 
       plus 1 custom level.

    Run the file in Python and observe:
    Which messages are actually printed on the console or to a file?
    """ 
    # TODO write a log message using each of these log levels.
    #      Your message should be an example of the kind of thing you
    #      would log at that level.
    #      Example: logger.error("Unable to connect to database")
    # debug
    # info
    # warning
    # level = logging.WARN + 5 (custom log level between WARN and ERROR)
    # error
    # critical
    level = logging.WARN + 5 # custom log level between WARN and ERROR
    print("You forgot to write logging_test")
```

```python
def simple_config():
    """Configure logging using basicConfig for simple configuration.

    You can use basicConfig to set the log format, threshold log level, 
    output file, handlers, and more. You should call basicConfig only once.
    See: help(logging.basicConfig)
    """
    # custom format of log messages
    FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
    logging.basicConfig(format=FORMAT)


def my_config():
    """Write your own logging configuration."""
    pass
```

```python
if __name__ == "__main__":
    # 1. call basicConfig first (and only once) to set logging defaults
    logging.basicConfig()

    # 2. Instead of basicConfig, call simple_config() to set the log format
    #    You must comment out the above call to basicConfig().
    # simple_config()

    # 3. Define your own logging configuration.
    #    You must comment out the above calls to basicConfig & simple_config
    # my_config()

    # Log some messages:
    logger = logging.getLogger()
    print("Logging to ", str(logger))
    logging_test(logger)
```

## Exercises

1. Complete the code for `logging_test(logger)`. 
   - Write one suitable log message for each of the 5 standard log levels.
   - Write a log message using the custom log level `leval = logging.WARN + 5`

2. Run the code with only a call to `basicConfig()` in main (default configuration).
   - Notice the logging output format.
   - What is lowest severity log message that is printed?
   - Which of your log messages are **not** printed?

3. In the "main" block, comment out the call to `basicConfig` and instead invoke `simple_config`, which sets a custom message format.  Run the file again.
   - How does the log message format change?

4. Write your own configuration method named `my_config`. In "main", comment out the call to `simple_config` and instead call `my_config`.  In `my_config` set:
   - a threshold level for logging, using the `level=` named parameter
   - an output file for log message, using the `filename=` named parameter    
   ```python
   logging.basicConfig(format=..., level=..., filename="...")
   ```
   - Run the program again, and notice how the output changes. 

5. Run the program **a second time**.  Does the output *append* to the log file or *overwrite* the old log file?

6. In `my_config`, add the parameter `filemode='w'` (truncate and write). 
   - run the application at least 2 times
   - does it append to the output file or replace the output file each time?
   - In a real application, you normally want to append ('a') to the output; for development when there are a lot of debug messages, using 'w' makes the logs easier to read.

7. Suppose you have an application that's working, so now you only want to log messages of level WARN or higher.  But you have one module named "foo" that is still in development, so for that module only you would like to see all log messages.  How to do this?  Do the following:
   - in main, after you create the root logger set the threshold to WARN
   ```python
   # root logger
   logger = logging.getLogger()
   logger.setLevel(logging.WARN) 
   logging_test(logger)
   ```
   - after that, define a named logger "foo" and set its threshold to DEBUG
   ```
   # logging for the 'foo' module
   mylogger = logging.getLogger("foo")
   mylogger.setLevel(logging.DEBUG)  # log everything
   logging_test(mylogger)
   ```
   - Run the application.  Do you see different messages for the root and foo loggers?

In real code, we would not pass the logger as a parameter to a module.  
Each module creates its own logger as needed using `logger = logging.getLogger("name")`.  

`logging.getLogger(name)` always returns the same instance of each named Logger (they are Singletons), so we can pre-configure named loggers in a configuration function (such as setting the log threshold to DEBUG). Later on, the module can call `logging.getLogger("name")` and it will get the same pre-configured logger object.


### Logging and Log Formats

[Python Logging](https://docs.python.org/3/library/logging) docs page for details on using loggers.  Has links to some tutorials.

[Logging Formats](https://docs.python.org/3/library/logging.html#logrecord-attributes) section lists all the things you can include in the log message format.
