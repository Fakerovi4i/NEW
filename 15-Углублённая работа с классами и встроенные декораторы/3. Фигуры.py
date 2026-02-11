from abc import ABC, abstractmethod

class Figure(ABC):
    def __init__(self, x, y, side_1, side_2):
        self.x = x
        self.y = y
        self.side_1 = side_1
        self.side_2 = side_2

    def move(self, x, y):
        self.x = x
        self.y = y

class ResizeMixin:
    def resize(self, size_1, size_2):
        self.side_1 = size_1
        self.side_2 = size_2

class Rectangle(Figure, ResizeMixin):
    '''Дочерний клас: Родительский класс Фигура'''

class Square(Figure, ResizeMixin):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)


rect = Rectangle(10, 10, 20, 10)
square = Square(10, 10, 20)

rect.resize(30, 40)
print(rect.side_1, rect.side_2)
square.resize(70, 70)
print(square.side_1, square.side_2)