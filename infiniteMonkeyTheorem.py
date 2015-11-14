import random


def generate(strLength, common):
	alphabet = 'abcdefghijklmnopqrstuvwxyz '
	result = ''
	for x in range(strLength):
		if x in common:
			result +=  common[x]
		else:
			result += alphabet[random.randrange(27)]
	return result


def score(goal, testString):
	numSame = 0
	common = {}
	alphabet = 'abcdefghijklmnopqrstuvwxyz '
	for x in range(len(goal)):
		if goal[x] == testString[x]:
			numSame += 1
			common[x] = testString[x]

	return(numSame/len(goal), common)

def main():
	goal = 'hello my name is dr greenthumb'
	newString = generate(len(goal), {})
	newScore = (score(goal, newString))
	bestScore = 0
	count = 0
	while (newScore[0] < 1):
		if newScore[0] > bestScore:
			bestScore = newScore[0]
			print(newScore[0])
			print(newScore[1])
			print(newString)
		newString = generate(len(goal),newScore[1])
		newScore = (score(goal, newString))
		count += 1

	print(newString)
	print("# of tries: ", count)

main()
