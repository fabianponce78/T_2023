'''
Created on Mar 7, 2023

@author: fponce
'''

import pandas as pd

'''
SEE.
https://sparkbyexamples.com/pandas/pandas-dataframe-query-examples/
'''


############################################################################################################
def fn_103_DF_XXX(df_Country,df_DF_Lat_Long):
    print('----------fn_103_DF_XXX')
    
    '''
    JOIN df's
    See. https://pandas.pydata.org/docs/user_guide/merging.html
    '''
    #print(df_Country.to_string())
    #print(df_DF_Lat_Long)
    
    result = pd.concat([df_Country, df_DF_Lat_Long], axis=1, join="inner")
    
    #print(result.head(5).to_string()   )
    #print(result.to_string()   )
    '''    
    name alpha-3    region                       sub-region                    Country/Region        Lat        Long
    '''

    df_new = result[['name', 'alpha-3', 'region' , 'sub-region' ,'Lat', 'Long']]
    #print(df_new.head(5).to_string()   )
    
    ######
    '''
    See. https://thispointer.com/pandas-add-two-columns-into-a-new-column-in-dataframe/
    Add a New Column.
    Calculate values in a new column
    '''
    #print('----///////////////////////////')
    df_new['NEW_COLUMN'] = 666
    #df_new['NEW_COLUMN_2'] = df_new['NEW_COLUMN'] + 2
    df_new['NEW_COLUMN_2'] = df_new['Lat'] + df_new['Long']
    #df_new.assign(  df_new['NEW_COLUMN'] + 1 )
    #print(df_new.head(5).to_string()   )
    #print('----///////////////////////////')
    ######
    
    
    ## See. https://www.kdnuggets.com/2022/11/4-ways-rename-pandas-columns.html
    ## rename columns
    df_new.set_axis(["[Country]", "[Code]", "[Region]", "[Sub-Region]", "[Lat]", "[Long]", "[NEW_COLUMN]", "[Lat+Long]"], axis="columns", inplace=True)
    print(df_new.head(5).to_string()   )
    
    df_new.to_csv('#_TEST_out_2.csv')  
    

############################################################################################################
def fn_101_DF_Lat_Long():
    print('----------fn_101_DF_Lat_Long')
    Str_Path = 'archive/RAW_global_deaths.csv'
    df = pd.read_csv(Str_Path)
    #print(df.to_string())     
    #print(df.head(5))
    #print(df.head(5).to_string()   )
    
    df_new = df[['Country/Region', 'Lat', 'Long']]        
    #print(df_new.head(5).to_string()   )
            
    df_new = df_new.query("Lat >= 1")
    return  df_new
    


############################################################################################################
def fn_100_DF_Country():
    print('----------fn_100_DF_Country')
    #Str_Path = 'archive/RAW_us_deaths.csv'
    Str_Path = 'archive/continents2.csv'
    df = pd.read_csv(Str_Path)
    #print(df.to_string())     
    #select columns called .....
    df_new = df[['name', 'alpha-3', 'region', 'sub-region']]
    #print('df_new = ', df_new.to_string()   )
    
    #print('------------------------------contains--------START------------------------------------------------')
    #df_A = df_new.query('name.str.contains("ur")', engine='python')     ## OK !!!
    #print('df_new = ', df_new.to_string()   )
    #print('------------------------------contains--------END------------------------------------------------')
    
    
    #['Asia', 'Europe', 'Africa', 'Oceania', 'Americas', nan]
    filter_list = []
    filter_list=['Americas']
    #filter_list=['Africa','Americas']
    #filter_list=['Asia', 'Europe', 'Africa', 'Oceania', 'Americas']
    
    df_A = df_new.query("region in @filter_list")
    #df_A.to_csv('#_TEST_out.csv')  
    #print(df_A.to_string())  
    
    return  df_A      



############################################################################################################
def main():
    ###Get 1st DataFaram
    #fn_100_DF_Country()    
    #fn_101_DF_Lat_Long()
    
    df_Country  = fn_100_DF_Country()    
    df_DF_Lat_Long = fn_101_DF_Lat_Long()
    
    fn_103_DF_XXX(df_Country,df_DF_Lat_Long)    
############################################################################################################
if __name__ == '__main__':
    main()