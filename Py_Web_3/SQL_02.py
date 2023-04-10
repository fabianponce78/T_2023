'''
Created on Feb 10, 2023

@author: fponce
'''

'''
Created on Jul 22, 2021

@author: Fabian Ponce
'''

import pyodbc 


str_2 = 'HOLA Python'

'''
FP2
Ap3x53120
'''






#print('\t DONE...')

###############################################################################
###############################################################################
server = 'MDC-DCMW8C3' 
database = 'DB_FP' 
username = 'FP2' 
#password = 'Ap3x53120' 
password = 'N1rvana53120' 


Query_SP_1 = 'insert into dbo.Flask_Form_A (STR_FORM) values (GETDATE())'


#===============================================================================
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=MDC-DCMW8C3;'
#                       'Database=DB_FP;'
#                       'Trusted_Connection=yes;')
#===============================================================================



#conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;PORT=1433;DATABASE=testdb;UID=me;PWD=pass')
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=MDC-DCMW8C3;PORT=1433;DATABASE=DB_FP;UID=FP2;PWD=N1rvana53120')


cursor = conn.cursor()

cursor.execute(Query_SP_1)
conn.commit()
###############################################################################
###############################################################################

print('\t DONE...')