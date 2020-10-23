"""
Examples of using Python's logging facility.

Details of the design, classes, and methods are in 
the 'Logging' page of Python docs.
https://docs.python.org/3/library/logging.html
"""
import logging


def simple_config():
    """Configure logging using basicConfig for simple configuration.

    You should call this before creating logging objects.
    Call basicConfig only once. 
    Some attributes you can set are:
        filename = (creates a FileHandler and uses it)
        stream = (name of a StreamHandler to use), cannot use with filename=
        filemode = 'a' (append mode), 'w' (truncate & open for writing)
        level = set the root logger level

    See: 
        help(logging.basicConfig)
        https://docs.python.org/3/library/logging.html#logging.basicConfig
    """
    # custom format of log messages
    FORMAT = '%(asctime)s %(name)s %(levelname)s: %(message)s'
    # use a FileHandler for log messages
    logging.basicConfig(format=FORMAT)


def configure():
    """Configure loggers and log handlers."""
    # write all messages to a file.
    # For a real app, use a configurable absolute path to log file.
    filehandler = logging.FileHandler("demo.log")
    filehandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
    filehandler.setFormatter(formatter)
    # add handler to root logger
    root = logging.getLogger()
    root.setLevel(logging.NOTSET)
    root.addHandler(filehandler)
    # Define a console handler for messages of level WARNING or higher
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    formatter = logging.Formatter(fmt="%(levelname)-8s %(name)s: %(message)s")
    console_handler.setFormatter(formatter)
    root.addHandler( console_handler )


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


if __name__ == "__main__":
    # Configure the logging using one of these choices, or none:
    # 1. Call basicConfig with the defaults
    logging.basicConfig()

    # 2. Use simple_config for slightly more detailed configuration
    #    It invokes basicConfig() so you should comment out the above 
    #    call to basicConfig()
    # simple_config()

    # 3. configure() lets you configure logging in more detail.
    #    You should comment out the above calls if you use this.
    # configure() 

    # Log some messages using different logging levels.
    logger = logging.getLogger()
    print("Logging to ", str(logger))
    log_test(logger)
