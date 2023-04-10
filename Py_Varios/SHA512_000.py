'''
Created on Mar 16, 2023

@author: fponce
'''

import hashlib

input = 'test'
hash = hashlib.sha512( str( input ).encode("utf-8") ).hexdigest()
print(hash)