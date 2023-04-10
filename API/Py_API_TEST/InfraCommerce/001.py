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
headersx = {
    'Content-type':'application/json',
    'Authorization':'Bearer '+Str_Token
} 
    
url = 'https://championsmx.myvtex.com/orders/protocols'
url = 'https://championsmx.myvtex.com/inventories/?updatedAt=[2020-05-16T14:01:29.480 TO 2020-05-16T14:04:29.480]&page=1&perPage=50'
url = 'https://championsmx.myvtex.com/catalog/brands'
url = 'https://championsmx.myvtex.com/catalog/categories'
# url = 'https://championsmx.myvtex.com/catalog/products'
# url = 'https://championsmx.myvtex.com/catalog/skus'

    
response = requests.get(url ,  headers=headersx  )        
print('\t response.text.encode = ',response.text.encode("utf-8"))

print('\t response.text.headers = ',response.headers)
print('\t response.text.status_code = ',response.status_code)
print('\t response.text.reason = ',response.reason)


##########################################################################################
str_Line = response.text
archi1=open("Log_Step.json","w") 
archi1.write(str(str_Line))    
archi1.close() 
##########################################################################################