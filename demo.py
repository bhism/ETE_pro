
from Pro_us_visa.logger import logging
from Pro_us_visa.exception import USvisaException
import sys


logging.info("started")

try:
    a = 2/0
except Exception as e:
    raise USvisaException(e,sys)