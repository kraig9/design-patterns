class State:
    def do_action(self, context):
        pass

class StateA(State):
    def do_action(self, context):
        print("State A: Performing action")
        context.state = StateB()

class StateB(State):
    def do_action(self, context):
        print("State B: Performing action")
        context.state = StateC()

class StateC(State):
    def do_action(self, context):
        print("State C: Performing action")
        context.state = StateA()

class Context:
    def __init__(self):
        self.state = StateA()

    def request(self):
        self.state.do_action(self)

# Usage example
context = Context()
context.request()  # Output: State A: Performing action
context.request()  # Output: State B: Performing action
context.request()  # Output: State C: Performing action
context.request()  # Output: State A: Performing action