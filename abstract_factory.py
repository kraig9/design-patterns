from abc import ABC, abstractmethod

# Abstract Product A
class AbstractProductA(ABC):
    @abstractmethod
    def do_something(self):
        pass

# Concrete Product A1
class ConcreteProductA1(AbstractProductA):
    def do_something(self):
        print("Doing something in ConcreteProductA1")

# Concrete Product A2
class ConcreteProductA2(AbstractProductA):
    def do_something(self):
        print("Doing something in ConcreteProductA2")

# Abstract Product B
class AbstractProductB(ABC):
    @abstractmethod
    def do_something_else(self):
        pass

# Concrete Product B1
class ConcreteProductB1(AbstractProductB):
    def do_something_else(self):
        print("Doing something else in ConcreteProductB1")

# Concrete Product B2
class ConcreteProductB2(AbstractProductB):
    def do_something_else(self):
        print("Doing something else in ConcreteProductB2")

# Abstract Factory
class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

# Concrete Factory 1
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()

# Concrete Factory 2
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()

# Client code
def client_code(factory: AbstractFactory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    product_a.do_something()
    product_b.do_something_else()

# Usage
if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    client_code(factory1)

    factory2 = ConcreteFactory2()
    client_code(factory2)