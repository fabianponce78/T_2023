'''
Created on Mar 17, 2023

@author: fponce
'''

'''
    https://pywombat.com/articles/json-python
'''


import json

str_json =  '''{
    "nombre": "Eduardo",
    "edad": 27,
    "correo": "eduardo78d@gmail.com",
    "cursos": ["Python", "MongoDB", "Flask"]
}'''

user = json.loads(str_json)
print(user)

print('\t    nombre:    ',   user['nombre'])
print('\t    edad:      ',   user['edad'])
print('\t    cursos:    ',   user['cursos'])

print('==========================================================================')

user = json.dumps(str_json)

print(user)
print(type(user))

print('==========================================================================')
print('==================    class')
'''
    Y ¿Qué pasa si queremos serializar un objeto propio? Bueno, lo intentemos. 🤐
'''


class Usuario:
    def __init__(self, username, email):
        self.username = username
        self.email = email


usuario = Usuario('eduardo_gpg', 'eduardo78d@gmail.com')
#data = json.dumps(usuario)
data = json.dumps(usuario.__dict__)

print(data)

#data2 = usuario.__dict__
#print(data2)


print('==========================================================================')
print('==========    READ    JSON')

with open('users.json') as f:
    payload = json.load(f)
    
    print('    \t    payload    =>    ',   payload)

    for user in payload['users']:
        print(user)
        
print('==========================================================================')        


print('==========    W    JSON')

users = [
      {
        "nombre": "Eduardo",
        "edad": 27
      },
      {
        "nombre": "Raquel",
        "edad": 29
      },
      {
        "nombre": "Fernando",
        "edad": 25
      },
      {
        "nombre": "Guadalupe",
        "edad": 30
      }
]


with open('users2.json', 'w') as f:
    json.dump(users, f, indent=4)



with open('users2.json') as f:
    payload = json.load(f)
    print(payload)

print('/////////////')    
data = json.dumps(payload, indent=4, sort_keys=True)
print(data) 
    
'''
    for user in payload['users']:
        print(user)
'''        
    
print('==========================================================================')  


usuario = {
    'username': 'eduardo_gpg',
    'nombre': 'Eduardo Ismael',
    'age': 27,
    'correo': 'eduardo78d@gmail.com'
}

data = json.dumps(usuario, indent=4, sort_keys=True)
print(data) 