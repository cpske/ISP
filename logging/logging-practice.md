---
title: Logging Practice
---

Create a directory named `logging` and copy (or write yourself) `demo_log.py`.  

Download URL:  https://cpske.github.io/ISP/logging/demo_log.py

`demo_log.py` has these functions:

```python
def log_test(logger):
    """ Log messages using each of the standard logging levels, plus 1 custom.

    Which messages are actually printed on the console or to a file?
    """    
    logger.debug("This is a debug message for developers")
    logger.info("This is an info message")
    logger.warning("You have been warned")
    level = logging.WARN + 5   # more severe than WARN, but less than ERROR
    logger.log(level, "Custom message level = "+str(level))
    logger.error("This is an error message")
    logger.critical("A CRITICAL problem")
```

```python
def simple_config():
    """Configure logging using basicConfig for simple configuration.

    Use this to set log format, threshold log level, and more.
    You should call basicConfig only once.
    See: help(logging.basicConfig)
    """
    # custom format of log messages
    FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
    # use a FileHandler for log messages
    logging.basicConfig(format=FORMAT)
```

Main shows 3 ways to initialize logging.  Uncomment **only 1** or **none** of them.
```python
if __name__ == "__main__":
    # 1. call basicConfig first to set defaults
    logging.basicConfig()

    # 2. For more detailed configuration, call simple_config()
    # simple_config()

    # 3. More complex configuration, call configure()
    # configure()

    # Log some messages:
    logger = logging.getLogger()
    print("Logging to ", str(logger))
    log_test(logger)
```

## Exercises

1. Try logging using the default configuration (`basicConfig`). 
   * Run the file using Python.
   * Which messages are printed?
   * Note the format

2. Comment out the call to `basicConfig` and uncomment the line to call `simple_config()`.
   * Run again
   * Any differences?

3. Edit simple_config() and specify a threshold (minimum) log severity:
   ```python
    logging.basicConfig(format=FORMAT, level=logging.DEBUG)
   ```
   * Run again and note the differences.

4. In main, create a **named logger** instead of the root logger:
   ```python
   logger = logging.getLogger('mylogger')
   ```
   * Run again.
   * Any differences.
   * In actual code, use the package, module, or class name as logger name.
   
5. Log to a file. Again edit `simple_config` and set:
    ```python
    logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename="demo.log")
    ```
    * Run again.
    * Did it create a file `demo.log`?  What's in the file?
    * If you run again, does it **overwrite** the file or **append** to the file?


1. Try logging using default configuration.  Create a function named `log_test(logger)` that logs a message to each log level. Use any message you like, this is just an example:
    Write a `main` block to create a root logger and a named logger, and call log_test for each one:
    ```python
    # root logger
    logger = logging.getLogger()  
    print("Logging to ", logger)
    log_test(logger)
    # named logger. 
    # The logger name is fully-qualified module or package name.
    foo_log = logging.getLogger('foo')
    print("Logging to ", foo_log)
    log_test(foo_log)
    ```
    * which log messages are printed?
    * Looking only at the log messages, can you tell which log messages were created by which logger?

2. Change the *threshold* level for the root logger to INFO and foo logger to DEBUG and run again:
    ```python
    # root logger
    logger = logging.getLogger()
    logger.setLevel( logging.INFO )  # added code
    log_test(logger)
    # a named logger
    foo_log = logging.getLogger('foo')
    foo_log.setLevel( logging.DEBUG ) # added code
    log_test(foo_log)
    ```
    * Did the root logger print INFO messages?  Did foo print DEBUG messages?
    * Did *anything* change?
    * Hint: *If you don't configure any "handlers" for your loggers then Python
       uses a default handler which cannot be modified.*

3. To explicitly add a "handler" to loggers, call the ugly, static `basicConfig` method
   before getting the loggers:
   ```python
   logging.basicConfig() # uses default values for all parameters
   # root logger
   logger = logging.getLogger()
   logger.setLevel( logging.INFO )
   log_test(logger)
   ...etc...
   ```
   * Now, does root logger print INFO messages?  Does foo logger print DEBUG messages?
   * The log format changed.  Is this a useful, readable log format?

4. Change the log format that `basicConfig` applies to all loggers:
    ```python
    logging.basicConfig(
        format='%(asctime)s %(name)s %(levelname)s: %(message)s'
    )   
    # root logger
   logger = logging.getLogger()
   logger.setLevel( logging.INFO )
   log_test(logger)
   etc.
   ```
   * Does it print the logging levels you'd expect?
   * Is this log format easier to read?  Can you easily identify the source of messages?

5. Comment out the static `basicConfig` and instead define 2 handlers for the root logger: (1) a handler that logs *everything* to a file with timestamp, (2) a handler that prints warnings and more serious messages to the console, without timestamp.  Since this is a lot of code, put it in a function named `configure()`:
    ```python
    def configure():
        """Configure loggers and log handlers"""
        # write all messages to a file.
        # For a real app, use a configurable absolute path to log file.
        filehandler = logging.FileHandler("demo.log")
        filehandler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
                 '%(asctime)s %(name)s %(levelname)s: %(message)s' )
        filehandler.setFormatter(formatter)
        # add handler to root logger
        root = logging.getLogger()
        root.addHandler(filehandler)
        # Define a console handler for messages of level WARNING or higher
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        formatter = logging.Formatter(fmt="%(levelname)-8s %(name)s: %(message)s")
        console_handler.setFormatter(formatter)
        root.addHandler( console_handler )
    ```
    And in the main block, comment out both `basicConfig` and the `logger.setLevel()` calls.  Instead, call `configure()`.
    ```python
    # main block
    #logging.basicConfig( format='...' )
    configure()
    logger = logging.getLogger()
    #logger.setLevel(logging.INFO)  Don't set logging threshold
    print("Logging to ", logger)
    log_test(logger)
    etc.
    ```
    * Does it log WARNING and above to console?  Is the format correct?
    * Does it log DEBUG, INFO, and everything to the log file you specified?

6. In previous problem, you probably observed that not everything was being logged to the filehandler.  That's because each logger has its own *logging threshold* that is applied *before* the messages are sent to handlers.  So, the logger's own *logging threshold* may filter out messages.    
    This is non-intuitive, so remember it: both the logger and handlers have their own thresholds and filters.
    To stop the root logger from filtering messages, set its log level to NOTSET:
    ```python
    def configure():
        ...
        root = logging.getLogger()
        root.setLevel( logging.NOTSET )
        ...
    ```
    * Rerun the file.  Are all messages recorded in the log file?

7. What if we call `foo_log.setLevel(level)` after configuring log handlers?  Which log level will be used?  In the main block, change the log level on `foo` to ERROR:
    ```python
    foo_log = logging.getLogger('foo')
    foo_log.setLevel( logging.ERROR )
    print("Logging to ", foo_log)
    log_test(foo_log)
    ```
    * Rerun the file.  Does `foo_log` now filter out messages from both logs?


"""
