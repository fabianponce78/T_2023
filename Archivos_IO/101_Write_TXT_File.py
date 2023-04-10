'''
Created on Jan 18, 2022

@author: Fabian Ponce
'''


str_Linea = '_____________________________________'
#str_Path_TXT = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile_2.txt'

str_Path_TXT = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile_OUT_1.txt'
str_Path_TXT_W_2 = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile_OUT_2.CSV'





def fn_002(Str_Linea):
    print(str_Linea, 'fn_002')
    print('--> ', Str_Linea)
    
    Str_Linea = Str_Linea.strip()
        
    Str_Linea = Str_Linea.replace('FullName','')
    Str_Linea = Str_Linea.replace('Name','')
    Str_Linea = Str_Linea.replace('CreationTime','')
    Str_Linea = Str_Linea.replace('LastWriteTime','')
    Str_Linea = Str_Linea.replace('Length','')
    
    Str_Linea = Str_Linea.replace(' : ','')
    
    Str_Linea = Str_Linea.replace('|@','\n')
    #print(len(Str_Linea))
    

        
    
    #Str_Linea = Str_Linea.replace('FullName', '|FullName')
    archi1=open(str_Path_TXT_W_2,"a")
    archi1.write(str(Str_Linea)) 
    archi1.close()




def fn_001_R_File():
    print(str_Linea, 'fn_001_R_File')

    f = open(str_Path_TXT, 'r')
    try:
        for linea in f:
            fn_002(linea)
            #linea = linea.replace(' ', '___')
            #linea = linea.replace('FullName', '|FullName')
            #print(linea)

    finally:

        f.close()


def main(): 
    print(str_Linea, 'main')    
    fn_001_R_File()
    



if __name__ == "__main__":
    main()