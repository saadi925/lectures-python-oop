'''
Lecture 17: Facade Pattern

The Facade Pattern is a structural design pattern that provides a simplified interface to a set of interfaces in a subsystem. It defines a higher-level interface that makes the subsystem easier to use, hiding its complexity.
'''
# Subsystem 1
class Subsystem1:
    def operation1(self):
        return "Subsystem 1: Operation 1"

    def operation2(self):
        return "Subsystem 1: Operation 2"

# Subsystem 2
class Subsystem2:
    def operation1(self):
        return "Subsystem 2: Operation 1"

    def operation2(self):
        return "Subsystem 2: Operation 2"

# Facade
class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()

    def operation(self):
        result = "Facade orders subsystems to perform the following operations:\n"
        result += self.subsystem1.operation1() + "\n"
        result += self.subsystem1.operation2() + "\n"
        result += self.subsystem2.operation1() + "\n"
        result += self.subsystem2.operation2() + "\n"
        return result

# Use the Facade Pattern
facade = Facade()
result = facade.operation()
print(result)

'''
In this example, we have two subsystems (Subsystem1 and Subsystem2) with their specific operations. The Facade class provides a simplified interface to these subsystems, allowing clients to interact with the subsystems through a single entry point. It hides the complexity of the subsystems and provides a higher-level interface.

Key Points:

The Facade Pattern provides a unified interface to a set of interfaces in a subsystem.
It simplifies the use of complex subsystems by providing a single entry point.
It's useful when you want to decouple the client code from the complexity of the subsystem.
'''