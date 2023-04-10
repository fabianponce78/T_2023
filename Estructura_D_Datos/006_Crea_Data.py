'''
Created on Jan 23, 2023

@author: fponce
'''

import uuid
import random
import pandas as pd

str_Line = '------------------------------------------------------------------------------------'

############################################################################################################################################
############################################################################################################################################

def fn_05_GetProdutPrice():
    #print(str_Line, " fn_05_GetProdutPrice")
    
    dic_Produt_Price ={
    "Produt_Price":[
    {
        "id": 1,
        "Produt": "almond",
        "Lower_Price": 10.01,
        "High_Price": 30.00
    },
    {
        "id": 2,
        "Produt": "apple",
        "Lower_Price": 15.20,
        "High_Price": 20.00
    },
    {
        "id": 3,
        "Produt": "apricot",
        "Lower_Price": 10.00,
        "High_Price": 30.00
    },
    {
        "id": 4,
        "Produt": "avocado",
        "Lower_Price": 10.00,
        "High_Price": 40.00
    },
    {
        "id": 5,
        "Produt": "banana",
        "Lower_Price": 10.00,
        "High_Price": 50.00
    },
    {
        "id": 6,
        "Produt": "blackberry",
        "Lower_Price": 10.00,
        "High_Price": 60.00
    },
    {
        "id": 7,
        "Produt": "cherry",
        "Lower_Price": 10.00,
        "High_Price": 70.00
    },
    {
        "id": 8,
        "Produt": "coconut",
        "Lower_Price": 10.00,
        "High_Price": 80.00
    },
    {
        "id": 9,
        "Produt": "grape",
        "Lower_Price": 10.00,
        "High_Price": 90.00
    },
    {
        "id": 10,
        "Produt": "lemon",
        "Lower_Price": 10.00,
        "High_Price": 100.00
    }           ]
    }
    
    #print(dic_Produt_Price)
    
    N_Random = random.randint(1, 10)
    #print('N_Random', N_Random)
    i = 0
    for Str_Dic in dic_Produt_Price["Produt_Price"]:
        i+= 1    
        #print(i, ' -- ', Str_Dic)
        if i == N_Random:
            #print(i, ' -- ', Str_Dic)
            ##Produt_Price
            #print(i, ' -- ', Str_Dic["Produt"])
            Produt = Str_Dic["Produt"]
            #print(i, ' -- ', Str_Dic["Lower_Price"])
            #print(i, ' -- ', Str_Dic["High_Price"])
            Rand_Price = random.uniform(Str_Dic["Lower_Price"], Str_Dic["High_Price"])
            Rand_Price  = round(Rand_Price,2)
            #print(" ---> Rand_Price: ", Rand_Price)
    
    #print("Produt: ", Produt)
    #print("Rand_Price: ", Rand_Price)
    
    return Produt, Rand_Price   # Return 2 variables !!!
            
            



############################################################################################################################################
############################################################################################################################################

def fn_04_GetProduccion():
    #print(str_Line, " fn_04_GetProduccion")
    N_Produccion = random.randint(0, 9)
    #print('Random Int', N_Produccion)
    return N_Produccion

############################################################################################################################################
############################################################################################################################################

def fn_03_GetDate():
    #print(str_Line, " fn_03_GetDate")

    from random import randint
    import datetime
    
    #date=datetime.date(randint(2005,2025), randint(1,12),randint(1,28))
    #print(date)
    
    lambda_dt = lambda a,b : datetime.date(randint(a,b), randint(1,12),randint(1,28))        
    #print("\t lambda_dt = ", lambda_dt (2005,2025))
    
    return lambda_dt (2005,2025)

############################################################################################################################################
############################################################################################################################################

def fn_02_GetPais():
    #print(str_Line, " fn_02_GetPais")
    List_Pais = ['Austria', 'Azerbaijan', 'Bonaire Sint Eustatius and Saba','Cambodia','China', 
    'Djibouti', 'European Union','Kosovo', 'Liberia','Liechtenstein','Low income','Malta', 'Tanzania','Yemen', 
    'Aruba', 'Belgium', 'Benin', 'Colombia', 'Eswatini','Ethiopia','Faeroe Islands','France', 
    'French Polynesia','Israel','Jamaica', 'New Zealand', 
    'Niue', 'Norway', 'Panama','Serbia', 'Slovenia','Uruguay','Bermuda', 'Burkina Faso', 
    'Burundi', 'Czechia','Dominica','Dominican Republic','Ghana', 'Grenada', 'International','Jersey', 
    'Kyrgyzstan', 'Laos','Maldives', 'Montenegro', 'North America','Northern Cyprus', 'Saint Helena', 'Saint Lucia', 
    'Thailand', 'Turkey', 'Angola', 'Anguilla', 'Antigua and Barbuda','Pitcairn', 
    'Sao Tome and Principe','Turkmenistan', 'Upper middle income', 'Argentina', 
    'Bosnia and Herzegovina','Bulgaria', 'Guernsey', 'Guinea-Bissau','Hungary', 
    'Nauru', 'Spain','United States', 'Australia', 'Brazil','British Virgin Islands', 
    'Canada', ]

    #print(random.choice(List_Pais))
    Str_Pais = random.choice(List_Pais)
    #print(Str_Pais)
    return Str_Pais

############################################################################################################################################
############################################################################################################################################
def fn_01():
    #print(str_Line, "fn_01")
    
    UID = uuid.uuid4()
    #print("\t UID =", UID)
    
    #Get Pais
    Str_Pais = fn_02_GetPais()
    #print("\t Str_Pais =", Str_Pais)
    
    #Get Date    
    dt_Date = fn_03_GetDate()
    #print("\t dt_Date =", dt_Date)
    
    #Get Produccion
    N_Produccion = fn_04_GetProduccion()
    #print("\t N_Produccion =", N_Produccion)
    
    #Get Produt Price
    Product, Product_Price = fn_05_GetProdutPrice()
    #print("\t Product =", Product)
    #print("\t Product_Price =", Product_Price)
    
    return UID, Str_Pais, dt_Date, N_Produccion, Product, Product_Price

    
    
############################################################################################################################################
############################################################################################################################################
def fn_00():
    #print(str_Line, "fn_00")
    List_cols = ['UID', 'Pais', 'dt', 'Produccion', 'Product', 'Product_Price']
    df = pd.DataFrame(columns=List_cols)
    print(df)
    
    
    for i in range(100):
        UID, Str_Pais, dt_Date, N_Produccion, Product, Product_Price = fn_01()
        print("-------")
        print(UID, '|', Str_Pais, '|',  dt_Date, '|',  N_Produccion, '|',  Product, '|',  Product_Price)
        
        New_data =     {
        "UID": UID,
        "Pais": Str_Pais,
        "dt": dt_Date,
        "Produccion": N_Produccion,
        "Product": Product,
        "Product_Price": Product_Price
        }
        df = pd.concat([df, pd.DataFrame(New_data, index=[0])], ignore_index=True)
        
        print("-------")
        
        print("\n*********************************************\n")
        print(df)
        df.to_csv('New_Data_Product_Price.csv' , index=False)
        print("\n*********************************************\n")
       
############################################################################################################################################
############################################################################################################################################
def main():
    fn_00()



if __name__ == '__main__':
    main()  