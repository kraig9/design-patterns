# Define the base component interface
class Component:
    def operation(self):
        pass

# Define the concrete component
class ConcreteComponent(Component):
    def operation(self):
        print("Executing operation in ConcreteComponent")

# Define the base decorator class
class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()

# Define concrete decorators
class ConcreteDecoratorA(Decorator):
    def operation(self):
        super().operation()
        print("Executing additional operation in ConcreteDecoratorA")

class ConcreteDecoratorB(Decorator):
    def operation(self):
        super().operation()
        print("Executing additional operation in ConcreteDecoratorB")

# Usage example
if __name__ == "__main__":
    # Create a concrete component
    component = ConcreteComponent()

    # Wrap the component with decorators
    decorated_component = ConcreteDecoratorB(ConcreteDecoratorA(component))

    # Call the operation on the decorated component
    decorated_component.operation()