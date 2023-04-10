'''
Created on Aug 29, 2022

@author: fponce
'''
import os

Str_Line = '_______________________________________________________________'
path = 'G:/data/input'
path = 'C:\#_FP_APEX\BP\#_Collections\Others\TMP_Recoverability_X'
path = 'C:\#_FP_APEX\BP\#_Collections\Others'


def searchText(path):
    
    os.chdir(path)
    files = os.listdir()
    #print(files)
    for file_name in files:
        #print(file_name)
        abs_path = os.path.abspath(file_name)
        print("Absolute path of the file: ", abs_path)
        
        if os.path.isdir(abs_path):
            searchText(abs_path)
    
    pass



def main():
    #----------------------------------------------
    print(Str_Line)
    searchText(path)
    #----------------------------------------------

if __name__ == "__main__":
    main()