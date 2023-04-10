'''
Created on Mar 21, 2023

@author: fponce
'''


'''
https://www.geeksforgeeks.org/hdf5-files-in-python/
'''

# Python program to demonstrate
# HDF5 file

import numpy as np
import h5py

# initializing a random numpy array
arr = np.random.randn(1000)

filename = 'tmp/test_02.h5'


# creating a file
with h5py.File(filename, 'w') as f:
    dset = f.create_dataset("default", data = arr)


print('/////////////////////////////////////////////////////////////////////////')


# open the file as 'f'
with h5py.File(filename, 'r') as f:
    data = f['default']
    
    # get the minimum value
    print('\t min(data) = ',   min(data))
    
    # get the maximum value
    print('\t max(data) = ',   max(data))
    
    # get the values ranging from index 0 to 15
    print('\t data[:15] = ',   data[:15])
    
print('/////////////////////////////////////////////////////////////////////////')    

#import numpy as np
#import h5py


arr1 = np.random.randn(10000)
arr2 = np.random.randn(10000)

with h5py.File(filename, 'w') as f:
    f.create_dataset('array_1', data = arr1)
    f.create_dataset('array_2', data = arr2)

print(arr1 )
print(arr2 )

'''    
with h5py.File('test_read.hdf5', 'r') as f:
    d1 = f['array_1']
    d2 = f['array_2']

    data = d2[d1[:]>1]
    print(data)
'''
    


