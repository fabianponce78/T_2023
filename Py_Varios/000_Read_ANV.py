'''
Created on Feb 2, 2023

@author: fponce
'''
from sqlalchemy.sql.expression import false
'''
Created on Jan 24, 2023

@author: fponce
'''
import re
import csv


str_Line = '------------------------------------------------------------------------------------'


######################## Lambda. START
lmbd_Search_Num = lambda x: (re.search(r'[0-9]+', x)).group()
######################## Lambda. END


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################    
############################################################################################################################################
############################################################################################################################################
def fn_20_CSV_AddRow(item_replace):
    print(str_Line, ' fn_20_CSV_AddRow')
    
    
    Lst_2_Exclude = ['Las Estacas', 'Participantes']
    
    # using list comprehension
    # checking if string contains list element
    res = [ele for ele in Lst_2_Exclude if(ele in item_replace)]

    # print result
    print("Does string contain any list element : " + str(bool(res)))    
    
    if bool(res) == False:
    
        row = item_replace + '\n'
        
        print('-- ', row)
        
        #===========================================================================
        # # open the file in the write mode
        # #f = open('path/to/csv_file', 'w')
        # f = open('ANV_CSV.CSV', 'a')
        # 
        # # create the csv writer
        # writer = csv.writer(f)
        # 
        # # write a row to the csv file
        # writer.writerow(row)
        # 
        # # close the file
        # f.close()    
        #===========================================================================
        
        with open('ANV_CSV.CSV', 'a', encoding='utf-8') as f:
            f.write(row)
        f.close()
    
############################################################################################################################################    
def fn_03_ReadTXT():
    print(str_Line, ' fn_03_ReadTXT')
    
    
    #===========================================================================
    # print('------------------------------------------')
    # with open('ANV.txt' , encoding='UTF-8') as file:
    #     print(file.readline())
    #     print(file.readline(10))
    # file.close()
    # print('------------------------------------------')
    #===========================================================================
    
    print('------------------------------------------')
    with open('ANV.txt' , encoding='UTF-8') as file:
        for item in file:
            #print(item)
            #strip() function
            
            #print('-->', item.strip())
            #print('-->', len(item.strip())   )
            if len(item.strip()) > 0:
                #print('-->', item.strip())
                item_strip = item.strip()
                #print('-->', item_strip)
                item_replace = item_strip.replace(' F ', '|F|')
                item_replace = item_replace.replace(' M ', '|M|')                                                
                print('-->', item_replace)
                
                match = re.search(r'\d+', item_replace)
                if match:
                    # 👇️ First number found: 12
                    print('First number found:', match.group())
                    # 👇️ Index of first digit: 5
                    print('Index of first digit:', match.start())
                    
                    if match.start() > 1:
                        print('\t ---------------------')
                        N_Len_item_replace = len(item_replace)
                        print('\t N_Len_item_replace:  ', N_Len_item_replace )
                        
                        Str_Name = item_replace[0:match.start()].strip()    #Remove Space
                        #print('\t Name: ', item_replace[0:match.start()] )
                        print('\t Str_Name: ', Str_Name )
                        
                        Str_Item_2 = item_replace[match.start():N_Len_item_replace].strip() #Remove Space
                        
                        #print('\t Str 2:', item_replace[match.start():len(item_replace)] )
                        print('\t Str 2:', Str_Item_2 )
                        #item_replace = item_replace[0:match.start()] + '|' + item_replace[match.start():len(item_replace)]
                        
                        N_Len_Str_Item_2 = len(Str_Item_2)
                        print('\t N_Len_Str_Item_2: ', N_Len_Str_Item_2)
                        
                        Space_Index = Str_Item_2.find(' ')
                        print('\t Space_Index: ', Space_Index)
                        
                        Str_Age = Str_Item_2[0:Space_Index]
                        print('\t Str_Age: ', Str_Age)
                        
                        Str_Item_3 = Str_Item_2[Space_Index:N_Len_Str_Item_2].strip() #Remove Space
                        print('\t Str_Item_3: ', Str_Item_3)
                        
                        
                        #item_replace = Str_Name + '|' + Str_Item_2
                        item_replace = Str_Name + '|' + Str_Age + '|' + Str_Item_3
                        print('\t item_replace: ', item_replace )
                        print('\t ---------------------')
                        
                        fn_20_CSV_AddRow(item_replace)
                
                ###########
                
                
                try:
                    print('__ ', lmbd_Search_Num(item_replace))
                except AttributeError:
                    print('__ +' )
                ###########
                
    file.close()
    print('------------------------------------------')    

