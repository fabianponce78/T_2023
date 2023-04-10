import os


text = 'RPT_DBASS_ACCOUNT_ATT_MAIL_SENT_LOG'


def fn_Find_Text(elem):
    with open(elem, 'r', encoding='utf-8', errors='ignore') as f:
        if text in f.read():
            final_path = os.path.abspath(elem)
            print(text + " word found in this path " + final_path)
            '''
                    
        else:
            print("No match found in " + elem)
            #print('--')
            '''    


def getListOfFiles(dirName):
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
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        
def main():
    
    #dirName = '/home/varun/Downloads';
    dirName = 'C:\#_FP_APEX\BP\#_Collections\Others'
    dirName = 'C:\#_FP_APEX\#_DEV\#_BP\DBAAS-5814 - DBaaS Database Instance Account Attestation Web Application'
    
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    
    # Print the files
    for elem in listOfFiles:
        print(elem)
    print ("****************")
    
    # Get the list of all files in directory tree at given path
    listOfFiles = list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listOfFiles += [os.path.join(dirpath, file) for file in filenames]
        
        
    # Print the files    
    for elem in listOfFiles:
        #print('-->', elem)
        fn_Find_Text(elem)

        
            
        
        
        
        
if __name__ == '__main__':
    main()