'''
Created on Feb 9, 2023

@author: fponce
'''

import json


str_Line = '___________________________________________________ '
Str_JSON_File = 'Test.JSON'

#####===============================================================================================
#####===============================================================================================
def fn_03_DataFrame(dict_Txt):
    import pandas as pd
    print(str_Line , "fn_03_DataFrame", str_Line, " START")
    print('\t dict_Txt:', dict_Txt)


    print("Str_JSON_File " , Str_JSON_File)
    print("dict_Txt ", dict_Txt)
    
    Str_CSV_OutPut = 'TEST_OutPut.CSV'
    Str_CSV_OutPut = '.\\JSON\\'+Str_CSV_OutPut
    print("Str_CSV_OutPut " , Str_CSV_OutPut)
    
    
    #See. https://pbpython.com/pandas-list-dict.html
    df = pd.DataFrame(dict_Txt)    
    print(df)
    #df.to_csv (r'##_OutPut_01.csv', index = None)
    df.to_csv (Str_CSV_OutPut, index = None)

    
    
    print(str_Line , "fn_03_DataFrame", str_Line, " END")    
    
#####===============================================================================================
#####===============================================================================================
def fn_01_Read_JSON():
    print(str_Line , "fn_01_Read_JSON", str_Line, " START")
    Str_FileName_InPut =  r'.\\JSON\\'+Str_JSON_File
    
    print("Str_FileName_InPut = ", Str_FileName_InPut)
    
    #https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ 
    # Opening JSON file
    f = open(Str_FileName_InPut,)      
    data = json.load(f)      
    
    
    print('\t dat     : ', data)
    print('\t expand  : ', data['expand'])
    print('\t startAt : ', data['startAt'])
    #print('\t issues', data['issues'])

    
                 
    # Closing file    
    f.close
        
