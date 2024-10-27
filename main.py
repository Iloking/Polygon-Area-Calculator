from abc import ABC, abstractmethod

# Abstract Base Class
class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

# Rectangle Class
class Rectangle(Polygon):
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    def calculate_area(self):
        return self._width * self._height

# Triangle Class
class Triangle(Polygon):
    def __init__(self, base, height):
        self._base = base
        self._height = height
    
    def calculate_area(self):
        return 0.5 * self._base * self._height

# Square Class
class Square(Polygon):
    def __init__(self, side):
        self._side = side
    
    def calculate_area(self):
        return self._side ** 2

# Circle Class
class Circle(Polygon):
    def __init__(self, radius):
        self._radius = radius
    
    def calculate_area(self):
        return 3.14159 * (self._radius ** 2)

# Main Function to demonstrate polymorphism
def main():
    shapes = [
        Rectangle(5, 10),
        Triangle(4, 6),
        Square(7),
        Circle(3)
    ]
    
    for shape in shapes:
        print(f"The area of {shape.__class__.__name__} is {shape.calculate_area()}")

if __name__ == "__main__":
    main()
