'''
Created on Oct 7, 2021

@author: Fabian Ponce
'''
import pandas as pd
import numpy as np
from ntpath import sep


def fn_2_Load_SPRINT_CSV():
    print("------------------------------------------------- fn_2_Load_SPRINT_CSV")
    Str_FileNAme_IN ='.\OutPut\Sprint_Sprint.CSV'
    Str_FileNAme_Out ='.\OutPut\SPRINT.CSV'
    #df = pd.read_csv(Str_FileNAme_IN, index_col=0, usecols=['Issue Type', 'Summary', 'Key',    'Assignee',    'Reporter',    'Priority',    'Status',    'Resolution',    'Created',    'Updated',    'Due date',    'Rank',    'parent',    'Resolved',    'Status Category Changed',    'Linked Issues',    'Parent Link',    'Labels'])
    df = pd.read_csv(Str_FileNAme_IN, index_col=0, usecols=['Date', 'SPRINT', 'ParentStory'])
    

    #print(df)
    df.to_csv(Str_FileNAme_Out, sep='|')
    '''
    print(df)
    df.to_csv(Str_FileNAme_Out)
    '''


def fn_1_Load_JIRA_CSV():
    print("-------------------------------------------------")
    Str_FileNAme_IN ='.\OutPut\JIRA_Your Jira Issues.CSV'
    Str_FileNAme_Out ='.\OutPut\JIRA.CSV'
    #df = pd.read_csv(Str_FileNAme_IN, index_col=0, usecols=['Issue Type', 'Summary', 'Key',    'Assignee',    'Reporter',    'Priority',    'Status',    'Resolution',    'Created',    'Updated',    'Due date',    'Rank',    'parent',    'Resolved',    'Status Category Changed',    'Linked Issues',    'Parent Link',    'Labels'])
    #df = pd.read_csv(Str_FileNAme_IN, index_col=0, usecols=['Issue Type', 'Summary', 'Key',    'Assignee',    'Reporter',    'Priority',    'Status',    'Resolution',    'Created',    'Updated',    'Due date',     'parent',    'Resolved',    'Status Category Changed',    'Linked Issues',    'Parent Link'   ])
    df = pd.read_csv(Str_FileNAme_IN, index_col=0, usecols=['Issue Type', 'Summary', 'Key',    'Assignee',    'Reporter',    'Priority',    'Status',    'Resolution',    'Created',    'Updated',    'Due date',     'parent',    'Resolved',    'Status Category Changed' ])
    
    values=['Fabian Ponce', 'Ricardo Martinez', 'Eduardo Silva', 'Miguel Martinez', 'Julio Alcala', 'Alex Gomez', 'Hugo Rodriguez']
    values_Parent=['DBAAS-5814']
    
    filtered_df = df[df.Assignee.isin(values)]
    filtered_df2 = filtered_df[filtered_df.parent.isin(values_Parent)]
    
    positions = np.flatnonzero(filtered_df)
    filtered_df=df.iloc[positions]
    
    #print(filtered_df)
    #filtered_df.to_csv(Str_FileNAme_Out, sep='|')
    
    print(filtered_df)
    filtered_df2.to_csv(Str_FileNAme_Out, sep='|')
    '''
    print(df)
    df.to_csv(Str_FileNAme_Out)
    '''


def fn_1C_Load_JIRA_CSV():
    print("------------------------------------------------- fn_1C_Load_JIRA_CSV")
    Str_FileNAme_IN ='.\OutPut\JIRA.CSV'
    Str_FileNAme_Out ='.\OutPut\JIRA_01.CSV'
    
    #df = pd.read_csv(Str_FileNAme_IN, index_col=0, on_bad_lines='skip')
    #df = pd.read_csv(Str_FileNAme_IN,  on_bad_lines='skip', usecols=['Key'])
    df = pd.read_csv(Str_FileNAme_IN, index_col=0,  on_bad_lines='skip')
    print('---> ',df)
    print ('--->>', list(df))
    
    #values_2=['Bug', 'Build Story', 'Enabler Story', 'Enhancement', 'Feature', 'Framework', 'Task']    
    #df_B = df[df['Issue Type'].isin(values_2)]
    #df_B = df[df['Key'].isin(values_2)]            
    #print('---> ',df_B)
    df.to_csv(Str_FileNAme_Out, sep='|')     


def fn_1B_Load_JIRA_CSV():
    print("------------------------------------------------- fn_1B_Load_JIRA_CSV")
    Str_FileNAme_IN ='.\OutPut\JIRA_Your Jira Issues.CSV'
    Str_FileNAme_Out ='.\OutPut\JIRA.CSV'
    #df = pd.read_csv(Str_FileNAme_IN, index_col=0, usecols=['Issue Type', 'Summary', 'Key',    'Assignee',    'Reporter',    'Priority',    'Status',    'Resolution',    'Created',    'Updated',    'Due date',    'Rank',    'parent',    'Resolved',    'Status Category Changed',    'Linked Issues',    'Parent Link',    'Labels'])
    #df = pd.read_csv(Str_FileNAme_IN, index_col=0, usecols=['Issue Type', 'Summary', 'Key',    'Assignee',    'Reporter',    'Priority',    'Status',    'Resolution',    'Created',    'Updated',    'Due date',     'parent',    'Resolved',    'Status Category Changed',    'Linked Issues',    'Parent Link'   ], on_bad_lines='skip')
    df = pd.read_csv(Str_FileNAme_IN, index_col=0, usecols=['Issue Type', 'Summary', 'Key',    'Assignee',    'Reporter',    'Priority',    'Status',    'Resolution',    'Created',    'Updated',    'Due date',     'parent',    'Resolved',    'Status Category Changed' ], on_bad_lines='skip')
    #df = pd.read_csv(Str_FileNAme_IN, index_col=0, usecols=['Issue Type', 'Summary', 'Key',    'Assignee',    'Reporter',    'Priority',    'Status',    'Resolution',    'Created',    'Updated',    'Due date',     'parent',    'Resolved',    'Status Category Changed'])
    
    values=['Fabian Ponce', 'Ricardo Martinez', 'Eduardo Silva', 'Miguel Martinez', 'Julio Alcala', 'Alex Gomez', 'Hugo Rodriguez']    
   
    
    filtered_df = df[df['Assignee'].isin(values)]

    
    #filtered_df.to_csv(Str_FileNAme_Out, sep='|')
    df_A = filtered_df
    #print('---> ',df_A)
    
    df_A.to_csv(Str_FileNAme_Out, sep='|')
    
    #####----------------------
    #print ('--->>', list(df_A.columns.values))
    #print ('--->>', list(df_A))
    
    #values_2=['Bug', 'Build Story', 'Enabler Story', 'Enhancement', 'Feature', 'Framework', 'Task']    
    #df_B = df_A[df_A['Issue Type'].isin(values_2)]            
    #print('---> ',df_B)
    #####----------------------

    #print(df)
    #df.to_csv(Str_FileNAme_Out)
    
    
    

def main():
    print("-------------------------------------------------")
    #----------------------------------------------
    #----------------------------------------------
    #----------------------------------------------
    ##fn_1_Load_JIRA_CSV()
    fn_1B_Load_JIRA_CSV()    
    fn_1C_Load_JIRA_CSV()    

    
    
    #fn_2_Load_SPRINT_CSV()
    print('\n\n\t------ 001 Done :) \n\n')    
    #----------------------------------------------

if __name__ == "__main__":
    main()