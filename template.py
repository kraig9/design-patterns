from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self):
        self.common_operation1()
        self.specialized_operation1()
        self.common_operation2()
        self.specialized_operation2()

    def common_operation1(self):
        print("Executing common operation 1")

    def common_operation2(self):
        print("Executing common operation 2")

    @abstractmethod
    def specialized_operation1(self):
        pass

    @abstractmethod
    def specialized_operation2(self):
        pass

class ConcreteClass(AbstractClass):
    def specialized_operation1(self):
        print("Executing specialized operation 1")

    def specialized_operation2(self):
        print("Executing specialized operation 2")

# Usage
if __name__ == "__main__":
    concrete_object = ConcreteClass()
    concrete_object.template_method()