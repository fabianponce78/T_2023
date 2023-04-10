'''
Created on 15 abr. 2021

@author: IB_FJPONCE
'''
# Python program to convert
# JSON file to CSV


import json

import csv
import pandas as pd
## Log_Step.json




df = pd.read_json('Log_Step.json')

print(df.to_string()) 
