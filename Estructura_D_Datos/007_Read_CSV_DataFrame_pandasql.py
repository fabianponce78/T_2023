'''
Created on Jan 24, 2023

@author: fponce
'''

import pandas as pd
from pandasql import sqldf


#===============================================================================
# See
# pip install pandasql 
# https://towardsdatascience.com/how-to-run-sql-queries-on-your-pandas-dataframes-with-python-4237ffecc43b
#===============================================================================

str_Line = '------------------------------------------------------------------------------------'

############################################################################################################################################
############################################################################################################################################
def fn_00_ReadCSV():
    print(str_Line, ' fn_00_ReadCSV')
    
    df = pd.read_csv('New_Data_Product_Price.csv')
    
    
    print(pd.options.display.max_rows)
    print(df)   #     use to_string() to print the entire DataFrame. 
    #print(df.to_string())   #     use to_string() to print the entire DataFrame.
    
    #===========================================================================
    # # calling head() method  
    # # storing in new variable 
    # data_top = df.head()
    # print("data_top = ",  data_top)     
    #===========================================================================
    
    #===========================================================================
    # # iterating the columns
    # for col in df.columns:
    #     print(col)    
    #===========================================================================
    
    print("******************************************************")
    #### sqldf !!!
    sqldf_df = sqldf("SELECT * FROM df")    
    print(sqldf_df)
    
    print("---"*10, '# Check the type of all_students')# Check the type of all_students
    print(type(sqldf_df))

    # Run Pandas Statement to show the type of the columns
    print("---"*10, '# Run Pandas Statement to show the type of the columns')
    print(sqldf_df.dtypes)
    
    
    print("******************************************************")
    
    # Query definition
    query = """ SELECT Pais, Product 
                FROM sqldf_df 
                LIMIT 300
            """
    query = """ SELECT distinct Pais 
                FROM sqldf_df
                WHERE Pais LIKE 'M%' 
                LIMIT 300                 
            """

    #------------------------------------------------------ query = """ SELECT *
                #------------------------------------------------- FROM sqldf_df
                #----------------------------------------- WHERE Pais = 'Panama'
                #----------------------------------------------------- LIMIT 300
            #--------------------------------------------------------------- """
    # Query execution
    Q_XXX = sqldf(query)
    print(Q_XXX)    


############################################################################################################################################
############################################################################################################################################
def main():
    fn_00_ReadCSV()



if __name__ == '__main__':
    main()  