class Flyweight:
    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        # Perform operations using both shared and unique states
        print(f"Shared state: {self._shared_state}")
        print(f"Unique state: {unique_state}")


class FlyweightFactory:
    def __init__(self):
        self._flyweights = {}



    def get_flyweight(self, shared_state):
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]


# Client code
if __name__ == "__main__":
    factory = FlyweightFactory()

    flyweight1 = factory.get_flyweight("Shared State 1")
    flyweight1.operation("Unique State 1")

    flyweight2 = factory.get_flyweight("Shared State 2")
    flyweight2.operation("Unique State 2")

    flyweight3 = factory.get_flyweight("Shared State 1")
    flyweight3.operation("Unique State 3")