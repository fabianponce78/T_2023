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

Str_InPut_File = 'ANV_Resultados.TXT'
Str_OutPut_File = 'ANV_Resultados_CSV.CSV'
Lst_2_Exclude = ['Las Estacas', 'Participantes', 'DISTANCIA SEXO CATEGORIA']

str_Line = '------------------------------------------------------------------------------------'


######################## Lambda. START
lmbd_Search_Num = lambda x: (re.search(r'[0-9]+', x)).group()
######################## Lambda. END


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################    
############################################################################################################################################
############################################################################################################################################
def fn_20_CSV_AddRow(item):    
    print(str_Line, ' fn_20_CSV_AddRow')
    #print('__ item : ', item)

    row = item + '\n'        
    print('-- ', row)
        
    with open(Str_OutPut_File, 'a', encoding='utf-8') as f:
        f.write(row)
    f.close()
    '''    
    Lst_2_Exclude = ['DISTANCIA SEXO CATEGORIA']    
    # using list comprehension
    # checking if string contains list element
    res = [ele for ele in Lst_2_Exclude if(ele in item_replace)]
    # print result
    print("Does string contain any list element : " + str(bool(res)))    
    
    if bool(res) == False:    
        row = item_replace + '\n'        
        print('-- ', row)
        
        with open(Str_OutPut_File, 'a', encoding='utf-8') as f:
            f.write(row)
        f.close()
        '''
    


############################################################################################################################################
def fn_05_Participante(Str_Competidor):
    print(str_Line, ' fn_05_Participante')
    print('\t Str_Competidor: ', Str_Competidor)        
    Lst_Teams_1 = ['anv Interlomas', 'anv Plaza Central', 'anv Interlomas', 'La Loma QRO', 'anv Santa Fe', 'Deportivo Salba', 'anv San Jeronimo', 'anv Lindavista']
    Lst_Teams_2 = ['anv Satelite', 'anv C. de Entrenamiento', 'anv Coyoacan', 'anv Puebla', 'anv Z. Esmeralda', 'anv Coapa']
    Lst_Teams_3 = ['Alpha swimmer HXQ', 'SportCity', 'anv Centenario', 'Club de Golf Bellavista']
    Lst_Teams = Lst_Teams_1 + Lst_Teams_2 + Lst_Teams_3
    
    #print('Lst_Teams: ', Lst_Teams)
    
    res = [ele for ele in Lst_Teams if(ele in Str_Competidor)]
    # print result
    #print("Does string contain any list element : " + str(bool(res)))
    
    if bool(res) != False:
        #print('-----------------------------------------------')
        Str_Competidor = Str_Competidor.replace('anv Interlomas','|anv Interlomas')
        Str_Competidor = Str_Competidor.replace('anv Plaza Central','|anv Plaza Central')
        Str_Competidor = Str_Competidor.replace('anv Interlomas','|anv Interlomas')
        Str_Competidor = Str_Competidor.replace('La Loma QRO','|La Loma QRO')
        Str_Competidor = Str_Competidor.replace('anv Santa Fe','|anv Santa Fe')
        Str_Competidor = Str_Competidor.replace('Deportivo Salba','|Deportivo Salba')
        Str_Competidor = Str_Competidor.replace('anv San Jeronimo','|anv San Jeronimo')
        Str_Competidor = Str_Competidor.replace('anv Lindavista','|anv Lindavista')
        Str_Competidor = Str_Competidor.replace('anv Satelite','|anv Satelite')
        Str_Competidor = Str_Competidor.replace('anv C. de Entrenamiento','|anv C. de Entrenamiento')
        Str_Competidor = Str_Competidor.replace('anv Coyoacan','|anv Coyoacan')
        Str_Competidor = Str_Competidor.replace('anv Puebla','|anv Puebla')
        Str_Competidor = Str_Competidor.replace('anv Z. Esmeralda','|anv Z. Esmeralda')
        Str_Competidor = Str_Competidor.replace('anv Coapa','|anv Coapa')
        Str_Competidor = Str_Competidor.replace('Alpha swimmer HXQ','|Alpha swimmer HXQ')
        Str_Competidor = Str_Competidor.replace('SportCity','|SportCity')
        Str_Competidor = Str_Competidor.replace('anv Centenario','|anv Centenario')
        Str_Competidor = Str_Competidor.replace('Club de Golf Bellavista','|Club de Golf Bellavista')
        #Str_Competidor = Str_Competidor.replace(',','|')
        #Str_Competidor = Str_Competidor.replace('xxxxx','|xxx')

        
        #print('\t\t Str_Competidor: ', Str_Competidor)
        #print('-----------------------------------------------')
    #else:
        #print('\t Str_Competidor: ', Str_Competidor)
        
    #print('\t\t Str_Competidor: ', Str_Competidor)
    
    N_Name = Str_Competidor.find(', ')
    N_Len_Str_Competidor = len(Str_Competidor)
    #print('N_Name: ', N_Name)
    #print('N_Len_Str_Competidor: ', N_Len_Str_Competidor)
    
    str_A = Str_Competidor[0:N_Name]
    str_B = Str_Competidor[N_Name+2:N_Len_Str_Competidor]
    str_C = str_A.strip() + '|' + str_B.strip()
    
    '''
    print('____: str_A = ', str_A)
    print('____: str_B = ', str_B)
    
    print('____: str_C = ', str_C)
    '''
    
    #fn_20_CSV_AddRow(str_C)
    
        
    


        
    
