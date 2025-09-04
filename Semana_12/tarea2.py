
from abc import ABC, abstractmethod
import math

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod
    def calculate_area(self):
        pass



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side


    def calculate_perimeter(self):
        return 4 * self.side


    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


    def calculate_area(self):
        return self.width * self.height


shapes = [
    Circle(5),
    Square(4),
    Rectangle(3, 6)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} -> Perimeter: {shape.calculate_perimeter():.2f}, Area: {shape.calculate_area():.2f}")
