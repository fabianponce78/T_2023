'''
Created on Mar 28, 2023

@author: fponce
'''


'''
    https://www.geeksforgeeks.org/extract-text-from-pdf-file-using-python/
    
    pip install PyPDF2
'''

# importing required modules
from PyPDF2 import PdfReader


LibroPath = 'Libro/El-Necronomicon_H.P_Lovecraft.pdf'

# creating a pdf reader object
#reader = PdfReader('example.pdf')
reader = PdfReader(LibroPath)

# printing number of pages in pdf file
N_Total_Pages = len(reader.pages)
print('number of pages in pdf file:    ',   N_Total_Pages   )

print('----------------------------------------------------')
# getting a specific page from the pdf file
#page = reader.pages[0]
page = reader.pages[2]


# extracting text from page
Page_Text = page.extract_text()
print(Page_Text)


print('----------------------------------------------------')
'''
# Import pandas library
import pandas as pd

# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])

# print dataframe.
print(df)
'''



print('----------------------------------------------------')
import pandas as pd

# initialize list of lists
data = [[N_Total_Pages, Page_Text]]
data = [[2, Page_Text]]

# Create the pandas DataFrame
#df = pd.DataFrame(data, columns=['Name', 'Age'])
df = pd.DataFrame(data, columns=['N_Total_Pages', 'Page_Text'])

# print dataframe.
#print(df)
print(df.to_string())


print('----------------------------------------------------')
for x in range(6):
    print(x)
