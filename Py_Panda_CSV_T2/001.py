'''
Created on Mar 7, 2023

@author: fponce
'''

import pandas as pd

#Str_Path = 'archive/RAW_us_deaths.csv'
Str_Path = 'archive/continents2.csv'

df = pd.read_csv(Str_Path)

print( df.head(5) )

print('-------------------------------------------------------------------')

'''
list_sub_region ==> ['Southern Asia', 'Northern Europe', 'Southern Europe', 'Northern Africa', 'Polynesia', 'Sub-Saharan Africa', 
'Latin America and the Caribbean', 
'Western Asia', 'Australia and New Zealand', 'Western Europe', 'Eastern Europe', 
'Northern America', 'South-eastern Asia', 'Eastern Asia', 'Melanesia', 'Micronesia', 'Central Asia']
'''

'''
filter_list = []
filter_list=['Latin America and the Caribbean', 'Northern America']
print(filter_list)

filter_list=['Northern America']
#df_A = df.query("name== @filter_list")
df_A = df.query('name.isin(@filter_list)')
'''

### SEE.  https://sparkbyexamples.com/pandas/pandas-dataframe-query-examples/

df_A = df.query('name.str.contains("ur")', engine='python')     ## OK !!!


#df_A = df.query("region in ('Africa','Americas')")  ## OK !!!

filter_list = []
filter_list=['Africa','Americas']
df_A = df.query("region in @filter_list")





df_A.to_csv('#_TEST_out.csv')  
print(df_A)