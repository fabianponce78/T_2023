# -*- coding: utf-8 -*-
'''
Created on Nov 25, 2021

@author: Fabian Ponce
'''
from datetime import datetime, date
import os, errno
import pyodbc
import sqlite3
import pandas as pd






str_Line = '___________________________________________________'
str_Path = '.\OutPut\#_JIRA_Report.XLSX'

#####===============================================================================================
#####===============================================================================================
#####===============================================================================================
#####===============================================================================================
#####===============================================================================================
#####===============================================================================================
#####===============================================================================================
def fn_02_A():
    print(str_Line, " fn_01_A")
    
    connection_info = 'Driver={SQL Server}; Server=DESKTOP-C1P2GG2; Database=JIRA; Trusted_Connection=yes;'    
    print('connection_info = ', connection_info)
    
    #sql = "SELECT TOP 10 * FROM [JIRA].[dbo].[JIRA]"
    sql = "SELECT * FROM dbo.JIRA"
    print(sql)
    
 

    

    conn = sqlite3.connect(connection_info) 
              
    sql_query = pd.read_sql_query (sql, conn)
    
    df = pd.DataFrame(sql_query, columns = ['Issue_Type', 'Summary', 'Key'])
    print (df)
    


#####===============================================================================================
#####===============================================================================================
#####===============================================================================================
#####===============================================================================================
#####===============================================================================================
#####===============================================================================================

def main():
    print(str_Line, " main")
    #----------------------------------------------
    dt_now1 = datetime.now()
    #----------------------------------------------
    #----------------------------------------------

    #fn_01_A()
    fn_02_A()



    print('\n\n\t------ Done :) \n\n')
    #----------------------------------------------
    #----------------------------------------------
    dt_now2 = datetime.now()
    print('---------START =', dt_now1)
    print('-----------END =', dt_now2)
    duration = dt_now2 - dt_now1                         # For build-in functions
    duration_in_s = duration.total_seconds()
    print('----------Time =', duration_in_s)
    #----------------------------------------------

if __name__ == "__main__":
    main()