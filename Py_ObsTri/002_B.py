'''
Created on Jan 18, 2023

@author: fponce
'''

# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup

# Opening the html file
HTMLFile = open("TEST.html", "r")

# Reading the file
index = HTMLFile.read()

# Creating a BeautifulSoup object and specifying the parser
S = BeautifulSoup(index, 'lxml')

# Using the select-one method to find the second element from the li tag
#Tag = S.select_one('li:nth-of-type(2)')
Tag = S.select_one('div ')

# Using the decompose method
Tag.decompose()

# Using the prettify method to modify the code
print(S.body.prettify())

###////////////////////////////////////////////////
with open('#_ObsTri_Output_A.HTML', 'w') as f:
    f.write(S.body.prettify())

