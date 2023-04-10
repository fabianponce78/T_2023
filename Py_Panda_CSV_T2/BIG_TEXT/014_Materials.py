'''
Created on Apr 1, 2023

@author: fponce
'''

import random

Lst_BUILDING_MATERIALS = ['BUILDING MATERIALS', 'brick', 'cement', 'concrete', 'glass', 'gravel', 'marble', 'metal', 'plastic', 'sand', 'slate', 'stone', 'wood']

Lst_FABRICS = ['FABRICS','cloth','cotton','lace','leather','linen','man-made fibres','nylon','polyester','silk','wool']

Lst_METALS = ['METALS','aluminium','brass','bronze','copper','gold','iron','lead','magnesium','mercury','nickel','platinum','silver','steel','tin','uranium','zinc','alloy','GASES','carbon dioxide','helium','hydrogen','nitrogen','oxygen']

Lst_OTHER_MATERIALS = ['OTHER MATERIALS','charcoal','coal','gas','oil','paraffin','petrol','asbestos','ash','cardboard','chalk','clay','dust','fibreglass','mud','paper','rubber','smoke','soil','ice','steam','water']


print('xxx ', Lst_BUILDING_MATERIALS)
print('xxx ', Lst_FABRICS)
print('xxx ', Lst_METALS)
print('xxx ', Lst_OTHER_MATERIALS)

lst = [
    Lst_BUILDING_MATERIALS, Lst_FABRICS
     ]

print('xxx ', lst)

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

T_dict = {
    'Lst_BUILDING_MATERIALS':Lst_BUILDING_MATERIALS ,
    'Lst_FABRICS':Lst_FABRICS ,
    'Lst_METALS':Lst_METALS ,
    'Lst_OTHER_MATERIALS':Lst_OTHER_MATERIALS ,
    }

print('T_dict ==>> ',   T_dict)
print('')


# ✅ get random key-value pair from dictionary
key, value = random.choice(list(T_dict.items()))
print('\t -->> ', key, value)  # 👉️ name Borislav Hadzhiev
print('\t -->> ', random.choice(value)    )       #Choose a random item from a sequence
print('')
 
# -----------------------------------------------

# ✅ get random key from dictionary
key = random.choice(list(T_dict))
print('\t -- ', key)  # 👉️ topic

# -----------------------------------------------

# ✅ get random value from dictionary
value = random.choice(list(T_dict.values()))
print('\t -- ', value)  # 👉️ bobbyhadz.com


# -----------------------------------------------
# -----------------------------------------------
# -----------------------------------------------