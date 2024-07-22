import copy

class Prototype:
    def __init__(self):
        self._name = None

    def clone(self):
        return copy.deepcopy(self)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


class ConcretePrototype(Prototype):
    def __init__(self):
        super().__init__()

    def clone(self):
        return super().clone()


# Usage example
if __name__ == '__main__':
    prototype = ConcretePrototype()
    prototype.set_name("Prototype 1")

    clone = prototype.clone()
    clone.set_name("Prototype 2")

    print(prototype.get_name())  # Output: Prototype 1
    print(clone.get_name())  # Output: Prototype 2