from abc import ABC, abstractmethod
from math import pi
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

    def area(self):
        return self.__side * 2

    def perimeter(self):
        return self.__side * 4



class Rectangle(Shape):
    def __init__(self, coordinate: tuple, width: int, height: int ):
        self.__coordinate: tuple = coordinate
        self.__width: int = width
        self.__height: int = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__width * self.__height) * 2

class Circle(Shape):
    def __init__(self, coordinate: tuple, radius: int):
        self.__coordinate: tuple = coordinate
        self.__radius: int = radius

    def area(self):
        return (self.__radius * pi) ** 2

    def perimeter(self):
        return self.__radius * pi * 2

class Ellipse(Shape):
    ...