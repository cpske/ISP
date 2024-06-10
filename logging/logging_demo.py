"""
Examples of using Python's logging facility.

Run this file in Python and observe:
Which messages are actually printed on the console or to a file?
What information is in the message?

For details, see: https://docs.python.org/3/library/logging.html
"""
import logging

def logging_test(logger):
    """Log messages using each of the standard logging levels.
       :param logger: a logging.Logger object for log messages.
    """ 

    # TODO write a log message that uses each of these log levels,
    #  and your message indicates the sort of information you would
    #  log at that level:
    #
    # debug
    # info
    # warning
    # error
    # critical or fatal
    pass


def console_config():
    """Configure logging for messages sent to the console.

    You should call this before creating any logging objects.
    You can call basicConfig only once.   Subsequent calls have no effect.

    named attributes you can set using basicConfig are:

    filename = name of a file to send log messages to
    filemode = 'a' (append), 'w' (truncate & open for writing)
    format = a string describing format of log messages
    stream = name of a StreamHandler to use, cannot use with filename attribute
    level = the threshold level for log messages

    See:  help(logging.basicConfig)
    Ref:  https://docs.python.org/3/library/logging.html#logging.basicConfig
    Ref:  https://docs.python.org/3/library/logging.html#logrecord-attributes
    """
    # define a custom format for log messages (use it in your
    # call to basicConfig)
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    #TODO use logging.basicConfig to set logging options


def file_config():
    """Configure logging to a file.

    See: https://docs.python.org/3/library/logging.html#logrecord-attributes
    """
    # TODO specify a log file, threshold level, format, 
    #      and append mode so log files are not overwritten
    # Format should be: "time  logger_name  loglevelname funcName: log-message"
    pass


if __name__ == "__main__":
    #
    # TODO Configure logging using one of these choices:

    # Call basicConfig with the default settings
    #logging.basicConfig()

    # Call basicConfig with a threshold logging level
    #logging.basicConfig(level=logging.ERROR)  -- fix this

    # Instead of the above, call your own config function:
    # console_config()
    #
    # or:
    # file_config()
    
    # After configuring logging, 
    # Log some messages to the root logger & observe the output.
    logger = logging.getLogger()
    print("Logging to ", str(logger))
    logging_test(logger)

    #TODO (last exercise) create a logger named "demo" instead
    # of the root logger.

