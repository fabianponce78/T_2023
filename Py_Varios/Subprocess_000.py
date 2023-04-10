'''
Created on Mar 14, 2023

@author: fponce
'''
import subprocess
#from bs4.diagnose import profile

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
print('\t data = ', data)

profiles =[i.split(":")[1][1:-1]  for i in data if "All User Profile" in i   ]
for i in profiles:
    #print('\t i =' ,i)

    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    
    print('\t\t results => ',results)
    
    for j in results:
        '''
        if j in ('\r'):
            print('is r')
        else:
            print('... ',j)
        '''
        if j not in ('\r'):
            print('... ',j)
    
    '''
    try:
        #print("{:<30}|{:<}",   format(i,results[0]) )
        #print("{:<30}|{:<}",   format(i,results[0]) )
        print( i ,'--',results[0]) 
    except IndexError:
        #print("{:<30} | {:<}", format(i,** ) )
        print('\t\t IndexError. ',i)
    '''
            
'''
print("Floating point {0:.2f}".format(345.7916732))
Floating point 345.79
'''            

