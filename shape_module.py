from abc import ABC, abstractmethod
from math import pi, sqrt
class Shape(ABC):
    @abstractmethod
    def area(self):
        ...
    @abstractmethod
    def perimeter(self):
        ...
    @abstractmethod
    def save(self, path: str):
        ...
    @abstractmethod
    def load(self, path: str):
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

    def save(self, path: str):
        with open(path, 'a', encoding= 'utf-8') as file:
            ...


class Circle(Shape):
    def __init__(self, coordinate: tuple, radius: int):
        self.__coordinate: tuple = coordinate
        self.__radius: int = radius

    def area(self):
        return (self.__radius * pi) ** 2

    def perimeter(self):
        return self.__radius * pi * 2

class Ellipse(Shape):
    def __init__(self, coordinate: tuple, width_el: int, height_el: int ):
        self.__coordinate: tuple = coordinate
        self.__width_el: int = width_el
        self.__height_el: int = height_el

    def area(self):
        return pi * (self.__height_el/ 2) * (self.__width_el / 2)

    def perimeter(self):
        return 2 * pi *sqrt((self.__width_el ** 2 + self.__height_el ** 2) / 8)
