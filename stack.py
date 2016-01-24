class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):

        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False
    
    def size(self):
        return len(self.items)

#Pass a string myStr and returns a new string in reverse
def reverse(myStr):
    temp = Stack()
    newStr = ''
    for x in myStr:
        temp.push(x)
    
    while not temp.isEmpty():
        newStr += str(temp.peek())
        temp.pop()
    return newStr


def parChecker(myStr):
    temp = Stack()
    balanced = True
    index = 0
    while index < len(myStr) and balanced:
        if myStr[index] in "({[":
            temp.push(myStr[index])
        else:
            if temp.isEmpty():
                balanced = False
            else:
                pop = temp.pop()
                if not help(pop, myStr[index]):
                    balanced = False      
        index += 1
    if temp.isEmpty() and balanced:
        return True
    else:
        return False

# print(parChecker('{{([][])}()}'))
# print(parChecker('[{()]'))

#Checks if parentheses match its corresponding closing parentheses
def help(pop, sym):
    opens = "{[("
    closes = "}])"
    
    return opens.index(pop) == closes.index(sym)

#Use stack to convert to binary
def baseConverter(num, base):
    digits = '0123456789ABCDEF'
    temp = Stack()
    myStr = ''
    while num != 0:
        temp.push(num%base)
        num //= base
    while not temp.isEmpty():
        myStr += digits[temp.pop()]

    return myStr

# print(baseConverter(42,2))
# print(baseConverter(256,16))
# print(baseConverter(25555,16))

def infixToPostfix(myStr):
    oper = {}
    oper['*'] = 3
    oper['/'] = 3
    oper['+'] = 2
    oper['-'] = 2
    oper['('] = 1
    temp = Stack()
    strList = list(myStr)
    convStr = ''
    for x in strList:
        if x in 'ABCDEFGHIJFKLMOPQRSTUVWXYZ' or x in '0123456789':
            convStr += x
        elif x == '(':
            temp.push(x)
        elif x == ')':
            found = False
            pop = temp.pop()
            while not found:
                convStr += pop
                pop = temp.pop()
                if pop == '(':
                    found = True
        elif x in '*/+-':
            while (not temp.isEmpty()) and (oper[temp.peek()] >= oper[x]):
                convStr += temp.pop()
            temp.push(x)

    while (not temp.isEmpty()):
        convStr += temp.pop()

    return convStr

print(infixToPostfix("A * B + C * D"))
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))


