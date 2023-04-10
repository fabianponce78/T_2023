'''
Created on Apr 7, 2022

@author: Fabian Ponce
'''

import requests

url = "https://reqres.in/api/users?page=2"

str_Line = '_________________________________'

response = requests.get(url)

print('response = ', response)
print(str_Line)

print(response.content)
print(str_Line)

print(response.headers)
print(str_Line)
#https://www.youtube.com/watch?v=3ts5fzmhN5o