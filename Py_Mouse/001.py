'''
Created on Sep 29, 2022

@author: fponce
'''

import pyautogui
import time

# generate random integer values
from random import seed
from random import randint

'''
x = randint(1, 9)
y = randint(1, 9)

print(" x = ", x)
print(" y = ", y)
'''

while True:
    x = randint(1, 80)
    y = randint(1, 80)

    print(" x = ", x)
    print(" y = ", y)
    #move your cursor 10 pixels
    pyautogui.moveRel(x,y)
    #pauses your code from running for 2 seconds
    time.sleep(3)




'''
while True:
    #move your cursor 10 pixels
    pyautogui.moveRel(0,10)
    #pauses your code from running for 2 seconds
    time.sleep(2)
'''    
    
    