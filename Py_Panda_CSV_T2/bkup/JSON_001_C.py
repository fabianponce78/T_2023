'''
Created on Mar 17, 2023

@author: fponce
'''


import json
import pandas as pd
import os
import time


# get the start time
st = time.time()


#file_name = "/Users/pankaj/abcdef.txt"
file_name = "###_TEST_01.json"

file_stats = os.stat(file_name)

print('****************************************************************************')
print(file_stats)
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')
print('****************************************************************************')



'''
with open('###_TEST_01.json') as f:
    data = json.load(f)
    print(data)
'''    

    
df = pd.read_json('###_TEST_01.json')

'''
# calling head() method  
# storing in new variable 
data_top = df.head() 
# display
print(data_top) 
'''

# calling keys() function
print(df.keys())
 
print('---------------------------------------------')
#print(df)
#print(df.to_string())     
print('---------------------------------------------')

print('\t Pais:        ',   df.Pais.unique()  )
#print('\t Produccion:  ',   df.Produccion.unique()  )
print('\t Product:     ',   df.Product.unique()  )
#print('\t Year:        ',   df.Year.unique()  )


#print('\t Get Number of Rows in DataFrame:        ',   len(df. index)  )
print('\t Get Number of Rows in DataFrame:        ',   df.shape[0]  )
#print('\t Get Number of Rows in DataFrame:        ',  df[df.columns[0]].count()  )
print('\t Get Number of Rows in DataFrame:        ', f"{df[df.columns[0]].count():,}")     





print('----------01---Filter Year, Sort by YEar--------------------------------')


#Using variable
'''
#df=df.query("Pais == 'Mexico'")
'''
value_Pais='Mexico'
#value_Pais=['Mexico', 'Francia']
df=df.query("Pais == @value_Pais")

print('\t Get Number of Rows in DataFrame:        ', f"{df[df.columns[0]].count():,}")    


#df.query("'Year' >= 1900 and 'Year' <= 2024")
#df_01 = df.query("`Year` >= 2017")
df_01 = df.query("`Year` == 2017")
#df_01 = df.query("`Year` >= 1900")
#df_01 = df_01.sort_values(by=['Year'])
df_01 = df_01.sort_values(by=['Year', 'Pais', 'Product'], ascending=False)
#print(df_01.to_string())
print(df_01)
print('\t Get Number of Rows in DataFrame:        ', f"{df_01[df_01.columns[0]].count():,}")    

print('----------02---se GroupBy() to compute the sum--------------------------------')
# Use GroupBy() to compute the sum
#df2 = df.groupby('Pais').sum()
#df_02 = df_01.groupby(['Pais', 'Year']).sum()
df_02 = df_01.groupby(['Pais', 'Year', 'Product']).sum()
#print(df_02)
print(df_02.to_string())

print('---------- SUM  By Pais --------------------------------')
df_02 = df_01.groupby(['Pais', 'Year']).sum()
#print(df_02)
print(df_02.to_string())

print('----------TOTAL SUM--------------------------------')
df_03 = df_01['Produccion'].sum()
#print('SUM Produccion = ', df_03)
#print(f"{df_03:,}")     
print('SUM Produccion = ', f"{df_03:,}")     





print('**************************************************************************** END')
# get the end time
et = time.time()
# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')