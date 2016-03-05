def bubbleSort(l):
    for x in range(len(l)-1):
        for y in range(len(l)-1-x):
            if l[y] > l[y+1]:
                 temp = l[y]
                 l[y] = l[y+1]
                 l[y+1] = temp

a = [4,3,1,8,9,2,15,14,6]

#shortBubbleSort
#Input: a list
#sorts using bubble sort, however if there are no swap, then the list is already sorted and we
#will exit the loop
def shortBubbleSort(l):
    pos = 0
    sorted = False
    while (pos < len(l)-1) and not sorted:
        print(pos)
        #set sorted to True, we must find one case where it is swap then we will set it to false to continue loop
        sorted = True
        for x in range(len(l)-1-pos):           
            if l[x] > l[x+1]:
                temp = l[x]
                l[x] = l[x+1]
                l[x+1] = temp
                sorted= False
                
        pos += 1
            

shortBubbleSort(a)
print(a)

b = [1,4,2,5,6]
shortBubbleSort(b)
print(b)