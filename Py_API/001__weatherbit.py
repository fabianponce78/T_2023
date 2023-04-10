'''
Created on Dec 9, 2022

@author: fponce
'''


#===============================================================================
# import requests
# 
# 
# url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/3hourly"
# 
# querystring = {"lat":"35.5","lon":"-78.5"}
# 
# headers = {
#     "X-RapidAPI-Key": "9d95a1a4e3msh765d1517b007f37p146f80jsne567c156db32",
#     "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
# }
# 
# response = requests.request("GET", url, headers=headers, params=querystring)
# 
# print(response.text)
#===============================================================================



#https://rapidapi.com/wettercom-wettercom-default/api/history3/pricing

import requests

url = "https://history3.p.rapidapi.com/v0/daily-zip/DE/81245/20210101"

querystring = {"parameters":"weather"}

headers = {
    "X-RapidAPI-Key": "9d95a1a4e3msh765d1517b007f37p146f80jsne567c156db32",
    "X-RapidAPI-Host": "history3.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

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

print('---------------------------------------------------')
#Str_FileName_OutPut = "###_JIRA_" + accountId + "_" + dt_Start + "_" + dt_End + ".JSON"
#Str_FileName_OutPut = "#_JIRA_Filea/"+Str_FileName_OutPut
Str_FileName_OutPut = "#_forecast9.JSON"
##----------------------------------------------------OK
Txt_json = response.json()
print(Txt_json)
    
#with open('#_000_Data_12.JSON', 'w') as f:
with open(Str_FileName_OutPut, 'w') as f:
    json.dump(Txt_json,f)
##----------------------------------------------------OK
print('---------------------------------------------------')