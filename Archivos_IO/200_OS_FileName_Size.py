'''
Created on Feb 8, 2023

@author: fponce
'''

import os.path, time
from fnmatch import fnmatch


str_Linea = '_______________________________________________________'

root = '/some/directory'

root = 'C:\#_FP_APEX\#_DEV\#_Tmp_Test'
root = 'C:\#_FP_APEX\#_DEV'
root = 'C:\#_FP_APEX'
root = 'C:\#_FP_APEX'
pattern = "*.*"


str_Path_CSV = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\OutFile_Log.CSV'

########################################################################################################
########################################################################################################


def fn_200_File_Size_MB(Str_PathFileName, N_File_Size_MB):
    print(str_Linea, ' fn_100_OS_FileName')
    print(' - Str_PathFileName = ', Str_PathFileName)      # ***
    print(' - N_File_Size_MB: ', N_File_Size_MB)    # ***
    
    N_File_Size_MB= round(N_File_Size_MB,2)
    
    Str_OutPut = Str_PathFileName.strip()+'|'+str(N_File_Size_MB).strip()+' MB \n'
    print(' - Str_OutPut: ', Str_OutPut)    # ***
    
    #########################------------------------
    archi1=open(str_Path_CSV,"a+")
    archi1.write(str(Str_OutPut)) 
    archi1.close()
    #########################------------------------

########################################################################################################
########################################################################################################
def fn_100_OS_FileName():
    print(str_Linea, ' fn_100_OS_FileName')
    
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                Str_PathFileName = os.path.join(path, name)
                #last_modified = time.ctime(os.path.getmtime(Str_PathFileName))
                #created =   time.ctime(os.path.getctime(Str_PathFileName))
                            
                #print('Str_PathFileName = ', Str_PathFileName)      # ***
                ##print("last modified: %s" % time.ctime(os.path.getmtime(Str_PathFileName)))
                ##print("created: %s" % time.ctime(os.path.getctime(Str_PathFileName)))
                #print('last_modified = ', last_modified)
                #print('created = ', created)
                
                file_stats = os.stat(Str_PathFileName)
                #print(' - file_stats: ', file_stats)
                
                #print(f' - File Size in Bytes is {file_stats.st_size}')
                #print(f' - File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')
                
                N_File_Size_MB = file_stats.st_size / (1024 * 1024)
                #print(' - N_File_Size_MB: ', N_File_Size_MB)    # ***
                
                n_MB = 10
                
                if N_File_Size_MB > n_MB:
                    print(f'MAS de {n_MB}')
                    fn_200_File_Size_MB(Str_PathFileName, N_File_Size_MB)
                
                #print('--------------------------------------------------------------------') 

    
########################################################################################################
########################################################################################################        
def fn_100_Create_Log_File():
    print(str_Linea, 'fn_00_Log_File')  
    #print(str_Linea, 'fn_Log_File')     
    #N_If_Log_Exist = os.path.isfile(str_Path_CSV)
    #print('---------------N_If_Log_Exist = ', N_If_Log_Exist  )
  
    if os.path.isfile(str_Path_CSV):
        #print ("Log File exist")
        print('')
        str_W_Line = 'PathFileName|MB\n'
        archi1=open(str_Path_CSV,"w")
        archi1.write(str(str_W_Line)) 
        archi1.close()
    else:
        #print ("Log File not exist")
        #str_W_Line = '==============================\n' + str(datetime.now()) + '\n=============================='
        str_W_Line = 'PathFileName|MB\n'
        archi1=open(str_Path_CSV,"w")
        archi1.write(str(str_W_Line)) 
        archi1.close()
           
    
########################################################################################################
########################################################################################################

def main(): 
    print(str_Linea, ' main')  
    fn_100_Create_Log_File()  
    fn_100_OS_FileName()
    



if __name__ == "__main__":
    main()