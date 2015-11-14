# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']


#o(n^2)
def duplicate(letter, temp):
  for x in temp:
    if letter == x:
        return True
  return False
    	

wordlist = ['cat','dog','rabbit']

#o(n^3)
temp = []
for x in wordlist:
  for letter in x:
    if not duplicate(letter, temp):
      temp.append(letter)

#o(n^2) average case      
temp = []
s = set()
for x in wordlist:
  for letter in x:
    if letter not in s:
        temp.append(letter)
        s.add(letter)
    
      
print(temp)

