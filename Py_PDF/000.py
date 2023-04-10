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
print('number of pages in pdf file:    ',   len(reader.pages))

print('----------------------------------------------------')
# getting a specific page from the pdf file
page = reader.pages[0]


# extracting text from page
text = page.extract_text()
print(text)