############################################################################################################################################
############################################################################################################################################    
def fn_02_ReadTXT():
    print(str_Line, ' fn_00_ReadTXT')
    
    
    print('------------------------------------------')
    file = open('ANV.txt' , encoding='UTF-8')
    print(file.read())
    file.close()
    print('------------------------------------------')

############################################################################################################################################
def fn_01_ReadTXT():
    print(str_Line, ' fn_00_ReadTXT')
    
    with open('ANV.txt' , encoding='UTF-8') as f:
        lines = [line for line in f]
        #print('--- ', lines)
        
    Lst_TXT = lines
    Lst_Busca = ['Ponce', '44', 'Sarabia Angeles Reeva Orli 8 00 - 08 F AC Swim\n']
    
    print('- Lst_TXT: ', Lst_TXT)
    print('- Lst_Busca: ', Lst_Busca)
    
    a_set = set(Lst_TXT)  # convert list to set
    b_set = set(Lst_Busca) 
    
    print('\n')
    print('- Lst_TXT: ', Lst_TXT)
    print('- Lst_Busca: ', Lst_Busca)    
    
    
    
    matches = a_set.intersection(b_set)

    print('matches : ', matches)

    print(list(matches)) # if you want a list instead of a set        
    
############################################################################################################################################    
def fn_00_ReadTXT():
    print(str_Line, ' fn_00_ReadTXT')
    

    
    with open('ANV.txt' , encoding='UTF-8') as f:
                
        lines = [line for line in f]
        print('--- ', lines)
        
     
    print(lines)
    print('********************************************')
    
    #print(list(filter(lambda x: '45 - 49 M' in x, lines)))
    #print(list(filter(lambda x: '40 - 44 M' in x, lines)))
    
    print(list(filter(lambda x: '45 - 49 F' in x, lines)))
    print(list(filter(lambda x: '40 - 44 F' in x, lines)))
    print(list(filter(lambda x: 'Zamudio' in x, lines)))
    
    
    
    #===========================================================================
    # print('********************************************')
    # if '45 - 49' in str(lines):
    #     print('zz')
    #     print(str(lines))
    #===========================================================================
    
    #===========================================================================
    # # removing the new line characters
    # with open('ANV.txt' , encoding='UTF-8') as f:
    #     lines = [line.rstrip() for line in f]        
    # print(lines)
    #===========================================================================
    
    
#===============================================================================
#     print('********************************************')
#     #A compact way to find multiple strings in another list of strings is to use set.intersection. 
#     #This executes much faster than list comprehension in large sets or lists.
#     astring = ['abc','def','ghi','jkl','mno']
#     bstring = ['def', 'jkl']
#     a_set = set(astring)  # convert list to set
#     b_set = set(bstring)
#     matches = a_set.intersection(b_set)
# 
#     print('matches : ', matches)
# 
#     print(list(matches)) # if you want a list instead of a set
#     
#     print('********************************************')
#===============================================================================

############################################################################################################################################
############################################################################################################################################
def fn_000_CreateCSV():
    print(str_Line, ' fn_00_ReadTXT')
    

    row = 'Name|Age|Category|Genre|Team' + '\n'
    
    with open('ANV_CSV.CSV', 'w', encoding='utf-8') as f:
        f.write(row)
    f.close()
    
    #===========================================================================
    # # open the file in the write mode
    # #f = open('path/to/csv_file', 'w')
    # f = open('ANV_CSV.CSV', 'w')
    # 
    # # create the csv writer
    # writer = csv.writer(f)
    # 
    # # write a row to the csv file
    # writer.writerow(row)    #Add Header
    # 
    # # close the file
    # f.close()    
    #===========================================================================
     
    
   


############################################################################################################################################
############################################################################################################################################
def main():
    fn_000_CreateCSV()
    #fn_00_ReadTXT()  ## !!! :)
    ###fn_01_ReadTXT()
    #fn_02_ReadTXT()
    fn_03_ReadTXT()



if __name__ == '__main__':
    main()  