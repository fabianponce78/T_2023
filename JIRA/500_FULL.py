'''
Created on Oct 7, 2021

@author: Fabian Ponce
'''

import os
from datetime import datetime, date
  


print("-------------------------------------------------")
#----------------------------------------------
dt_now1 = datetime.now()
#----------------------------------------------
#----------------------------------------------
#----------------------------------------------

os.system('python 000.py')
os.system('python 001_Filter_CSV.py')
os.system('python 002_SQL_SP.py')

os.system('python 006_SQL_2_XLS_00.py')
os.system('python 006_SQL_2_XLS_01.py')
os.system('python 006_SQL_2_XLS_02.py')
os.system('python 006_SQL_2_XLS_03.py')

print('\n\n\t------ DONE :) \n\n')


#----------------------------------------------
#----------------------------------------------
#----------------------------------------------
dt_now2 = datetime.now()
print('---------START =', dt_now1)
print('-----------END =', dt_now2)
duration = dt_now2 - dt_now1                         
duration_in_s = duration.total_seconds()
print('----------Time =', duration_in_s)
#----------------------------------------------  