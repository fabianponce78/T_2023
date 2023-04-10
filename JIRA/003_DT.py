'''
Created on Oct 13, 2021

@author: Fabian Ponce
'''
import pandas as pd
from csv import reader


Str_Line = '____________________________________________________ '

#Str_FileNAme_JIRA ='.\OutPut\JIRA.CSV'
#Str_FileNAme_SPRINT ='.\OutPut\SPRINT.CSV'
Str_FileNAme_DT ='.\OutPut\DT.CSV'
Str_FileNAme_DT2 ='.\OutPut\DT2.CSV'


#####================================================================================
#####================================================================================

def fn_F1_File_Create():
    print(Str_Line, 'fn_1B_Create_File')
    f = open(Str_FileNAme_DT, "w")
    #f.write("Woops! I have deleted the content!")
    #f.write("DT")
    f.close()

def fn_F2_File_AddRow(Str_Row):
    print(Str_Line, 'fn_1B_Create_File')
    #print(Str_Row)
    
    #Str_Add_Row = '\n' + Str_Row
    Str_Add_Row = Str_Row + '\n'
    
    f = open(Str_FileNAme_DT, "a+")
    #f.write("Woops! I have deleted the content!")
    f.write(Str_Add_Row)
    f.close()   

#####================================================================================
#####================================================================================

def fn_L1_Load_SPRINT_CSV():
    print(Str_Line , "fn_2_Load_SPRINT_CSV")
    Str_FileNAme_IN ='.\OutPut\Sprint_Sprint.CSV'
    Str_FN_SPRINT ='.\OutPut\SPRINT.CSV'

    # iterate over each line as a ordered dictionary and print only few column by column Number
    with open(Str_FN_SPRINT, 'r') as read_obj:
        csv_reader = reader(read_obj, delimiter='|')
        next(csv_reader, None)  # skip the headers
        line_count = 0
        for row in csv_reader:
            #print(row)
            print(row[0])
            fn_F2_File_AddRow(row[0])


#####================================================================================        
#####================================================================================

def fn_L2_Load_JIRA_CSV():
    print(Str_Line , "fn_2_Load_SPRINT_CSV")
    Str_FN_JIRA ='.\OutPut\JIRA.CSV'

    # iterate over each line as a ordered dictionary and print only few column by column Number
    with open(Str_FN_JIRA, 'r') as read_obj:
        csv_reader = reader(read_obj, delimiter='|')
        next(csv_reader, None)  # skip the headers
        line_count = 0
        for row in csv_reader:
            #print(row)
            Str_A = row[13]
            Str_A = Str_A[0:10]
            #print(row[13] , '--->' , Str_A)
            fn_F2_File_AddRow(Str_A)
            
#####================================================================================
#####================================================================================

def fn_Remove_Duplicate():
    print(Str_Line , "fn_Remove_Duplicate")
    #Str_FileNAme_DT2
    with open(Str_FileNAme_DT) as result:
            uniqlines = set(result.readlines())
            with open(Str_FileNAme_DT2, 'w') as rmdup:
                rmdup.writelines(set(uniqlines))    
#####================================================================================
#####================================================================================

def main():
    print(Str_Line , "main")
    #----------------------------------------------
    #----------------------------------------------
    #----------------------------------------------
    fn_F1_File_Create()
    
    fn_L1_Load_SPRINT_CSV()
    fn_L2_Load_JIRA_CSV()
    
    fn_Remove_Duplicate()
    #----------------------------------------------

if __name__ == "__main__":
    main()