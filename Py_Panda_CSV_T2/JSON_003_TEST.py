
'''
https://sparkbyexamples.com/python/convert-python-list-to-json/
'''

import json

# Below are the quick examples

# Example 1: Convert python list to JSON
numbers = [25, 36, 48, 54]
json_numbers = json.dumps(numbers)
print(json_numbers)

# Example 2: Convert python  string type list to JSON
technology = ["Hadoop", "Spark", "Python"]
json_string = json.dumps(technology)
print(json_string)

# Example 3: Convert list of dictionaries to JSON
my_dict = [{'course':'python','fee':4000}, {'duration':'60days', 'discount':1200}]
jsondict = json.dumps(my_dict)
print(jsondict)

# Example 4: Convert a list of lists to JSON
List = [[{'course':'python','fee':4000}], [{'duration':'60days', 'discount':1200}]]
jsonList = json.dumps(List)
print(jsonList)



# Syntax of json.dumps() function

print(     json.dumps(jsonList)  )

print('==========================================================================')


import json
# Convert python list to JSON
numbers = [25, 36, 48, 54]
json_numbers = json.dumps(numbers)
print(json_numbers)

# Output
# [25, 36, 48, 54]

import json
# Convert python string type list to JSON
technology = ["Hadoop", "Spark", "Python"]
json_string = json.dumps(technology)
print(json_string)

# Output
# ["Hadoop", "Spark", "Python"]



print('==========================================================================')

sampleDict = {
    "colorList": ["Red", "Green", "Blue"],
    "carTuple": ("BMW", "Audi", "range rover"),
    "sampleString": "pynative.com",
    "sampleInteger": 457,
    "sampleFloat": 225.48,
    "booleantrue": True,
    "booleanfalse": False,
    "nonevalue": None
}
print("Converting Python primitive types into JSON")
resultJSON = json.dumps(sampleDict)
print("Done converting Python primitive types into JSON")
print(resultJSON)


print('==========================================================================')

# assume you have the following dictionary
developer = {
    "name": "jane doe",
    "salary": 9000,
    "email": "JaneDoe@pynative.com"
}
print("Started writing JSON data into a file")
with open("developer.json", "w") as write_file:
    json.dump(developer, write_file) # encode dict into JSON
print("Done writing JSON data into .json file")

print('==========================================================================')

developer_dict = {
    "name": "jane doe",
    "salary": 9000,
    "skills": ["Raspberry pi", "Machine Learning", "Web Development"],
    "companies": ["Google", "Facebook", "IBM"],
    "email": "JaneDoe@pynative.com"
}

print("Started writing compact JSON data into a file")
with open("developerDetailCompact.json", "w") as write_file:
    json.dump(developer_dict, write_file, separators=(',', ':'))
print("Done writing compact JSON data into json file")