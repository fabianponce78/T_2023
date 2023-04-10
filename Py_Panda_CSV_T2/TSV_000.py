'''
Created on Mar 8, 2023

@author: fponce
'''
'''
Created on Mar 7, 2023

@author: fponce
'''

import pandas as pd


'''
SEE. 
    https://www.youtube.com/watch?v=0rKrDGS2gkA
    Primeros pasos en ingenieria de datos con Apache Spark
    
    
Download. Apache Spark
    https://spark.apache.org/downloads.html
    
CÓMO INSTALAR APACHE SPARK (PYSPARK) en Windows 10 | Big Data en Python - #1    
https://www.youtube.com/watch?v=wt2wM8C2SXA    

CREAR, LEER Y ESCRIBIR DATAFRAMES (PYSPARK) | Big Data en Python - #2
https://www.youtube.com/watch?v=U-kHrMF3b-A
'''

############################################################################################################
def fn_101():
    print('----------fn_101')
    input_file = open('TSV/name_basics.tsv','r')
     
    while(1):
        for lines in range(50):
            print ( input_file.readline()   )
        user_input = print('Type STOP to quit, otherwise press the Enter/Return key ')
        if user_input == 'STOP':
            break
############################################################################################################
def fn_100():
    print('----------fn_100')
    #Str_Path = 'archive/RAW_us_deaths.csv'
    Str_Path = 'TSV/name_basics.tsv'
    df = pd.read_csv(Str_Path)
    #print(df.to_string())
    print( df.head(10) )     
############################################################################################################
def main():
    ###Get 1st DataFaram
    fn_100()
    fn_101()
 
############################################################################################################
if __name__ == '__main__':
    main()