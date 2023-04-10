'''
Created on 27 abr. 2021

@author: IB_FJPONCE
'''
import json
import requests


####__________________________________________________
with open('#Config.json', 'r') as file:
    config = json.load(file)
        
    Str_Token = config['Token_HCP']
####__________________________________________________

print('Str_Token = ', Str_Token)
print('-----------------')

###https://doc.stage-api.infrahub.com.br/#19574177-0d75-4654-96c0-334cdbe2a3d9
#Str_Token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjNkODNkZWVjYTMzYTk1NDliZWI4OGViNGY3YmI5ZGZhM2Q1ZDQ5MjY0MDRkM2RiZTlkOGI0MTBiMWUxMjhjYTRjZWM2M2FlNGEzNzgzYzI3In0.eyJhdWQiOiIxIiwianRpIjoiM2Q4M2RlZWNhMzNhOTU0OWJlYjg4ZWI0ZjdiYjlkZmEzZDVkNDkyNjQwNGQzZGJlOWQ4YjQxMGIxZTEyOGNhNGNlYzYzYWU0YTM3ODNjMjciLCJpYXQiOjE1OTYxMzc4MzIsIm5iZiI6MTU5NjEzNzgzMiwiZXhwIjoxNjI3NjczODMyLCJzdWIiOiIxIiwic2NvcGVzIjpbImNvbXBhbnlfdG9rZW4iXX0.v-ZAExOwhW1moQMlirOqhzXKCyezyI9LtJjMskuf6HIjfIW9cJEESo9NbuVP3oPZOYavkcK7dtG6FpV0C9D_d7ZnO5HZSexWkcHbeqB75p5sN8C3PsfaqXFSDPCrez7xeZyBG8iQtchmcbhtBzjqN91XdjuifMGAasNGd2w8Fd3JKpQ1pRY4MQPndf7GRimP71Mf3tyjlFt2AN_3SK28eV2orERId3iMzxQrXSrUvLrFGRfbaTGPEgVcYB5b4S6umMB32szH0BVm2saQDUAff2GWowr9TdzyyqqKl9xmDrkFGzv3j8rUpTNxP2iLI25VVCnRrtQNEmXctKYD8F3UOWSE_KbFY1o2wstNZcDr83m_mHFmmAUJmXxQ-T31XmMqPCnw0mKPvHUI0uMZrelcehcCiIdY1oCbuwbu5k-K62W14pW3vp6T3V5VC5sMpY5als2r4fVwhri-QzxTl1k6Hsg4f8kUi4-gQWOmaF1ESaIn41TNF8xEoSE795AUk6Tr4Wilnske8ZdgTEOtdgmWw6DlmKZEZ4NZNT14ORiWM80iF0xwBjR5N8XwfN5YTlaxPb-fi-yW-VnZtiBS-mxBIDpjLMUYr_fLk_G5mbkVvbJUq2oH4tQ1zW6CRbqBBagItTi6pvBvTe2a5EOKXavYUIsJ2g4Qpqy7gLw81hRhy7M'
    
headersx = {
    'Content-type':'application/json',
    'Authorization':'Bearer '+Str_Token
} 
    

url = 'https://championsmx.myvtex.com/catalog/products'
url = 'https://championsmx.myvtex.com/orders/protocols'
url = 'https://championsmx.myvtex.com/inventories/?updatedAt=[2020-05-16T14:01:29.480 TO 2020-05-16T14:04:29.480]&page=1&perPage=50'
# url = 'https://championsmx.myvtex.com/catalog/brands'
url = 'https://championsmx.myvtex.com/catalog/categories'
# url = 'https://championsmx.myvtex.com/catalog/products'
# url = 'https://championsmx.myvtex.com/catalog/skus'

    
payload={}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

##########################################################################################
str_Line = response.text
archi1=open("Log_Step.json","w") 
archi1.write(str(str_Line))    
archi1.close() 
##########################################################################################