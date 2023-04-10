'''
Created on Mar 8, 2023

@author: fponce
'''
'''
Created on Mar 7, 2023

@author: fponce
'''




'''
    
    https://www.geeksforgeeks.org/how-to-read-large-text-files-in-python/

'''


input_file = 'TSV/name_basics.tsv'



import time
 
start = time.time()
count = 0
with open(input_file, encoding='UTF-8') as file:
#with open("sample.txt") as file:
    for line in file:
        print(line)
        count = count + 1
end =  time.time()
print("Execution time in seconds: ",(end-start))
print("No of lines printed: ",count)
