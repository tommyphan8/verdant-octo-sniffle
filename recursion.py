import string
#Recursion practice 

#sum of a list of numbers 
#L: list of numbers
#returns sum of numbers
def sum(L):
    if len(L) <= 1:
        return L[0]
    else:
        return(L[0] + sum(L[1:]))

print(sum([1,2,3,4,5]))

#Convert to different base
#n: number to convert
#b: base
#returns number after converting 
def toStr(n,b):
    letters = '0123456789ABCDEF'
    if n<b:
        return letters[n]
    else:
        return toStr(n//b, b) + letters[n%b]

print(toStr(1453,16))

#Reverse String
#str: input a String
#returns string in reveresed
def reverse(str):
    if len(str) == 0:
        return 'Cannot reverse empty string'
    elif len(str) == 1:
        return str[0]
    else:
        return reverse(str[1:]) + str[0]

print(reverse('radar'))


#Removes punctuation and spaces in string
#str: the string we will process
#returns the proccessed string
def translate(str):
    replace_punctuation = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    str = str.replace('', ' ')
    return str.translate(replace_punctuation)

#Checks if a string is a palindrome 
#str: the string we will check
#returns boolean
#Example: radar is a palindrom if spelled backwards
def isPal(str):
    return translate(reverse(str)) == translate(str)

print(isPal('radaar'))

class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fib(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            temp = self.fib(n-1) + self.fib(n-2)
            return temp

a = Solution()
print(a.fib(40))