class Circle:
    pi = 3.14

    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius * radius * self.pi

    def setRadius(self, radius):
        self.radius = radius
        self.area = radius * radius * self.pi

    def circumference(self):
        return self.radius * 2 * Circle.pi


x = Circle()

print(x.area)
print(x.circumference())

x.setRadius(2)
print(x.radius)
print(x.area)
print(x.circumference())