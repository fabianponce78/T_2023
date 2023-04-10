'''
Created on Feb 9, 2023

@author: fponce
'''

'''
Created on Feb 7, 2023

@author: fponce
'''
# https://rapidapi.com/vaccovidlive-vaccovidlive-default/api/vaccovid-coronavirus-vaccine-and-treatment-tracker/

#===============================================================================
# import requests
# 
# url = "https://covid-193.p.rapidapi.com/countries"
# 
# headers = {
#     "X-RapidAPI-Key": "d1e94a0abdmshbec1c3df7e51df5p100c60jsnfbc71e0ee30a",
#     "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
# }
# 
# #response = requests.request("GET", url, headers=headers, params=querystring)
# 
# #response = requests.request("GET", url , verify=False)  
# response = requests.request("GET", url, headers=headers, verify=False)    ### ### !!!
# 
# print(response.text)
#===============================================================================


import requests

url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/"

headers = {
    "X-RapidAPI-Key": "d1e94a0abdmshbec1c3df7e51df5p100c60jsnfbc71e0ee30a",
    "X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, verify=False)

print(response.text)

#===============================================================================
#     _       _       _        ___   _       _       _    
#  /\| |/\ /\| |/\ /\| |/\    /  //\| |/\ /\| |/\ /\| |/\ 
#  \ ` ' / \ ` ' / \ ` ' /   /  / \ ` ' / \ ` ' / \ ` ' / 
# |_     _|_     _|_     _| /  / |_     _|_     _|_     _|
#  / , . \ / , . \ / , . \ /  /   / , . \ / , . \ / , . \ 
#  \/|_|\/ \/|_|\/ \/|_|\//__/    \/|_|\/ \/|_|\/ \/|_|\/ 
#                                                         
#===============================================================================

import json, codecs
from datetime import datetime

print('---------------------------------------------------')
# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%Y%m%d_%H%M%S")
print("date and time =", dt_string)
#Str_FileName_OutPut = "#_weatherapi_2023.JSON"
Str_FileName_OutPut = "#_COVID_"+dt_string+".JSON"       ## --> Str_FileName_OutPut:  #_TEST_20230209_145904.JSON
print("Str_FileName_OutPut: ", Str_FileName_OutPut)

#----------------------------------------------------OK
Txt_json = response.json()
print(Txt_json)
     
 
with open(Str_FileName_OutPut, 'w') as f:
    json.dump(Txt_json,f)
#----------------------------------------------------OK
print('---------------------------------------------------')
