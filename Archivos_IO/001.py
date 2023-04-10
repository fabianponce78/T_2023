'''
Created on Jan 14, 2022

@author: Fabian Ponce
'''

import os
 
 
 
rootdir = 'C:\#_FP_APEX\#_DEV\#_Tmp_Test'
        
        
def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            print(it.path)
            listdirs(it)
 
#rootdir = 'path/to/dir'
listdirs(rootdir)




