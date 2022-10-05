---
title: Logging Practice
---

Create a directory named `logging` and copy (or write yourself) `logging_demo.py`.  



## Part 1: Practice Using Logging

These exercises use the `logging_demo.py` file.

1. In the file `logging_demo.py` complete the code for `log_demo(logger)`. 
   - Log a message using each of the 5 standard logging functions (debug, warning, info, error, critical).
   - For each log level, write a message that is a good example of what you would log at that level. *Write your own message, **not** something from the class presentation.*

2. Run the code without any configuration of loggers.  All the configuration code in the `__main__` block must be commented out.
   - which log messages are printed?
   - which log messages are **not** printed?
   - what is the format of the output?

3. In `__main__`, before calling `log_demo`, call basicConfig with the default values:
   ```python
   logging.basicConfig()
   ```
   Run the code.
   - which log messages are printed? 
   - did the format of the output change? how different?

4. Add a `level=...` parameter to the call to `basicConfig` to set the threshold log level to `logging.DEBUG`.
   Run the code again.
   - what is different?

5. Complete the `console_config` function. The function should set:
   - log threshold is WARNING
   - log format is "{datetime} {loglevelname}: {message}"
   - log output goes to the console (the default)
   Run it.  
   - How did the output change from previous case?

6. Complete the `file_config` function. The function should use basicConfig to:
   - log threshold is DEBUG
   - log format is "{datetime} {logger_name} {loglevelname} {functionName}: {message}"
   - functionName = name of function that logged the message
   - send log messages to the file `demo.log`
   - modify `__main__` to use `file_config` instead of `console_config`.
   Run the program.
   - Did it print any messages on the console? (should not)
   - Are messages logged to the file?

7. Run it again.  View the file `demo.log`.
   - Did the 2nd run **append** messages to the file or **overrite** the file contents?  (Usually you want to append messages.)

8. In `__main__` instead of using the root logger, create a logger named "demo".
   Rerun the code.  
   - Can you see any changes in the log messages?

Push your final code to Github.


## Part 2: Add Logging to `factor.py`

1. In `factor.py` replace "print" statements with suitable logging statements.
2. Log the exceptions in "main", including a stacktrace (`logger.exception`).
3. Create a function named `configure()` that configures the root logger so that all log messages all go to a file named `factor.log`.
4. Call `configure` from main.
5. Test your code -- all logging info should be saved in `factor.log` and no log messages cluttering the interactive console dialog.

Push your final `factor.py` to Github.


### Logging and Log Formats

- [Python Logging Howto](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)

- [Python Logging](https://docs.python.org/3/library/logging) complete documentation for logging, with links to tutorials & cookbook. Easy to understand after you read the Logging Howto.

- [Logging Formats](https://docs.python.org/3/library/logging.html#logrecord-attributes) section lists all the things you can include in the log message format.
