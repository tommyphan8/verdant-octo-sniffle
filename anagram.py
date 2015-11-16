
#O(n^2)
def anagram(a, b):
    temp = list(b)
    posA = 0
    contSearch = True
    while(posA < len(a) and contSearch):
        posB = 0
        found = False
        while(posB < len(b) and not found):
            if a[posA] == temp[posB]:
                found = True
            else:
                posB += 1
        if found == True:
            temp[posB] = None
            posA += 1
        else:
            contSearch = False
    return contSearch

#O(n)
def anagram1(a,b):
    count = dict()
    count1 = dict()
    for x in range(len(a)):
        if a[x] not in count:
            count[a[x]] = 0
        if b[x] not in count1:
            count1[b[x]] = 0
        count[a[x]] += 1
        count1[b[x]] += 1
    return count == count1

print(anagram("abcd", "bcda"))