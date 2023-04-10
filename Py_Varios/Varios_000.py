'''
Created on Feb 13, 2023

@author: fponce
'''
#===============================================================================
# def indexes(iterable, obj):
#     result = []
#     for index, elem in enumerate(iterable):
#         if elem == obj:
#             yield index
#===============================================================================
            
def indexes(iterable, obj):
    return (index for index, elem in enumerate(iterable) if elem == obj)
            
names = ["Alice", "Alice", "Bob", "Alice", "Charlie", "Alice"]
idxs = indexes(names, "Alice X")
idxs = indexes(names, "Alice")

print(list(idxs))

print(names[1])



#===============================================================================
#===============================================================================
#===============================================================================
print('===============================================================================')
txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)


print('===============================================================================')
txt = "27|28|Doring Gutierrez| Erik |La Loma QRO| 8 23 - May - 2014"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("|", 5)

print('--> ', x)
 
 
 
print('===============================================================================')
txt = "27|28|Doring Gutierrez| Erik |La Loma QRO| 8 23 - May - 2014"
#splits with string in the form of list
list_1 = txt.split("|")
for st in list_1:
    print(st) 
    
    
    
print('===============================================================================')
text = "27|28|Doring Gutierrez| Erik |La Loma QRO| 8 23 - May - 2014"
 