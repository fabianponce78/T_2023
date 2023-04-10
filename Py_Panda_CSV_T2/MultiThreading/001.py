'''
Created on Apr 3, 2023

@author: fponce
'''

'''
    https://www.youtube.com/watch?v=uv6AM0JFhLA&t=704s
'''

import threading
import time

def worker_1(rango):
    lista = list()
    for i in range(rango):
        lista.append(i)
        time.sleep(0.01)
    return lista


t0 = time.time()
lista = worker_1(100)
tf = time.time()-t0
#print(tf)
print('tiempo total en 1 thread: {}'.format(tf))
print('lista = ', lista)
print('lista len', len(lista))


######################################################

n_threads = 4
lista_2 = list()

def worker(inicio, fin):

    for i in range(inicio, fin):
        lista_2.append(i)
        time.sleep(0.01)
    return lista_2    

p = len(lista)//n_threads   # p = pasos ,//  divicion entera
print('\t p =>    ', p)
inicios = list()
fines = list()
inicio = 0
fin = p

for i in range(n_threads):
    inicios.append(inicio)
    fines.append(fin)
    inicio += p
    fin += p

t0 = time.time()    
threads = list()
for i in range(len(inicios)):
    t = threading.Thread(target=worker, args=(inicios[i], fines[i],) )
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()
    
lista_2.sort()    
tf = time.time() - t0
print('---')
print('Tiempo total en {} threads {} \n '.format(n_threads, tf))
print('lista ', lista_2)
print('lista len', len(lista_2))
    
        