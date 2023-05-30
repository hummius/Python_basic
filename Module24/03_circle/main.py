import math

class Circle:

    def __init__(self, x=0.0, y=0.0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def square_found(self):
        s = math.pi * self.r ** 2
        return f'Площадь окружности: {s}'

    def perimeter_found(self):
        c = 2 * math.pi * self.r
        return f'Периметр окружности: {c}'

    def circle_increase(self, number):
        self.r *= number

    def circles_(self, another):
        d = math.sqrt((another.x - self.x) ** 2 + (another.y - self.y) ** 2)
        if d >= self.r + another.r:
            print('Окружности не пересекаются.')
        else:
            print('Окружности пересекаются')

circle_1 = Circle(0.45456, 0.56746, 3)
circle_2 = Circle(-3.934353, -3.54756765, 1)

print(circle_1.square_found())
print(circle_1.perimeter_found())
circle_1.circle_increase(1)
circle_1.circles_(circle_2)