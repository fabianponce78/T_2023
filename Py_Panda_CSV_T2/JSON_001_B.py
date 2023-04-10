'''
Created on Mar 17, 2023

@author: fponce
'''


import random 
import json
import time


'''
 Create a LARGE data set!!!
 Random values
'''


# get the start time
st = time.time()

#print('==========================================================================') 

lst_0_Pais = ['Mexico',  'China',  'EEUU',   'Canada', 'Australia', 'Francia'  ]
lst_0_Producto = ['Arroz',  'Zanahoria',  'Papel',   'Oro' ,'Platano', 'Plata' ]
 
rndm_lst_Value = lambda lst_X: random.choice(lst_X)
#print('==========================================================================')


lst_1_Pais      = []
lst_1_Prod      = []
lst_1_Year      = []
lst_1_Produccion = []

#10,000,000 rows en 145.4 segundos / 2.4 minutos / 1.13 GB

for i in range(0,100):
    #print('\t',   i)
    rdn_Pais        = rndm_lst_Value(lst_0_Pais)
    rdn_Producto    = rndm_lst_Value(lst_0_Producto)
    
    rdn_Produccion  = random.randint(100, 999)
    rdn_Year  = random.randint(2000, 2020)
    
    lst_1_Pais.append(  rdn_Pais    )
    lst_1_Prod.append(  rdn_Producto    )
    lst_1_Year.append(  rdn_Year    )
    lst_1_Produccion.append(    rdn_Produccion  )

print('---------------------------!!!!!!')

'''
print('lst_1_Pais    = ', lst_1_Pais)
print('lst_1_Prod    = ', lst_1_Prod )
print('lst_1_Year    = ', lst_1_Year )
print('lst_1_Produccion    = ', lst_1_Produccion )
'''


d = [ { 'Pais': A, 'Year': B, 'Product': C, 'Produccion': D } 
      for A,B,C,D in zip(lst_1_Pais, lst_1_Year, lst_1_Prod, lst_1_Produccion) ]
      



pretty_json = json.dumps(d, sort_keys=True, indent=4)
#pretty_json = json.dumps(d,  indent=4)

#print(pretty_json)

'''
with open("###_TEST_01.json", "w") as write_file:
    json.dump(pretty_json, write_file, indent=4, separators=(", ", ": "), sort_keys=True)

with open("###_TEST_02_Compact.json", "w") as write_file:
    json.dump(pretty_json, write_file, separators=(',', ':'))    
'''


# Using a JSON string    !!!! OK
with open('###_TEST_01.json', 'w') as outfile:
    outfile.write(pretty_json)

'''
# Directly from dictionary    \n....
with open('###_TEST_02_Compact.json', 'w') as outfile:
    json.dump(pretty_json, outfile)
'''    

print('**************************************************************************** END')
# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')