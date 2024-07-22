# Define the interface for the subject and proxy
class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request")

class Proxy(Subject):
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        # Perform additional operations before delegating to the real subject
        print("Proxy: Logging request")
        self.real_subject.request()
        # Perform additional operations after the real subject has handled the request
        print("Proxy: Cleaning up")

# Usage
if __name__ == "__main__":
    proxy = Proxy()
    proxy.request()