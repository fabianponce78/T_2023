'''
Created on 25 may. 2021

@author: IB_FJPONCE
'''
import requests

url = "https://championsmx.myvtex.com/api/catalog_system/pvt/brand/"
url = "https://championsmx.myvtex.com/api/catalog/pvt/product/1/salespolicy"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.request("GET", url, headers=headers)

print(response.text)