#####===============================================================================================
#####===============================================================================================
def fn_02_Read_JSON():
    print(str_Line , "fn_02_Read_JSON", str_Line, " START")
    Str_FileName_InPut =  r'.\\JSON\\'+Str_JSON_File
    
    print("Str_FileName_InPut = ", Str_FileName_InPut)
    
    #https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ 
    # Opening JSON file
    f = open(Str_FileName_InPut,)      
    # returns JSON object as
    # a dictionary
    data = json.load(f)      
    # Iterating through the json
    
    #print(data)
    #print(str_Line)
    #print(data['issues'])
    
    # list
    str_xxx = 'APEX'
    # Create line item objects.         #*********** TEST
    line_items = []                     #*********** TEST    
    Var_id = 0        
    for i in data['issues']:    
        Var_id = Var_id + 1
        print('-----------------for------data[issues]-----------------. START')
        v_id    =   i["id"]             #print("\t id          = ",   i["id"])   #Print
        v_key   =   i["key"]            #print("\t key         = ",   i["key"])   #Print
        v_self  =   i["self"]           
        #print("\t self        = ",   i["self"])   #Print
        #print(i["self"])
        v_fields_statuscategorychangedate   =   i["fields"]["statuscategorychangedate"] #print("\t fields - statuscategorychangedate    = ",   i["fields"]["statuscategorychangedate"]  )   #Print
        v_fields_created        =   i["fields"]["created"]          #print("\t fields -   - created  = ",   i["fields"]["created"]  )   
        rity_name    =   i["fields"]["priority"]["name"] #print("\t fields / priority / name  = ",   i["fields"]["priority"]["name"]  )
        v_flds_labels           =   i["fields"]["labels"]   #print("\t fields / labels /    = ",   i["fields"]["labels"]  )   
                
        v_flds_Assgn_AccntId    =   i["fields"]["assignee"]["accountId"]        #print("\t fields / assignee / accountId   = ",   i["fields"]["assignee"]["accountId"]  )
        v_flds_Assgn_email      =   i["fields"]["assignee"]["emailAddress"]     #print("\t fields / assignee /  emailAddress  = ",   i["fields"]["assignee"]["emailAddress"]  )
        v_flds_Assgn_DsplyNm    =   i["fields"]["assignee"]["displayName"]      #print("\t fields / assignee / displayName   = ",   i["fields"]["assignee"]["displayName"]  )
                
        v_flds_Stts_Nm          =   i["fields"]["status"]["name"]               #print("\t fields / status / name   = ",   i["fields"]["status"]["name"]  )
                
        v_flds_Crtr_AccntId     =   i["fields"]["creator"]["accountId"]         #print("\t fields / creator / accountId     = ",   i["fields"]["creator"]["accountId"]  )
        #print("\t fields / creator / emailAddress   = ",   i["fields"]["creator"]["emailAddress"]  )
        v_flds_Crtr_DsplayNm    =   i["fields"]["creator"]["displayName"]       #print("\t fields / creator / displayName   = ",   i["fields"]["creator"]["displayName"]  )            
                
        v_flds_Rprtr_AccntId    =   i["fields"]["reporter"]["accountId"]        #print("\t fields / reporter / accountId     = ",   i["fields"]["reporter"]["accountId"]  )
        #print("\t fields / reporter / emailAddress   = ",   i["fields"]["reporter"]["emailAddress"]  )
        v_flds_Rprtr_DsplyNm    =   i["fields"]["reporter"]["displayName"]      #print("\t fields / reporter / displayName   = ",   i["fields"]["reporter"]["displayName"]  )
            
        v_flds_Prgrss_Prgrss    =   i["fields"]["progress"]["progress"]         #print("\t fields / progress / progress   = ",   i["fields"]["progress"]["progress"]  )
        v_flds_Prgrss_Ttl       =   i["fields"]["progress"]["total"]            #print("\t fields / progress / total   = ",   i["fields"]["progress"]["total"]  )       
                
        v_flds_Isstp_Dsc        =   i["fields"]["issuetype"]["description"]     #print("\t fields / issuetype / description   = ",   i["fields"]["issuetype"]["description"]  )
        v_flds_Isstp_Nm         =   i["fields"]["issuetype"]["name"]            #print("\t fields / issuetype / name   = ",   i["fields"]["issuetype"]["name"]  )
                
        v_flds_Prjct_Id         =   i["fields"]["project"]["id"]                #print("\t fields / project / id   = ",   i["fields"]["project"]["id"]  )
        v_flds_Prjct_Ky         =   i["fields"]["project"]["key"]               #print("\t fields / project / key   = ",   i["fields"]["project"]["key"]  )
        v_flds_Prjct_Nm         =   i["fields"]["project"]["name"]              #print("\t fields / project / name   = ",   i["fields"]["project"]["name"]  )
                
        v_flds_Crtd             =   i["fields"]["created"]                      #print("\t fields / created /     = ",   i["fields"]["created"]  )
        v_flds_Updtd            =   i["fields"]["updated"]                      #print("\t fields / updated /     = ",   i["fields"]["updated"]  )
        v_flds_Smmry            =   i["fields"]["summary"]                      #print("\t fields / summary /     = ",   i["fields"]["summary"]  )
        #//////////////////////////////////////////////////////////////////////////////////////////////////////
        line_item = {'id': Var_id
                         ,  'v_id': v_id 
                         ,  'key': v_key
                         ,  'v_fields_statuscategorychangedate': v_fields_statuscategorychangedate
                         ,  'v_fields_created': v_fields_created
                         #,  'v_flds_priority_name': v_flds_priority_name
                         ,  'v_flds_labels': v_flds_labels
                         ,  'v_flds_Assgn_AccntId': v_flds_Assgn_AccntId
                         ,  'v_flds_Assgn_email': v_flds_Assgn_email
                         ,  'v_flds_Assgn_DsplyNm': v_flds_Assgn_DsplyNm
                         ,  'v_flds_Stts_Nm': v_flds_Stts_Nm        
                         ,  'v_flds_Crtr_AccntId': v_flds_Crtr_AccntId
                         ,  'v_flds_Crtr_DsplayNm': v_flds_Crtr_DsplayNm
                         ,  'v_flds_Rprtr_AccntId': v_flds_Rprtr_AccntId
                         ,  'v_flds_Rprtr_DsplyNm': v_flds_Rprtr_DsplyNm
                         ,  'v_flds_Prgrss_Prgrss': v_flds_Prgrss_Prgrss
                         ,  'v_flds_Prgrss_Ttl': v_flds_Prgrss_Ttl
                         ,  'v_flds_Isstp_Dsc': v_flds_Isstp_Dsc
                         ,  'v_flds_Isstp_Nm': v_flds_Isstp_Nm
                         ,  'v_flds_Prjct_Id': v_flds_Prjct_Id
                         ,  'v_flds_Prjct_Ky': v_flds_Prjct_Ky
                         ,  'v_flds_Prjct_Nm': v_flds_Prjct_Nm
                         ,  'v_flds_Crtd': v_flds_Crtd
                         ,  'v_flds_Updtd': v_flds_Updtd
                         ,  'v_flds_Smmry': v_flds_Smmry
                         #,  'str_Col_File_Source': str_Col_File_Source
                         ,  'id_test': str_xxx }
        line_items.append(line_item)                   
        print("line_items -->> ", line_items)                              
        #//////////////////////////////////////////////////////////////////////////////////////////////////////                 
    # Closing file    
    f.close
    print("line_items --> ", line_items)                                       #*********** TEST
    fn_03_DataFrame(line_items) 

#####===============================================================================================
#####===============================================================================================

def main():
    print(str_Line, "main")
    #----------------------------------------------    
    #----------------------------------------------
    fn_01_Read_JSON()
    fn_02_Read_JSON()
    print('\n\n\t------ Done :) \n\n')
    #----------------------------------------------
    #----------------------------------------------

if __name__ == "__main__":
    main()