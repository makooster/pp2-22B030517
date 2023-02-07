class Point:
    def __init__(self, x_point, y_point):
        self.x_point = x_point
        self.y_point = y_point
    def show(self):
        print(self.x_point + " " + self.y_point)
    def move(self, x_point1, y_point1):
        self.x_point1 = x_point1
        self.y_point1 = y_point1
    def dist(self):
        return ((self.x_point1 - self.x_point)**2 + (self.y_point1 - self.y_point)**2)**0.5
point1 = Point(int(input()), int(input()))
point1.move(int(input()), int(input()))
print("%.2f" % point1.dist())