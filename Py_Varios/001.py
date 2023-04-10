'''
Created on Feb 3, 2023

@author: fponce
'''


#    https://bobbyhadz.com/blog/python-get-first-number-in-string

import re

my_str = 'bobby12hadz34.com'


match = re.search(r'\d+', my_str)

if match:
    # 👇️ First number found: 12
    print('First number found:', match.group())

    # 👇️ Index of first digit: 5
    print('Index of first digit:', match.start())
else:
    print('The string does NOT contain any numbers')
    
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################     
print('###################################################################################################################################')

import re

my_str = 'bobby12hadz34.com'
my_str = 'AEIOU12hadz34.com'


match = re.search(r'[0-9]+', my_str)

print('match: ', match)

if match:
    # 👇️ First number found: 12
    print('First number found:', match.group())
else:
    print('The string does NOT contain any numbers')

###
lmbd_Search_Num = lambda x: (re.search(r'[0-9]+', x)).group()

print('__ ', lmbd_Search_Num(my_str))