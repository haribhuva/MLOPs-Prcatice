# code is to check the logging configuration

from src.logger import logging

logging.info("This is an debug message")
logging.info("This is an info message")
logging.warning("This is an warning message")
logging.error("This is an error message")
logging.critical("This is an critical message")