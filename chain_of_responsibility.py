class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        pass


class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == 'A':
            print("ConcreteHandler1 handles request:", request)
        elif self.successor is not None:
            self.successor.handle_request(request)


class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == 'B':
            print("ConcreteHandler2 handles request:", request)
        elif self.successor is not None:
            self.successor.handle_request(request)


class ConcreteHandler3(Handler):
    def handle_request(self, request):
        if request == 'C':
            print("ConcreteHandler3 handles request:", request)
        elif self.successor is not None:
            self.successor.handle_request(request)


# Usage example
handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2()
handler3 = ConcreteHandler3()

handler1.successor = handler2
handler2.successor = handler3

handler1.handle_request('A')  # Output: ConcreteHandler1 handles request: A
handler1.handle_request('B')  # Output: ConcreteHandler2 handles request: B
handler1.handle_request('C')  # Output: ConcreteHandler3 handles request: C
handler1.handle_request('D')  # No output