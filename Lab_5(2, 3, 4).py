import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def getXY(self):
        return [self.x, self.y]
    def Show(self, text):
        print(text, " = (", self.x, "; ", self.y, ")")
    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    def __mul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self
    def __truediv__(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

P1 = Point(8, 9)
P1.Show("P1")

P2 = Point(4, 3)
P2.Show("P2")

P3 = P1 + P2
P3.Show("P3 = P1 + P2")

P3 = P1 - P2
P3.Show("P3 = P1 - P2")

P3 = P1 * P2
P3.Show("P3 = P1 * P2")

P3 = P1 / P2
P3.Show("P3 = P1 / P2")