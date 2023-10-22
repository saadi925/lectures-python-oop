'''
Lecture 19: Chain of Responsibility Pattern

The Chain of Responsibility Pattern is a behavioral design pattern that passes requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain. It provides a way to decouple senders and receivers of requests.
'''
from abc import ABC, abstractmethod

# Define an abstract handler interface
class Handler(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    @abstractmethod
    def handle_request(self, request):
        pass

# Create concrete handler classes
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            return f"ConcreteHandlerA: Handled request {request}"
        elif self.successor:
            return self.successor.handle_request(request)
        return f"ConcreteHandlerA: Cannot handle request {request}"

class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            return f"ConcreteHandlerB: Handled request {request}"
        elif self.successor:
            return self.successor.handle_request(request)
        return f"ConcreteHandlerB: Cannot handle request {request}"

# Use the Chain of Responsibility Pattern
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB(handler_a)

request1 = "A"
result1 = handler_b.handle_request(request1)
print(result1)

request2 = "B"
result2 = handler_b.handle_request(request2)
print(result2)

request3 = "C"
result3 = handler_b.handle_request(request3)
print(result3)

'''
In this example, we have an abstract handler class Handler with concrete handler classes ConcreteHandlerA and ConcreteHandlerB. Handlers are organized into a chain, and each handler can decide whether to process the request or pass it to the next handler. The client initiates the request with the first handler in the chain.

Key Points:

The Chain of Responsibility Pattern decouples senders and receivers of requests.
Handlers are organized into a chain, and each handler can process or pass requests to the next handler.
It's useful for creating flexible and extensible processing pipelines.
'''