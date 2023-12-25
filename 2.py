import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def circumference(self):
        return 2 * math.pi * self.radius

class Tri:
    def circumference(self):
        return 2 * math.pi * self.radius
# Usage example:
# circle2 = Circle(😎
# print(circle2.area())           # Output: 201.06192982974676
# print(circle2.circumference())  # Output: 50.26548245743669