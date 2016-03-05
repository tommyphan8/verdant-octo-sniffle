def binarySearch(list,value):
    start = 0
    end = len(list) - 1
    found = False
    while(not found and end >= start):
        if value < list[start] or value > list[end]:
            return False
        elif value == list[start] or value == list[end]:
            found = True
        else:
            mid = (end - start // 2) + start
            if list[mid] == value:
                found = True
            elif value < list[mid]:
                end = mid - 1
            elif value > list[mid]:
                start = mid +1
                
    return found

#divide and conquer
def binarySearch1(l, value):
    if len(l) == 0:
        return False
    else:
        mid = (len(l)) // 2 
        if value == l[mid]:
            return True
        elif value < l[mid]:
            return binarySearch1(l[:mid],value)
        elif value > l[mid]:
            return binarySearch1(l[mid+1:],value)
list = [-1, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch1(list,1))
for x in range(-20,66):
    if(binarySearch1(list,x)):
        print(x)