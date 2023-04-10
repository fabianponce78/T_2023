'''
Created on Jan 20, 2023

@author: fponce
'''

import uuid
import random



# make a random UUID
New_UID = uuid.uuid4()



List_Pais = ['Austria', 'Azerbaijan', 'Bonaire Sint Eustatius and Saba','Cambodia','China', 
'Djibouti', 'European Union','Kosovo', 'Liberia','Liechtenstein','Low income','Malta', 'Tanzania','Yemen', 
'Aruba', 'Belgium', 'Benin', 'Colombia', 'Eswatini','Ethiopia','Faeroe Islands','France', 
'French Polynesia','Israel','Jamaica', 'New Zealand', 
'Niue', 'Norway', 'Panama','Serbia', 'Slovenia','Uruguay','Bermuda', 'Burkina Faso', 
'Burundi', 'Czechia','Dominica','Dominican Republic','Ghana', 'Grenada', 'International','Jersey', 
'Kyrgyzstan', 'Laos','Maldives', 'Montenegro', 'North America','Northern Cyprus', 'Saint Helena', 'Saint Lucia', 
'Thailand', 'Turkey', 'Angola', 'Anguilla', 'Antigua and Barbuda','Pitcairn', 
'Sao Tome and Principe','Turkmenistan', 'Upper middle income', 'Argentina', 
'Bosnia and Herzegovina','Bulgaria', 'Guernsey', 'Guinea-Bissau','Hungary', 
'Nauru', 'Spain','United States', 'Australia', 'Brazil','British Virgin Islands', 
'Canada', ]


print(random.choice(List_Pais))

print(New_UID)

######################################################################
######################################################################

from random import randint
import datetime

date=datetime.date(randint(2005,2025), randint(1,12),randint(1,28))

lambda_dt = lambda a,b : datetime.date(randint(a,b), randint(1,12),randint(1,28))

print(date)
print("\t lambda_dt = ", lambda_dt (2005,2025))
 
######################################################################
######################################################################

#import random

print('Random Int', random.randint(3, 9))
 
print('######################################################################') 
 
Dic_A = {
  "UID": uuid.uuid4(),
  "Pais": random.choice(List_Pais),
  "dt": datetime.date(randint(2005,2025), randint(1,12),randint(1,28)),
  "Numero": random.randint(3, 9)
}
 
print(Dic_A) 


print('######################################################################')


 
import pandas as pd

List_cols = ['UID', 'Pais', 'dt', 'Numero']
df = pd.DataFrame(columns=List_cols)
print(df)

'''
df = df.append(
    {
  "UID": uuid.uuid4(),
  "Pais": random.choice(List_Pais),
  "dt": datetime.date(randint(2005,2025), randint(1,12),randint(1,28)),
  "Numero": random.randint(3, 9)
        }
              , ignore_index=True  )

print(df)
'''

New_data =     {
  "UID": uuid.uuid4(),
  "Pais": random.choice(List_Pais),
  "dt": datetime.date(randint(2005,2025), randint(1,12),randint(1,28)),
  "Numero": random.randint(3, 9)
        }
print('New_data : ', New_data)



df = pd.concat([df, pd.DataFrame(New_data, index=[0])], ignore_index=True)
print(df)


##########
for i in range(10):
    New_data =     {
        "UID": uuid.uuid4(),
        "Pais": random.choice(List_Pais),
        "dt": datetime.date(randint(2005,2025), randint(1,12),randint(1,28)),
        "Produccion": random.randint(3, 9)
        }
    df = pd.concat([df, pd.DataFrame(New_data, index=[0])], ignore_index=True)
##########    
print("---------------------------\n", df, "\n---------------------------\n")        
 
df.to_csv('xxxx.csv' , index=False)

print('######################################################################')
#===============================================================================
# for i in range(5):
#     print(i)
#===============================================================================
