from datetime import datetime
import os, os.path
import shutil

str_Linea = '_____________________________________'
str_Path_A = 'C:\#_FP_APEX\#_DEV\#_Tmp_Test\\'
str_Path_Image_OK = 'C:\#_FP_APEX\#_DEV\#_Tmp_Test\Log_Images_OK.log'
str_Path_Image_Error = 'C:\#_FP_APEX\#_DEV\#_Tmp_Test\Log_Images_Error.log'

def fn_Log_OK_WL(str_FileName_arr):
    print(str_Linea, 'fn_Log_OK_WL')
    Str_File = str_FileName_arr
    N_Str_File_Len = len(Str_File)
    N_FileName = Str_File.find('.')
    Str_FileName = Str_File[0:N_FileName]
   
    N_SKU = Str_File.find('_')
    Str_SKU = Str_File[0:N_SKU]
   
    if N_SKU < 0:
        Str_SKU = Str_FileName
   
    Str_Desc = Str_File[N_SKU:N_FileName]
           
    print('Str_File = ', Str_File)
    print('N_Str_File_Len = ', N_Str_File_Len)
    print('N_FileName = ', N_FileName)
    print('Str_FileName = ', Str_FileName)
    print('N_SKU = ', N_SKU)
    print('Str_SKU = ', Str_SKU)
    print('Str_Desc = ', Str_Desc)
       
    str_W_Line = Str_File + ' , ' + Str_FileName + ' , ' + Str_SKU + ' , ' + Str_Desc
    print (str_W_Line)
 
    #str_W_Line = str(str_FileName_arr)
    str_W_Line = str_W_Line + '\n' 
 
    archi1=open(str_Path_Image_OK,"a+")
    archi1.write(str(str_W_Line)) 
    archi1.close() 

def fn_Log_Error_WL(str_FileName_arr):
    print(str_Linea, 'fn_Log_Error_WL')

    str_W_Line = '\n'
    str_W_Line = str_W_Line + str(str_FileName_arr)  
 
    archi1=open(str_Path_Image_Error,"a+")
    archi1.write(str(str_W_Line)) 
    archi1.close()


def fn_Folder_Item():
    print(str_Linea, 'fn_Files_2_FTP')
    arr = os.listdir(str_Path_A) 
    #print(arr)
 
    for str_FileName_arr in arr:
       
        if str_FileName_arr.find('.jpg') > - 1:
            #print('ES JPG')
            print(str_FileName_arr)
            fn_Log_OK_WL(str_FileName_arr)
           
        elif str_FileName_arr.find('.png') > - 1:
            #print('ES png')  
            print(str_FileName_arr)    
            fn_Log_OK_WL(str_FileName_arr)                         
        else:
            print('--NO es JPG ni PNG', str_FileName_arr)
            #fn_Log_Error_WL(str_FileName_arr)   
            #print('No es .TXT')


def fn_Log_File():  
    #print(str_Linea, 'fn_Log_File')     
    #N_If_Log_Exist = os.path.isfile(str_Path_Image_OK)
    #print('---------------N_If_Log_Exist = ', N_If_Log_Exist  )
  
    if os.path.isfile(str_Path_Image_OK):
        #print ("Log File exist")
        print('')
    else:
        #print ("Log File not exist")
        #str_W_Line = '==============================\n' + str(datetime.now()) + '\n=============================='
        str_W_Line = ''
        archi1=open(str_Path_Image_OK,"w")
        archi1.write(str(str_W_Line)) 
        archi1.close()
       
       
       
    if os.path.isfile(str_Path_Image_Error):
        #print ("Log File exist")
        print('')
    else:
        #print ("Log File not exist")
        str_W_Line = '==============================\n' + str(datetime.now()) + '\n=============================='
        archi1=open(str_Path_Image_Error,"w")
        archi1.write(str(str_W_Line)) 
        archi1.close()      

def main(): 
    print(str_Linea, 'main')
    fn_Log_File() 
 
  
    fn_Folder_Item() 
 

if __name__ == "__main__":
    main()