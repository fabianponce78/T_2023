'''
Created on Mar 10, 2023

@author: fponce
'''

'''
https://stackoverflow.com/questions/27203161/convert-large-csv-to-hdf5
'''


'''
----------------------
----------------------
import numpy as np
import pandas as pd

filename = '/tmp/test.h5'

df = pd.DataFrame(np.arange(10).reshape((5,2)), columns=['A', 'B'])
print(df)
#    A  B
# 0  0  1
# 1  2  3
# 2  4  5
# 3  6  7
# 4  8  9

# Save to HDF5
df.to_hdf(filename, 'data', mode='w', format='table')
del df    # allow df to be garbage collected

# Append more data
df2 = pd.DataFrame(np.arange(10).reshape((5,2))*10, columns=['A', 'B'])
df2.to_hdf(filename, 'data', append=True)

print(pd.read_hdf(filename, 'data'))
'''



import numpy as np
import pandas as pd

#filename = '/tmp/test.h5'
filename = 'tmp/test.h5'


store = pd.HDFStore(filename)

for i in range(2):
    df = pd.DataFrame(np.arange(10).reshape((5,2)) * 10**i, columns=['A', 'B'])
    store.append('data', df)

store.close()

store = pd.HDFStore(filename)
data = store['data']
print(data)
store.close()


