'''
Created on Jan 23, 2023

@author: fponce
'''

import random


lst_Productos = ['almond' ,'apple' ,'apricot' ,'avocado' ,'banana' ,'blackberry' ,'blueberry' ,'cherry' ,'chestnut' ,'coconut' ,'grape' ,'grapefruit' ,'hazelnut' ,'lemon' ,'lime' ,'mango' ,'melon' ,'nectarine' ,'orange' ,'papaya' ,'peach' ,'peanut' ,'pear' ,'pineapple' ,'plum']

print('-- lst_Productos',   lst_Productos)

'''
print("-----------------------------------------------------------------")

dic_XXX =[
    {
        "id": 2,
        "name": "An ice sculpture",
        "price": 12.50,
        "tags": ["cold", "ice"],
        "dimensions": {
            "length": 7.0,
            "width": 12.0,
            "height": 9.5
        },
        "warehouseLocation": {
            "latitude": -78.75,
            "longitude": 20.4
        }
    },
    {
        "id": 3,
        "name": "A blue mouse",
        "price": 25.50,
        "dimensions": {
            "length": 3.1,
            "width": 1.0,
            "height": 1.0
        },
        "warehouseLocation": {
            "latitude": 54.4,
            "longitude": -32.7
        }
    }
]

print(dic_XXX)
'''




dic_XXX =[
    {
        "id": 1,
        "name": "almond",
        "price_1": 12.50,
        "price_N": [10,30],
        "Lower_Price": 10.01,
        "High_Price": 30.00
    },
    {
        "id": 2,
        "name": "apple",
        "price_1": 12.50,
        "price_N": [15,20],
        "Lower_Price": 15.20,
        "High_Price": 20.00
    },
    {
        "id": 3,
        "name": "apricot",
        "price_1": 12.50,
        "price_N": [10,30],
        "Lower_Price": 10.00,
        "High_Price": 30.00
    },
    {
        "id": 4,
        "name": "avocado",
        "price_1": 12.50,
        "price_N": [10,40],
        "Lower_Price": 10.00,
        "High_Price": 40.00
    },
    {
        "id": 5,
        "name": "banana",
        "price_1": 12.50,
        "price_N": [10,30],
        "Lower_Price": 10.00,
        "High_Price": 50.00
    },
    {
        "id": 6,
        "name": "blackberry",
        "price_1": 12.50,
        "price_N": [10,30],
        "Lower_Price": 10.00,
        "High_Price": 60.00
    },
    {
        "id": 7,
        "name": "cherry",
        "price_1": 12.50,
        "price_N": [10,30],
        "Lower_Price": 10.00,
        "High_Price": 70.00
    },
    {
        "id": 8,
        "name": "coconut",
        "price_1": 12.50,
        "price_N": [10,30],
        "Lower_Price": 10.00,
        "High_Price": 80.00
    },
    {
        "id": 9,
        "name": "grape",
        "price_1": 12.50,
        "price_N": [10,30],
        "Lower_Price": 10.00,
        "High_Price": 90.00
    },
    {
        "id": 10,
        "name": "lemon",
        "price_1": 12.50,
        "price_N": [10,30],
        "Lower_Price": 10.00,
        "High_Price": 100.00
    }           
]

print(dic_XXX)

print("-----------------------------------------------------------------")


N_Random = random.randint(1, 10)
print('N_Random', N_Random)
i = 0
for Str_Dic in dic_XXX:
    i+= 1    
    #print(i, ' -- ', Str_Dic)
    if i == N_Random:
        print(i, ' -- ', Str_Dic)
        print(i, ' -- ', Str_Dic["Lower_Price"])
        print(i, ' -- ', Str_Dic["High_Price"])
        Rand_Price = random.uniform(Str_Dic["Lower_Price"], Str_Dic["High_Price"])
        Rand_Price  = round(Rand_Price,2)
        print(" ---> Rand_Price: ", Rand_Price)
        

        
