'''
Created on Mar 30, 2023

@author: fponce
'''


import json

person_string = '{"name": "Bob", "languages": "English", "numbers": [2, 1.6, null]}'

# Getting dictionary
person_dict = json.loads(person_string)

# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 4, sort_keys=True))

print(person_dict.keys())


print('//////////////////////////////')


json_str = '{"id": 12345, "person":  {"name":  "John Smith"}}'
        
data = json.loads(json_str)


print(  data    )
print(  data["person"]    )
print(f'Name: {data["person"]["name"]}')

# output: Name: John Smith



print('//////////////////////////////')


#import json

with open('archive/Test_Continent_Country2.json') as file_object:
    data = json.load(file_object)

print(data)

'''
print('//////////////////////////////')


obj = {"Id": 12345, "Quantity": 1, "Price": 18.00}

json_str = json.dumps(obj, indent=4)
        
print(json_str)
'''
