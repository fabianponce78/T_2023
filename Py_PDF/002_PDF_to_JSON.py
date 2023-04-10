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
import json

LibroPath = 'Libro/El-Necronomicon_H.P_Lovecraft.pdf'


# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

 



def fn_05_CreateJSON(dictionary):
    print('----------------------------------------------------')
    print('--fn_05_CreateJSON')
    #print('PageNumber: ', PageNumber)
    #print('Page_Text:  ', Page_Text)
    print('Str_Json:  ', dictionary)
    
    # Serializing json  
    json_object = json.dumps(dictionary, indent = 4) 
    print('---->    json_object:    ',   json_object)
    
    # Writing to sample.json
    with open("Libro/Book_J.json", "w") as outfile:
        outfile.write(json_object)
    
 



def fn_04_CreateDictionary(PageNumber, Page_Text):
    #print('----------------------------------------------------')
    #print('--fn_04_CreateJSON')
    #print('PageNumber: ', PageNumber)
    #print('Page_Text:  ', Page_Text)
    
    # Adding elements one at a time
    Dict[PageNumber] = Page_Text
    '''
    Dict[2] = 'For'
    Dict[3] = 1
    print("\nDictionary after adding 3 elements: ")
    print(Dict)    
    '''




def fn_03_ReadPage(PageNumber):
    #print('----------------------------------------------------')
    #print('--fn_03_ReadPage')
    #print('--PageNumber = ', PageNumber)
    
    #LibroPath = 'Libro/El-Necronomicon_H.P_Lovecraft.pdf'
    
    # creating a pdf reader object
    #reader = PdfReader('example.pdf')
    reader = PdfReader(LibroPath)
        
    # getting a specific page from the pdf file
    #page = reader.pages[0]
    page = reader.pages[PageNumber]
        
    # extracting text from page
    Page_Text = page.extract_text()
    #print(Page_Text)   
    
    fn_04_CreateDictionary(PageNumber, Page_Text)
    
    


def fn_02_GetPageNumber(N_Total_Pages):
    #print('----------------------------------------------------')
    #print('--fn_02_GetText')
    #print('--N_Total_Pages = ', N_Total_Pages)
    
    for x in range(N_Total_Pages):
        #print(x)
        fn_03_ReadPage(x)



def fn_01_Get_Total_Pages():
    print('----------------------------------------------------')
    print('--fn_01_Get_Total_Pages')
    #LibroPath = 'Libro/El-Necronomicon_H.P_Lovecraft.pdf'
    
    # creating a pdf reader object
    #reader = PdfReader('example.pdf')
    reader = PdfReader(LibroPath)
    
    # printing number of pages in pdf file
    N_Total_Pages = len(reader.pages)
    print('number of pages in pdf file:    ',   N_Total_Pages   )
    return N_Total_Pages
    
   
print('----------------------------------------------------')
def main():
    N_Total_Pages = 0
    N_Total_Pages = fn_01_Get_Total_Pages()
    print('number of pages in pdf file:    ',   N_Total_Pages   )
    
    #Test
    #N_Total_Pages = 3
    
    fn_02_GetPageNumber(N_Total_Pages)
    
    #print('---------------> Dict    ',  Dict    )
    #print(Dict)
    #print(Json_data )
    fn_05_CreateJSON(Dict)
    
    
if __name__ == '__main__':
    main()       