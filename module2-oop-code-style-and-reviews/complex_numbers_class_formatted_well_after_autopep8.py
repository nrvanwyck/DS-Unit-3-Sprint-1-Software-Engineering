class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def add(self, addend):
        return Complex(self.r + addend.r,
                       self.i + addend.i)

    def subtract(self, subtrahend):
        return Complex(self.r - subtrahend.r,
                       self.i - subtrahend.i)

    def multiply(self, multiplicand):
        return Complex((self.r * multiplicand.r) - (self.i * multiplicand.i),
                       (self.r * multiplicand.i) + (self.i * multiplicand.r))

    def divide(self, divisor):
        return Complex(((self.r * divisor.r) + (self.i * divisor.i)) /
                       ((divisor.r)**2 + (divisor.i)**2),
                       ((self.i * divisor.r) - (self.r * divisor.i)) /
                       ((divisor.r)**2 + (divisor.i)**2))


a = Complex(3.0, -4.5)
b = Complex(4.0, -9)

x = a.add(b)
y = a.subtract(b)
z = a.multiply(b)
w = a.divide(b)

print('sum:', x.r, '+', str(x.i) + 'i',
      '\ndifference:', y.r, '+', str(y.i) + 'i',
      '\nproduct:', z.r, '+', str(z.i) + 'i',
      '\nquotient:', w.r, '+', str(w.i) + 'i')
