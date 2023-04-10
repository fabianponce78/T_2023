'''
Created on Mar 30, 2023

@author: fponce
'''


import json

# Consider the json string with 5 key value pairs, where each value is a list
input_json_string = '{  "tutorial-1": ["subject1","subject2","subject3"],  \
                        "tutorial-2":  ["subject1","subject2","subject3"], \
                        "tutorial-3":  ["subject1","subject2","subject3"], \
                        "tutorial-4":  ["subject1","subject2","subject3"], \
                        "tutorial-5":  ["subject1","subject2","subject3"] }'

# Load input_json_string into a dictionary-loaded
loaded = json.loads(input_json_string)

print('loaded => ', loaded)

# Loop along dictionary keys
for iterator in loaded:
    print(iterator, ":", loaded[iterator])
    
print('//////////////////////////////////////////////////////////////////')    

#import json

# consider the json string with 2 string elements
# with 3 key-value pairs through a dictionary
input_json_string = '{"tutorial-1": {"subject1":"python",   \
                                     "subject2":"php",      \
                                     "subject3":"node.js"}, \
                      "tutorial-2": {"subject1":"java",     \
                                     "subject2":"android",  \
                                      "subject3":"css" } }'

# Load input_json_string into a dictionary-loaded
loaded = json.loads(input_json_string)

#Loop along dictionary keys
for iterator in loaded:
    print(iterator, ":", loaded[iterator])

print('//////////////////////////////////////////////////////////////////')


#import json

#load the json file
with open('archive/Test_Continent_Country2.json') as value:
    #load each element using load() function
    dictionary = json.load(value)

    #iterate the dictionary
    for iterator in dictionary:
        print(iterator, ":", dictionary[iterator])