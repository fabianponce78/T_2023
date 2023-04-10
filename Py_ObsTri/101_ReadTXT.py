'''
Created on Jan 18, 2023

@author: fponce
'''
'''
Created on Jan 18, 2023

@author: fponce
'''

# Importing BeautifulSoup class from the bs4 module
 


####-----------------------------------------------------------
####-----------------------------------------------------------
#===============================================================================
# # Opening the html file
# HTMLFile = open("#_ObsTri_Output_A.HTML", "r")
# 
# # Reading the file
# HTML_content = HTMLFile.read()
# 
# 
# #print(HTML_content)
#===============================================================================
####-----------------------------------------------------------
####-----------------------------------------------------------

import pandas as pd

def fn_01_ReadHTML():
    #===========================================================================
    # f = open("#_ObsTri_Output_B.txt", "r")
    # #print(f.read())
    # 
    # df = pd.DataFrame(f)
    # print(df)
    # 
    #===========================================================================
    df = pd.read_csv('#_ObsTri_Output_B.txt', sep='|', index_col=1, skiprows=[0])
    
    #print(df)
    
    
    
    print(df.head(5))
    
    print('---')
    #print(df.columns[:2])
    #print(df.columns.tolist())
    #print('----')
    #print(df[:1])
    
    #print( df.iloc[:, 0] ) # Primera columna     | 2019 IRONMAN Boulder
    #print( df.iloc[:, 1] ) # Segunda columna      |    Fecha , Categoria y Numero
    #print( df.iloc[:, 2] ) #                        |    Natacion
    #print( df.iloc[:, 3] ) #                        |    Bici
    #print( df.iloc[:, 4] )  #                        |    RUN
    print( df.iloc[:, 5] )   #                        |    Total
    #print( df.iloc[:, 6] ) 
    #print( df.iloc[:, -1] ) # Última columna
    
    
    

            


def main():
    fn_01_ReadHTML()



if __name__ == '__main__':
    main()        