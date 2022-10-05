---
title: Logging Practice
---

Create a directory named `logging` and copy (or write yourself) `logging_demo.py`.  



## Exercises

1. In the file `logging_demo.py` complete the code for `log_demo(logger)`. 
   - Log a message using each of the 5 standard logging functions (debug, warning, info, error, critical).
   - For each log level, write a message that is a good example of what you would log at that level. *Write your own message, **not** something from the class presentation.*

2. Run the code without any configuration of loggers.  All the configuration code in the `__main__` block must be commented out.
   - which log messages are printed?
   - what is the format of the output?

3. In `__main__`, before calling `log_demo`, call basicConfig with the default values:
   ```python
   logging.basicConfig()
   ```
   Run the code.
   - which log messages are printed? which are **not** printed?
   - how did the format of the output change?

4. Add a `level=...` parameter to the call to `basicConfig` to set the threshold log level to DEBUG (`logging.DEBUG`).
   Run the code again.
   - What is different?

5. Complete the `console_config` function. The function should set:
   - log threshold is WARNING
   - log format is "{datetime} {loglevelname}: {message}"
   - log output goes to the console (the default)
   Run it.  How did the output change from previous case?

6. Complete the `file_config` function. The function should use basicConfig to:
   - log threshold is DEBUG
   - log format is "{datetime} {logger_name} {loglevel} {functionName}: {message}"
   - functionName = name of function that logged the message
   - send log messages to the file `demo.log`
   - modify `__main__` to use `file_config` instead of `console_config`.
   Run the program.
   - Did it print any messages on the console? (should not)
   - Are messages logged to file?

7. Run it again.  View the file `demo.log`.
   - Are there *two* sets of log messages (appended to file) or did new messages overwrite the old contents?

8. In `__main__` instead of using the root logger, create a logger named "demo".
   - Rerun the code.  Any changes in the log messages?

### Logging and Log Formats

- [Python Logging Howto](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)

- [Python Logging](https://docs.python.org/3/library/logging) complete documentation for logging, with links to tutorials & cookbook. Easy to understand after you read the Logging Howto.

- [Logging Formats](https://docs.python.org/3/library/logging.html#logrecord-attributes) section lists all the things you can include in the log message format.
