

def hexa(dec):
    hex = '0123456789ABCDEF'
    if dec < 16:
        return hex[dec]
    else:
        return hexa(dec//16) + hex[dec%16]
    
print(hexa(79))

def hexDec(hexa):
    hex = '0123456789ABCDEF'
    temp = list(hexa)
    power = 0
    decimal = 0
    while(temp != []):
        decimal += hex.index(temp.pop()) * 16**power
        power += 1
    return decimal

print(hexDec('4F'))    
