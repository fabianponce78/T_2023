'''
Created on Mar 21, 2023

@author: fponce
'''

import numpy as np
import pandas as pd
#from numpy.lib import _datasource
#from lxml.parser #import column


'''
    See.
        https://www.youtube.com/watch?v=mYcZCDvCR_M
'''

filename = 'tmp/test_01.h5'

'''
#####
'''

df = pd.DataFrame(np.arange(10).reshape((5,2)), columns=['A', 'B'])

print(df)

#Save to HDF5
#df.to_hdf(filename, key, mode, complevel, complib, append, format, index, min_itemsize, nan_rep, dropna, data_columns, errors, encoding)
df.to_hdf(filename, 'data', mode='w', format='table')

del df






#######################################################

# Append more data
'''
df2 = pd.DataFrame(np.arange(10).reshape((5,2))*10, columns=['A', 'B']  )

print(df2)
df2.to_hdf(filename, 'data', append=True)

print(  df2.read_hdf(filename, 'data')  )


#print(  df2.read_hdf(filename)  )
'''


store = pd.HDFStore(filename)

for i in range(2):
    df = pd.DataFrame(np.arange(10).reshape((5,2))*10**i, columns=['A', 'B']      )
    store.append('data', df)

store.close()

store = pd.HDFStore(filename)
data = store['data']
print(data)
store.close()    



#######################################################
print('#######################################################')

#import numpy as np
import h5py

# open the file as 'f'
with h5py.File(filename, 'r') as f:
    data = f['default']
        
    # get the values ranging from index 0 to 15
    print('\t data[:15] = ',   data[:15])