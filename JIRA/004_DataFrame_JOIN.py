'''
Created on Oct 13, 2021

@author: Fabian Ponce
'''

import pandas as pd
from csv import reader

Str_FN_DT ='.\OutPut\DT2.CSV'
Str_FN_JIRA ='.\OutPut\JIRA.CSV'
Str_FN_SPRINT ='.\OutPut\SPRINT.CSV'
Str_Line = '______________________________________________'



print('Str_FN_DT = ', Str_FN_DT)
print('Str_FN_JIRA = ', Str_FN_JIRA)
print('Str_FN_SPRINT = ', Str_FN_SPRINT)
################==================================================================================
################==================================================================================

print(Str_Line)

DT_df = pd.read_csv(Str_FN_DT, keep_default_na=False, na_values=[""] , index_col=False)
DT_df.reset_index(drop=True, inplace=True)



print(DT_df)



################==================================================================================
################==================================================================================

print(Str_Line)

Sprnt_df = pd.read_csv(Str_FN_SPRINT, keep_default_na=False, na_values=[""] , index_col=False)
Sprnt_df.reset_index(drop=True, inplace=True)



print(Sprnt_df)

################==================================================================================
################==================================================================================
'''
print(Str_Line)
Str_FN_JIRA ='.\OutPut\JIRA.CSV'

# iterate over each line as a ordered dictionary and print only few column by column Number
with open(Str_FN_JIRA, 'r') as read_obj:
    csv_reader = reader(read_obj, delimiter='|')
    next(csv_reader, None)  # skip the headers
    line_count = 0
    for row in csv_reader:
        #print(row)
        #print(row[8])  #---Created
        Str_A = row[8]
        Str_A = Str_A[0:10]
        #print(row[8] , '--->' , Str_A)
        print(Str_A)
'''        


################==================================================================================
################==================================================================================
#####================================================================================
#####================================================================================


 