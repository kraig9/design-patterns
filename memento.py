class Originator:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def restore_memento(self, memento):
        self._state = memento.get_state()

    def show_state(self):
        print(f"Current state: {self._state}")


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        self._mementos.append(memento)

    def get_memento(self, index):
        return self._mementos[index]


# Usage example
originator = Originator()
caretaker = Caretaker()

originator.set_state("State 1")
originator.show_state()

# Save the state
memento = originator.create_memento()
caretaker.add_memento(memento)

originator.set_state("State 2")
originator.show_state()

# Save the state again
memento = originator.create_memento()
caretaker.add_memento(memento)

originator.set_state("State 3")
originator.show_state()

# Restore the first saved state
memento = caretaker.get_memento(0)
originator.restore_memento(memento)
originator.show_state()