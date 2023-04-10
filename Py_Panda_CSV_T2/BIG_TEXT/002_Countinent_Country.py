'''
Created on Mar 30, 2023

@author: fponce
'''



import csv

'''
    https://realpython.com/python-csv/
'''

'''
with open('archive/countryContinent.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
'''        

print('************************************************************************************')
'''
    To print a range of line, in this case from line 4 to 7
'''
with open('archive/countryContinent.csv') as csv_file:
    data = csv.reader(csv_file)
    #for row in list(data)[4:7]:
    for row in list(data)[0:3]:
        print(row)
    
print('************************************************************************************')
'''        
with open('archive/countryContinent.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} xxxx {row[1]} yyyy {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.') 
'''       