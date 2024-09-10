"""
Practice using Python's logging facility.

For details, see: https://docs.python.org/3/library/logging.html
"""
import logging


def log_demo(logger):
    """Log messages using each of the standard logging levels.

       :param logger: a logging.Logger object for log messages.
    """ 

    # TODO 1. write one example log message that uses each of these log levels.
    #  Your message indicates the sort of information you think should be
    #  logged at that level:
    #
    # logger.debug
    # logger.info
    # logger.warning
    # logger.error
    # logger.fatal

    pass   # To state the blazingly obvious -- you should remove this line. 


def console_config():
    """Configure logging for messages sent to the console.

    You should call this before creating any logging objects.
    You can call basicConfig only once. Subsequent calls have no effect.

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
    # call to basicConfig). See the reference for all field names.
    # FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    
    # TODO invoke logging.basicConfig to set logging options


def file_config():
    """Configure logging to a file.

    See: https://docs.python.org/3/library/logging.html#logrecord-attributes
    """
    # TODO specify a log file, threshold level, format, 
    #      and append mode so log files are not overwritten
    # Format should be: "time  logger_name  loglevelname funcName: log-message"
    pass


if __name__ == "__main__":
    # Configure the Logging facility by calling a method 
    # Exercises 3, 5-7

    # Log some messages to the root logger & observe the output.
    logger = logging.getLogger()

    print("Logging to ", str(logger))
    log_demo(logger)
