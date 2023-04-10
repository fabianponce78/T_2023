'''
Created on Jan 17, 2022

@author: Fabian Ponce
'''
from datetime import datetime
import datetime as dt
#import os, os.path
import os.path, time
import shutil
from fnmatch import fnmatch
import pandas as pd


str_Linea = '_____________________________________'
str_Path_CSV = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\#_Filelog.csv'

 
def fn_10_LoadCSV():
    print(str_Linea, 'fn_10_LoadCSV')
    #t = pd.read_csv(str_Path_CSV)
    #print(t)    
    df = pd.read_csv(str_Path_CSV, sep = '|' ,  usecols=[1,2] )
    
    
    print(type(df))
    
    df['B'] = pd.to_datetime(df['B'])
    df['C'] = pd.to_datetime(df['C'])
    
    df['dt_Dif'] = df['B'] - df['C']
        
    print(df)
    '''        
    print(df.columns)
    print(df.dtypes)
    '''
    
    print('---SUM = ', df['dt_Dif'].sum()  )
    
        
    
    
            
 
 


def fn_02_ListFiles(root):
    print(str_Linea, 'fn_02_ListFiles')
    print(' root =', root )
    
    pattern = "*.*"
    
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                Str_PathFileName = os.path.join(path, name)
                
                #last_modified = time.ctime(os.path.getmtime(Str_PathFileName))
                
                last_modified = dt.datetime.fromtimestamp(os.path.getmtime(Str_PathFileName))
                #last_modified = last_modified.strftime("%Y/%m/%d %H:%M:%S")
                last_modified = last_modified.strftime("%Y-%m-%d %H:%M:%S") 
                
                
                #created =   time.ctime(os.path.getctime(Str_PathFileName))
                created = dt.datetime.fromtimestamp(os.path.getctime(Str_PathFileName))
                #created = last_modified.strftime("%Y/%m/%d %H:%M:%S")
                created = created.strftime("%Y-%m-%d %H:%M:%S")
                
                
                
                print('Str_PathFileName = ', Str_PathFileName)
                #print("last modified: %s" % time.ctime(os.path.getmtime(Str_PathFileName)))
                #print("created: %s" % time.ctime(os.path.getctime(Str_PathFileName)))
                print('created = ', created)
                print('last_modified = ', last_modified)
                
                dt_Dif = datetime.fromisoformat(last_modified) - datetime.fromisoformat(created)
                print('dt_Dif = ', dt_Dif)
                dt_Dif = str(dt_Dif)
                n_delimiter = dt_Dif.find(',')
                n_len_Dif = len(dt_Dif)
                print('n_delimiter = ', n_delimiter)
                print('n_len_Dif = ', n_len_Dif)
                
                str_Time = dt_Dif[n_delimiter+1:n_len_Dif]
                print('____ str_Time = ' , str_Time ) 
                
                #########==================================================================
                str_W_Line = Str_PathFileName + ' | ' + last_modified + ' | ' + created + ' | ' +  str(dt_Dif)  + ' | ' +  str_Time
                print (str_W_Line)
             
                #str_W_Line = str(str_FileName_arr)
                str_W_Line = str_W_Line + '\n' 
             
                archi1=open(str_Path_CSV,"a+")
                archi1.write(str(str_W_Line)) 
                archi1.close()
                #########==================================================================                 
                print('--------------------------------------------------------------------')    
    

        
        
def fn_01_ListDirs(rootdir):
    print(str_Linea, 'fn_01_ListDirs')
    for it in os.scandir(rootdir):
        if it.is_dir():
            print(it.path)
            fn_02_ListFiles(it.path)
            fn_01_ListDirs(it)
 


def fn_00_Log_File():
    print(str_Linea, 'fn_00_Log_File')  
    #print(str_Linea, 'fn_Log_File')     
    #N_If_Log_Exist = os.path.isfile(str_Path_CSV)
    #print('---------------N_If_Log_Exist = ', N_If_Log_Exist  )
  
    if os.path.isfile(str_Path_CSV):
        #print ("Log File exist")
        print('')
        str_W_Line = 'A|B|C|D\n'
        archi1=open(str_Path_CSV,"w")
        archi1.write(str(str_W_Line)) 
        archi1.close()
    else:
        #print ("Log File not exist")
        #str_W_Line = '==============================\n' + str(datetime.now()) + '\n=============================='
        str_W_Line = 'A|B|C|D\n'
        archi1=open(str_Path_CSV,"w")
        archi1.write(str(str_W_Line)) 
        archi1.close()
       
       
def fn_X_datetime():
    print(str_Linea, 'fn_00_Log_File')
    #X = 65
    #result = datetime.datetime.now() - datetime.timedelta(seconds=X)
    #print('result = ', result)
    now = datetime.now()
    dt2 = '2022-01-18 11:00:25.270407'
    dt2 = '2022-01-14 16:21:49'
    dt2 = datetime.fromisoformat(dt2)
    print('now = ', now)
    print('dt2 = ', dt2)
    
    res = dt2 - now
    print('res = ', res)
    
    


def main(): 
    print(str_Linea, 'main')
    #rootdir = 'path/to/dir'
    rootdir = 'C:\#_FP_APEX\#_DEV\#_Tmp_Test'
    
    fn_00_Log_File()
    
    fn_01_ListDirs(rootdir)
    
    #fn_X_datetime()
    
    fn_10_LoadCSV()


if __name__ == "__main__":
    main()