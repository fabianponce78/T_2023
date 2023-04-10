'''
Created on Feb 7, 2023

@author: fponce
'''


string = 'Python programming. Network programming.'
substring = 'prog'
substring = ' '

index = string.find(substring)
print(index)

print('###################################################################################################################################')

# Python3 code to demonstrate
# checking if string contains list element
# using list comprehension

# initializing string
test_string = "There are 2 apples for 4 persons"

# initializing test list
test_list = ['apples', 'oranges']

# printing original string
print("The original string : " + test_string)

# printing original list
print("The original list : " + str(test_list))

# using list comprehension
# checking if string contains list element
res = [ele for ele in test_list if(ele in test_string)]

# print result
print("Does string contain any list element : " + str(bool(res)))



print('###################################################################################################################################')
#initialize a string
input_string = 'Pencil(10Rs),Rubber(5Rs),Ruler(8Rs),Sharpener(5Rs)'
 
#create a new lists by parsing the string using "," delimiter
new_string=input_string.split(",")
 
print("After string parsing: ",new_string)
print("The price of Rubber is: ",new_string[1])
print("The price of Rubber is: ",new_string[2])
print("The price of Rubber is: ",new_string[3])

'''
print("The price of Rubber is: ",new_string[1])
'''
print('###################################################################################################################################')
#1) Write a function that parses strings like this one to get the value of the id field
String = '"query_path": "import", "title": "Import", "id": 21712'
print('...', String)    

String=String.split(",")
print("After string parsing: ",String)
print("The price of Rubber is: ",String[1])
print("The price of Rubber is: ",String[2])

str_id = String[2]
str_id = str_id.strip()
str_id = str_id.replace(' ', '')
str_id = str_id.replace('"id":', '')
print('str_id 0 = ', str_id)
