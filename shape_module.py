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
        return round(self.__side * 2, 2)

    def perimeter(self):
        return round(self.__side * 4, 2)

    def save(self):
        __name_file = "Squares.txt"
        with open(__name_file, 'a', encoding='utf-8') as file:
            file.writelines(["Square,", str(self.__side) + ',', str(self.__coordinate) + ',',
                             str(self.perimeter()) + ',', str(self.area())])

    def load(self):
        ...


class Rectangle(Shape):
    def __init__(self, coordinate: tuple, width: int, height: int ):
        self.__coordinate: tuple = coordinate
        self.__width: int = width
        self.__height: int = height

    def area(self):
        return round(self.__width * self.__height, 2)

    def perimeter(self):
        return round((self.__width * self.__height) * 2, 2)

    def save(self):
        __name_file = "Rectangles.txt"
        with open(__name_file, 'a', encoding='utf-8') as file:
            file.writelines(["Rectangle,", str(self.__width) + ',', str(self.__height) + ',',
                             str(self.__coordinate) + ',', str(self.perimeter()) + ',', str(self.area())])

    def load(self):
        ...


class Circle(Shape):
    def __init__(self, coordinate: tuple, radius: int):
        self.__coordinate: tuple = coordinate
        self.__radius: int = radius

    def area(self):
        return round((self.__radius * pi) ** 2, 2)

    def perimeter(self):
        return round(self.__radius * pi * 2, 2)

    def save(self):
        __name_file = "Circles.txt"
        with open(__name_file, 'a', encoding='utf-8') as file:
            file.writelines(["Circle,", str(self.__radius) + ',',
                             str(self.__coordinate) + ',', str(self.perimeter()) + ',', str(self.area())])

    def load(self):
        ...

class Ellipse(Shape):
    def __init__(self, coordinate: tuple, width_el: int, height_el: int ):
        self.__coordinate: tuple = coordinate
        self.__width_el: int = width_el
        self.__height_el: int = height_el

    def area(self):
        return round(pi * (self.__height_el/ 2) * (self.__width_el / 2), 2)

    def perimeter(self):
        return round(2 * pi * sqrt((self.__width_el ** 2 + self.__height_el ** 2) / 8), 2)

    def save(self):
        __name_file = "Ellipses.txt"
        with open(__name_file, 'a', encoding='utf-8') as file:
            file.writelines(["Ellipse,", str(self.__width_el) + ',', str(self.__height_el),
                             str(self.__coordinate) + ',', str(self.perimeter()) + ',', str(self.area())])

    def load(self):
        ...
