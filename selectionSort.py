def selectionSort(l):
    for x in range(len(l)-1):
        mini = x
        for y in range(x+1,(len(l))):
            try:
                if l[y] < l[mini]:
                    mini = y
            except:
                print(y,mini)
        if l[mini] != x:
            temp = l[x]
            l[x] = l[mini]
            l[mini] = temp

a = [4,3,1,8,9,2,15,14,6]
selectionSort(a)
print(a)