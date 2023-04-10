'''
Created on Mar 30, 2023

@author: fponce
'''

import json
import random
import pandas as pd
import time


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
        print('\t value 3 type   => ',   type(value)    )
        
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
def fn_110_Continent():
    print('______________________ fn_110_Continent')
    
    # Create. List Continent
    Lst_Continent = []
          
    with open('archive/Test_Continent_Country.json') as json_file:
        data = json.load(json_file)
     
        # for reading nested data [0] represents
        # the index value of the list
        #print('data => ',   data)
        #print('type => 1 ' ,   type(data))
        #print('') 
        
        for i in data['Continent']:
            #print('\t key   1    => '  , key)
            #print('\t value 1    => ',   value)
            #print(key, value)     
            #fn_001_Node(key, value)    
            print('\t - ',   i)   
            Lst_Continent.append(i)    # append. Continent      
    
    print('\t Lst_Continent = ', Lst_Continent  )
############################################################################################################################################
############################################################################################################################################
def fn_110(i):
    print('______________________ fn_110')           
    print(i) 

    with open('archive/Test_Continent_Country.json') as json_file:
        data = json.load(json_file)
     
        # for reading nested data [0] represents
        # the index value of the list
        #print('data => ',   data)
        #print('type => 1 ' ,   type(data))
        #print('') 
        
        for i in data['Continent']:
            #print('\t key   1    => '  , key)
            #print('\t value 1    => ',   value)
            #print(key, value)     
            #fn_001_Node(key, value)    
            print('\t - ',   i)
############################################################################################################################################
############################################################################################################################################
def fn_100():
    print('______________________ fn_100')
    

    fn_110_Continent()
    
    '''
    i = 0
    for x in range(0,5):
        i+=1
        #print(x,i)
        fn_110(i)
        '''
    
############################################################################################################################################
############################################################################################################################################    
def fn_250_Materials():
    #print('______________________ fn_250_Materials')

    Lst_BUILDING_MATERIALS = ['BUILDING MATERIALS', 'brick', 'cement', 'concrete', 'glass', 'gravel', 'marble', 'metal', 'plastic', 'sand', 'slate', 'stone', 'wood']
    
    Lst_FABRICS = ['FABRICS','cloth','cotton','lace','leather','linen','man-made fibres','nylon','polyester','silk','wool']
    
    Lst_METALS = ['METALS','aluminium','brass','bronze','copper','gold','iron','lead','magnesium','mercury','nickel','platinum','silver','steel','tin','uranium','zinc','alloy','GASES','carbon dioxide','helium','hydrogen','nitrogen','oxygen']
    
    Lst_OTHER_MATERIALS = ['OTHER MATERIALS','charcoal','coal','gas','oil','paraffin','petrol','asbestos','ash','cardboard','chalk','clay','dust','fibreglass','mud','paper','rubber','smoke','soil','ice','steam','water']
    
    Materials_dict = {
    'Lst_BUILDING_MATERIALS':Lst_BUILDING_MATERIALS ,
    'Lst_FABRICS':Lst_FABRICS ,
    'Lst_METALS':Lst_METALS ,
    'Lst_OTHER_MATERIALS':Lst_OTHER_MATERIALS ,
    }
    
    # ✅ get random key-value pair from dictionary
    key, value = random.choice(list(Materials_dict.items()))
    #print('\t -->> ', key, value)  # 👉️ 
    #print('\t -->> ', random.choice(value)    )       #Choose a random item from a sequence
    
    Str_Materials = key
    Str_Product = random.choice(value)
    #print('')
    #print('\t -->> 👉️ ', Str_Materials, '|' , Str_Product)  #
    #print('    ☢ ☣ ☪        ')
    return Str_Materials, Str_Product
    
    
        
############################################################################################################################################
############################################################################################################################################    
def fn_240_date():
    #print('______________________ fn_240_date')     

    from datetime import datetime

    start   = datetime.strptime('1/1/2000 1:30 PM', '%m/%d/%Y %I:%M %p')
    end     = datetime.strptime('1/1/2022 4:50 AM', '%m/%d/%Y %I:%M %p')

    random_date = start + (end - start) * random.random()
    random_date = random_date.strftime("%Y/%m/%d")
    
    #print('-' , random_date)
    return random_date
    
    
    
