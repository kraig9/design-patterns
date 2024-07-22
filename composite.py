from abc import ABC, abstractmethod

# Component interface
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass

# Leaf class
class Leaf(Component):
    def operation(self):
        # Leaf-specific operation
        print("Leaf operation")

# Composite class
class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        # Composite-specific operation
        print("Composite operation")
        for child in self.children:
            child.operation()

# Usage example
if __name__ == "__main__":
    leaf1 = Leaf()
    leaf2 = Leaf()

    composite1 = Composite()
    composite1.add(leaf1)
    composite1.add(leaf2)

    leaf3 = Leaf()

    composite2 = Composite()
    composite2.add(leaf3)
    composite2.add(composite1)

    composite2.operation()
