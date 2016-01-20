# "Write a program that prints the numbers from 1 to 100. But for multiples of three print 
# “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which 
# are multiples of both three and five print “FizzBuzz”."
def fizzBuzz(startNum, endNum):
    tmp1 = []

    for x in range(startNum, endNum+1):
        if x%3 == 0 and x%5 == 0:
            # print("FizzBuzz")
            tmp1.append("FizzBuzz")
        elif x%3 == 0:
            # print("Fizz")
            tmp1.append("Fizz")
        elif x%5 == 0:
            # print("Buzz")
            tmp1.append("Buzz")
        else:
            # print(x)
            tmp1.append(x)
    return tmp1

def compareList(tmp, tmp1):
    for x in range(len(tmp)):
        if tmp[x] != tmp1[x]:
            return False
    return True
        

print(fizzBuzz(-50,50))