def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

class Fraction:
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherFraction):
        newNum = (self.num * otherFraction.den) + (otherFraction.num * self.den)
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum//common, newDen//common)

    def __sub__(self, otherFraction):
        newNum = (self.num * otherFraction.den) - (otherFraction.num * self.den)
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum//common, newDen//common)

    def __mul__(self, otherFraction):
        newNum = self.num * otherFraction.num
        newDen = self.den * otherFraction.den
        common = gcd(newNum, newDen)
        return Fraction(newNum//common, newDen//common)

    def __truediv__(self, otherFraction):
        newNum = self.num * otherFraction.den
        newDen = self.den * otherFraction.num
        common = gcd(newNum, newDen)
        return Fraction(newNum//common, newDen//common)

    def __eq__(self, otherFraction):
        firstNum = self.num * otherFraction.den
        secondNum = otherFraction.num * self.den
        return firstNum == secondNum

    def __lt__(self, otherFraction):
        firstNum = self.num * otherFraction.den
        secondNum = otherFraction.num * self.den
        return firstNum < secondNum

    def __le__(self, otherFraction):
        firstNum = self.num * otherFraction.den
        secondNum = otherFraction.num * self.den
        return firstNum <= secondNum

    def __gt__(self, otherFraction):
        firstNum = self.num * otherFraction.den
        secondNum = otherFraction.num * self.den
        return firstNum > secondNum

    def __ge__(self, otherFraction):
        firstNum = self.num * otherFraction.den
        secondNum = otherFraction.num * self.den
        return firstNum >= secondNum

a = Fraction(1,2)
b = Fraction(1,6)
print(a / b)      