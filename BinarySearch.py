# This program is written to implement Binary Search algorithm in Python

def binSearch(list, val):
    
    list_Size = len(list) - 1
    
    index0 = 0
    indexn = list_Size
    
    while index0 <= indexn:
        
        midval = (index0+indexn)//2
        
        if list[midval] == val:
            return midval
            
        if list[midval] > val:
            indexn = midval - 1
        else:
            index0 = midval + 1
            
    if index0 > indexn:
        return None
        
list = [12 , 13 , 14 , 15 , 16, 17, 18]

print(binSearch(list,17))
print(binSearch(list,11))
