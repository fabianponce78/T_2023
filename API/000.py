'''
Created on 9 abr. 2021

@author: IB_FJPONCE
'''

import requests
import json
import pandas as pd
'''
response = requests.get("https://randomuser.me/api/")
print(response.text)
'''

str_Token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjNkODNkZWVjYTMzYTk1NDliZWI4OGViNGY3YmI5ZGZhM2Q1ZDQ5MjY0MDRkM2RiZTlkOGI0MTBiMWUxMjhjYTRjZWM2M2FlNGEzNzgzYzI3In0.eyJhdWQiOiIxIiwianRpIjoiM2Q4M2RlZWNhMzNhOTU0OWJlYjg4ZWI0ZjdiYjlkZmEzZDVkNDkyNjQwNGQzZGJlOWQ4YjQxMGIxZTEyOGNhNGNlYzYzYWU0YTM3ODNjMjciLCJpYXQiOjE1OTYxMzc4MzIsIm5iZiI6MTU5NjEzNzgzMiwiZXhwIjoxNjI3NjczODMyLCJzdWIiOiIxIiwic2NvcGVzIjpbImNvbXBhbnlfdG9rZW4iXX0.v-ZAExOwhW1moQMlirOqhzXKCyezyI9LtJjMskuf6HIjfIW9cJEESo9NbuVP3oPZOYavkcK7dtG6FpV0C9D_d7ZnO5HZSexWkcHbeqB75p5sN8C3PsfaqXFSDPCrez7xeZyBG8iQtchmcbhtBzjqN91XdjuifMGAasNGd2w8Fd3JKpQ1pRY4MQPndf7GRimP71Mf3tyjlFt2AN_3SK28eV2orERId3iMzxQrXSrUvLrFGRfbaTGPEgVcYB5b4S6umMB32szH0BVm2saQDUAff2GWowr9TdzyyqqKl9xmDrkFGzv3j8rUpTNxP2iLI25VVCnRrtQNEmXctKYD8F3UOWSE_KbFY1o2wstNZcDr83m_mHFmmAUJmXxQ-T31XmMqPCnw0mKPvHUI0uMZrelcehcCiIdY1oCbuwbu5k-K62W14pW3vp6T3V5VC5sMpY5als2r4fVwhri-QzxTl1k6Hsg4f8kUi4-gQWOmaF1ESaIn41TNF8xEoSE795AUk6Tr4Wilnske8ZdgTEOtdgmWw6DlmKZEZ4NZNT14ORiWM80iF0xwBjR5N8XwfN5YTlaxPb-fi-yW-VnZtiBS-mxBIDpjLMUYr_fLk_G5mbkVvbJUq2oH4tQ1zW6CRbqBBagItTi6pvBvTe2a5EOKXavYUIsJ2g4Qpqy7gLw81hRhy7M'

headersx = {
        'Content-type':'application/json',
        'Authorization':'Bearer '+str_Token
        } 



#url = 'https://dev.orkestra.mx/api/v1/external/dashboard/customer-prospect-breakdown' 
url = 'https://aeropostale.orkestra.mx/api/v1/external/dashboard/customer-prospect-breakdown'
url = 'https://aeropostale.orkestra.mx/api/v1/external/dashboard/performance-report'
url = 'https://aeropostale.orkestra.mx/api/v1/external/dashboard/performance-report'
response = requests.get(url ,  headers=headersx)        


print(response.text)


print('-------------------------------------------')
# convert into JSON:
y = json.dumps(response.text)

##########################################################################################
str_Line = response.text
archi1=open("Log_Step.json","w") 
archi1.write(str(str_Line))    
archi1.close() 
##########################################################################################

# the result is a JSON string:
print(y)

print('-------------------------------------------')




print(response.headers)
print(response.status_code)
print(response.reason)

print('-------------------------------------------')
##########################################################################################
##########################################################################################
####__________________________________________________
with open('Log_Step.json', 'r') as file:
    data = json.load(file)
        
    name = data['status']
    msg = data['msg']
    data = data['data']
    general = data['general']


    file.close()
 
####__________________________________________________  
print('name = ', name)
print('msg  = ', msg)
print('data  = ', data)
print('general  = ', general)
print('-------------------------------------------')


df = pd.DataFrame(general)

for column_name, item in df.iteritems():
    print(type(column_name))
    print(column_name)
    print('------\n')
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
ruta_archivo_json = 'Log_Step.json'
with open(ruta_archivo_json) as archivo_json:
    datos_json = json.load(archivo_json)
lista_de_diccionarios = datos_json['data']
datos = pd.DataFrame(lista_de_diccionarios)
print(datos)
print('-------------------------------------------')


##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
'''
# json string                                                                                                                
s = '{"col1":{"row1":1,"row2":2,"row3":3},"col2":{"row1":"x","row2":"y","row3":"z"}}'

# read json to data frame                                                                                                    
df = pd.read_json(s)
print(df)
print('-------------------------------------------')
'''
 