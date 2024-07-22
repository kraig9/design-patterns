# Define the Visitor interface
class Visitor:
    def visit(self, element):
        pass

# Define the elements to be visited
class ElementA:
    def accept(self, visitor):
        visitor.visit(self)

class ElementB:
    def accept(self, visitor):
        visitor.visit(self)

# Define concrete Visitor implementations
class ConcreteVisitor1(Visitor):
    def visit(self, element):
        if isinstance(element, ElementA):
            print("ConcreteVisitor1 visited ElementA")
        elif isinstance(element, ElementB):
            print("ConcreteVisitor1 visited ElementB")

class ConcreteVisitor2(Visitor):
    def visit(self, element):
        if isinstance(element, ElementA):
            print("ConcreteVisitor2 visited ElementA")
        elif isinstance(element, ElementB):
            print("ConcreteVisitor2 visited ElementB")

# Usage example
elements = [ElementA(), ElementB()]
visitors = [ConcreteVisitor1(), ConcreteVisitor2()]

for element in elements:
    for visitor in visitors:
        element.accept(visitor)