class circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

class triangle:
    def __init__(self, a, b, c, height_a):
        self.a = a
        self.b = b
        self.c = c
        self.height_a = height_a

    def area(self):
        return self.height_a * self.a * 0.5
    def perimeter(self):
        return self.a + self.b + self.c
    
class square:
    def __init__(self, side_len):
        self.side_len = side_len

    def area(self):
        return self.side_len * self.side_len
    def perimeter(self):
        return 4 * self.side_len 