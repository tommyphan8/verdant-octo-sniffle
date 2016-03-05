# You are given an integer X. You must choose a group of (at least two) identical 
# adjacent digits and remove a single digit from that group.

# For example, from the integer X = 223336226, you can obtain:

# 23336226
# 22336226
# 22333626

# You want to find th e largest number that can be obtained from X by removing
# one digit from a group of identical adjacent digits. In the above example the
# largest such number is 23336226


x = 223336226

def solution(x):
    temp = str(x)
    group  = []
    num = temp[0]
    for x in range(len(temp)-1):
        if temp[x] == temp[x+1]:
            num += temp[x+1]
        else:
            group.append(num)
            num = temp[x+1]
    group.append(num)

    
    max = None
    for x in range(len(group)):
        temp = list(group)
        if len(temp[x]) > 1:
            temp[x] = temp[x][1:]
            num = int(''.join(temp))
            if max == None or num > max:
                max = num
            
    return max
            
print(solution(x))
            
            