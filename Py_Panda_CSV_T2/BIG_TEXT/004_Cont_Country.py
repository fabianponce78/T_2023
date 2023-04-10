'''
Created on Mar 30, 2023

@author: fponce
'''


'''
Created on Mar 30, 2023

@author: fponce
'''

import pandas as pd


csvFilePath = r'archive/countryContinent.csv'


    


# Reading data frame from csv file
#data = pd.read_csv(csvFilePath, encoding='utf-8')
data = pd.read_csv(csvFilePath, encoding="ISO-8859-1")


print('************************************************************************************') 
# calling head() method  
# storing in new variable 
data_top = data.head(2)    
# display 
print(data_top.to_string()) 
print('************************************************************************************')

#print(data)


print('************************************************************************************')
'''
    https://sparkbyexamples.com/pandas/pandas-find-unique-values-from-columns/
    1. Quick Examples of Get Unique Values in Columns
'''
# Find unique values of a column
print(data['continent'].unique())
print(data.continent.unique())

# Convert to List
print(data.continent.unique().tolist())
print('************************************************************************************')

'''
    https://www.tutorialspoint.com/python-filtering-data-with-pandas-query-method
'''
# Data frame from csv file
df_01 = data

#df_01.query('continent < 230' and 'age > 60', inplace=True)
df_01.query('continent == "Americas"', inplace=True)

# Result
print(df_01)
print(data.country.unique())
print(data.country.unique().tolist() )

        
 

 
 
