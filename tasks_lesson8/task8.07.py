class ComplexNumbers:
    a: int
    b: int

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        self.a += other.a
        self.b += other.b
        return ComplexNumbers(self.a, self.b)

    def __mul__(self, other):
        self.a = self.a * other.a - self.b * other.b
        self.b = self.a * other.b + self.b * other.a
        return ComplexNumbers(self.a, self.b)

    def __str__(self):
        if self.a == 0 and self.b == 0:
            return f'комплексное число z = 0'
        if self.a == 0:
            return f'комплексное число z = {self.b}i'
        elif self.b == 0:
            return f'комплексное число z = {self.a}'
        elif self.b < 0:
            return f'комплексное число z = {self.a} - {-self.b}i'
        else:
            return f'комплексное число z = {self.a} + {self.b}i'


z1 = ComplexNumbers(4, -6)
z2 = ComplexNumbers(2, 5)

print(f'Результат сложения: {z1 + z2}')
print(f'Результат произведения: {z1 * z2}')
