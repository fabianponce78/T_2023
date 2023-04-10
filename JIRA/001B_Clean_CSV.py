'''
Created on Oct 27, 2021

@author: Fabian Ponce
'''
from csv import reader


var_Line = '___________________________'
str_OutPut = '.\OutPut\JIRA_2.CSV'


def fn_2_Load_JIRA_CSV(str_String):
    print(var_Line, ' fn_2_Load_JIRA_CSV')
    print(str_String)


def fn_1_Load_JIRA_CSV():
    print(var_Line, ' fn_1_Load_JIRA_CSV')
    Str_FileNAme_In ='.\OutPut\JIRA.CSV'
    # open file in read mode
    str_String = ''
    with open(Str_FileNAme_In, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            #print(row)
            
            str_String = list(map(lambda st: str.replace(st, "-", " "), row))
            str_String = list(map(lambda st: str.replace(st, ",", " "), str_String))
            str_String = list(map(lambda st: str.replace(st, "\"", " "), str_String))
            
            #print(str_String)
            fn_2_Load_JIRA_CSV(str_String)
            

def fn_1B_File_Create():
    print(str_Linea, 'fn_1B_Create_File')
    f = open(str_OutPut, "w")
    #f.write("Woops! I have deleted the content!")
    f.write("[DT],[DT_SPRINT],[SPRINT],[Issue_Type],[Summary],[Key],[Assignee],[Reporter],[Priority],[Status],[Resolution],[Created],[Updated],[Due_date],[parent],[Resolved],[Status_Category_Changed],[Linked_Issues],[Parent_Link]")
    f.close()
            
            

def main():
    print("-------------------------------------------------")
    #----------------------------------------------
    #----------------------------------------------
    #----------------------------------------------
    fn_1B_File_Create
    fn_1_Load_JIRA_CSV()
    #----------------------------------------------

if __name__ == "__main__":
    main()