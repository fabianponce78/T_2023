'''
Created on Jan 11, 2023

@author: fponce
'''

'''
https://j2logo.com/python/tutorial/tipo-list-python/

list python – Listas en Python: El tipo list y operaciones más comunes
'''


'''
┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌
┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘
┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌
┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘
┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌
'''

Str_Lineas_1 = '┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌' + '\n'
Str_Lineas_2 = '┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘' + '\n'
Str_Lineas_3 = '┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌' + '\n'
Str_Lineas_4 = '┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘' + '\n'
Str_Lineas_5 = '┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌┘┌' + '\n'

Str_Lineas = '\n' + Str_Lineas_1 + Str_Lineas_2 + Str_Lineas_3 + Str_Lineas_4 + Str_Lineas_5


print(Str_Lineas)

###################################################################################################
###################################################################################################

Lista_A = [3, 'a', 8, 7.2, 'hola', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
Lista_B = [3, 'a', 'X', 'Y', 'Z']
Lista_C = [1, 2, 3, 4, 5]

print('Lista_A = ', Lista_A)

print('Lista_A = ', Lista_A[0])
print('Lista_A = ', Lista_A[-1])

print('Lista_A = ', Lista_A[1:3])

print('Lista_A = ', Lista_A.append('123'))

print('Lista_A = ', Lista_A)


nueva_lista = Lista_A + Lista_B
print('nueva_lista = ', nueva_lista)


Lista_C *= 3
print('Lista_C = ', Lista_C)
print('nueva_lista = ', nueva_lista)

print(Str_Lineas)

for i in Lista_A:
    print('... ',i)
    

###################################################################################################
###################################################################################################
print(Str_Lineas)    
#Modificar elementos de una lista
vocales = ['o', 'o', 'o', 'o', 'u']

print('vocales = ', vocales)
# Actualiza el elemento del índice 0
vocales[0] = 'a'
print('vocales = ', vocales)

# Actualiza los elementos entre las posiciones 1 y 2
vocales[1:3] = ['e', 'i']
print('vocales = ', vocales)


###################################################################################################
###################################################################################################
#Eliminar un elemento de una lista en Python
# Elimina el elemento del índice 1
vocales = ['a', 'e', 'i', 'o', 'u']
del vocales[1]
print('vocales = ', vocales)

# Elimina los elementos con índices 2 y 3
vocales = ['a', 'e', 'i', 'o', 'u']
del vocales[2:4]
print('vocales = ', vocales)

# Elimina todos los elementos
del vocales[:]
print('vocales = ', vocales)



letras = ['a', 'b', 'c']
letras.clear()
print('letras = ', letras)



###################################################################################################
###################################################################################################
## Longitud (len) de una lista en Python

vocales = ['aa', 'e', 'i', 'o', 'u']
print('len(vocales) = ', len(vocales))


###################################################################################################
###################################################################################################
print(Str_Lineas)
#sort list Python – Ordenar una lista en Python
 
# Lista desordenada de números enteros
numeros = [3, 2, 6, 1, 7, 4]
print('numeros = ', numeros)
# Identidad del objeto numeros

print('id = ', id(numeros))

# Se llama al método sort() para ordenar los elementos de la lista
numeros.sort()
print('numeros = ', numeros)

# Se comprueba que la identidad del objeto numeros es la misma

print('id = ', id(numeros))