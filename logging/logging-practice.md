---
title: Logging Practice
---


## Part 1: Add logging to `logging_demo`

These exercises use the `logging_demo.py` file.

1. Complete the code for function `log_demo(logger)`. 
   - Log one message using each of the 5 standard logging functions (debug, warning, info, error, critical or fatal).
   - For each log level, write a message that is a **good example** of what you would log at that level. 
   - *Write your own message, **not** something from the class presentation.*

2. Run the code (without any configuration of loggers).
   - which log messages are printed?
   - which log messages are **not** printed?

3. In `__main__`, invoke `basicConfig()` to initialize the logging facility, then call `log_demo`.
   - This causes `basicConfig` to use default values for all settings.
   - You must call this **before** any other logging calls, or it has no effect.
   ```python
   if __name__ == `__main__`:
       # basic config with default settings
       logging.basicConfig()

       logger = logging.getLogger()
       log_demo(logger)
   ```
   Run the code.
   - what changed?
   - what do the **fields** in the output messages mean?

4. Create a **named logger** instead the default (root) logger. In `__main__`:
   ```python
    logger = logging.getLogger("demo")
   ```
   Run the code.
   - how does the output change? 

5. In `__main__` add a `level=...` parameter to the call to `basicConfig` to set the threshold log level to `logging.DEBUG`.
   ```python
       logging.basicConfig(level=...)
   ```
   Run the code again.
   - what does `level=n` do?
   - what is the **datatype** of the level value? (int, str, something else?) 
   - Can you use `level=15`?  `level="DEBUG"`?

6. Complete the `console_config` function. The function should set:
   - log threshold is WARNING
   - log format is "{datetime} {loglevelname}: {message}"
   - log output goes to the console (the default)
   
   Modify main again:
   - **Remove** call to `basicConfig`.
   - Invoke `console_config` instead.

   Run it.  
   - How did the output change from previous case?

7. Complete the `file_config` function. The function should use basicConfig to:
   - set log threshold is DEBUG
   - log format is "{datetime} {logger_name} {loglevelname} {functionName}: {message}"   
   - functionName = name of function that logged the message
   - send log messages to a file named `demo.log`
   - modify `__main__` to invoke `file_config` **instead of** `console_config`.

   Run the program.
   - Did it print any messages on the console? (should not)
   - Are messages logged to the file?

8. If you run the code several times, what happens to the file `demo.log`?
   Does each run **append** messages to the file or **overrite** the old contents? 
   - Does this make sense?


Push your final code to Github Classroom.


### Logging and Log Formats

- [Python Logging Howto](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)

- [Python Logging](https://docs.python.org/3/library/logging) complete documentation for logging, with links to tutorials & cookbook. Easy to understand after you read the Logging Howto.

- [Logging Formats](https://docs.python.org/3/library/logging.html#logrecord-attributes) section lists all the things you can include in the log message format.
