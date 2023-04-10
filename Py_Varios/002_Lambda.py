'''
Created on Feb 3, 2023

@author: fponce
'''
print('###################################################################################################################################')

import re

my_str = 'bobby12hadz34.com'
my_str = 'AEIOU12hadz34.com'
my_str = 'sss2dr'


#===============================================================================
# match = re.search(r'[0-9]+', my_str)
# 
# print('match: ', match)
# 
# if match:
#     # 👇️ First number found: 12
#     print('First number found:', match.group())
# else:
#     print('The string does NOT contain any numbers')
#===============================================================================

###
lmbd_Search_Num = lambda x: (re.search(r'[0-9]+', x)).group()

print('__ ', lmbd_Search_Num(my_str))

print(my_str[0:lmbd_Search_Num(my_str)])