import pandas as pd
import csv

# Create a quick sample DataFrame to test it
df = {
    'Name': ['John', 'Sarah', 'Miriam'],
    'Grade': ['B', 'C', 'A']
}

#df = pd.DataFrame(Student_data.csv)
print("Pandas imported successfully!")
#print(df)

def validate_csv(Student_data):
    try:
        # 1. Try reading the file (catches structural/parser errors)
        # error_bad_lines=False will skip bad rows, but keeping it default (True) forces it to fail on bad structure
        df = pd.validate_csv(Student_data, error_bad_lines=True)
        
        # 2. Validate expected columns
        expected_columns = {'Name', 'Grade', 'Address'}
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
        
    #except pd.errors.ParserError as e:
       # return False, f"CSV parsing failed (likely formatting issue): {e}"

    except Exception as e:
        return False, f"An unexpected error occurred: {e}"






    


    