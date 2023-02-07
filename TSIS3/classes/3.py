class Shape:
    def __init__(self, area):
        self.area = area
class Square(Shape):
    def __init__(self, length, area):
        self.length = length
        super().__init__(area)
    def areaa(self):
        print(int(self.length) ** 2)
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area1(self):
        return (self.width) * (self.length)
# figure = Square(int(input()))
# figure.areaa()
figure2 = Rectangle(int(input()), int(input()))
print(figure2.area1())