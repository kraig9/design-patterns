class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer:
    def update(self, message):
        print(f"Received message: {message}")


# Usage example
subject = Subject()

observer1 = Observer()
observer2 = Observer()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello, observers!")

subject.detach(observer2)

subject.notify("Observer2 has been detached.")
