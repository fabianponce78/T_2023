'''
Created on Feb 7, 2023

@author: fponce
'''

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
dt_string = now.strftime("%Y_%m_%d_%H_%M_%S")
dt_string = now.strftime("%Y%m%d_%H%M%S")
print("date and time =", dt_string)

Str_FileName_OutPut = "#_weatherapi_2023.JSON"

Str_FileName_OutPut = "#_weatherapi_"+dt_string+".JSON"

print(Str_FileName_OutPut)