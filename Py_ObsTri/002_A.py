'''
Created on Jan 18, 2023

@author: fponce
'''

# Importing BeautifulSoup class from the bs4 module
 


####-----------------------------------------------------------
####-----------------------------------------------------------
#===============================================================================
# # Opening the html file
# HTMLFile = open("#_ObsTri_Output_A.HTML", "r")
# 
# # Reading the file
# HTML_content = HTMLFile.read()
# 
# 
# #print(HTML_content)
#===============================================================================
####-----------------------------------------------------------
####-----------------------------------------------------------
i = 0
with open('#_ObsTri_Output_A.HTML', encoding='utf8') as f:
    for line in f:
        i = i + 1
        print('i =', i)
        #print(line.strip())
        
        str_A = line.strip()
         
        N_CharIndex_OpenTag = str_A.find('<')
        #print('\t    <'   ,    N_CharIndex_OpenTag )


        if N_CharIndex_OpenTag >= 0:
            #print('\t    <')
            print('\t\t    < N_CharIndex_OpenTag =  '   ,    N_CharIndex_OpenTag )
            N_CharIndex_CloseTag = str_A.find('>')
            print('\t\t    > N_CharIndex_CloseTag = ', N_CharIndex_CloseTag)
            if N_CharIndex_CloseTag > 0:
                #print('\t    >'   ,    N_CharIndex_CloseTag )
                print('\t\t   ... String with Tags: ',   str_A[N_CharIndex_OpenTag:N_CharIndex_CloseTag+1])
        else:
            print('--------------???---------')
            print(line.strip())
            
            
            
 
        
        print('------')