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
    ...

class Rectangle(Shape):
    ...

class Circle(Shape):
    ...

class Ellipse(Shape):
    ...