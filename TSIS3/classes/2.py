class Shape:
    def __init__(self, area):
        self.area = 0
class Square(Shape):
    def __init__(self, length, area = 0):
        self.length = length
        super().__init__(area)
    def areaa(self):
        print(int(self.length) ** 2)
figure = Square(int(input()))
figure2 = Shape(area = 10)
print(figure2)
figure.areaa()

