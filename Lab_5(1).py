import math
class Sphere:
    def __init__(self, r=2.0, x=7.0, y=4.0, z=5.0):
        self.r, self.x, self.y, self.z = r, x, y, z
    def get_volume(self):
        volume = 4 / 3.0 * math.pi * self.r ** 3
        return volume 
    def get_square(self):
        square = 4 * math.pi * self.r ** 2
        return square 
    def get_radius(self):
        return self.r
    def get_center(self):
        return (self.x, self.y, self.z)
    def set_radius(self, r):
        self.r = r
    def set_center(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def is_point_inside(self, x, y, z):
        if math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2) <= self.r:
            return True
        return False
    