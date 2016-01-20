import math
import random

l = random.sample(range(100),25)

def mergeSort(l):
    if len(l) == 1:
        return l
    else:
        mid = math.floor(len(l)/2)
        a = mergeSort(l[:mid])
        b = mergeSort(l[mid:])
        return merge(a,b)
        

def merge(a,b):
    temp = []
    while(len(a) + len(b) > 0):
        if(len(a) == 0):
            return temp + b
        elif(len(b) == 0):
            return temp + a
        else:
            if(a[0] < b[0]):
                temp.append(a[0])
                a.pop(0)
            else:
                temp.append(b[0])
                b.pop(0)
    return temp
    
print(l)
print(mergeSort(l))

print(mergeSort([2,1,1,3,6,4,4]))