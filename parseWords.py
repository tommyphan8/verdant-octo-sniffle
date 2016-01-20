def parse(str):
    temp = ''
    words = []
    for x in range(len(str)):
        if x == len(str)-1:
            if str[x] != ' ':
                temp += str[x]
            words.append(temp)
        elif str[x] == ' ' and temp != '':
            words.append(temp)
            temp = ''
        elif str[x] != ' ':
            temp += str[x]
    print(words)
        
parse(str)