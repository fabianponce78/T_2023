'''
Created on Mar 29, 2023

@author: fponce
'''
import json


'''
https://www.w3schools.com/python/python_json.asp
'''
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))



print('----------------------------')

import copy
uno = {
    'NoSol': '1192017',
    'idDocumento': '4fd174c8-3439-4c80-9b1c-1c3e6721f827',
    'Status': 'ENVIANDO',
    'Documento': 'D',
    'Id': 'prueba 1',
    'Tipo': 'SOLICITUD ',
    'Grupo': 'S',
    'Doc': '',
    'AGT': '1',
    'Path': 'null',
    'STATUS': 1
}

dos = {
    "Res": {
        "usuario": "Jesus",
        "sistemaId": "Clave",
        "resultado": {
            "codigo": 0,
            "subcodigo": 0,
            "mensaje": "Success",
            "descripcion": "descripcion",
            "fechaHora": "2018-01-04T12:43"
        }
    }
}


result = copy.copy(uno)
result.update(dos)
print(result)