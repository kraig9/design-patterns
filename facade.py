# Subsystem classes
class SubsystemA:
    def operation_a(self):
        print("Subsystem A operation")

class SubsystemB:
    def operation_b(self):
        print("Subsystem B operation")

class SubsystemC:
    def operation_c(self):
        print("Subsystem C operation")

# Facade class
class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()
        self.subsystem_c = SubsystemC()

    def operation(self):
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()
        self.subsystem_c.operation_c()

# Client code
def main():
    facade = Facade()
    facade.operation()

if __name__ == "__main__":
    main()