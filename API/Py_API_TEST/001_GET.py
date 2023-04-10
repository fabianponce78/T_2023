'''
Created on 9 abr. 2021

@author: IB_FJPONCE
'''

import requests
import json
import csv
from datetime import datetime, date



str_Linea = '_____________________________________________________________'

#┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
#┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
#┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼

def fn_2():
    print(str_Linea, 'fn_2')
    # Python program to convert
    # JSON file to CSV    
    # Opening JSON file and loading the data
    # into the variable data
    with open('Log_Step.json') as json_file:
        data = json.load(json_file)
    
    employee_data = data['status']
    
    # now we will open a file for writing
    data_file = open('Log_Step.csv', 'w')
    
    # create the csv writer object
    csv_writer = csv.writer(data_file)
    
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    
    for emp in employee_data:
        if count == 0:
    
            # Writing headers of CSV file
            header = emp.keys()
            csv_writer.writerow(header)
            count += 1
    
        # Writing data of CSV file
        csv_writer.writerow(emp.values())
    
    data_file.close()
#┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
#┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
#┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼


def fn_1():
    print(str_Linea, 'fn_1')
        
    str_Token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjNkODNkZWVjYTMzYTk1NDliZWI4OGViNGY3YmI5ZGZhM2Q1ZDQ5MjY0MDRkM2RiZTlkOGI0MTBiMWUxMjhjYTRjZWM2M2FlNGEzNzgzYzI3In0.eyJhdWQiOiIxIiwianRpIjoiM2Q4M2RlZWNhMzNhOTU0OWJlYjg4ZWI0ZjdiYjlkZmEzZDVkNDkyNjQwNGQzZGJlOWQ4YjQxMGIxZTEyOGNhNGNlYzYzYWU0YTM3ODNjMjciLCJpYXQiOjE1OTYxMzc4MzIsIm5iZiI6MTU5NjEzNzgzMiwiZXhwIjoxNjI3NjczODMyLCJzdWIiOiIxIiwic2NvcGVzIjpbImNvbXBhbnlfdG9rZW4iXX0.v-ZAExOwhW1moQMlirOqhzXKCyezyI9LtJjMskuf6HIjfIW9cJEESo9NbuVP3oPZOYavkcK7dtG6FpV0C9D_d7ZnO5HZSexWkcHbeqB75p5sN8C3PsfaqXFSDPCrez7xeZyBG8iQtchmcbhtBzjqN91XdjuifMGAasNGd2w8Fd3JKpQ1pRY4MQPndf7GRimP71Mf3tyjlFt2AN_3SK28eV2orERId3iMzxQrXSrUvLrFGRfbaTGPEgVcYB5b4S6umMB32szH0BVm2saQDUAff2GWowr9TdzyyqqKl9xmDrkFGzv3j8rUpTNxP2iLI25VVCnRrtQNEmXctKYD8F3UOWSE_KbFY1o2wstNZcDr83m_mHFmmAUJmXxQ-T31XmMqPCnw0mKPvHUI0uMZrelcehcCiIdY1oCbuwbu5k-K62W14pW3vp6T3V5VC5sMpY5als2r4fVwhri-QzxTl1k6Hsg4f8kUi4-gQWOmaF1ESaIn41TNF8xEoSE795AUk6Tr4Wilnske8ZdgTEOtdgmWw6DlmKZEZ4NZNT14ORiWM80iF0xwBjR5N8XwfN5YTlaxPb-fi-yW-VnZtiBS-mxBIDpjLMUYr_fLk_G5mbkVvbJUq2oH4tQ1zW6CRbqBBagItTi6pvBvTe2a5EOKXavYUIsJ2g4Qpqy7gLw81hRhy7M'
    
    headersx = {
            'Content-type':'application/json',
            'Authorization':'Bearer '+str_Token
            } 
    
    
    
    
    url = 'https://aeropostale.orkestra.mx/api/v1/external/dashboard/performance-report'
    #url = 'https://aeropostale.orkestra.mx/api/v1/external/dashboard/customer-prospect-breakdown'
    url = 'https://aeropostale.orkestra.mx/api/v1/external/payments'
    url = 'https://aeropostale.orkestra.mx/api/v1/external/customer-purchases'
    
    
    response = requests.get(url ,  headers=headersx  )        
    
    
    print(response.text.encode("utf-8"))
    
    ##########################################################################################
    
    str_Line = response.text
    archi1=open("Log_Step.json","w") 
    archi1.write(str(str_Line))    
    archi1.close() 
    
    ##########################################################################################
print('-------------------------------------------')

#┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
#┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
#┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
def main():
    print("-------------------------------------------------")
    #----------------------------------------------
    dt_now1 = datetime.now()
    #----------------------------------------------
    #----------------------------------------------
    fn_1()
    fn_2()

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