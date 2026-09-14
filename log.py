#from pathlib import Path
#import pandas as pd
import csv 
import logging
import os


# 1. setup the error log file
logging.basicConfig(
    filename='validation_errors.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'  # 'w' resets the log file every run. Use 'a' to keep appending.
)


