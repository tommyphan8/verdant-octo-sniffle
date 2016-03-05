# Convert a string to an integer number
def strToInt(s):
    string = '0123456789'
    num = 0
    posNeg = False
    pos = 0
    
    if s[0] == '-' or s[0] == '+':
        posNeg = True
        pos = 1
    power = 0
    
    for x in range(len(s)-1, pos-1, -1):
        try:
            num += string.index(s[x])*10**power
            power += 1
        except:
            print('invalid value')
            return
            
        
    if posNeg:
        if s[0] == "-":
            return num * -1
    return num
        

print(strToInt('123'))
print(strToInt('-123'))
print(strToInt('+123'))
print(strToInt('12k3'))
print(strToInt('123 '))