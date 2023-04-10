'''
Created on Mar 30, 2023

@author: fponce
'''


import json

'''
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
'''
# Python program to read
# json file



print('//////////////////////////////')


json_str = '{"id": 12345, "person":  {"name":  "John Smith"}}'
        
data = json.loads(json_str)


print(  data    )
print(  data["person"]    )
print(f'Name: {data["person"]["name"]}')


print('********************************************************************************************')
print('********************************************************************************************') 

# Opening JSON file
f = open('archive/Test_Continent_Country.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
print('\t data =>    ', data)

print('********************************************************************************************')
for i in data:
    print(i)
print('********************************************************************************************')    

for i in data['Continent']:
    print(i)
    #print(i).['country']
    
    
    #i_fields = i["country"]
    #print('---', i_fields)
    '''
            i_fields = i["fields"]
        dict_fields = json.dumps(i_fields)
        #print('\nobjectJson to dictionary :\n\t', dict_fields)
    '''
    

# Closing file
f.close()
