'''
Created on 25 may. 2021

@author: IB_FJPONCE
'''
import requests

url = "https://apiexamples.vtexcommercestable.com.br/api/catalog_system/pvt/sku/stockkeepingunitids"
url = "https://championsmx.myvtex.com/api/catalog_system/pvt/sku/stockkeepingunitids"

querystring = {"page":"1","pagesize":"25"}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)