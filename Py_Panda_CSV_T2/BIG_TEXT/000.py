


 

# Importar el módulo
import json

# Cadena de caracteres en el formato JSON
datos_JSON =  """
{
    "tamano": "mediana",
    "precio": 15.67,
    "toppings": ["champinones", "queso extra", "pepperoni", "albahaca"],
    "cliente": {
        "nombre": "Jane Doe",
        "telefono": "455-344-234",
        "correo": "janedoe@email.com"
    }
}
"""

# Convertir cadena de caracteres JSON a un diccionario
datos_diccionario = json.loads(datos_JSON)

print(datos_diccionario)

print(datos_diccionario["tamano"])
print(datos_diccionario["precio"])
print(datos_diccionario["toppings"])
print(datos_diccionario["cliente"])


print('==========================================================================')
'''
https://www.programarya.com/Cursos/Python/estructuras-de-datos/diccionarios
'''

nombre_del_diccionario = {}

otro_diccionario = {
    "nombre": "Alberto",
    "usuario": "alb_123",
}
 
 
mi_diccionario = {
    "nombre": "Juan",
    "usuario": "jn123",
}

# Muestra Juan
print(mi_diccionario["nombre"])

# Muestra jn123
print(mi_diccionario["usuario"]) 


print('==========================================================================')
mi_diccionario = {
    "nombre": "Juan",
    "edad": "23",
    "usuario": "jn23",
}

# Recorriendo los elementos

for llave in mi_diccionario:
    print(llave, ": ", mi_diccionario[llave], sep='')


print('==========================================================================')
'''
https://ellibrodepython.com/diccionarios-en-python
'''

anidado1 = {"aa": 1, "ab": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print(d)
#{'anidado1': {'a': 1, 'b': 2}, 'anidado2': {'a': 1, 'b': 2}}