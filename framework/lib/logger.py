"""
*************************************************************************
@Purpose :: This module is an API to connect remote Linux host and get the repsonse

@Author         ::

@revision History

@DATE [ DD/MM/YYYY]               @Name                   @Remarks

30-10-2022                       winteck                 This module is to generate log files
"""

import logging
import os
import sys
import re
import time
from logging.handlers import TimedRotatingFileHandler

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/logs"

FORMATTER = logging.Formatter("%(asctime)s %(levelname)s %(filename)s'' %(funcName)s %(lineno)s :: %(message)s")

#out = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
dd = time.strftime("%Y-%m-%d")
LOG_FILE = "{}/".format(path) + dd

def mkdir_p(path):
    """
    Method: to create log dir
    :param path: path of log dir
    :return: None
    """
    if not os.path.exists(path):
        os.makedirs(path)

def get_console_handler():
    """
    Method :to get console handler
    :return: console handler
    """
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler(arg1):
    """
    Method: to get file handler
    :return: return file handler
    """
    temp1 = LOG_FILE + "_" + arg1
    mkdir_p(temp1)
    temp = os.path.basename(temp1)
    import re
    temp = re.sub("^\d{4}\d{2}\d{2}_", "", temp)
    out = os.environ.get('PYTEST_CURRENT_TEST', "a:b").split(':')[-1].split(' ')[0]
    if out == None:
        out = ""
    #print("DEBUG pytest", out)
    file_handler = TimedRotatingFileHandler(temp1 + "/" + temp + ".log", when="H", interval=48)
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name, arg1=""):
    """
    Method: to get logger
    :param logger_name: Logger name
    :return: logger

    Usage:
    logger = logger.get_logger(_name_)
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG) #better to have too much log than not enough
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler(arg1))
    logger.propagate = False
    return logger

def get_logname():
    """
    Method: to get the log name file name
    :return: log name

    Usage:
    logger.get_logname()
    """
    return LOG_FILE

def get_logpath():
    """
    Method: to get log path
    :return: log path
    Usage:
    logger.get_logpath()
    """
    return path