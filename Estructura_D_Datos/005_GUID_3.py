'''
Created on Jan 23, 2023

@author: fponce
'''



import random







dic_Produt_Price ={
    "Produt_Price":[
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
    }

print(dic_Produt_Price)


print("-----------------------------------------------------------------")


N_Random = random.randint(1, 10)
print('N_Random', N_Random)
i = 0
for Str_Dic in dic_Produt_Price["Produt_Price"]:
    i+= 1    
    print(i, ' -- ', Str_Dic)
    if i == N_Random:
        print(i, ' -- ', Str_Dic)
        #Produt_Price
        print(i, ' -- ', Str_Dic["Lower_Price"])
        print(i, ' -- ', Str_Dic["High_Price"])
        Rand_Price = random.uniform(Str_Dic["Lower_Price"], Str_Dic["High_Price"])
        Rand_Price  = round(Rand_Price,2)
        print(" ---> Rand_Price: ", Rand_Price)