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


def fn_05_WriteFile(Str_Text):
    print('fn_05_WriteFile  = ', Str_Text)
    with open('#_ObsTri_Output_B.txt', 'a', encoding='utf-8') as f:
        f.write(Str_Text)    

def fn_04_Clean_KeyWords(Str_Text):
    #print('Str_Text = ', Str_Text)
    
    Str_lista_1 = ['menu', 'feed', 'News', 'sports_esports', 'live_tv']
    Str_lista_2 = ['Fantasy', 'emoji_events', 'Obsessed Triathlete', 'Live', 'close']
    Str_lista_3 = ['format_list_numbered', 'Rankings','image','Medias','All Medias','Import', 'Races']
    Str_lista_4 = ['construction', 'Tools', 'search', 'Search', 'Log In', 'email']
    Str_lista_5 = ['Contact Us', 'Twitter', 'Discord', 'arrow_back']
    Str_lista_6 = ['Clear', 'military_tech']
    Str_lista_X = Str_lista_1 + Str_lista_2 + Str_lista_3 + Str_lista_4 + Str_lista_5 + Str_lista_6
    
    #Str_lista_IronMan = ['IRONMAN', 'YYYY']
    
    #print('Str_lista_X = ', Str_lista_X)
    
    if Str_Text not in Str_lista_X:
        #print('Str_Text = ', Str_Text)
        Str_Text = Str_Text + ' | '
        #print(Str_Text)
        is_IronMan = Str_Text.find('IRONMAN')
        print('is_IronMan = ', is_IronMan)
        if is_IronMan > 0:
            Str_Text = '\n' + Str_Text + '|'
            #print('IM', Str_Text)
            fn_05_WriteFile(Str_Text)
        else:
            #print('OK', Str_Text)
            fn_05_WriteFile(Str_Text)
            
        
        
          
        

def fn_03_CleanTags_B(str_A):
    #print('------------fn_03_CleanTags_B')
    #print(str_A)
    N_CharIndex_OpenTag = str_A.find('(')
    #print('\t    <'   ,    N_CharIndex_OpenTag )
        
    if N_CharIndex_OpenTag >= 0:
        #print('\t    <')
        #print('\t\t    < N_CharIndex_OpenTag =  '   ,    N_CharIndex_OpenTag )
        N_CharIndex_CloseTag = str_A.find(')')
        #print('\t\t    > N_CharIndex_CloseTag = ', N_CharIndex_CloseTag)
        if N_CharIndex_CloseTag > 0:
            #print('\t    >'   ,    N_CharIndex_CloseTag )
            Str_Tags = str_A[N_CharIndex_OpenTag:N_CharIndex_CloseTag+1]
            #print('\t\t   ... String with Tags: ', Str_Tags )
                    
    else:
        #print('--------------???---------')
        #print('---> ', str_A)
        fn_04_Clean_KeyWords(str_A)    
        


def fn_02_CleanTags_A(str_A):
    #print('------------fn_02_CleanTags_A')
    #print(str_A)
    N_CharIndex_OpenTag = str_A.find('<')
    #print('\t    <'   ,    N_CharIndex_OpenTag )
        
    if N_CharIndex_OpenTag >= 0:
        #print('\t    <')
        #print('\t\t    < N_CharIndex_OpenTag =  '   ,    N_CharIndex_OpenTag )
        N_CharIndex_CloseTag = str_A.find('>')
        #print('\t\t    > N_CharIndex_CloseTag = ', N_CharIndex_CloseTag)
        if N_CharIndex_CloseTag > 0:
            #print('\t    >'   ,    N_CharIndex_CloseTag )
            Str_Tags = str_A[N_CharIndex_OpenTag:N_CharIndex_CloseTag+1]
            #print('\t\t   ... String with Tags: ', Str_Tags )
                    
    else:
        #print('--------------???---------')
        #print('---> ', str_A)
        fn_03_CleanTags_B(str_A)
    

def fn_01_ReadHTML():
    i = 0
    with open('#_ObsTri_Output_A.HTML', encoding='utf8') as f:
        for line in f:
            i = i + 1
            #print('i =', i)
            #print(line.strip())
            
            str_A = line.strip()
            
            fn_02_CleanTags_A(str_A) ## Clean Tags <, >
             
    #===========================================================================
    #         N_CharIndex_OpenTag = str_A.find('<')
    #         #print('\t    <'   ,    N_CharIndex_OpenTag )
    # 
    # 
    #         if N_CharIndex_OpenTag >= 0:
    #             #print('\t    <')
    #             #print('\t\t    < N_CharIndex_OpenTag =  '   ,    N_CharIndex_OpenTag )
    #             N_CharIndex_CloseTag = str_A.find('>')
    #             #print('\t\t    > N_CharIndex_CloseTag = ', N_CharIndex_CloseTag)
    #             if N_CharIndex_CloseTag > 0:
    #                 #print('\t    >'   ,    N_CharIndex_CloseTag )
    #                 Str_Tags = str_A[N_CharIndex_OpenTag:N_CharIndex_CloseTag+1]
    #                 #print('\t\t   ... String with Tags: ', Str_Tags )
    #                 
    #         else:
    #             #print('--------------???---------')
    #             #print(line.strip())
    #             fn_02_Clean(line.strip())
    # 
    #         #print('------')
    #===========================================================================

def main():
    fn_01_ReadHTML()



if __name__ == '__main__':
    main()        