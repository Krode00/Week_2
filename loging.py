import csv
import logging
import os

# 1. Setup the error log file
logging.basicConfig(
    filename='validation_errors.log',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'  # 'w' resets the log file every run. Use 'a' to keep appending.
)

def log_csv_errors(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    print("Scanning CSV for validation errors...")
    error_count = 0

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            # DictReader maps row headers to keys automatically
            reader = csv.DictReader(file)
            
            # Start counting at row 2 because the header is row 1
            for row_num, row in enumerate(reader, start=2):
                row_errors = []

                # Rule 1: Check for empty Name field
                name = row.get('Name', '').strip()
                if not name:
                    row_errors.append("Missing or empty 'Name'")

                # Rule 2: Check for valid Age (must be integer between 0 and 120)
                age_val = row.get('Age', '').strip()
                try:
                    age_int = int(age_val)
                    if not (0 <= age_int <= 120):
                        row_errors.append(f"Age out of range: {age_val}")
                except ValueError:
                    row_errors.append(f"Invalid age format (not an integer): '{age_val}'")

                # Rule 3: Check for valid Email format (must contain '@')
                email = row.get('Email', '').strip()
                if '@' not in email:
                    row_errors.append(f"Invalid email structure: '{email}'")

                # If errors exist for this row, log them
                if row_errors:
                    error_count += 1
                    error_message = f"Row {row_num} failed: {', '.join(row_errors)}"
                    logging.warning(error_message)

        # Print simple console outcome statement
        if error_count > 0:
            print(f"Scan complete. Found {error_count} rows with errors. Check 'validation_errors.log' for details.")
        else:
            print("Scan complete. Zero errors found!")

    except csv.Error as e:
        logging.critical(f"A system parsing error occurred while reading the file: {e}")
        print("Critical CSV parsing error encountered. Check log for details.")

# Run the validation scan
log_csv_errors('data.csv')

