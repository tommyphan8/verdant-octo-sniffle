#converts hex to decimal
def hex(h):
    hexValue = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    decValue = 0
    temp = list(h)
    temp.reverse()
    for x in range(len(temp)):
        if hexValue.get(temp[x].upper()) == None:
            decValue += int(temp[x]) * (16**x)
        else:
            decValue += int(hexValue.get(temp[x].upper())) * (16**x)
    return decValue

#converts decimal to hex
def dec(d):
    hex = ''
    hexValue = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    stack = []
    result = d
    while(result >= 16):
        remainder = result % 16
        result = int(result/16)
        if remainder >= 10:
            stack.append(hexValue.get(remainder))
        else:
            stack.append(str(remainder))
    stack.append(str(result))
    
    print(stack)    
    for x in range(len(stack)):
        hex += stack.pop()
    return(hex)        
            
        
def hexAdd(a,b):
    temp = hex(a) + hex(b)
    return(
    