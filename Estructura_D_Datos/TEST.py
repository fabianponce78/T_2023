'''
Created on Jan 16, 2023

@author: fponce
'''

def find_max(nums):
    max_num = float("-inf") # smaller than all other numbers
    for num in nums:
        if num > max_num:
            #num= max_num
            #max_num += 1
            max_num = num  ##
            #max_num += num
    return max_num

nums = [5,16,6,1,20]
x = find_max(nums)
print("... ", x)
    