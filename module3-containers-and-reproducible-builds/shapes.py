#shapes class
class Shape:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "defined later"
        self.author = "Nobody as of yet"

#methods
    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def describe(self, text):
        self.description = text

    def authorName(self, text):
        self.author = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

class Square(Shape):
    def __init__(self, x):
        self.x = x
        self.y = x

one = Square(10)
print(one.area())
print(one.perimeter())

rectangle = Shape(100, 50)

print(rectangle.area())
print(rectangle.perimeter())
rectangle.describe('twice as long as wide')

rectangle.scaleSize(0.5)
print(rectangle.area())