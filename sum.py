a = list(range(1,100))

def sum(a, num):
    for x in range(len(a)):
        for y in range(x+1, len(a)):
            if a[x] + a[y] == num:
                return True
    return False
    
print(sum(a,1011))