'''
Created on 25 may. 2021

@author: IB_FJPONCE
'''
import requests

url = "https://apiexamples.vtexcommercestable.com.br/api/catalog_system/pvt/products/GetProductAndSkuIds"
#https://{accountName}.{environment}.com.br/api/catalog_system/pvt/products/GetProductAndSkuIds
URL = 'https://championsmx.myvtex.com/catalog/skus'
URL = 'https://championsmx.myvtex.com/api/catalog_system/pvt/products/GetProductAndSkuIds'


querystring = {"categoryId":"1","_from":"1","_to":"10"}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)