'''
Lecture 15: Adapter Pattern

The Adapter Pattern is a structural design pattern that allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.
'''
# Define an interface expected by the client
class Target:
    def request(self):
        pass

# Create a class that needs to be adapted
class Adaptee:
    def specific_request(self):
        return "Adaptee's specific request."

# Create an adapter class
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: {self.adaptee.specific_request()}"

# Use the Adapter Pattern
adaptee = Adaptee()
adapter = Adapter(adaptee)

result = adapter.request()
print(result)

'''
In this example, we have an existing class Adaptee with a specific interface, and we want to use it as a Target interface. The Adapter class wraps the Adaptee object and provides the expected interface of the Target class. It adapts the specific request of Adaptee to work with the client code.

Key Points:

The Adapter Pattern allows objects with incompatible interfaces to work together.
It's useful when you need to make existing classes compatible with new code without modifying their source code.
The adapter acts as a bridge between the client code and the adapted object.
'''