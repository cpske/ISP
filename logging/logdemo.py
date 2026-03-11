"""
Example of Handlers, Formatters, and handler-specific logging threshold.
"""
import logging 


logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO)     # base threshold value 
# Create handlers
shandler = logging.StreamHandler()
shandler.setLevel(logging.WARNING)   # raise logging threshold 
fhandler = logging.FileHandler('demo.log') 
format1 = logging.Formatter('%(levelname)s: %(message)s') 
shandler.setFormatter(format1) 
format2 = logging.Formatter(
          '%(asctime)s %(funcName)s:%(levelname)s: %(message)s')
fhandler.setFormatter(format2) 
# Add handlers to the logger 
logger.addHandler(shandler)
logger.addHandler(fhandler)
# what will be logged to where? 
logger.debug('This is a debug message') 
logger.info('This is an info message') 
logger.warning('This is a warning message') 
logger.error('This is an error message')
