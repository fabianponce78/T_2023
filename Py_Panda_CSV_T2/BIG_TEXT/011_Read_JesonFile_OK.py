'''
Created on Mar 30, 2023

@author: fponce
'''

import json
import random


'''
    Read a Json file 
    
    use multiple foor loops to get the key and values
    
{'Continent': 
{
'Asia': {'xxx': 'TEST', 'country': ['Afghanistan', 'Qatar',  'United Arab Emirates', 'Uzbekistan', 'Viet Nam', 'Yemen']}, 
'Europe': {'xxx': 'TEST', 'country': ['Ã…land Islands', 'Albania', 'Andorra', 'Austria', 'Ukraine', 'United Kingdom of Great Britain and Northern Ireland']}, 
'Africa': {'xxx': 'TEST', 'country': ['Algeria', 'Angola',     'Niger', 'Nigeria',  'Western Sahara', 'Zambia', 'Zimbabwe']}, 
'Oceania': {'xxx': 'TEST', 'country': ['American Samoa',  'Tokelau', 'Tonga', 'Tuvalu', 'Vanuatu', 'Wallis and Futuna']}, 
'Americas': {'xxx': 'TEST', 'country': ['Anguilla', 'Antigua and Barbuda', 'Virgin Islands (British)', 'Virgin Islands (U.S.)']}
}
}    
    
'''
    
print('###############################################')

    

############################################################################################################################################
############################################################################################################################################    
def fn_002_Continent(key, value):
    print('______________________ fn_002_Continent')
    print('key     = ', key)
    print('value   = ', value)
    print('')      
    data = value
    print('data => ',   data)
    print(type(data))       

    for key, value in data.items():
        print('\t Continent:')
        print('\t key   3    => '  , key)
        print('\t value 3    => ',   value)  
        # using random.choice() to
        # get a random number
        random_value = random.choice(value)    
        print('\t Random country = ', random_value)          
############################################################################################################################################
############################################################################################################################################    
def fn_001_Node(key, value):
    print('______________________ fn_001_Node')
    print('key     = ', key)
    print('value   = ', value)
    print('')    
    data = value
    print('data => ',   data)
    print(type(data))    
    
    for key, value in data.items():
        print('\t Node:')
        print('\t key   2    => '  , key)
        print('\t value 2    => ',   value)
        fn_002_Continent(key, value)
    '''    
        
    for x in data:
        print(x)
    for x, y in data.items():
        print(x, '|', y)
    '''        
    
    
############################################################################################################################################
############################################################################################################################################    
def fn_000():
    print('______________________ fn_000')    
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
            fn_001_Node(key, value)
        ###------------------------------------------------------------------------------

        ###------------------------------------------------------------------------------    
        # Serializing json  
        #dictionary
        #dic_2 = data
        #print('\t type => 2 ' ,   type(dic_2))
        #print('')
        
        
        
        '''
        json_object = json.dumps(dic_2, indent = 4)
        print('') 
        print('\t type => 3 ' ,   type(json_object))
        #print(json_object)
        '''    
############################################################################################################################################
############################################################################################################################################
def main():
    fn_000()

if __name__ == '__main__':
    main()      
        
 
        



