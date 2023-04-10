# coding=utf8

from csv import reader
import pyodbc 


str_Line = '___________________________________________________________'


def fn_02_SQL(row):
    print(str_Line, 'fn_02_SQL')
    print(row)
    print(row[0])

    Query_Inter = 'INSERT INTO [dbo].[RPT_ACCOUNT_COMPLIANCE_COLLECTION_FULL] \
    ([DATABASE_INSTANCE_UID]  \
    ,[DATABASE_INSTANCE_PARENT_UID] \
    ,[DATABASE_UID] \
    ,[ACCOUNT_UID] \
    ,[Tier_1]    ,[Tier_2]    ,[Tier_3]    ,[Tier_4]    ,[Tier_5] \
    ,[Portfolio] \
    ,[Portfolio_Owner] \
    ,[IT_Service]    ,[IT_Service_Owner]    ,[IT_Service_Owner_Email]    ,[IT_Sevice_Status] \
    ,[Application_Package]    ,[Application_Package_Status]    ,[Application_Deployment]     ,[Application_Deployment_Status]\
    ,[Integrity_Rating]    ,[Availability_Rating]    ,[Confidentiality_Rating]     ,[Derived_Integrity_Rating] \
    ,[Derived_Availability_Rating]    ,[Derived_Confidentiality_Rating]    \
    ,[Sarbanes_Oxley_Scoped]    ,[Application_Deployment_Environment]    ,[Cloud_Environment]    \
    ,[Operating_Environment]    ,[Operating_Region]    \
    ,[DBaaS_Product]    ,[Support_Supplier]    \
    ,[Database_Instance_Name]    ,[Database_Instance_Type]    ,[Database_Instance_Record_Status]    ,[Database_Instance_Parent_Name]    \
    ,[Software_Product]    \
    ,[Report_Run_Date]    \
    ,[Database_Instance_Account]    ,[Database_Name]    \
    ,[Account_Creation_Date]        ,[Registered_in_DBaaS_Directory]    ,[Account_Managed_By]    ,[Audit_Category]    ,[Account_Login_Level]    \
    ,[Discovered_Privilege_Level]    ,[Account_Status]    ,[Account_Status_Date]    ,[Account_Authenticiation_Type]    ,[Account_User_Type]    ,[Audit_Category_Password_Expiry_Days]    \
    ,[Last_Password_Reset_Date]    ,[Password_Age_Days]    ,[Password_Expired]    ,[Account_Password_Complexity_Enforced]    ,[Account_Lockout_on_Failed_Logins])    \
    VALUES        (     '
    Query_Inter = Query_Inter + '\'' + row[0] + '\','
    Query_Inter = Query_Inter + '\'' + row[1] + '\','
    Query_Inter = Query_Inter + '\'' + row[2] + '\','
    Query_Inter = Query_Inter + '\'' + row[3] + '\','
    Query_Inter = Query_Inter + '\'' + row[4] + '\','
    Query_Inter = Query_Inter + '\'' + row[5] + '\','
    Query_Inter = Query_Inter + '\'' + row[6] + '\','
    Query_Inter = Query_Inter + '\'' + row[7] + '\','
    Query_Inter = Query_Inter + '\'' + row[8] + '\','
    Query_Inter = Query_Inter + '\'' + row[9] + '\','
    Query_Inter = Query_Inter + '\'' + row[10] + '\','
    Query_Inter = Query_Inter + '\'' + row[11] + '\','
    Query_Inter = Query_Inter + '\'' + row[12] + '\','
    Query_Inter = Query_Inter + '\'' + row[13] + '\','
    Query_Inter = Query_Inter + '\'' + row[14] + '\','
    Query_Inter = Query_Inter + '\'' + row[15] + '\','
    Query_Inter = Query_Inter + '\'' + row[16] + '\','
    Query_Inter = Query_Inter + '\'' + row[17] + '\','
    Query_Inter = Query_Inter + '\'' + row[18] + '\','
    Query_Inter = Query_Inter + '\'' + row[19] + '\','
    Query_Inter = Query_Inter + '\'' + row[20] + '\','
    Query_Inter = Query_Inter + '\'' + row[21] + '\','
    Query_Inter = Query_Inter + '\'' + row[22] + '\','
    Query_Inter = Query_Inter + '\'' + row[23] + '\','
    Query_Inter = Query_Inter + '\'' + row[24] + '\','
    Query_Inter = Query_Inter + '\'' + row[25] + '\','
    Query_Inter = Query_Inter + '\'' + row[26] + '\','
    Query_Inter = Query_Inter + '\'' + row[27] + '\','
    Query_Inter = Query_Inter + '\'' + row[28] + '\','
    Query_Inter = Query_Inter + '\'' + row[29] + '\','
    Query_Inter = Query_Inter + '\'' + row[30] + '\','
    Query_Inter = Query_Inter + '\'' + row[31] + '\','
    Query_Inter = Query_Inter + '\'' + row[31] + '\','
    Query_Inter = Query_Inter + '\'' + row[32] + '\','
    Query_Inter = Query_Inter + '\'' + row[33] + '\','
    Query_Inter = Query_Inter + '\'' + row[34] + '\','
    Query_Inter = Query_Inter + '\'' + row[35] + '\','
    Query_Inter = Query_Inter + '\'' + row[36] + '\','#,<Report_Run_Date, datetime2(7),>
    Query_Inter = Query_Inter + '\'' + row[37] + '\','
    Query_Inter = Query_Inter + '\'' + row[38] + '\','
    Query_Inter = Query_Inter + '\'' + row[39] + '\','#,<Account_Creation_Date, datetime2(7),>
    Query_Inter = Query_Inter + '\'' + row[40] + '\','
    Query_Inter = Query_Inter + '\'' + row[41] + '\','
    Query_Inter = Query_Inter + '\'' + row[42] + '\','
    Query_Inter = Query_Inter + '\'' + row[43] + '\','
    Query_Inter = Query_Inter + '\'' + row[44] + '\','
    Query_Inter = Query_Inter + '\'' + row[45] + '\','
    Query_Inter = Query_Inter + '\'' + row[46] + '\','#,<Account_Status_Date, datetime2(7),>
    Query_Inter = Query_Inter + '\'' + row[47] + '\','
    Query_Inter = Query_Inter + '\'' + row[48] + '\','
    Query_Inter = Query_Inter + '\'' + row[49] + '\','#,<Audit_Category_Password_Expiry_Days, int,>
    Query_Inter = Query_Inter + '\'' + row[50] + '\','#,<Last_Password_Reset_Date, datetime2(7),>
    Query_Inter = Query_Inter + '\'' + row[51] + '\','#,<Password_Age_Days, int,>
    Query_Inter = Query_Inter + '\'' + row[52] + '\','#,<Password_Expired, bit,>
    Query_Inter = Query_Inter + '\'' + row[53] + '\','#,<Account_Password_Complexity_Enforced, bit,>
    Query_Inter = Query_Inter +  row[54] 
    Query_Inter = Query_Inter + ')'
    
    print(Query_Inter)

    



def fn_01_Read_CSV():
    print(str_Line, 'fn_01_Read_CSV')    
    #str_File = 'C:\#_FP_APEX\#_DEV\#_BP\DBAAS-5814\RPT_ACCOUNT_COMPLIANCE_COLLECTION.csv'
    str_File = 'C:\#_FP_APEX\#_DEV\#_BP\DBAAS-5814\zzz.csv'
    
    with open(str_File, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            #print(row)
            fn_02_SQL(row)
        
def main():
    print(str_Line, 'main')
    
    #####-----------------------------------------------------------
    #####-----------------------------------------------------------
    fn_01_Read_CSV()
    #####-----------------------------------------------------------
    #####-----------------------------------------------------------    



if __name__ == "__main__":
    main()        