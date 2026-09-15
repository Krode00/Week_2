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

 # Rule 2: Check for valid Age (must be integer between 0 and 120)
                age_val = row.get('Age', '').strip()
                try:
                    age_int = int(age_val)
                    if not (0 <= age_int <= 120):
                        row_errors.append(f"Age out of range: {age_val}")
                except ValueError:
                    row_errors.append(f"Invalid age format (not an integer): '{age_val}'")









log_csv_errors('data.csv')


