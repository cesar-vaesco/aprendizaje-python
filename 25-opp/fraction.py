class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def show(self):
        print(f"{self.numerator}/{self.denominator}")


f1 = Fraction(2, 3)
f1.show()
f2 = Fraction(2, -3)
f2.show()
f3 = Fraction(-5, -6)
f3.show()
f4 = Fraction(10)
f4.show()