############################################################################################################################################    
def fn_04_ReadTXT():
    print(str_Line, ' fn_04_ReadTXT')            
    #print('------------------------------------------')
    with open(Str_InPut_File , encoding='UTF-8') as file:
        for item in file:
            #print(item)
            
            if ',' in item: 
                #Lugar|Numero|Apellido,Nombre|Edad|Fecha De NAcimiento|Equipo|Tiempo
                #24 11 Sanchez Hernandez, Bruno Iván Deportivo Salba 5 06 - Mar - 2017                
                #print(item) #24 11 Sanchez Hernandez, Bruno Iván Deportivo Salba 5 06 - Mar - 2017
                item = item.strip()
                
                #Find 1st. spaced " "
                N_1st_Space = item.find(" ")
                N_Item_Len = len(item.strip())
                #print('__ N_1st_Space ',   N_1st_Space)
                #print('__ N_Item_Len ',   N_Item_Len)
                
                Str_Lugar = item[0:N_1st_Space]
                Str_2ndPart = item[N_1st_Space:N_Item_Len].strip()
                
                #print('\t__ Str_Lugar:'   , Str_Lugar      )
                #print('__ Str_2ndPart: ' , Str_2ndPart    )
                
                #Find 2nd. spaced " "
                N_2nd_Space = Str_2ndPart.find(" ")
                #print('__ N_2nd_Space : ',   N_2nd_Space)
                
                Str_Num_Participante = Str_2ndPart[0:N_2nd_Space]
                #print('\t__ Str_Num_Participante:'   , Str_Num_Participante      )
                
                Str_3rd_Part = Str_2ndPart[N_2nd_Space:N_Item_Len]
                #print('__ Str_3rd_Part: ' , Str_3rd_Part    )
                
                print('Str_3rd_Part = ', Str_3rd_Part)
                
                try:
                    #print('__ ', lmbd_Search_Num(Str_3rd_Part))
                    Str_Edad = ' ' + lmbd_Search_Num(Str_3rd_Part) + ' '
                    Str_Edad_Pipe = '|' + lmbd_Search_Num(Str_3rd_Part) + '|'   ## -->    '|7|'
                    Str_Edad_X =  Str_3rd_Part.replace(Str_Edad,Str_Edad_Pipe)      
                    #print('\t__ Str_Edad_X:'   , Str_Edad_X      )
                    
                    N_Str_Edad_X = Str_Edad_X.find(Str_Edad_Pipe)
                    #print('_**', N_Str_Edad_X )
                    
                    N_Len_Str_Edad_Pipe = len(Str_Edad_Pipe) 
                    #print('_N_Len_Str_Edad_Pipe : ', N_Len_Str_Edad_Pipe)
                    Str_Dt_Birth = Str_Edad_X[N_Str_Edad_X+N_Len_Str_Edad_Pipe:N_Item_Len].strip()
                    #print('\t__ Str_Dt_Birth : ', Str_Dt_Birth)
                    
                    ##### Str_3rd_Part = Mancini Bañuelos, Moises anv Interlomas 7 24 - Jan - 2016
                    ##### Str_Edad_X = Mancini Bañuelos, Moises anv Interlomas|7|24 - Jan - 2016
                    N_1st_Pipe = Str_Edad_X.find('|')
                    N_Len_Str_Edad_X = len(Str_Edad_X)
                    #print('N_1st_Pipe = ', N_1st_Pipe )
                    #print('N_Len_Str_Edad_X = ', N_Len_Str_Edad_X )
                    
                    Str_LastName_And_Team = Str_Edad_X[0:N_1st_Pipe]
                    #Str_LastName_And_Team = Str_LastName_And_Team.replace(', ', '|')
                    #print('Str_LastName_And_Team : ', Str_LastName_And_Team)
                    
                except AttributeError:
                    print('__ +' )
                
                
                #item = Str_Lugar + '|' + Str_2ndPart
                #print('__ item: ', item) 
                
                
                #print('++++++++++++++++++++++++++++++++++++++++++')
                print('\t__ Str_Lugar:'   , Str_Lugar      )
                print('\t__ Str_Num_Participante:'   , Str_Num_Participante      )
                print('\t__ Str_FullName_Team:', Str_LastName_And_Team)
                print('\t__ Str_LastName:')
                print('\t__ Team:')
                print('\t__ Age: ', Str_Edad)
                print('\t__ Date of birth:', Str_Dt_Birth)
                
                Str_Competidor = Str_Lugar.strip()
                Str_Competidor = Str_Competidor +'|' + Str_Num_Participante.strip()
                Str_Competidor = Str_Competidor +'|' + Str_LastName_And_Team.strip()
                Str_Competidor = Str_Competidor +'|' + Str_Edad.strip()
                Str_Competidor = Str_Competidor +'|' + Str_Dt_Birth.strip()
                
                
                print('\t... ', Str_Competidor)
                #fn_05_Participante(Str_Competidor)
                
                print('++++++++++++++++++++++++++++++++++++++++++')
                
            
            '''
            if len(item.strip()) > 0:
                #print('-->', item.strip())
                item_strip = item.strip()
                
                Str_out = item_strip
                fn_20_CSV_AddRow(Str_out)
                #print('-->', item_strip)
                #item_replace = item_strip.replace(', ', '|')                                                
                #print('-->', item_replace)      
            '''      
            
            '''
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
                        
                        #fn_20_CSV_AddRow(item_replace)
                
                ###########
                
                
                try:
                    print('__ ', lmbd_Search_Num(item_replace))
                except AttributeError:
                    print('__ +' )
                ###########
             '''   
    file.close()
    print('------------------------------------------')    

