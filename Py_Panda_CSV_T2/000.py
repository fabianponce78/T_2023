'''
Created on Mar 6, 2023

@author: fponce
'''


import pandas as pd

#Str_Path = 'archive/RAW_us_deaths.csv'
Str_Path = 'archive/continents2.csv'

df = pd.read_csv(Str_Path)
#print(df.to_string()) 

############----------------------------------
# calling head() method  
# storing in new variable 
#data_top = df.head() 
#print('\t data_top = ', data_top) 


# iterating the columns
#i = 0
#for columns in df.columns:
#    i += 1    
#    print('\t ', i , ' - ',columns)
    
# list(data) or
#print('\t columns =>',   list(df.columns))    
############----------------------------------    
 


############----------------------------------
############---- max_rows
#print(pd.options.display.max_rows)
pd.options.display.max_rows = 60
max_rows = pd.options.display.max_rows
print('\t max_rows = ', max_rows)
############----------------------------------

############----------------------------------
############---- How to Select Multiple Columns in Pandas (With Examples)
###    https://www.statology.org/pandas-select-multiple-columns/
#print(pd.options.display.max_rows)
#df_new = df.iloc[:, [0,1,3]]     ## !!!!!
#df_new = df.iloc[:, [1,7]]
#print('\t df_new = ', df_new)


#select columns called 'points' and 'blocks'
df_new = df[['name', 'region', 'sub-region']]
print('df_new = ', df_new)
############----------------------------------


#https://sparkbyexamples.com/pandas/pandas-find-unique-values-from-columns/#:~:text=You%20can%20get%20unique%20values,to%20get%20from%20multiple%20columns.
# Find unique values of a column
#print(df_new['name'].unique())
print(df_new['sub-region'].unique())

print('------------------------------------')
#list = [1, 3, 5, 7, 9]

list = []
#list = df_new['sub-region'].unique()


## See. https://sparkbyexamples.com/pandas/pandas-find-unique-values-from-columns/#:~:text=You%20can%20get%20unique%20values,to%20get%20from%20multiple%20columns.
# Convert to List
#list = df_new['sub-region'].unique().tolist()
list_region = df_new['region'].unique().tolist()


print('list_region => ', list_region)



#new_list = new_list.sort()
#print('new_list sort => ',new_list.sort())
#Using for loop
i = 0

list_sub_region = []
for j in list:
    i += 1
    #print(i)
    #print(j)
    #print('--', i , '-\t', str(j))
    #print(f"\t It's pd.isna  : {pd.isna(j)}")
    if pd.isna(j) != True:  # NAN
        print('--', i , '-\t', str(j))
        list_sub_region.append(str(j))

print('list_sub_region ==>', list_sub_region)

print('-------------------------------------------------------------------')
####-------------------------------------------------------------
print('-------------------------------------------------------------------')
#print(df_new)
print(  df_new.head(3)    )
print('-------------------------------------------------------------------')


list = df_new['name'].unique().tolist()
i = 0
for j in list:
    i += 1
    #print(i)
    #print(j)
    #print('--', i , '-\t', str(j))
    #print(f"\t It's pd.isna  : {pd.isna(j)}")
    if pd.isna(j) != True:  # NAN
        print('--', i , '-\t', str(j))


print('----------------------contains---------------------------------------------')
#df_A = df_new.query('name == "Algeria" ')
#df_A = df_new.query('column_name.str.contains("abc")', engine='python')
df_A = df_new.query('name.str.contains("Mexico")', engine='python')     ### !!!!
df_A = df_new.query('name.str.contains("ur")', engine='python')     ### !!!!
#df_A = df.query('sub-region == "Northern Europe" ')

print(df_A) 


  


        
 
