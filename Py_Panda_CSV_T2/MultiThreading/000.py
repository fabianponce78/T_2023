


'''
https://www.youtube.com/watch?v=uv6AM0JFhLA&t=704s
'''

import threading
import time


def worker():
    print('Inicio')
    time.sleep(2)
    print('fin')
    
    
#worker()


threads = list()
for i in range(5):
    t = threading.Thread(target=worker)    
    threads.append(t)
    t.start()

for t in threads:
    t.join()    