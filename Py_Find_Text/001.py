'''
Created on Aug 29, 2022

@author: fponce
'''
import os

Str_Line = '_______________________________________________________________'
path = 'G:/data/input'
path = 'C:\#_FP_APEX\BP\#_Collections\Others\TMP_Recoverability_X'
#path = 'C:\#_FP_APEX\BP\#_Collections\Others'

text = 'DBAAS_CONNECTION_STATUS'


def searchText(path):
    
    os.chdir(path)
    files = os.listdir()
    #print(files)
    for file_name in files:
        #print(file_name)
        abs_path = os.path.abspath(file_name)
        
        if os.path.isdir(abs_path):
            searchText(abs_path)
            
        if os.path.isfile(abs_path):
            with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
                if text in f.read():
                    final_path = os.path.abspath(file_name)
                    print(text + " word found in this path " + final_path)
                    
                else:
                    print("No match found in " + abs_path)
                    #print('--')

    pass



def main():
    #----------------------------------------------
    print(Str_Line)
    searchText(path)
    #----------------------------------------------

if __name__ == "__main__":
    main()