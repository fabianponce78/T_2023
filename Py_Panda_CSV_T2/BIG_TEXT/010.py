'''
Created on Mar 30, 2023

@author: fponce
'''

'''
import os
import json
f = open(os.environ["HOME"] + "/archive/macos.json", "r", encoding="utf-8")
data = json.load(f)
f.close()
'''



import json

'''
f = open('archive/Test_Continent_Country2.json')
#f = open('archive/Test_Continent_Country.json')
data = json.load(f)
f.close()


print('    data => ', data  ,   '\n')
# Print the type of data variable
print("Type:", type(data))

for (k, v) in data.items():
    print("\t    Key: " + k)
    print("\t    Value: " + str(v))
'''    
    
print('###############################################')

    

# Opening JSON file
with open('archive/Test_Continent_Country.json') as json_file:
    print('type => 0 ' ,   type(json_file))
    print('') 
    data = json.load(json_file)
 
    # for reading nested data [0] represents
    # the index value of the list
    print('data => ',   data)
    print(type(data))
    print('type => 1 ' ,   type(data))
    print('') 
    
    for key, value in data.items():
        print('\t key   1    => '  , key)
        print('\t value 1    => ',   value)
        #print(key, value)     
    ###------------------------------------------------------------------------------
    for i in data['Continent']:
        print('\t -+- ', i)
        '''
        for i in data['country']:
            print('\t\t -+- ', i)
            '''
            
        for key, value in data.items():
            print('\t\t key => '    , key   )
            print('\t\t value => '  , value )
            #print('\t value => ',   value)
            #print(key, value)  
            data_2 = value
            for key, value in data_2.items():
                print('\t\t key   2    => '  , key)
                print('\t\t value 2    => ',   value)
    ###------------------------------------------------------------------------------    
    # Serializing json  
    #dictionary
    dic_2 = data
    print('\t type => 2 ' ,   type(dic_2))
    print('')
    
    
    
    '''
    json_object = json.dumps(dic_2, indent = 4)
    print('') 
    print('\t type => 3 ' ,   type(json_object))
    #print(json_object)
    '''
    
        
 
        



