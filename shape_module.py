from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        ...
    @abstractmethod
    def perimeter(self):
        ...
    @abstractmethod
    def save(self):
        ...
    @abstractmethod
    def load(self):
        ...


class Square(Shape):
    def __init__(self, coordinate: tuple, side: int):
        self.__coordinate: tuple = coordinate
        self.__side: int = side

class Rectangle(Shape):
    def __init__(self, coordinate: tuple, width: int, height: int ):
        self.__coordinate: tuple = coordinate
        self.__width: int = width
        self._height: int = height

class Circle(Shape):
    def __init__(self, coordinate: tuple, radius: int):
        self.__coordinate: tuple = coordinate
        self.__radius: int = radius

class Ellipse(Shape):
    ...