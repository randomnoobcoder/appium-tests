import inspect
import logging


def customLogger():
    # Used to get the class/method name from where this customlogger is called
    logName = inspect.stack()[1][3]
    logger = logging.getLogger(logName)
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler(f'../logs/Test_logs', mode='w')
    fileHandler.setLevel(logging.DEBUG)
    logFormat = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %B')
    # logging.critical("This Critical message")
    fileHandler.setFormatter(logFormat)
    logger.addHandler(fileHandler)
    return logger
