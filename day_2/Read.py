import csv

with open('Student_data.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)  # row is a list of strings, e.g., ['John', '30', 'New York']

    #for column in reader:
        #print(column)    # column is a list of strings, e.g., ['name', 'grade', 'address']
    

