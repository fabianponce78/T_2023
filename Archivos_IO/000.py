'''
Created on Jan 14, 2022

@author: Fabian Ponce
'''

#import os
import os.path, time
from fnmatch import fnmatch

root = '/some/directory'
root = 'C:\#_FP_APEX\#_DEV\#_Tmp_Test'
pattern = "*.*"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            Str_PathFileName = os.path.join(path, name)
            last_modified = time.ctime(os.path.getmtime(Str_PathFileName))
            created =   time.ctime(os.path.getctime(Str_PathFileName))
                        
            print('Str_PathFileName = ', Str_PathFileName)
            #print("last modified: %s" % time.ctime(os.path.getmtime(Str_PathFileName)))
            #print("created: %s" % time.ctime(os.path.getctime(Str_PathFileName)))
            print('last_modified = ', last_modified)
            print('created = ', created)
            
            file_stats = os.stat(Str_PathFileName)
            print(' - file_stats: ', file_stats)
            
            print(f' - File Size in Bytes is {file_stats.st_size}')
            print(f' - File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')
            
            
            print('--------------------------------------------------------------------')