############################################################################################################################################
############################################################################################################################################
def fn_230_Product():   
    #print('______________________ fn_230_Product') 
    lst_Products_1 = ['Gold', 'Beans', 'Jewelry', 'safflower', 'seeds', 'Palm oil']
    lst_Products_2 = ['Corn', 'Silver ', 'Cocoa beans', 'Rice', 'Meat', 'fish']
    lst_Products_3 = ['Coffee', 'Antibiotics ', 'Cocoa beans', 'Bananas', 'T-shirts', 'Jerseys']
    lst_Products_4 = ['pullovers ', 'Alcohol  ', 'Provitamins', 'Caps', 'Sugar ', 'Chocolate', 'Diamonds']
    
    lst_Products_5 = ['pullovers ', 'Alcohol  ', 'Provitamins', 'Caps', 'Sugar ', 'Chocolate', 'Diamonds'] ## For Test, Duplicate Values
    
    lst_Products_6 = ['aluminium ', 'bronze  ', 'copper', 'iron', 'magnesium ', 'mercury', 'uranium'] 
    
    
    lst_Prd = lst_Products_1    +   lst_Products_2 + lst_Products_3 + lst_Products_4 + lst_Products_5 + lst_Products_6
    
    #print ('lst_Prd = ' ,   lst_Prd)
    
    # Remove any duplicates from a List:    
    lst_Prd = list(dict.fromkeys(lst_Prd))
    
    #print ('lst_Prd = ' ,   lst_Prd )
    
    # using random.choice() to
    # get a random number
    random_Product = random.choice(lst_Prd)
    #print('random_Product = ', random_Product   )
    
    return random_Product
        
############################################################################################################################################
############################################################################################################################################
def fn_220_Continent(str_Continent, data):
    #print('______________________ fn_220_Continent')
    #print('str_Continent    = ', str_Continent)
    #print('data             = ', data)
    #print('type             = ', type(data) )
    #print('')
    
    #print('\t ///////////////////////////////////////////////////')
    for key, value in data.items():
        #print('\t .Continent: ' , str_Continent)
        #print('\t .key       => '  , key)
        #print('\t .value     => ',   value)    
        #print('\t .value  type   => ',   type(value)    )
        
        data_2 = value
        
        for key_2, value_2 in data_2.items():
            #print('\t key_2   2        => '  , key_2)
            #print('\t value_2 2        => ',   value_2)
            
            if key_2 == str_Continent:
                #print('\t ', key_2, '|', str_Continent)
                #print('\t key_2   2        => ' ,   key_2           )
                #print('\t value_2 2        => ' ,   value_2         )
                #print('\t value_2  type   => '  ,   type(value_2)   )
                
                lst_country = value_2["country"]
                
                #print('\t lst_country   => '  ,   lst_country   )
                str_Country  = random.choice(lst_country)
                #print('\t str_Country   => '  ,   str_Country   )
                
                return str_Country

############################################################################################################################################
############################################################################################################################################
def fn_210_Continent(data):
    #print('______________________ fn_210_Continent')
    #print(data)
    
    # Create. List Continent
    Lst_Continent = []    
    
    for i in data['Continent']:
        #print('\t key   1    => '  , key)
        #print('\t value 1    => ',   value)
        #print(key, value)     
        #fn_001_Node(key, value)    
        
        #print('\t - ',   i)    
        Lst_Continent.append(i)    # append. Continent      
    
    #print('\t Lst_Continent = ', Lst_Continent  )
    
    return Lst_Continent        
          
          
############################################################################################################################################
############################################################################################################################################
def fn_200_Open_Json():
    #print('______________________ fn_200_Open_Json')
    
    # Opening JSON file
    Str_FileName = 'archive/Test_Continent_Country.json'
    f = open(Str_FileName,)
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    #print(' data => ', data)
    #print(' type => ', type(data)   )
    # Closing file
    f.close()
    return data

############################################################################################################################################
############################################################################################################################################
def main():
    
    # -------------------------------------------
    # get the start time
    st = time.time()
    # -------------------------------------------
        
    #fn_000()
    #fn_100()
    
    # Read Json file, assign into data
    data = fn_200_Open_Json()                           #######    fn_200_Open_Json
    #print(' data => ', data)
    
    #Get List of Continent
    Lst_Continent = fn_210_Continent(data)              #######    fn_210_Continent
    #print('Lst_Continent = ', Lst_Continent  )
    print('')
    
    
    ### Generate random item from a list    
    i = 0
    for x in range(0,100):
        i+=1
        #print(x,i)
        # using random.choice() to
        # get a random number
        str_Continent = random.choice(Lst_Continent)
        #print('str_Continent = ', str_Continent)
        #fn_220_Continent(str_Continent, data)                       #######    fn_220_Continent
        str_Country = fn_220_Continent(str_Continent, data)          #######    fn_220_Continent
        
        str_Product = fn_230_Product()                               #######    fn_230_Product
        
        Str_Date = fn_240_date()                                     #######    fn_240_date
        
        #Generate a Random Number
        n_Value = round(random.uniform(100.33, 5000.66), 2)        
        #print(n_Value)
        
        Str_Materials, Str_Product = fn_250_Materials()              #######    fn_250_Materials        
        #print(Str_Materials, Str_Product)
        
        print('\t\t... ', str_Continent, '|', str_Country, '|', str_Product, '|', Str_Date,  '|', Str_Materials,  '|', Str_Product, '|', n_Value)
        
    
    
    # -------------------------------------------
    # get the end time
    et = time.time()

    # get the execution time
    elapsed_time = et - st
    print('')
    print('\t Execution time:', elapsed_time, 'seconds')
    # -------------------------------------------
            

if __name__ == '__main__':
    main()      
        
 
        



