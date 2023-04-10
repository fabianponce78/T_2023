'''
Created on Mar 17, 2023

@author: fponce
'''


'''
 Crea listas con elementos Random
'''


import random 
import json
print('==========================================================================')  



lst_Pais = ['Mexico',  'China',  'EEUU',   'Canada'  ]
lst_Producto = ['Arroz',  'Zanahoria',  'Papel',   'Oro'  ]
 
#print('---------------------------    \t    Random Choice. List') 
#random_lst_Pais = random.choice(lst_Pais)
#print(random_lst_Pais)


print('---------------------------    \t    Random Choice. List / lambda ')
rndm_lst_Value = lambda lst_X: random.choice(lst_X)
#print('- Pais:     \t', rndm_lst_Value(lst_Pais)        )
#print('- Producto: \t', rndm_lst_Value(lst_Producto)    )

#print('---------------------------    \t    Random int number') 
#N_Value = random.randint(100, 200)
#print(N_Value)

#print(random.randint(0, 10**5)/ 10**5)
print('==========================================================================')
lst_A = []

#Str_Pais =  '"Pais": "'+rndm_lst_Value(lst_Pais)+'"'
#Str_Pais =  "Pais:"  +  '"' +   rndm_lst_Value(lst_Pais) +  '"'
Str_Pais =  rndm_lst_Value(lst_Pais)
Str_Producto =  rndm_lst_Value(lst_Producto)
N_Produccion = N_Value = random.randint(100, 999)

#lst_A = lst_A.append(Str_Pais)
#print('Str_Pais = ', Str_Pais)

lst_A.append(   Str_Pais   )    #    "Pais": "xxxx",
lst_A.append(   Str_Producto    )
lst_A.append(   N_Produccion    )


print('lst_A    =    ', lst_A )


print('---------------------------')
class Pais_Prod:
    def __init__(self, Pais, Producto, Produccion):
        self.Pais = Pais
        self.Producto = Producto
        self.Produccion = Produccion


#Str_Pais_Prod = Pais_Prod('eduardo_gpg', 'eduardo78d@gmail.com')
Str_Pais_Prod = Pais_Prod(Str_Pais, Str_Producto, N_Produccion)
data = json.dumps(Str_Pais_Prod.__dict__)

print(data)

print('---------------------------')
lst_Pais_Prod = []

lst_Pais_X    = []
lst_Prod_X    = []
lst_Produccion_X = []
lst_Year_X = []

for i in range(1,3):
    print('\t',   i)

    rdn_Pais        = rndm_lst_Value(lst_Pais)
    rdn_Producto    = rndm_lst_Value(lst_Producto)
    rdn_Produccion  = random.randint(100, 999)
    rdn_Year  = random.randint(2000, 2020)
    
    
    lst_Pais_Prod.append(   rdn_Pais    )
    lst_Pais_Prod.append(   rdn_Producto    )
    lst_Pais_Prod.append(   rdn_Produccion    )
    lst_Pais_Prod.append(   rdn_Year    )
    
    lst_Pais_X.append(    rdn_Pais    )
    lst_Prod_X.append(    rdn_Producto    )
    lst_Produccion_X.append(  rdn_Produccion    )
    lst_Year_X.append(  rdn_Year    )

    
    
print('---------------------------')
print('lst_Pais_Prod = ', lst_Pais_Prod)
jsonString = json.dumps(lst_Pais_Prod)
print('jsonString= ', jsonString)

print('---------------------------!!!!!!')

print('lst_Pais_X = ', lst_Pais_X)
print('lst_Year_X  = ', lst_Year_X )
print('lst_Prod_X  = ', lst_Prod_X )
print('lst_Produccion_X  = ', lst_Produccion_X )




d = [ { 'Pais': A, 'Year': B, 'Product': C, 'Produccion': D } 
      for A,B,C,D in zip(lst_Pais_X, lst_Year_X, lst_Prod_X, lst_Produccion_X) ]
pretty_json = json.dumps(d, sort_keys=True, indent=4)
#pretty_json = json.dumps(d,  indent=4)

print(pretty_json)


