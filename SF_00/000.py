'''
Created on Jul 5, 2021

@author: Fabian Ponce
'''
import pandas as pd

from colorama import init, Fore

#C:/#_FP_APEX/#_DEV/#_Py_FP/Py_Test/SF_00/avg_ride_length.csv
Str_Path_FN = 'C:/#_FP_APEX/#_DEV/#_Py_FP/Py_Test/SF_00/Data/avg_ride_length.csv'
Str_Linea = '________________________________________________________________________'

df = pd.read_csv(Str_Path_FN)
print(df.to_string())
#print(df)

###------------------------------------------------
print(Str_Linea)
data_top = df.head() 
print(data_top.to_string())


###------------------------------------------------
print(Str_Linea)
print(list(df.columns))
print(list(df.columns.values))
print(list(df.columns.values.tolist()))

###------------------------------------------------
print(Str_Linea)

col_list = ["all_trips_v2$member_casual", "all_trips_v2$ride_length"]
df = pd.read_csv(Str_Path_FN, usecols=col_list)

#print(df["all_trips_v2$member_casual"])
print(  ["all_trips_v2$ride_length"]    )


###------------------------------------------------
print(Str_Linea)
fields = ["all_trips_v2$member_casual", "all_trips_v2$ride_length"]

df = pd.read_csv(Str_Path_FN, skipinitialspace=True, usecols=fields)
# See the keys
print ( df.keys()    )
# See content in 'star_name'
print ( df['all_trips_v2$member_casual']    )

init(autoreset=True)

print(Str_Linea)
print(Str_Linea)

init()
print(Fore.GREEN +  Str_Linea   +  "Recursos Python")


