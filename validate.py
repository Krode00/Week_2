#from pathlib import Path
from pathlib import Path
import pandas as pd  
import csv


def validate_Student_data_csv():
    # 1. Check that the file exists
    file = Path('Student_data.csv')

    if not file.exists():
        return False, print("File not found.")

    
    if file.suffix != '.csv':
        return False, print("Invalid file format. Please provide a CSV file.")
    if file.stat().st_size == 0:
        return False, print("CSV file is empty.")

    try:
        print("Reading CSV file...")
        df = pd.read_csv('Student_data.csv')
        print("CSV file read successfully!")

        if df.empty:
            return False, print("CSV file is empty.")
        elif df.shape[1] < 2:
            return False, print("CSV file has insufficient columns.")
        
    except Exception as e:
        return False, f"Error reading CSV file: {e}"

    # 2. Validate expected columns
    expected_columns = {'School_id', 'Name', 'Gender', 'Class', 'Grade', 'Address', 'Semester', 'Subject_offered'}
    print("Validating expected columns...")
    if not expected_columns.issubset(df.columns):
        missing = expected_columns - set(df.columns)
        return False, f"Missing required columns: {missing}"
    
    if not expected_columns.issubset(df.columns):
        missing = expected_columns - set(df.columns)
        return False, f"Missing required columns: {missing}"

    # 3. Check for completely empty rows and drop them
    df.dropna(how='all', inplace=True)

    # 4. Validate Data Types / Missing Values
    if df['Name'].isnull().any():
        return False, "Validation Error: 'Name' column contains missing values."

    if not pd.to_numeric(df['Grade'], errors='coerce').notnull().all():
        return False, "Validation Error: 'Grade' column contains non-numeric data."

    return True, "CSV file is structurally valid."

valid, message = validate_Student_data_csv()
print(message)
