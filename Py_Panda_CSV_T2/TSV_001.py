'''
Created on Mar 8, 2023

@author: fponce
'''
'''
Created on Mar 7, 2023

@author: fponce
'''


# import module
import fileinput
import time


'''
    
    https://www.geeksforgeeks.org/how-to-read-large-text-files-in-python/

'''


input_file = 'TSV/name_basics.tsv'


#time at the start of program is noted
start = time.time()

#keeps a track of number of lines in the file
count = 0
#for lines in fileinput.input(['sample.txt']):
for lines in fileinput.input([input_file], encoding='UTF-8'):    
    #print(lines)
    count = count + 1
    
#time at the end of program execution is noted
end = time.time()

#total time taken to print the file
print("Execution time in seconds: ",(end - start))
print("No. of lines printed: ",count)
