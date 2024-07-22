from abc import ABC, abstractmethod

# Abstraction
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass

# Refined Abstraction
class Circle(Shape):
    def draw(self):
        print(f"Drawing a circle with color {self.color}")

class Square(Shape):
    def draw(self):
        print(f"Drawing a square with color {self.color}")

# Implementor
class Color(ABC):
    @abstractmethod
    def fill(self):
        pass

# Concrete Implementor
class RedColor(Color):
    def fill(self):
        return "Red"

class BlueColor(Color):
    def fill(self):
        return "Blue"

# Client
if __name__ == "__main__":
    red_circle = Circle(RedColor())
    red_circle.draw()

    blue_square = Square(BlueColor())
    blue_square.draw()