############################################################################################################################################
############################################################################################################################################    
############################################################################################################################################    
def fn_03_ReadTXT():
    print(str_Line, ' fn_03_ReadTXT')
            
    print('------------------------------------------')
    with open(Str_InPut_File , encoding='UTF-8') as file:
        for item in file:
            print(item)
            '''
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
                        
                        #fn_20_CSV_AddRow(item_replace)
                
                ###########
                
                
                try:
                    print('__ ', lmbd_Search_Num(item_replace))
                except AttributeError:
                    print('__ +' )
                ###########
             '''   
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
    
    with open(Str_InPut_File , encoding='UTF-8') as f:
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
    

    
    with open(Str_InPut_File , encoding='UTF-8') as f:
                
        lines = [line for line in f]
        print('--- ', lines)
        
     
    print(lines)
    print('********************************************')
    
    #print(list(filter(lambda x: '45 - 49 M' in x, lines)))
    #print(list(filter(lambda x: '40 - 44 M' in x, lines)))
    
    print(list(filter(lambda x: '45 - 49 F' in x, lines)))
    print(list(filter(lambda x: '40 - 44 F' in x, lines)))
    print(list(filter(lambda x: 'Zamudio' in x, lines)))
    
    
    


############################################################################################################################################
############################################################################################################################################
def fn_000_CreateCSV():
    print(str_Line, ' fn_00_ReadTXT')    
    #Lugar|Numero|Apellido,Nombre|Edad|Fecha De NAcimiento|Equipo|Tiempo
    row = 'Lugar|Numero|Apellido,Nombre|Edad|Fecha De NAcimiento|Equipo|Tiempo' + '\n'
    
    with open(Str_OutPut_File, 'w', encoding='utf-8') as f:
        f.write(row)
    f.close()
    

############################################################################################################################################
############################################################################################################################################
def main():
    fn_000_CreateCSV()
    #fn_03_ReadTXT()
    fn_04_ReadTXT()



if __name__ == '__main__':
    main()  