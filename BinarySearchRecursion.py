# This program is written to implement Binary Search algorithm using Recursion in Python

def bSearch(list, index0, indexn, val):
    
    if index0 > indexn:
        return None
    else:
        midval = index0 + (indexn-index0)//2
        
    if val < list[midval]:
        return bSearch(list,index0,midval-1,val)
    elif val > list[midval]:
        return bSearch(list,midval+1,indexn,val)
    else:
        return midval
        
list = [11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19]

print(bSearch(list,0,8,18))
print(bSearch(list,0,8,13))
print(bSearch(list,0,8,20))
