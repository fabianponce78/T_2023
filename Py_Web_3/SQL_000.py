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



#===============================================================================
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=DESKTOP-C1P2GG2;'
#                       'Database=DB_FP;'
#                       'Trusted_Connection=yes;')
# cursor = conn.cursor()
# #cursor.execute('exec [dbo].[SP_VW_SALES] 5,10')
#   
# 
# cursor.execute(Query_SP_1)            
# cursor.commit()
#    
# cursor.close()
# conn.close()
#===============================================================================


#print('\t DONE...')

###############################################################################
###############################################################################

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
#server = 'DESKTOP-C1P2GG2'
server = 'MDC-DCMW8C3' 
database = 'DB_FP' 
username = 'FP2' 
#password = 'Ap3x53120' 
password = 'N1rvana53120' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)


#===============================================================================
# #Query_SP_1 = 'Insert into dbo.Flask_Form_A (STR_FORM) values (\''' ' +str_2+' \''')'
# Query_SP_1 = 'insert into dbo.Flask_Form_A (STR_FORM) values (GETDATE())'
# print(Query_SP_1)
# 
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()
# ###-----
# cursor.execute(Query_SP_1)            
# cursor.commit()
# ###-----    
# cnxn.close()
#===============================================================================
###############################################################################



###############################################################################
###############################################################################
try:
    #Query_SP_1 = 'Insert into dbo.Flask_Form_A (STR_FORM) values (\''' ' +str_2+' \''')'
    Query_SP_1 = 'insert into dbo.Flask_Form_A (STR_FORM) values (GETDATE())'
    print(Query_SP_1)    
    #cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password+';Encrypt=no')
    cursor = cnxn.cursor()
    ###-----
    cursor.execute(Query_SP_1)            
    cursor.commit()
    ###-----    
    cnxn.close()
except AssertionError as error:
    print('... ', error)
#except Exception as inst:
#    print(type(inst))    # the exception instance
#    print(inst.args)     # arguments stored in .args
#    print(inst)          # __str__ allows args to be printed directly,

###############################################################################
###############################################################################

print('\t DONE...')