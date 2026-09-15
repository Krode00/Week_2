import csv
import logging
import os
from pathlib import Path

def validate_Student_data_csv():
    # 1. Check that the file exists
    file = Path('Student_data.csv')
    if not file.exists():
        return False, print("File not found.")
    

# 1. Setup the error log file
#logging.basicConfig(
    #filename='validation_errors.log',
    #level=logging.WARNING,
    #format='%(asctime)s - %(levelname)s - %(message)s',
    #filemode='w'  # 'w' resets the log file every run. Use 'a' to keep appending.
#)

#def log_csv_errors(file_path):
    #if not os.path.exists(file_path):
        #print(f"Error: File '{file_path}' not found.")
        #return

    #print("Scanning CSV for validation errors...")
    #error_count = 0

    #try:
        #with open(file_path, mode='r', encoding='utf-8') as file:
            # DictReader maps row headers to keys automatically
            #reader = csv.DictReader(file)
            
            # Start counting at row 2 because the header is row 1
            #for row_num, row in enumerate(reader, start=2):
                #row_errors = []

                # Rule 1: Check for valid or empty School_id(must be integer between 101 and 109)
                #school_id = row.get('School_id', '').strip()
                #if int not in school_id:
                    #row_errors.append(f"Missing 'school_id'")

                # Rule 2: Check for empty Name field
                #name = row.get('Name', '').strip()
                #if not name:
                    #row_errors.append("Missing or empty 'Name'")

                # Rule 3: Check for valid Gender (must be either Male or Female)
                #gender = row.get('Gender', '').strip()
                #if not gender :
                        #row_errors.append("Missing or empty 'Gender'")
                
                    

                # Rule 4: Check for valid Class (must be Integer between 0 and 10)
                #Class = row.get('Class', '').strip()
                #if int not in Class:
                    #row_errors.append(f"Invalid Class: '{Class}'")

                # Rule 5: Check for valid Grade (must be between A to F)
                #grade = row.get('Grade', '').strip()
                #if not grade :
                    #row_errors.append("Missing or empty 'Grade'")

                # Rule 6:  Check for empty address field
                #address = row.get('Address', '').strip()
                #if not address:
                    #row_errors.append("Missing or empty 'Address'")

                # Rule 7:  Check for valid semester(must be second)
                #semester = row.get('Semester', '').strip()
                #if not semester:
                    #row_errors.append("Missing or empty 'Semnester'")

                # Rule 8: Check for valid Subjects_offered(must be between 8 and 9)
                #subjects_offered = row.get('Subjects_offered', '').strip()
                #if int not in subjects_offered:
                    #row_errors.append(f"Invalid 'Subjects_offered'")    

                # If errors exist for this row, log them
                #if row_errors:
                    #error_count += 1
                    #error_message = f"Row {row_num} failed: {', '.join(row_errors)}"
                    #logging.warning(error_message)

        # Print simple console outcome statement
        #if error_count > 0:
            #print(f"Scan complete. Found {error_count} rows with errors. Check 'validation_errors.log' for details.")
        #else:
            #print("Scan complete. Zero errors found!")
            #pass

    #except csv.Error as e:
        #logging.critical(f"A system parsing error occurred while reading the file: {e}")
        #print("Critical CSV parsing error encountered. Check log for details.")

# Run the validation scan
#log_csv_errors('School_data.csv')

