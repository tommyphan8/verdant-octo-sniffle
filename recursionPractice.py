def isPa(str):
    if len(str) <= 1:
        return True
    else:
        first = str[0]
        last = str[len(str)-1]
        if first == last :
            return isPa(str[1:len(str)-1])
        return False    


def factorial(num):
    if num <= 1:
        return num
    else:
        return factorial(num-1) * num