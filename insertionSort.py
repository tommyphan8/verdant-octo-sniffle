def insertion(l):
    for x in range(1,len(l)):
        
        compare = x
        pos = x-1
        sorted = False
        while(pos >= 0 and not sorted):
            sorted = True
            if l[pos] > l[compare]:
                temp = l[compare]
                l[compare] = l[pos]
                l[pos] = temp
                compare = pos
                pos -= 1
                sorted = False
                


def insertionSort(l):
    for x in range(1,len(l)):
        currentValue = l[x]
        pos = x
        while pos > 0 and currentValue < l[pos-1]:
            l[pos] = l[pos-1]
            pos -= 1
            
        l[pos] = currentValue

alist = [5,4,3,2,1]
insertionSort(alist)
print(alist)




#l = [1,2,3,4]
l = [4,3,2,1]
insertion(l)
print(l)
alist = [54,26,93,17,77,31,44,55,20]
insertion(alist)
print(alist)