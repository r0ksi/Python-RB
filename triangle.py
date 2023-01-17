class abc:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class A(abc):
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s*(s - self.a)*(s - self.b)*(s - self.c))**0.5


triangle = A(10,12,14)

print("area of triangle : {}".format(triangle.area()))