'''
Created on Sep 21, 2022

@author: fponce
'''
import os


text = 'DBAAS_CONNECTION_STATUS'
Str_Line = '_____________________________________________'


def fn_03_Dir_File_2(str_Dir_FileName, file_size_MegaBytes):
    #print('___ fn_03_Dir_File_2 ', Str_Line)
    print('___    ', str_Dir_FileName)
    print('___ MB ', file_size_MegaBytes)


def fn_02_Dir_File(elem):
    #print('___ fn_02_Dir_File ', Str_Line)
    #print(' --> ', elem)
    
    str_Dir_FileName = elem
    
    try:
        # using getsize function os.path module
        file_size_Bytes = os.path.getsize(str_Dir_FileName)
        file_size_MegaBytes = file_size_Bytes / (1024 * 1024)
        
        #print("File Size is :", file_size_Bytes, "bytes")
        #print("File Size is :", file_size_MegaBytes, "MegaBytes")
        
        if file_size_MegaBytes > 20:
            #print("File Size is :", file_size_MegaBytes, "MegaBytes")
            fn_03_Dir_File_2(str_Dir_FileName, file_size_MegaBytes)
    except:
        print("An exception occurred")
        
    


'''
def fn_Find_Text(elem):
    print('___ fn_Find_Text ', Str_Line)
    with open(elem, 'r', encoding='utf-8', errors='ignore') as f:
        if text in f.read():
            final_path = os.path.abspath(elem)
            print(text + " word found in this path " + final_path)

                    
        else:
            print("No match found in " + elem)
            #print('--')
'''



def fn_01_getListOfFiles(dirName):
    print('___ getListOfFiles ', Str_Line)
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + fn_01_getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        

def main():
    print('___ main ', Str_Line)
    
    #dirName = '/home/varun/Downloads';
    dirName = 'C:\#_FP_APEX\BP\#_Collections\Others'
    dirName = 'C:\#_FP_APEX'
    #dirName = 'C:\#_FP_APEX\BP\#_Collections\Others\TMP_Recoverability_X'
    
    # Get the list of all files in directory tree at given path
    listOfFiles = fn_01_getListOfFiles(dirName)
    
    # Print the files
    for elem in listOfFiles:
        #print(elem)
        print('.')
    #print ("****************")
    
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
                
    # Print the files    
    for elem in listOfFiles:
        #print('-->', elem)
        fn_02_Dir_File(elem)

        
if __name__ == '__main__':
    main()