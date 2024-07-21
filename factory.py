class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Invalid shape type")

# Usage
factory = ShapeFactory()
circle = factory.create_shape("circle")
circle.draw()  # Output: Drawing a circle

rectangle = factory.create_shape("rectangle")
rectangle.draw()  # Output: Drawing a rectangle

square = factory.create_shape("square")
square.draw()  # Output: Drawing a square