'''
Created on Jan 18, 2022

@author: Fabian Ponce
'''
#from _ast import If
#import re
#import string


str_Linea = '_____________________________________'
str_Path_TXT = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile_2.txt'

str_Path_TXT_W_1 = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile_OUT_1.txt'
str_Path_TXT_W_2 = 'C:\#_FP_APEX\#_DEV\#_Py_FP\Py_Test\Archivos_IO\Output\APEX_OutFile_OUT_2.CSV'


def fn_002(Str_Linea):
    print(str_Linea, 'fn_002')
    print('--> ', Str_Linea)
    
    Str_Linea = Str_Linea.strip()
    #print(len(Str_Linea))
    
    if(len(Str_Linea)>2):
        #Str_Linea = Str_Linea.replace('', '-')
        #Str_Linea = Str_Linea = ''.join(Str_Linea.split())

        Str_Linea = Str_Linea + '|'

        #print(' Str_Linea ?? = ', Str_Linea.find('Length')   )
        if( Str_Linea.find('Length') == 0):
            Str_Linea = Str_Linea + '@'
        
        
        print(Str_Linea)
        
        archi1=open(str_Path_TXT_W_1,"a")
        archi1.write(str(Str_Linea)) 
        archi1.close()
        
    
    #Str_Linea = Str_Linea.replace('FullName', '|FullName')
    
def fn_000_W1_File():    
        str_W_Line = ''
        
        archi1=open(str_Path_TXT_W_1,"w")
        archi1.write(str(str_W_Line)) 
        archi1.close()
        
        str_W_Line = 'FullName|Name|CreationTime|LastWriteTime|Length\n'
        archi1=open(str_Path_TXT_W_2,"w")
        archi1.write(str(str_W_Line)) 
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
    fn_000_W1_File()
    fn_001_R_File()
    



if __name__ == "__main__":
    main()