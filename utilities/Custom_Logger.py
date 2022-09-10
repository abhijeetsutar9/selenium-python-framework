import inspect
import logging

def customLogger(logLevel=logging.DEBUG):

    #Get name of the class/ method from where this method is called
    # loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(__name__)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a') # <loggerName> is string substitution that will be used to put the name of the logger
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger