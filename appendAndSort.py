a = [1,2,3,4,5]
b = [6,7,8,9,10,'','','','','']
n = 5

def append(a,b):
    for x in range(5):
        b[x+5] = a[x]
        
def sort(b):
    for x in range(len(b)):
        print("First variable " + str(x))
        lowest = x
        for y in range(x+1, len(b)):
            print("Second variable " + str(y))
            if  b[y] < b[lowest]:
                lowest = y
        if lowest != x:
            print("Lowest: " + str(lowest))
            temp = b[x]
            b[x] = b[lowest]
            b[lowest] = temp
            print(b)
    
    
    
append(a,b)
print(b)
sort(b)
print(b)