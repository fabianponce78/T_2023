
'''
Created on Jul 23, 2021

@author: Fabian Ponce
'''

import pyodbc 
import time
import pandas as pd


str_Linea = '__________________________________________________'
str_OutPut = '.\OutPut\#_JIRA_STORIES.CSV'


def fn_TIME():
    print(str_Linea, 'fn_TIME - START')
    time.sleep(2)
    print(str_Linea, 'fn_TIME - END')
    
def fn_1B_File_Create():
    print(str_Linea, 'fn_1B_Create_File')
    f = open(str_OutPut, "w")
    #f.write("Woops! I have deleted the content!")
    f.write("[DT],[DT_SPRINT],[SPRINT],[Issue_Type],[Summary],[Key],[Assignee],[Reporter],[Priority],[Status],[Resolution],[Created],[Updated],[Due_date],[parent],[Resolved],[Status_Category_Changed],[Linked_Issues],[Parent_Link]")
    f.close()

def fn_2B_File_AddRow(Str_Row):
    print(str_Linea, 'fn_1B_Create_File')
    print(Str_Row)
    
    Str_Add_Row = '\n' + Str_Row
    
    f = open(str_OutPut, "a+")
    #f.write("Woops! I have deleted the content!")
    f.write(Str_Add_Row)
    f.close()        


def fn_1_BULK():
    print(str_Linea, 'fn_1_BULK')
    Query_SP_1 = 'EXEC SP_BULK'
    print('--> EXEC SP_BULK')
    
    '''
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=DESKTOP-C1P2GG2;'
                          'Database=JIRA;'
                          'Trusted_Connection=yes;')
    '''
    #server = r"DESKTOP-C1P2GG2"
    server = r"MDC-DCMW8C3"
    
    db = "JIRA"
    user = "sa"
    password = "123456"
        
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server + ';DATABASE=' + db +';UID=' + user + ';PWD=' + password)
    cursor = conn.cursor()
    #cursor.execute('exec [dbo].[SP_VW_SALES] 5,10')
      
    
    cursor.execute(Query_SP_1)            
    cursor.commit()
       
    cursor.close()
    conn.close()
    
def fn_2_SQL_2_CSV():    
    print(str_Linea, 'fn_2_SQL_2_CSV')
    
    Query_SP_1 = 'select * FROM [dbo].[V_JIRA_STORIES] order by DT'

    server = r"DESKTOP-C1P2GG2"
    db = "JIRA"
    user = "sa"
    password = "123456"
        
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server + ';DATABASE=' + db +';UID=' + user + ';PWD=' + password)
                           
    cursor = conn.cursor()
    #cursor.execute('exec [dbo].[SP_VW_SALES] 5,10')
    
    Str_Row = ''
    
                

    cursor.execute(Query_SP_1)
    lineas = cursor.fetchall()    
    for l in lineas:
        
        '''
        print(l[0])
        print(l[1])
        print(l[2])        
        print(l[3])
        print(l[4])
        print(l[5])
        print(l[6])
        print(l[7])
        print(l[8])
        print(l[9])
        print(l[10])
        print(l[11])
        print(l[12])
        print(l[13])
        print(l[14])
        print(l[15])
        print(l[16])
        print(l[17])
        print(l[18])
        '''
  
        
        
        DT = l[0]
        print('DT = ', DT)
        
        DT_SPRINT = l[1]
        print('DT_SPRINT = ', DT_SPRINT)

        SPRINT = l[2]
        print('SPRINT = ', SPRINT)
                
        Issue_Type = l[3]
        print('Issue_Type = ', Issue_Type)
        
        Summary = l[4]
        #Summary = Summary.replace(',', '')
        #Summary = Summary.replace('-', '')
        print('Summary = ', Summary)
        '''
        Key = l[5]
        Assignee = l[6]
        Reporter = l[7]
        Priority = l[8]
        Status = l[9]
        Resolution = l[10]
        Created = l[11]
        Updated = l[12]
        Due_date = l[13]
        parent = l[14]
        Resolved = l[15]
        Status_Category_Changed = l[16]
        Linked_Issues = l[17]
        Parent_Link = l[18]      
        '''
        
        
        
        #print(' Key ', Key)
    
        '''
        Str_Row = DT + ', ' +   DT_SPRINT + ', ' + SPRINT + ', ' + Issue_Type + ', ' + Summary + ', ' + Key
        Str_Row = Str_Row + ', ' + Assignee + ', ' + Reporter + ', ' + Priority + ', ' + Status + ', ' + Resolution
        Str_Row = Str_Row + ', ' + Created + ', ' + Updated + ', ' + Due_date + ', ' + parent + ', ' + Resolved
        Str_Row = Str_Row + ', ' + Status_Category_Changed + ', ' + Linked_Issues + ', ' + Parent_Link 
        '''
        print('Str_Row = ', Str_Row)
        #fn_2B_File_AddRow(Str_Row)

        

        
    
    '''
    df = pd.DataFrame(cursor.execute(Query_SP_1))
    df.to_csv (str_OutPut, index = False) # place 'r' before the path name
    '''
            
    
    
                
    cursor.commit()
       
    cursor.close()
    conn.close()    
    


def main():
    print("-------------------------------------------------")
    #----------------------------------------------
    #----------------------------------------------
    #----------------------------------------------
    fn_1_BULK()
    #fn_TIME()
    fn_1B_File_Create()
    #fn_2_SQL_2_CSV()
    print('\t DONE...')

    #----------------------------------------------

if __name__ == "__main__":
    main()
