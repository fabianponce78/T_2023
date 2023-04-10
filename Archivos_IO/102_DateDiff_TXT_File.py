'''
Created on Jan 18, 2022

@author: Fabian Ponce
'''


str_Linea = '_____________________________________'
#str_Path_TXT = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile_2.txt'

str_Path_TXT = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile_OUT_1.txt'
str_Path_TXT_W_2 = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile_OUT_2.txt'



from datetime import datetime
import datetime as dt
#import os, os.path
import os.path, time
import shutil
from fnmatch import fnmatch
import pandas as pd


str_Linea = '_____________________________________'
str_Path_TXT_W_2 = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile_OUT_2.CSV'

 
def fn_10_LoadCSV():
    print(str_Linea, 'fn_10_LoadCSV')
    #t = pd.read_csv(str_Path_CSV)
    #print(t)    
    #df = pd.read_csv(str_Path_TXT_W_2, sep = '|' ,  usecols=[2,3] )
    df = pd.read_csv(str_Path_TXT_W_2, sep = '|'  )
    
    
    #print(type(df))
    
    #print(df['CreationTime'])
    
    '''
    df['CreationTime'] = pd.to_datetime(df['CreationTime'])
    df['LastWriteTime'] = pd.to_datetime(df['LastWriteTime'])
    
    df['dt_Dif'] = df['LastWriteTime'] - df['CreationTime']
    '''
        
    print(df)
    '''        
    print(df.columns)
    print(df.dtypes)
    '''
    
    #print('---SUM = ', df['dt_Dif'].sum()  )
    
        
    
    


def main(): 
    print(str_Linea, 'main')    
    fn_10_LoadCSV()
    



if __name__ == "__main__":
    main()