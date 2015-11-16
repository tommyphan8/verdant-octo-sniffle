def min(n):
    min = None
    for x in n:
        if min == None:
            min = x
        elif x < min:
            min = x
    return min


def sort(n):
    min = None
    for x in range(len(n)):
        min = x
        for y in range(x+1, len(n)):
            if n[y] < n[min]:
                min = y
        if min != n[x]:
            temp = n[x]
            n[x] = n[min]
            n[min] = temp
a = [5,2,4,6,3,6,6]            
sort(a)
print(a)    


for (x = 0; i <= 5, x+2)
    print("hello")
#print(sort([4,2,3,#1]))
#print(min([4,2,3,-5,1]))