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
        
#assume pop front is o1, if not then it will be on^2
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

def merge1(a,b):
    temp = []
    i = 0
    j = 0
    while(len(a) > i and len(b) > j):
        if(a[i] < b[j]):
            temp.append(a[i])
            i = i + 1
        else:
            temp.append(b[j])
            j = j + 1
    while(i < len(a)):
        temp.append(a[i])
        i = i + 1
    
    while(j < len(b)):
        temp.append(b[j])
        j = j + 1
    return temp


print(l)
print(mergeSort(l))

print(mergeSort([2,1,1,3,6,4,4]))