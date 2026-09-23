

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.y, self.y - other.y)
    def __mul__(self, other):
        return Point(self.x * other.y, self.y * other.y)
    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __repr__(self):
        return f"(x : {self.x}, y : {self.y})"


a = 10
b = 20
p1 = Point(a,b)
p2 = Point(20,30)

print(p1 + p2)
p1.__add__(p2)


