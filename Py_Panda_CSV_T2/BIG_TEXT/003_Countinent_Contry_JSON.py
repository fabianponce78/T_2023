'''
Created on Mar 30, 2023

@author: fponce
'''
import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    
    # create a dictionary
    data = {}
    
    # Open a csv reader called DictReader
    #with open(csvFilePath, encoding='utf-8') as csvf:
    with open(csvFilePath) as csvf:
        csvReader = csv.DictReader(csvf)
        
        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            
            # Assuming a column named 'No' to
            # be the primary key
            #key = rows['No']
            key = rows['continent']
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    
    
    print('----')
    print(data)
    print('----')

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        #jsonf.write(json.dumps(data, indent=4))
        j = json.dumps(data, indent=4)
        print(j)
        jsonf.write(j)

        
# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'archive/countryContinent.csv'
jsonFilePath = r'archive/countryContinent.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
