from math import pi
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        print()

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return round((pi * self.__radius**2), 2)

class Rectangle(Shape):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def area(self):
        return self.__a * self.__b

class Triangle(Shape):
    def area(self, a=None, high=None):
        return (a * high) / 2

circle = Circle(20)
print(circle.area())

rectengle = Rectangle(4, 8)
print(rectengle.area())

triangle = Triangle()
print(triangle.area(10, 8))
print(triangle.area(5, 4))
