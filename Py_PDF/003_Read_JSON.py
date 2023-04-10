'''
Created on Mar 28, 2023

@author: fponce
'''


import json
import pandas as pd

JSonLibroPath   =   "Libro/Book_J.json"

with open(JSonLibroPath) as user_file:
    file_contents = user_file.read()
  
#print(file_contents)

jsonStr = file_contents


print('----------------------------------------------------')
# Convert JSON to DataFrame Using read_json()
df2 = pd.read_json(jsonStr, orient ='index')
#print(df2)
print(df2.to_string())