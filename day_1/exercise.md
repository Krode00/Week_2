I am creating a CLI - python style program that reads files, validates records, produces summary and also log records

APPROACH :I plan to structure this program into four main components: reading the CSV file, validating the data, logging any errors, and providing a summary of the validation results
I would create a csv file that contains student information with columns such as Name, Age, Grade, Address, and Email. The program will read this CSV file, validate each row against the defined schema, log any validation errors to a log file, and finally provide a summary of the validation results.
i would first create a function to validate the data in the csv fie , this function will validate for empty rows, missing columns and as well as validate the data types and formats of each field.
 For example, it will check if the Name and Address fields are not empty, , if the Grade is a valid letter grade (A-F), and if the subjects offered are valid. Any validation errors will be logged to a log file for further review.

after the validation process, I would create a read file that would read the csv file and display the table.
then after  the reading and validation process, I would create a function to log the validation errors to a log file and finally, I would create a summary function that would provide a summary of the validation results, including the number of valid rows, invalid rows, and any specific errors encountered during the validation process.




IMPORTANT DECISIONS : firstly, I tried to understand what the aim of the project was, possible problems and the direction to go.
I made sure to use the appropriate file that would be use to run this program
I tried to structure my program to be able to read inputs then validate, in which the valid records will be stored and the errors from the invalid ones will be logged  then i would summarize.


PROBLEMS ENCOUNTERED : how to import a csv file
empty files 
duplicate records
little data or columns

RESOURCES USED : Youtube, Google and W3schools

CHANGES : 




